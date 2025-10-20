HOME_IMG = "https://i.ibb.co/ZzwRyQYL/HD.jpg"

import os

# Carga una imagen en especifico de la carpeta image
async def load_image(name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "images", f"{name}")
    
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    return image_path

# Carga una fuente en especifico de la carpeta fonts
async def load_fonts(tipe):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(current_dir, "fonts", f"{tipe}")
    
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font not found at {font_path}")
    
    return font_path