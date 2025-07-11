from fontTools.ttLib import TTFont
import sys

def merge_fonts(bengali_font_path, english_font_path, output_path):
    # Load fonts
    bengali_font = TTFont(bengali_font_path)
    english_font = TTFont(english_font_path)

    # Copy English (Latin) glyphs into Bengali font
    for table in english_font["cmap"].tables:
        if table.isUnicode():
            for code, glyph_name in table.cmap.items():
                # Basic Latin (A-Z, a-z, 0-9, symbols)
                if 0x0000 <= code <= 0x007F:
                    bengali_font["cmap"].tables[0].cmap[code] = glyph_name

    # Save the merged font
    bengali_font.save(output_path)
    print(f"Merged font saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python merge_fonts.py <bengali_font.ttf> <english_font.ttf> <output_font.ttf>")
        sys.exit(1)
    
    merge_fonts(sys.argv[1], sys.argv[2], sys.argv[3])  # FIXED: Added missing ')'
