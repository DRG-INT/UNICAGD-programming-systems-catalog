#!/usr/bin/env python3
"""
Partial link obfuscation system for UNICAGD catalog.

Steganographic-style approach:
- Local links become GitHub links with ~25-49% character obfuscation
- ~51-75% remains human-readable
- Single source of truth: .cache/link_redirect_map.json
- Reversible decode system
- Visual cursor blocks for quality indicators

Example:
  Before: [text](catalog/index.md)
  After:  [text](Xcatalog/indX.md)<!--g:https://github.com/.../blob/main/catalog/index.md-->

The trigger characters are randomly inserted at deterministic positions,
with only ~30% of characters replaced (within 25-49% range).
"""

import argparse
import hashlib
import json
import os
import re
import time
from pathlib import Path
from typing import Dict, Optional

REPO_URL = "https://github.com/DRG-INT/UNICAGD-programming-systems-catalog"
BRANCH = "main"
CACHE_DIR = Path(".cache")
REDIRECT_MAP_PATH = CACHE_DIR / "link_redirect_map.json"

# Theme-based cursor blocks
CURSOR_BLOCKS = ["▇", "▆", "▅", "▄", "▃", "▂", "▁"]

# Themed obfuscation character sets
THEMES = {
    "default": "·∘•◦°○",           # Dot/bullet theme
    "tech": "·¨ˆ˜ˇ^",              # Technical/accent marks
    "greek": "αβγδεζηθ",           # Greek letters
    "math": "∓∓∓∓∓∓∓∓",           # Mathematical operators  
    "cyrillic": "абвгдежз",         # Cyrillic alphabet
    "arabic": "ابتجدرزس",          # Arabic script
    "braille": "⠃⠉⠙⠑⠋⠛⠓⠊",  # Braille patterns
    "blocks": "░▒▓█▓▒░",            # Block density pattern
    "arrows": "←↑→↓↖↗↘↙",           # Arrow directions
    "stars": "★☆☆☆☆☆☆☆",           # Star patterns
    "weather": "☀☁☂☃☄☎☑☒",       # Weather/symbols
    "shapes": "◯◉○○○○○○",           # Circle shapes
    "circles": "●○○○○○○○",          # Filled/hollow circles
}

# Default single character for backward compatibility
OBFUSCATION_CHAR = "·"
TRIGGER_CHARS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


