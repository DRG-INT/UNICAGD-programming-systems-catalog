#!/usr/bin/env python3
"""
ASCII/Unicode visual rendering utilities for UNICAGD catalog.

Provides:
- Font-based headers (using pyfiglet)
- Image-to-ASCII conversion (using PIL/matplotlib)
- Gradient effects using character density
- Proportional layout support
- Scrollable visual patterns

Usage in build_catalog.py:
  from visual_renderer import render_header, render_gradient_bar, ascii_image
"""

import io
import os
from pathlib import Path
from typing import Optional, List, Tuple

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

try:
    import pyfiglet
    FIGLET_AVAILABLE = True
except ImportError:
    FIGLET_AVAILABLE = False

# Character density ramp for gradients (GitHub-compatible)
DENSITY_RAMP = " .:-=+*#%@"

# GitHub-compatible block gradient
BLOCK_GRADIENT = "█▓▒░ "

# Step blocks for fine gradients
BLOCK_STEPS = "▏▎▍▌▋▊▉"

# Dot-like characters for obfuscation
OBFUSCATION_DOTS = ".∘·•◦°○"

# Cursor block characters for quality indicators
CURSOR_BLOCKS = list("▇▆▅▄▃▂▁")

# Trigger characters for link obfuscation
TRIGGER_CHARS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

# Font mapping for record icons - use only available pyfiglet fonts
FONT_ALIASES = {
    "rust": "big",
    "python": "big",
    "julia": "big",
    "lua family": "big",
    "node.js/javascript": "standard",
    "node.js/typescript": "standard",
    "c++23": "big",
    "c99": "big",
    "go": "big",
    "c#": "big",
    "c23": "big",
    "swift": "big",
    "php": "big",
    "haskell": "big",
    "matlab": "big",
    "nix": "big",
    "starlark": "big",
    "assembly": "big",
    "dart": "big",
    "octave": "big",
    "cocoa": "big",
    "wasm": "big",
    "basilisk": "big",
    "aim's": "big",
    "bc": "big",
    "pattern language": "big",
}


# Cursor block characters for quality indicators
CURSOR_BLOCKS = list("▇▆▅▄▃▂▁")

# Trigger characters for link obfuscation
TRIGGER_CHARS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


def render_header(text: str, font: str = "standard", width: int = 80) -> str:
    """Render ASCII art header text using pyfiglet fonts."""
    if not FIGLET_AVAILABLE:
        return f"# {text}"
    
    try:
        # Auto-select font based on text
        actual_font = FONT_ALIASES.get(text.lower(), font)
        fig = pyfiglet.Figlet(font=actual_font, width=width)
        return fig.renderText(text)
    except Exception:
        try:
            fig = pyfiglet.Figlet(font=font, width=width)
            return fig.renderText(text)
        except Exception:
            return f"# {text}"


def render_gradient_bar(length: int = 40, style: str = "horizontal") -> str:
    """Render a gradient visual bar using Unicode block characters."""
    gradients = [
        "░▒▓█",
        " ░▒▓█",
        "░▒▓▓▓",
        ".:-=+*#%@@",
    ]
    
    gradient = gradients[0]
    result = ""
    
    if style == "horizontal":
        for i in range(length):
            idx = int(i / length * (len(gradient) - 1))
            result += gradient[min(idx, len(gradient)-1)]
    elif style == "vertical":
        for level in range(4):
            line_len = length * (level + 1) // 4
            char = gradient[level]
            result += char * line_len + "\n"
    elif style == "radar":
        # Circular/radar-like pattern
        for i in range(8):
            line_len = int(length * (i + 1) / 8)
            result += gradient[i % len(gradient)] * line_len + "\n"
    
    return result.rstrip()


def ascii_image(
    image_path: str,
    width: int = 100,
    height: Optional[int] = None,
    invert: bool = False,
) -> str:
    """Convert an image file to ASCII art."""
    if not PIL_AVAILABLE:
        return f"[Image: {os.path.basename(image_path)}]"
    
    try:
        img = Image.open(image_path)
        
        if height is None:
            # Maintain aspect ratio (ASCII chars are ~2x taller than wide)
            height = int(width * img.height / img.width * 0.5)
        
        img = img.resize((width, height))
        img = img.convert("L")  # Grayscale
        
        pixels = list(img.getdata())
        chars = []
        
        for pixel in pixels:
            if invert:
                idx = 255 - pixel
            else:
                idx = pixel
            
            # Map to density ramp
            density_idx = int(idx / 255 * (len(DENSITY_RAMP) - 1))
            chars.append(DENSITY_RAMP[density_idx])
        
        # Format as lines
        lines = []
        for i in range(0, len(chars), width):
            lines.append("".join(chars[i:i + width]))
        
        return "\n".join(lines)
    except Exception as e:
        return f"[Image conversion failed: {image_path}]"


