import argparse
import getpass
from pathlib import Path
from .storage import initialize_vault, save_snippets, load_snippets

# 🔖 Version info
VERSION = "v0.1.0"

# 🔐 Vault setup
VAULT_DIR = Path.home() / ".codevault"
VAULT_FILE = VAULT_DIR / "snippets.enc"
SALT_FILE = VAULT_DIR / "salt.bin"
initialize_vault()

def get_password(confirm=False):
    """Prompt for password with optional confirmation"""
    while True:
        pwd = getpass.getpass("Vault password: ")
        if not confirm:
            return pwd
        
        confirm_pwd = getpass.getpass("Confirm password: ")
        if pwd == confirm_pwd:
            return pwd
        print("Passwords don't match. Try again.")

def main():
    parser = argparse.ArgumentParser(prog="codevault", description="Secure code snippet manager")
    parser.add_argument('--version', action='store_true', help="Show CodeVault version")

    # Parse known args first to check for version
    args, remaining_args = parser.parse_known_args()
    
    if args.version:
        print(f"CodeVault {VERSION}")
        return

    # Only now require subcommands
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new snippet")
    add_parser.add_argument("file", help="Path to code file")
    add_parser.add_argument("--tags", nargs="+", required=True, help="Tags for categorization")
    add_parser.add_argument("--desc", help="Description (optional)")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search snippets")
    search_parser.add_argument("term", help="Search term")

    # List command
    subparsers.add_parser("list", help="List all snippets")

    # Now parse full args
    args = parser.parse_args(remaining_args)

    try:
        if not VAULT_FILE.exists():
            # First-time setup
            password = get_password(confirm=True)
            snippets = []
            save_snippets(snippets, password)
            print("Vault initialized successfully!")
        else:
            password = get_password()

        snippets = load_snippets(password)

        if args.command == "add":
            with open(args.file, "r") as f:
                code = f.read()
            snippets.append({
                "title": args.file,
                "code": code,
                "tags": args.tags,
                "desc": args.desc or ""
            })
            save_snippets(snippets, password)
            print(f"Added {args.file} to vault")

        elif args.command == "search":
            results = [s for s in snippets 
                      if args.term.lower() in s["title"].lower() 
                      or args.term.lower() in " ".join(s["tags"]).lower()
                      or (s["desc"] and args.term.lower() in s["desc"].lower())]
            
            for i, r in enumerate(results, 1):
                print(f"\n[{i}] {r['title']} (Tags: {', '.join(r['tags'])})")
                if r["desc"]:
                    print(f"Description: {r['desc']}")
                print("-" * 50)

        elif args.command == "list":
            for i, s in enumerate(snippets, 1):
                print(f"{i}. {s['title']} [{', '.join(s['tags'])}]")
                
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