class LinkObfuscator:
    def __init__(self, seed: Optional[str] = None):
        self.seed = seed or str(int(time.time()))
        self._sot = self._load_or_build_sot()

    def _load_or_build_sot(self) -> dict:
        """Load existing SOT or build new one."""
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        
        if REDIRECT_MAP_PATH.exists():
            try:
                sot = json.loads(REDIRECT_MAP_PATH.read_text())
                if sot.get("seed") == self.seed:
                    return sot
            except Exception:
                pass
        
        # Build new SOT
        import random
        rng = random.Random(self.seed)
        
        # Collect all unique paths
        local_paths = set()
        records_dir = Path("catalog/records")
        if records_dir.exists():
            for md_file in records_dir.glob("*.md"):
                local_paths.add(f"catalog/records/{md_file.name}")
        
        for d in ["catalog/by-category", "catalog/by-language"]:
            cat_dir = Path(d)
            if cat_dir.exists():
                for md_file in cat_dir.glob("*.md"):
                    local_paths.add(f"{d}/{md_file.name}")
        
        for page in ["catalog/index.md", "catalog/release-watch.md",
                     "catalog/license-index.md", "catalog/provenance.md",
                     "catalog/source-map.md", "README.md"]:
            local_paths.add(page)
        
        # Build redirect map with targeted 25-49% character obfuscation
        import random
        rng = random.Random(self.seed)
        
        # Collect all unique paths
        local_paths = set()
        records_dir = Path("catalog/records")
        if records_dir.exists():
            for md_file in records_dir.glob("*.md"):
                local_paths.add(f"catalog/records/{md_file.name}")
        
        for d in ["catalog/by-category", "catalog/by-language"]:
            cat_dir = Path(d)
            if cat_dir.exists():
                for md_file in cat_dir.glob("*.md"):
                    local_paths.add(f"{d}/{md_file.name}")
        
        for page in ["catalog/index.md", "catalog/release-watch.md",
                     "catalog/license-index.md", "catalog/provenance.md",
                     "catalog/source-map.md", "README.md"]:
            local_paths.add(page)
        
        # Build redirect map with ~35% character obfuscation (25-49% range)
        redirect_map = {}
        cursor_map = {}
        
        for path in sorted(local_paths):
            github_url = f"{REPO_URL}/blob/{BRANCH}/{path}"
            
            # Target 25-49% obfuscation density using even distribution
            hash_val = int(hashlib.sha256(path.encode()).hexdigest()[:8], 16)
            
            # Every 3rd character (skip / and .) → ~33% density
            # Use hash to offset pattern per path
            offset = hash_val % 3
            chars_to_hide = set()
            for i in range(len(path)):
                if (i + offset) % 3 == 0 and path[i] not in ('/', '.'):
                    chars_to_hide.add(i)
            
            # Single trigger character for redirect mapping
            trigger = TRIGGER_CHARS[hash_val % len(TRIGGER_CHARS)]
            cursor = CURSOR_BLOCKS[hash_val % len(CURSOR_BLOCKS)]
            
            redirect_map[path] = {
                "github_url": github_url,
                "trigger": trigger,
                "cursor": cursor,
                "chars_to_hide": sorted(list(chars_to_hide)),
                "density": len(chars_to_hide) / max(len(path), 1),
            }
            cursor_map[path] = cursor
        
        sot = {
            "seed": self.seed,
            "redirect_map": redirect_map,
            "created": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        
        REDIRECT_MAP_PATH.write_text(json.dumps(sot, indent=2, sort_keys=True))
        return sot

    def encode_link(self, link_text: str, local_path: str, theme: str = "default") -> str:
        """Encode a local link with partial obfuscation using themed characters.
        
        Args:
            link_text: Display text for the link
            local_path: Local file path (e.g., 'catalog/by-category/rust.md')
            theme: Obfuscation theme from THEMES dict (default, tech, greek, etc.)
        """
        clean_path = re.sub(r'^\./', '', local_path)
        github_url = f"{REPO_URL}/blob/{BRANCH}/{clean_path}"
        
        # Lookup in SOT
        entry = self._sot.get("redirect_map", {}).get(clean_path)
        
        if entry:
            chars_to_hide = entry["chars_to_hide"]
        else:
            # Fallback
            hash_val = int(hashlib.sha256(clean_path.encode()).hexdigest()[:8], 16)
            offset = hash_val % 3
            chars_to_hide = [i for i in range(len(clean_path))
                            if (i + offset) % 3 == 0 and clean_path[i] not in ('/', '.')]
        
        # Select obfuscation characters based on theme
        obfuscation_chars = THEMES.get(theme, THEMES["default"])
        
        # Apply partial obfuscation - each hidden char gets a different theme character
        chars = list(clean_path)
        for i, pos in enumerate(chars_to_hide):
            if pos < len(chars):
                chars[pos] = obfuscation_chars[i % len(obfuscation_chars)]
        
        obfuscated_target = "".join(chars)
        
        # Hide full URL in HTML comment for reversibility
        return f"[{link_text}]({obfuscated_target})<!--g:{github_url}-->"

    def decode_link(self, obfuscated: str) -> Optional[str]:
        """Decode an obfuscated link back to original path."""
        match = re.search(r'<!--g:([^>]+)-->', obfuscated)
        if match:
            github_url = match.group(1)
            parts = github_url.split(f'/blob/{BRANCH}/')
            if len(parts) == 2:
                return parts[1]
        return None

    def process_file(self, filepath: Path, mode: str, theme: str = "default") -> bool:
        """Process a markdown file.
        
        Args:
            filepath: Path to markdown file
            mode: 'encode', 'decode', or 'verify'
            theme: Obfuscation theme (default, tech, greek, etc.)
        """
        content = filepath.read_text(encoding='utf-8')
        
        if mode == 'encode':
            def replace_link(match):
                full_match = match.group(0)
                link_text = match.group(1)
                link_target = match.group(2)
                
                if '<!--g:' in full_match:
                    return full_match
                if link_target.startswith('http://') or link_target.startswith('https://'):
                    return full_match
                if link_target.startswith('#'):
                    return full_match
                if 'blob/main/' in link_target:
                    return full_match
                
                return self.encode_link(link_text, link_target, theme)
            
            new_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)
            
        elif mode == 'decode':
            def restore_link(match):
                full_match = match.group(0)
                mapping_match = re.search(r'<!--g:([^>]+)-->', full_match)
                if mapping_match:
                    github_url = mapping_match.group(1)
                    parts = github_url.split(f'/blob/{BRANCH}/')
                    local_path = parts[1] if len(parts) == 2 else github_url
                    text_match = re.match(r'\[([^\]]+)\]', full_match)
                    link_text = text_match.group(1) if text_match else ""
                    return f"[{link_text}]({local_path})"
                return full_match
            
            new_content = re.sub(
                r'\[([^\]]+)\]\([^)]+\)<!--g:[^>]+-->', restore_link, content
            )
        else:
            return False
        
        if content != new_content:
            filepath.write_text(new_content, encoding='utf-8')
            return True
        return False

    def process_directory(self, dir_path: str, mode: str, theme: str = "default") -> dict:
        results = {"processed": 0, "changed": 0, "errors": []}
        dir_obj = Path(dir_path)
        for md_file in dir_obj.rglob("*.md"):
            results["processed"] += 1
            try:
                if self.process_file(md_file, mode, theme):
                    results["changed"] += 1
            except Exception as e:
                results["errors"].append(f"{md_file}: {e}")
        return results

    def verify(self, dir_path: str) -> dict:
        """Verify obfuscation integrity - check density and readability."""
        results = {"files": 0, "total_links": 0, "obfuscated_links": 0, "avg_density": 0}
        densities = []
        
        dir_obj = Path(dir_path)
        for md_file in dir_obj.rglob("*.md"):
            content = md_file.read_text(encoding='utf-8')
            # Find obfuscated links
            obfuscated = re.findall(r'\]\([^)]+<!--g:', content)
            total = re.findall(r'\]\(([^)]+)\)', content)
            
            results["files"] += 1
            results["total_links"] += len(total)
            results["obfuscated_links"] += len(obfuscated)
            
            # Calculate density for obfuscated links
            for match in re.finditer(r'\]\(([^)]+)<!--g:([^>]+)-->', content):
                visible_path = match.group(1)
                github_url = match.group(2)
                local_path = github_url.split(f'/blob/{BRANCH}/')[-1]
                
                if len(local_path) > 0:
                    # Count differences
                    diffs = sum(1 for a, b in zip(visible_path, local_path) if a != b)
                    density = diffs / len(local_path)
                    densities.append(density)
        
        if densities:
            results["avg_density"] = sum(densities) / len(densities)
            results["min_density"] = min(densities)
            results["max_density"] = max(densities)
        
        return results


