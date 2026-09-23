import math
from PIL import Image, ImageDraw

def render_mariposa_icon(size=512):
    # Canvas blanco puro
    img = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Borde sutil #E5E7EB
    pad = int(size * 0.04)
    r = int(size * 0.18)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=r, outline=(229, 231, 235, 255), width=int(size * 0.015))
    
    # Centro geométrico del icono
    cx = size / 2.0
    cy = size / 2.0
    s = size / 512.0 # Escalar respecto a 512
    
    # Paleta de Colores
    gold_main = (212, 175, 55, 255)       # #D4AF37
    gold_light = (243, 208, 121, 255)     # #F3D079
    gold_dark = (184, 144, 40, 255)       # #B89028
    amber = (215, 168, 110, 255)          # #D7A86E
    graphite = (31, 31, 31, 255)          # #1F1F1F
    
    # Cuerpo Central Geométrico (Grafito Tech)
    body_points = [
        (cx, cy - 80 * s),
        (cx + 8 * s, cy - 20 * s),
        (cx + 10 * s, cy + 50 * s),
        (cx, cy + 90 * s),
        (cx - 10 * s, cy + 50 * s),
        (cx - 8 * s, cy - 20 * s),
    ]
    draw.polygon(body_points, fill=graphite)
    
    # Cabeza (círculo / rombo tech grafito)
    draw.ellipse([cx - 10 * s, cy - 105 * s, cx + 10 * s, cy - 85 * s], fill=graphite)
    
    # Antenas minimalistas geométricas en oro
    draw.line([(cx - 3 * s, cy - 98 * s), (cx - 30 * s, cy - 135 * s)], fill=gold_dark, width=int(4 * s))
    draw.line([(cx + 3 * s, cy - 98 * s), (cx + 30 * s, cy - 135 * s)], fill=gold_dark, width=int(4 * s))
    draw.ellipse([cx - 35 * s, cy - 140 * s, cx - 25 * s, cy - 130 * s], fill=gold_main)
    draw.ellipse([cx + 25 * s, cy - 140 * s, cx + 35 * s, cy - 130 * s], fill=gold_main)
    
    # --- Alas Superiores Geométricas (Facetadas estilo Origami / Tech) ---
    # Ala Derecha Superior
    wing_tr_1 = [(cx + 10 * s, cy - 20 * s), (cx + 155 * s, cy - 120 * s), (cx + 175 * s, cy - 40 * s), (cx + 10 * s, cy + 10 * s)]
    wing_tr_2 = [(cx + 10 * s, cy - 20 * s), (cx + 155 * s, cy - 120 * s), (cx + 100 * s, cy - 145 * s), (cx + 4 * s, cy - 65 * s)]
    wing_tr_3 = [(cx + 10 * s, cy + 10 * s), (cx + 175 * s, cy - 40 * s), (cx + 140 * s, cy + 30 * s), (cx + 8 * s, cy + 40 * s)]
    
    draw.polygon(wing_tr_2, fill=gold_light)
    draw.polygon(wing_tr_1, fill=gold_main)
    draw.polygon(wing_tr_3, fill=amber)
    
    # Ala Izquierda Superior (Espejo simétrico perfecto)
    wing_tl_1 = [(cx - 10 * s, cy - 20 * s), (cx - 155 * s, cy - 120 * s), (cx - 175 * s, cy - 40 * s), (cx - 10 * s, cy + 10 * s)]
    wing_tl_2 = [(cx - 10 * s, cy - 20 * s), (cx - 155 * s, cy - 120 * s), (cx - 100 * s, cy - 145 * s), (cx - 4 * s, cy - 65 * s)]
    wing_tl_3 = [(cx - 10 * s, cy + 10 * s), (cx - 175 * s, cy - 40 * s), (cx - 140 * s, cy + 30 * s), (cx - 8 * s, cy + 40 * s)]
    
    draw.polygon(wing_tl_2, fill=gold_light)
    draw.polygon(wing_tl_1, fill=gold_main)
    draw.polygon(wing_tl_3, fill=amber)
    
    # --- Alas Inferiores Geométricas ---
    # Ala Derecha Inferior
    wing_br_1 = [(cx + 8 * s, cy + 25 * s), (cx + 130 * s, cy + 40 * s), (cx + 100 * s, cy + 125 * s), (cx + 5 * s, cy + 70 * s)]
    wing_br_2 = [(cx + 5 * s, cy + 70 * s), (cx + 100 * s, cy + 125 * s), (cx + 45 * s, cy + 145 * s), (cx + 2 * s, cy + 85 * s)]
    draw.polygon(wing_br_1, fill=gold_main)
    draw.polygon(wing_br_2, fill=gold_dark)
    
    # Ala Izquierda Inferior (Espejo)
    wing_bl_1 = [(cx - 8 * s, cy + 25 * s), (cx - 130 * s, cy + 40 * s), (cx - 100 * s, cy + 125 * s), (cx - 5 * s, cy + 70 * s)]
    wing_bl_2 = [(cx - 5 * s, cy + 70 * s), (cx - 100 * s, cy + 125 * s), (cx - 45 * s, cy + 145 * s), (cx - 2 * s, cy + 85 * s)]
    draw.polygon(wing_bl_1, fill=gold_main)
    draw.polygon(wing_bl_2, fill=gold_dark)
    
    # Líneas divisorias internas tech sutiles
    line_col = (255, 255, 255, 180)
    lw = max(1, int(2 * s))
    draw.line([(cx + 10 * s, cy - 20 * s), (cx + 155 * s, cy - 120 * s)], fill=line_col, width=lw)
    draw.line([(cx - 10 * s, cy - 20 * s), (cx - 155 * s, cy - 120 * s)], fill=line_col, width=lw)
    draw.line([(cx + 10 * s, cy + 10 * s), (cx + 175 * s, cy - 40 * s)], fill=line_col, width=lw)
    draw.line([(cx - 10 * s, cy + 10 * s), (cx - 175 * s, cy - 40 * s)], fill=line_col, width=lw)
    draw.line([(cx + 8 * s, cy + 25 * s), (cx + 100 * s, cy + 125 * s)], fill=line_col, width=lw)
    draw.line([(cx - 8 * s, cy + 25 * s), (cx - 100 * s, cy + 125 * s)], fill=line_col, width=lw)

    return img

# Generar y guardar todas las resoluciones necesarias
base_img = render_mariposa_icon(512)
base_img.save("static/img/icons/icon-512x512.png")

icon_192 = render_mariposa_icon(192)
icon_192.save("static/img/icons/icon-192x192.png")

icon_180 = render_mariposa_icon(180)
icon_180.save("static/img/icons/apple-touch-icon.png")

icon_48 = render_mariposa_icon(48)
icon_48.save("static/img/icons/favicon-48x48.png")

icon_32 = render_mariposa_icon(32)
icon_32.save("static/img/icons/favicon-32x32.png")

icon_16 = render_mariposa_icon(16)
icon_16.save("static/img/icons/favicon-16x16.png")

# Favicon .ico
base_img.save("static/favicon.ico", format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
print("Iconos PWA e Isotipo Mariposacel generados con éxito.")
