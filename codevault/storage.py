"""Storage management for CodeVault."""
import json
import os
from pathlib import Path
from typing import List, Optional
from .models import Snippet


class SnippetStorage:
    """Handles storage and retrieval of code snippets."""
    
    def __init__(self, storage_path: Optional[str] = None):
        if storage_path is None:
            home = Path.home()
            self.storage_dir = home / ".codevault"
        else:
            self.storage_dir = Path(storage_path)
        
        self.storage_dir.mkdir(exist_ok=True)
        self.storage_file = self.storage_dir / "snippets.json"
    
    def load_snippets(self) -> List[Snippet]:
        """Load all snippets from storage."""
        if not self.storage_file.exists():
            return []
        
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Snippet.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            return []
    
    def save_snippets(self, snippets: List[Snippet]) -> None:
        """Save snippets to storage."""
        data = [snippet.to_dict() for snippet in snippets]
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def add_snippet(self, snippet: Snippet) -> None:
        """Add a new snippet."""
        snippets = self.load_snippets()
        snippets.append(snippet)
        self.save_snippets(snippets)
    
    def get_snippet(self, snippet_id: str) -> Optional[Snippet]:
        """Get a snippet by ID."""
        snippets = self.load_snippets()
        for snippet in snippets:
            if snippet.id == snippet_id:
                return snippet
        return None
    
    def delete_snippet(self, snippet_id: str) -> bool:
        """Delete a snippet by ID."""
        snippets = self.load_snippets()
        original_length = len(snippets)
        snippets = [s for s in snippets if s.id != snippet_id]
        
        if len(snippets) < original_length:
            self.save_snippets(snippets)
            return True
        return False
    
    def search_snippets(self, query: str) -> List[Snippet]:
        """Search snippets by query."""
        snippets = self.load_snippets()
        query = query.lower()
        
        matching_snippets = []
        for snippet in snippets:
            if (query in snippet.title.lower() or 
                query in snippet.language.lower() or
                query in snippet.code.lower() or
                any(query in tag.lower() for tag in snippet.tags) or
                (snippet.description and query in snippet.description.lower())):
                matching_snippets.append(snippet)
        
        return matching_snippets