def ascii_image_from_url(url: str, width: int = 60) -> str:
    """Convert image from URL to ASCII art."""
    if not PIL_AVAILABLE:
        return f"[Image: {url}]"
    
    try:
        import urllib.request
        with urllib.request.urlopen(url, timeout=10) as resp:
            img_data = resp.read()
        img = Image.open(io.BytesIO(img_data))
        
        height = int(width * img.height / img.width * 0.5)
        img = img.resize((width, height))
        img = img.convert("L")
        
        return _img_to_ascii(img, width, height)
    except Exception:
        return f"[Image: {url}]"


def _img_to_ascii(img: Image.Image, width: int, height: int) -> str:
    """Convert PIL image to ASCII string."""
    pixels = list(img.getdata())
    chars = []
    
    for pixel in pixels:
        density_idx = int(pixel / 255 * (len(DENSITY_RAMP) - 1))
        chars.append(DENSITY_RAMP[density_idx])
    
    lines = []
    for i in range(0, len(chars), width):
        lines.append("".join(chars[i:i + width]))
    
    return "\n".join(lines)


def render_proportional(text: str, min_width: int = 60) -> str:
    """Render text in a proportional layout (not monospace).
    
    Creates visual blocks of varying widths to simulate proportional text.
    """
    result = ""
    for char in text:
        # Vary character width based on character type
        if char in "iIlL,.': ":
            width = 1
        elif char in "tIf":
            width = 2
        elif char in "()[]{}":
            width = 3
        else:
            width = 4
        
        result += char * width
    
    # Ensure minimum width
    if len(result) < min_width:
        padding = " " * (min_width - len(result))
        result += padding
    
    return result


def render_scroll_pattern(scroll_pos: float = 0.0, length: int = 60) -> str:
    """Render a visual pattern that changes based on scroll position.
    
    scroll_pos: 0.0 to 1.0 representing scroll position in document.
    Creates different visual patterns at different scroll positions.
    """
    if scroll_pos < 0.2:
        # Top - header zone
        return "╔" + "═" * (length - 2) + "╗"
    elif scroll_pos < 0.4:
        # Early content - gradient
        return render_gradient_bar(length, "horizontal")
    elif scroll_pos < 0.6:
        # Middle - dense
        return "▓" * length
    elif scroll_pos < 0.8:
        # Late - patterned
        pattern = ""
        for i in range(length):
            if i % 4 == 0:
                pattern += "░"
            elif i % 4 == 1:
                pattern += "▒"
            elif i % 4 == 2:
                pattern += "▓"
            else:
                pattern += "█"
        return pattern
    else:
        # Bottom - footer
        return "╚" + "═" * (length - 2) + "╝"


def render_visual_separator(char: str = "═", length: int = 80, double: bool = False) -> str:
    """Render a visual separator line."""
    line = char * length
    if double:
        return f"{line}\n{line}"
    return line


def render_logo_ascii(name: str, max_width: int = 40) -> str:
    """Render a company/project logo as ASCII art from its name."""
    if not FIGLET_AVAILABLE:
        return name.upper()
    
    best_font = "standard"
    try:
        fig = pyfiglet.Figlet(font=best_font, width=max_width)
        return fig.renderText(name)
    except Exception:
        return name.upper()


def get_font_for_language(branch: str) -> str:
    """Get the appropriate pyfiglet font for a language branch."""
    return FONT_ALIASES.get(branch.lower(), "standard")


def render_category_banner(category: str, record_count: int, width: int = 80) -> str:
    """Render a category banner with ASCII art header and stats."""
    header = render_header(category.title(), font="standard", width=width)
    
    # Create a visual bar showing relative record count
    bar_length = min(record_count // 10, 50)  # Scale down
    bar = "█" * bar_length + "░" * max(0, 50 - bar_length)
    
    return f"{header}\n{bar} [{record_count} records]"


def render_record_icon(branch: str, category: str) -> str:
    """Generate a simple icon/block for a record based on branch and category."""
    # Use first letters of branch and category
    branch_init = branch[0].upper() if branch else "R"
    category_init = category[0].upper() if category else "C"
    
    # Choose cursor block based on hash
    hash_val = hash(branch + category) % len(CURSOR_BLOCKS)
    
    return f"[{CURSOR_BLOCKS[hash_val]}]"


# Cursor blocks for use in main build script
CURSOR_BLOCKS = ["▇", "▆", "▅", "▄", "▃", "▂", "▁", "▏", "▎", "▍", "▌", "▋", "▊", "▉"]

if __name__ == "__main__":
    # Demo
    print("=== Header Demo ===")
    print(render_header("Rust", font="chunk", width=80))
    print()
    
    print("=== Gradient Bar Demo ===")
    print(render_gradient_bar(40))
    print()
    
    print("=== Scroll Pattern Demo ===")
    print(render_scroll_pattern(0.1, 60))
    print(render_scroll_pattern(0.3, 60))
    print(render_scroll_pattern(0.5, 60))
    print(render_scroll_pattern(0.7, 60))
    print(render_scroll_pattern(0.9, 60))
    print()
    
    print("=== Proportional Text Demo ===")
    print(render_proportional("Hello World!"))
