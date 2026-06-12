import os
from PIL import Image
import subprocess

texture_width = 512
texture_height = 732

base_texture_path = r'.\text_base.png'
input_path = r'.\input'
output_dir = r'.\output\textures\clutter\bbr'

def run():
    process_hair_color('BL')
    process_hair_color('BR')
    process_hair_color('RH')
    process_hair_color('S')
    return

def process_hair_color(prefix):
    count = process_and_paste_images(prefix, 'C', 0)
    count = process_and_paste_images(prefix, 'U', count)
    count = process_and_paste_images(prefix, 'R', count)
    process_and_paste_images(prefix, 'L', count)

def process_and_paste_images(prefix, rarity, starting_count) -> int:
    images_path = input_path + '\\' + rarity + '\\' + prefix
    count = starting_count

    # Loop through all files in the input folder
    for filename in os.listdir(images_path):
        if filename.lower().endswith('.png'):
            png_path = os.path.join(images_path, filename)

            try:
                base_img = Image.open(base_texture_path).convert('RGBA')
                png_img = Image.open(png_path).convert('RGBA')

                resized_png = png_img.resize((texture_width, texture_height), Image.Resampling.LANCZOS)
                base_img.paste(resized_png, (512, 0), resized_png)

                output_name = 'bbr_' + prefix.lower() + str(count + 1)

                temp_png = os.path.join(output_dir, f"{output_name}.dds")
                base_img.save(temp_png)

                subprocess.run([
                    'texconv.exe',
                    '-f', 'BC7_UNORM',
                    '-y',  # Overwrite existing
                    '-o', output_dir,  # Output directory
                    temp_png
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                print(f"Successfully processed and saved (BC7): {temp_png}")
                count += 1

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return count

if __name__ == '__main__':
    run()
