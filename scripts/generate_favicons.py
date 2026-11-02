#!/usr/bin/env python3
"""
Generates the official Alira Digital favicon family:
- favicon.ico (16x16, 32x32, 48x48)
- assets/img/favicon-32x32.png
- assets/img/favicon-192.png
- apple-touch-icon.png (180x180)
"""
from PIL import Image, ImageDraw

def render_alira_badge(size):
    scale = 16
    dim = size * scale
    im = Image.new('RGBA', (dim, dim), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    
    cx, cy = dim / 2.0, dim / 2.0
    r_outer = (dim / 2.0) - (1.0 * scale)
    
    # Badge background: deep obsidian teal (#0A282D)
    draw.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer], fill=(10, 40, 45, 255))
    
    # Emerald rim (#10B981)
    rim_w = max(int(1.5 * scale), int(dim * 0.045))
    draw.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer], outline=(16, 185, 129, 255), width=rim_w)
    
    # Coordinates of 'A'
    leg_thick_mult = 1.25 if size <= 32 else 1.05
    
    top_y = cy - (dim * 0.31)
    bottom_y = cy + (dim * 0.31)
    
    half_outer_w = dim * 0.32
    half_inner_w = half_outer_w * (0.42 / leg_thick_mult)
    inner_apex_y = top_y + (bottom_y - top_y) * 0.52
    
    poly = [
        (cx, top_y),
        (cx - half_outer_w, bottom_y),
        (cx - half_inner_w, bottom_y),
        (cx, inner_apex_y),
        (cx + half_inner_w, bottom_y),
        (cx + half_outer_w, bottom_y),
        (cx, top_y)
    ]
    draw.polygon(poly, fill=(255, 255, 255, 255))
    
    # Crossbeam: Emerald (#10B981)
    beam_w = half_outer_w * 1.55
    beam_h = max(int(2.0 * scale), int((bottom_y - top_y) * 0.17))
    beam_cy = cy + (dim * 0.06)
    beam_x1 = cx - (beam_w / 2.0)
    beam_x2 = cx + (beam_w / 2.0)
    beam_y1 = beam_cy - (beam_h / 2.0)
    beam_y2 = beam_cy + (beam_h / 2.0)
    draw.rounded_rectangle([beam_x1, beam_y1, beam_x2, beam_y2], radius=int(beam_h / 2.0), fill=(16, 185, 129, 255))
    
    # Apex focal point dot: Emerald (#10B981)
    dot_r = max(int(1.5 * scale), int(dim * 0.08))
    draw.ellipse([cx - dot_r, top_y - dot_r, cx + dot_r, top_y + dot_r], fill=(16, 185, 129, 255))
    
    return im.resize((size, size), Image.Resampling.LANCZOS)

def main():
    print("Generating Alira favicons...")
    # 32x32
    f32 = render_alira_badge(32)
    f32.save("assets/img/favicon-32x32.png", "PNG")
    print("Saved assets/img/favicon-32x32.png")
    
    # 192x192
    f192 = render_alira_badge(192)
    f192.save("assets/img/favicon-192.png", "PNG")
    print("Saved assets/img/favicon-192.png")
    
    # 180x180 (Apple touch icon)
    f180 = render_alira_badge(180)
    f180.save("apple-touch-icon.png", "PNG")
    print("Saved apple-touch-icon.png")
    
    # favicon.ico (16, 32, 48)
    f16 = render_alira_badge(16)
    f48 = render_alira_badge(48)
    f48.save("favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print("Saved favicon.ico")
    
    print("Done! All favicon assets updated.")

if __name__ == '__main__':
    main()
