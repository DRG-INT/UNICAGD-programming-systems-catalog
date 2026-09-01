#!/usr/bin/env python3
"""Refactor markdown links: local relative links -> full GitHub URLs.

- Skips URLs that already start with http:// or https://
- Preserves the full filename including extension
- Only rewrites links that are local paths (not absolute URLs)
- Ignores image links to external domains
"""

import re
import sys
from pathlib import Path

REPO_URL = "https://github.com/DRG-INT/UNICAGD-programming-systems-catalog"
BRANCH = "main"

def convert_links(content: str) -> str:
    # Pattern: ![alt](path) or [text](path)
    md_link_re = re.compile(
        r'(\!?\[[^\]]*\]\()'        # opening: ![ or [ ... ](
        r'([^\s)]+)'                 # the link target (no spaces, no closing paren)
        r'(\))'                      # closing )
    )
    
    def replacer(match):
        prefix = match.group(1)
        url = match.group(2)
        suffix = match.group(3)
        
        # Skip if already a full URL (http/https)
        if re.match(r'^https?://', url, re.IGNORECASE):
            return match.group(0)
        
        # Skip anchor-only links (#something)
        if url.startswith('#'):
            return match.group(0)
        
        # Convert local path to GitHub URL
        # Strip leading ./ if present
        clean_path = re.sub(r'^\./', '', url)
        
        github_url = f"{REPO_URL}/blob/{BRANCH}/{clean_path}"
        
        return f"{prefix}{github_url}{suffix}"
    
    return md_link_re.sub(replacer, content)

def process_file(filepath: Path) -> bool:
    content = filepath.read_text(encoding='utf-8')
    new_content = convert_links(content)
    
    if content != new_content:
        filepath.write_text(new_content, encoding='utf-8')
        return True
    return False

if __name__ == '__main__':
    files = sys.argv[1:] if len(sys.argv) > 1 else []
    changed = 0
    for f in files:
        if process_file(Path(f)):
            print(f"Converted: {f}")
            changed += 1
    print(f"\nDone: {changed} files converted.")
