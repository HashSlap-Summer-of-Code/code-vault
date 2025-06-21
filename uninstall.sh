#!/bin/bash


###############################################################################
# uninstall.sh - Clean Uninstaller for CodeVault
#
# Description:
#   This script safely removes the CodeVault CLI tool from your system.
#   It performs the following steps:
#     1. Uninstalls the `codevault` Python package using pip.
#     2. Deletes the local encrypted vault directory located at ~/.codevault.
#     3. Prompts the user for confirmation before removing data.
#
# Usage:
#   chmod +x uninstall.sh     # Make the script executable
#   ./uninstall.sh            # Run the uninstaller
#
# ⚠️ WARNING:
#   This action is irreversible and will permanently delete all stored snippets.
#
###############################################################################

echo "🚨 CodeVault Uninstall Script"

read -p "Are you sure you want to uninstall CodeVault and delete all your stored snippets? (y/N): " confirm
if [[ "$confirm" != "y" ]]; then
    echo "Uninstallation cancelled."
    exit 0
fi

echo "→ Uninstalling Python package..."
pip uninstall -y codevault

VAULT_DIR="$HOME/.codevault"
if [ -d "$VAULT_DIR" ]; then
    echo "→ Removing vault directory at $VAULT_DIR..."
    rm -rf "$VAULT_DIR"
else
    echo "→ No vault directory found at $VAULT_DIR."
fi

echo "✅ CodeVault has been uninstalled."
