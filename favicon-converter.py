#!/usr/bin/env python3
"""
Favicon Converter
Converts a PNG image to a multi-size ICO favicon.
"""

from PIL import Image
import sys
import os

def convert_png_to_ico(png_path, ico_path=None):
    """
    Convert PNG to ICO with multiple sizes.
    """
    if not os.path.exists(png_path):
        print(f"Error: {png_path} not found.")
        return False

    try:
        img = Image.open(png_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return False

    # Ensure the image is in RGBA mode for transparency
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # Common favicon sizes
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

    # Resize and collect icons
    icons = []
    for size in sizes:
        resized = img.resize(size, Image.Resampling.LANCZOS)
        icons.append(resized)

    # Default output path
    if ico_path is None:
        base_name = os.path.splitext(png_path)[0]
        ico_path = f"{base_name}.ico"

    try:
        # Save the first icon with the others appended
        icons[0].save(ico_path, format='ICO', sizes=sizes, append_images=icons[1:])
        print(f"Successfully converted {png_path} to {ico_path}")
        return True
    except Exception as e:
        print(f"Error saving ICO: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python favicon-converter.py <png_file> [output_ico_file]")
        print("Example: python favicon-converter.py priceW.png")
        print("If output not specified, will create favicon.ico in same directory")
        sys.exit(1)

    png_file = sys.argv[1]
    ico_file = sys.argv[2] if len(sys.argv) > 2 else None

    success = convert_png_to_ico(png_file, ico_file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
