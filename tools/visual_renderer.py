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
from typing import Optional

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

# Cursor block characters for quality indicators
CURSOR_BLOCKS = ["▇", "▆", "▅", "▄", "▃", "▂", "▁", "▏", "▎", "▍", "▌", "▋", "▊", "▉"]

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


def render_collapsible(title: str, content: str, open_by_default: bool = False) -> str:
    """Render a collapsible section using HTML details/summary tags.
    
    Args:
        title: Title shown in the summary
        content: Content inside the collapsible (already formatted markdown)
        open_by_default: Whether the section starts open
    """
    open_attr = ' open' if open_by_default else ''
    return f"<details{open_attr}>\n<summary><strong>{title}</strong></summary>\n\n{content}\n\n</details>"


def render_ascii_header(text: str, theme: str = "default") -> str:
    """Render an ASCII art header for language pages using block characters.
    
    Args:
        text: The heading text (e.g., language name)
        theme: Visual theme for the header border
    
    Returns:
        ASCII art header string suitable for Markdown code blocks
    """
    themes = {
        "default": "═║╔╗╚╝",
        "tech": "█▓▒░║╔╗",
        "minimalist": "──│┌┘└",
    }
    chars = themes.get(theme, themes["default"])
    top_left, top_right, bottom_left, bottom_right = chars[2], chars[3], chars[4], chars[5]
    h_line, v_line = chars[0], chars[1]
    
    # Create a box header
    width = min(max(len(text) + 8, 40), 60)
    text_padded = text.center(width - 4)
    
    top = f"{top_left}{h_line * (width - 2)}{top_right}"
    middle = f"{v_line} {text_padded} {v_line}"
    bottom = f"{bottom_left}{h_line * (width - 2)}{bottom_right}"
    
    return f"{top}\n{middle}\n{bottom}"


def render_unicode_bar(length: int = 40, filled: int = 20, style: str = "blocks") -> str:
    """Render a Unicode gradient progress bar.
    
    Args:
        length: Total length of the bar
        filled: Number of filled characters
        style: Style of the bar (blocks, dots, arrows, mixed)
    
    Returns:
        Unicode bar string
    """
    styles = {
        "blocks": ("█", "░"),
        "dots": ("●", "○"),
        "arrows": ("►", "○"),
        "mixed": ("▰", "▱"),
    }
    filled_char, empty_char = styles.get(style, styles["blocks"])
    filled_count = min(filled, length)
    empty_count = length - filled_count
    return f"{filled_char * filled_count}{empty_char * empty_count}"


def render_robot_meta(canonical_url: str, crawl_delay: str = "10") -> str:
    """Render robots.txt-compatible metadata for a record page.
    
    Args:
        canonical_url: The canonical GitHub URL for this record
        crawl_delay: Crawl delay in seconds
    
    Returns:
        HTML meta tags string
    """
    return (
        f"<!-- robots: index, follow -->\n"
        f"<!-- canonical: {canonical_url} -->\n"
        f"<!-- crawl-delay: {crawl_delay} -->\n"
        f"<!-- robots.txt: compliant -->"
    )


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
        loaded = Image.open(image_path)
        
        if height is None:
            # Maintain aspect ratio (ASCII chars are ~2x taller than wide)
            height = int(width * loaded.height / loaded.width * 0.5)
        
        img = loaded.resize((width, height)).convert("L")  # Grayscale
        
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
    except Exception:
        return f"[Image conversion failed: {image_path}]"


def ascii_image_from_url(url: str, width: int = 60) -> str:
    """Convert image from URL to ASCII art."""
    if not PIL_AVAILABLE:
        return f"[Image: {url}]"
    
    try:
        import urllib.request
        with urllib.request.urlopen(url, timeout=10) as resp:
            img_data = resp.read()
        loaded = Image.open(io.BytesIO(img_data))
        
        height = int(width * loaded.height / loaded.width * 0.5)
        img = loaded.resize((width, height)).convert("L")
        
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
    # Choose cursor block based on hash
    hash_val = hash(f"{branch}:{category}") % len(CURSOR_BLOCKS)
    return f"[{CURSOR_BLOCKS[hash_val]}]"

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
