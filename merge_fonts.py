from fontTools.ttLib import TTFont
import sys

def merge_fonts(bengali_font_path, english_font_path, output_path):
    # Load fonts
    bengali_font = TTFont(bengali_font_path)
    english_font = TTFont(english_font_path)

    # Get the maximum existing glyph ID in Bengali font
    max_glyph_id = len(bengali_font.getGlyphOrder())

    # Copy missing English glyphs + their outlines
    for glyph_name in english_font.getGlyphOrder():
        if glyph_name not in bengali_font.getGlyphOrder():
            # Add glyph to Bengali font
            bengali_font['glyf'].glyphs[glyph_name] = english_font['glyf'].glyphs[glyph_name]
            
            # Update max glyph ID
            max_glyph_id += 1

    # Update cmap (character mappings)
    for table in english_font["cmap"].tables:
        if table.isUnicode():
            for code, glyph_name in table.cmap.items():
                # Basic Latin range (A-Z, a-z, 0-9, symbols)
                if 0x0000 <= code <= 0x007F:
                    bengali_font["cmap"].tables[0].cmap[code] = glyph_name

    # Save merged font
    bengali_font.save(output_path)
    print(f"✅ Success! Merged font saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python merge_fonts.py <bengali_font.ttf> <english_font.ttf> <output_font.ttf>")
        sys.exit(1)
    
    merge_fonts(sys.argv[1], sys.argv[2], sys.argv[3])
