import os
from PIL import Image
import numpy as np

def generate_all_icons(source_path=None):
    if source_path is None:
        # Check standard paths
        potential_sources = [
            'static/img/Maripocel_raw.png',
            'static/img/Maripocel.png',
            'static/img/Mariposacel.png'
        ]
        for p in potential_sources:
            if os.path.exists(p):
                source_path = p
                break

    if not source_path or not os.path.exists(source_path):
        print("No se encontró imagen fuente para generar iconos.")
        return

    img = Image.open(source_path).convert('RGBA')
    arr = np.array(img)

    # Clean white background: if RGB is very close to white (all >= 250), ensure pure white
    rgb = arr[:, :, :3]
    mask_bg = np.all(rgb >= 250, axis=2)
    arr[mask_bg, 0] = 255
    arr[mask_bg, 1] = 255
    arr[mask_bg, 2] = 255
    arr[mask_bg, 3] = 255
    cleaned_img = Image.fromarray(arr)

    # Content bounding box
    mask_fg = np.any(arr[:, :, :3] < 250, axis=2)
    coords = np.argwhere(mask_fg)
    if len(coords) > 0:
        y0, x0 = coords.min(axis=0)
        y1, x1 = coords.max(axis=0)
        pad = 20
        crop_x0 = max(0, x0 - pad)
        crop_y0 = max(0, y0 - pad)
        crop_x1 = min(img.width, x1 + pad)
        crop_y1 = min(img.height, y1 + pad)
        cropped = cleaned_img.crop((crop_x0, crop_y0, crop_x1, crop_y1))
    else:
        cropped = cleaned_img

    # Square canvas with padding for icons
    w, h = cropped.size
    max_dim = max(w, h)
    target_dim = int(max_dim / (1 - 2 * 0.08))
    square_logo = Image.new('RGBA', (target_dim, target_dim), (255, 255, 255, 255))
    offset_x = (target_dim - w) // 2
    offset_y = (target_dim - h) // 2
    square_logo.paste(cropped, (offset_x, offset_y), cropped)

    os.makedirs("static/img/icons", exist_ok=True)
    
    # Save standard logos
    cropped.save("static/img/Maripocel_wide.png")
    square_logo.save("static/img/Maripocel.png")
    square_logo.save("static/img/Mariposacel.png")

    # Generate icons
    square_logo.resize((512, 512), Image.Resampling.LANCZOS).save("static/img/icons/icon-512x512.png")
    square_logo.resize((192, 192), Image.Resampling.LANCZOS).save("static/img/icons/icon-192x192.png")
    square_logo.resize((180, 180), Image.Resampling.LANCZOS).save("static/img/icons/apple-touch-icon.png")
    square_logo.resize((48, 48), Image.Resampling.LANCZOS).save("static/img/icons/favicon-48x48.png")
    square_logo.resize((32, 32), Image.Resampling.LANCZOS).save("static/img/icons/favicon-32x32.png")
    square_logo.resize((16, 16), Image.Resampling.LANCZOS).save("static/img/icons/favicon-16x16.png")

    # Favicon ICO
    square_logo.save("static/favicon.ico", format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print("Iconos PWA e Isotipo Maripocel generados con éxito.")

if __name__ == "__main__":
    generate_all_icons()
