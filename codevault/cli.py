"""CLI interface for CodeVault."""
import uuid
from datetime import datetime
from typing import List

import click
from colorama import init, Fore, Style

from .models import Snippet
from .storage import SnippetStorage

# Initialize colorama for cross-platform colored output
init()

# Global storage instance
storage = SnippetStorage()


def print_success(message: str) -> None:
    """Print success message in green."""
    click.echo(f"{Fore.GREEN}✓ {message}{Style.RESET_ALL}")


def print_error(message: str) -> None:
    """Print error message in red."""
    click.echo(f"{Fore.RED}✗ {message}{Style.RESET_ALL}")


def print_info(message: str) -> None:
    """Print info message in blue."""
    click.echo(f"{Fore.BLUE}ℹ {message}{Style.RESET_ALL}")


def print_snippet(snippet: Snippet, show_code: bool = False) -> None:
    """Print a formatted snippet."""
    click.echo(f"{Fore.CYAN}ID:{Style.RESET_ALL} {snippet.id}")
    click.echo(f"{Fore.CYAN}Title:{Style.RESET_ALL} {snippet.title}")
    click.echo(f"{Fore.CYAN}Language:{Style.RESET_ALL} {snippet.language}")
    click.echo(f"{Fore.CYAN}Tags:{Style.RESET_ALL} {', '.join(snippet.tags)}")
    
    if snippet.description:
        click.echo(f"{Fore.CYAN}Description:{Style.RESET_ALL} {snippet.description}")
    
    click.echo(f"{Fore.CYAN}Created:{Style.RESET_ALL} {snippet.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
    
    if show_code:
        click.echo(f"{Fore.CYAN}Code:{Style.RESET_ALL}")
        click.echo(f"{Fore.YELLOW}{snippet.code}{Style.RESET_ALL}")
    
    click.echo("-" * 50)


@click.group()
def cli():
    """CodeVault - Manage your code snippets from the command line."""
    pass


@cli.command()
@click.option('--title', '-t', required=True, help='Title of the snippet')
@click.option('--language', '-l', required=True, help='Programming language')
@click.option('--tags', '-T', help='Comma-separated tags')
@click.option('--description', '-d', help='Optional description')
@click.option('--file', '-f', type=click.File('r'), help='Read code from file')
def add(title: str, language: str, tags: str, description: str, file):
    """Add a new code snippet."""
    if file:
        code = file.read()
    else:
        click.echo("Enter your code (press Ctrl+D on Unix/Linux/Mac or Ctrl+Z on Windows when done):")
        code = click.get_text_stream('stdin').read()
    
    if not code.strip():
        print_error("Code cannot be empty!")
        return
    
    snippet_id = str(uuid.uuid4())[:8]
    tag_list = [tag.strip() for tag in tags.split(',')] if tags else []
    
    snippet = Snippet(
        id=snippet_id,
        title=title,
        code=code.strip(),
        language=language,
        tags=tag_list,
        description=description
    )
    
    storage.add_snippet(snippet)
    print_success(f"Snippet '{title}' added with ID: {snippet_id}")


@cli.command()
def list():
    """List all code snippets."""
    snippets = storage.load_snippets()
    
    if not snippets:
        print_info("Your vault is empty! Add snippets with 'codevault add'")
        return
    
    click.echo(f"{Fore.GREEN}Found {len(snippets)} snippet(s):{Style.RESET_ALL}\n")
    
    for snippet in snippets:
        print_snippet(snippet)


@cli.command()
@click.argument('query')
def search(query: str):
    """Search for code snippets."""
    snippets = storage.search_snippets(query)
    
    if not snippets:
        print_info(f"No snippets found matching '{query}'")
        return
    
    click.echo(f"{Fore.GREEN}Found {len(snippets)} snippet(s) matching '{query}':{Style.RESET_ALL}\n")
    
    for snippet in snippets:
        print_snippet(snippet)


@cli.command()
@click.argument('snippet_id')
def show(snippet_id: str):
    """Show a specific snippet with full code."""
    snippet = storage.get_snippet(snippet_id)
    
    if not snippet:
        print_error(f"Snippet with ID '{snippet_id}' not found!")
        return
    
    print_snippet(snippet, show_code=True)


@cli.command()
@click.argument('snippet_id')
@click.confirmation_option(prompt='Are you sure you want to delete this snippet?')
def delete(snippet_id: str):
    """Delete a code snippet."""
    if storage.delete_snippet(snippet_id):
        print_success(f"Snippet '{snippet_id}' deleted successfully!")
    else:
        print_error(f"Snippet with ID '{snippet_id}' not found!")


@cli.command()
def stats():
    """Show vault statistics."""
    snippets = storage.load_snippets()
    
    if not snippets:
        print_info("Your vault is empty! Add snippets with 'codevault add'")
        return
    
    # Calculate statistics
    total_snippets = len(snippets)
    languages = {}
    total_tags = set()
    
    for snippet in snippets:
        languages[snippet.language] = languages.get(snippet.language, 0) + 1
        total_tags.update(snippet.tags)
    
    click.echo(f"{Fore.GREEN}Vault Statistics:{Style.RESET_ALL}\n")
    click.echo(f"Total snippets: {total_snippets}")
    click.echo(f"Unique languages: {len(languages)}")
    click.echo(f"Unique tags: {len(total_tags)}")
    
    if languages:
        click.echo(f"\n{Fore.CYAN}Languages:{Style.RESET_ALL}")
        for lang, count in sorted(languages.items(), key=lambda x: x[1], reverse=True):
            click.echo(f"  {lang}: {count}")


if __name__ == '__main__':
    cli()