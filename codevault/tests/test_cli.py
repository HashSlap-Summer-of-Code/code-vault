"""Tests for CLI functionality."""
import tempfile
import shutil
from pathlib import Path
from click.testing import CliRunner

from codevault.cli import cli
from codevault.storage import SnippetStorage


def test_empty_vault_list():
    """Test that list command shows appropriate message for empty vault."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Use temporary storage
        import codevault.cli
        codevault.cli.storage = SnippetStorage(temp_dir)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['list'])
        
        assert result.exit_code == 0
        assert "Your vault is empty! Add snippets with 'codevault add'" in result.output


def test_empty_search_results():
    """Test that search shows appropriate message when no results found."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Use temporary storage
        import codevault.cli
        codevault.cli.storage = SnippetStorage(temp_dir)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['search', 'python'])
        
        assert result.exit_code == 0
        assert "No snippets found matching 'python'" in result.output