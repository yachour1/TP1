import os
from PIL import Image

image_folder = 'pic/1_2'

def get_image_files(folder):
    image_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.png'):
                image_files.append(os.path.join(root, file))
    return image_files

image_files = get_image_files(image_folder)

print("Fichiers PNG :", image_files)

#image_files.sort()

if not image_files:
    print("Aucun fichier PNG trouvé dans le dossier.")
else:
    images = [Image.open(img) for img in image_files]

    first_image = images[0]
    gif_size = first_image.size
    gif_duration = 200 

    # Créer un fichier GIF
    gif_filename = 'animation.gif'
    gif = Image.new('RGB', gif_size)
    gif.save(gif_filename, save_all=True, append_images=images, duration=gif_duration, loop=0)

    print(f"Animation enregistrée dans {gif_filename}")