def main():
    parser = argparse.ArgumentParser(description="Partial link obfuscation for catalog")
    parser.add_argument("mode", choices=["encode", "decode", "verify", "sot", "themes"],
                        help="encode: obfuscate links, decode: restore, verify: check integrity, sot: show mapping, themes: list available themes")
    parser.add_argument("paths", nargs="*", help="Files or directories to process")
    parser.add_argument("--seed", default=None, help="Build seed")
    parser.add_argument("--theme", default="default", help="Obfuscation theme (see 'themes' command)")
    
    args = parser.parse_args()
    
    if args.mode == "sot":
        if REDIRECT_MAP_PATH.exists():
            print(json.dumps(json.loads(REDIRECT_MAP_PATH.read_text()), indent=2))
        else:
            print("No SOT found. Run encode first.")
        return
    
    if args.mode == "themes":
        print("Available obfuscation themes:")
        for name, chars in THEMES.items():
            sample = "".join(chars[:3])
            print(f"  {name}: {sample}")
        return
    
    obfuscator = LinkObfuscator(seed=args.seed)
    
    if args.mode == "verify":
        for path in args.paths:
            r = obfuscator.verify(path)
            print(f"{path}: {r}")
        return
    
    total_changed = 0
    total_processed = 0
    
    for path in args.paths:
        p = Path(path)
        if p.is_dir():
            result = obfuscator.process_directory(str(p), args.mode, args.theme)
            total_changed += result["changed"]
            total_processed += result["processed"]
        elif p.is_file():
            total_processed += 1
            if obfuscator.process_file(p, args.mode, args.theme):
                total_changed += 1
    
    print(f"Mode: {args.mode}, Seed: {obfuscator.seed}")
    print(f"Processed: {total_processed} files, Changed: {total_changed} files")


if __name__ == "__main__":
    main()
