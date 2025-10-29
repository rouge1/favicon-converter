# Favicon Converter

A simple Python script to convert PNG images to multi-size ICO favicons.

## Description

This script takes a PNG image and converts it to an ICO file containing multiple resolutions commonly used for favicons (16x16, 32x32, 48x48, 64x64, 128x128, 256x256). This ensures compatibility across different browsers and devices.

## Requirements

- Python 3.x
- Pillow (PIL) library

The script uses Pillow for image processing. If not installed, you can install it with:

```bash
pip install pillow
```

## Usage

```bash
python favicon-converter.py <input_png_file> [output_ico_file]
```

### Arguments

- `input_png_file`: Path to the PNG file you want to convert
- `output_ico_file` (optional): Path for the output ICO file. If not specified, it will create `favicon.ico` in the same directory as the input file.

### Examples

Convert `priceW.png` to `favicon.ico`:

```bash
python favicon-converter.py priceW.png
```

Convert to a custom output file:

```bash
python favicon-converter.py myicon.png custom.ico
```

## Output

The generated ICO file contains multiple icon sizes for optimal display across different contexts.

## Notes

- The input PNG should ideally be square for best results, but the script will resize it maintaining aspect ratio.
- Transparency is preserved if the PNG has an alpha channel.

## Troubleshooting

If you encounter errors:
- Ensure the input file exists and is a valid PNG
- Make sure Pillow is installed in your Python environment
- Check that you have write permissions in the output directory