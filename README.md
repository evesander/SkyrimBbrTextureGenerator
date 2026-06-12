## Description

This Python script will allow you to easily generate the override textures for Skyrim Mod BBR Cards (and paintings as they share textures).

Mod in question: https://www.nexusmods.com/skyrimspecialedition/mods/122838

Textures are compressed using BC7 that reduces the filesize but is still compatibile with Skyrim Special Edition.

## Requirements

1. Python 3.12.10+ (preferably the newest) and `pip` installed
2. Download `textconv.exe` from [Microsoft](https://github.com/microsoft/DirectXTex/releases) and place it in the main repo folder (where `bbr_gen.py` is)

## Folder structure

There is an `input` folder provided in the repo with a structure that makes the conversion easier.

It contains various subfolders: `C` (common cards), `U` (uncommon cards), `R` (rare), `L` (legendary)

And each of these folders is divided into "hair color" - `BL` for blondes, `BR` for brunettes, `RH` for redheads and `S` for special.

Keep in mind how many images goes into each subfolder:
1. `C/BL` - 16 images
2. `C/BR` and `C/RH` - 15 images each
3. `C/S` - 4 images
4. `U/BL` - 7 images
5. `U/BR` and `U/RH` - 8 images each
6. `U/S` - 2 images
7. `R/BL` and `R/BR` and `R/RH` - 5 images each
8. `R/S` - 2 images
9. `L/BL` and `L/BR` and `L/RH` and `L/S` - 2 images each

`output` folder however is structured like the mod requires to work - for convinience. Just remember to remove the `.gitkeep` file!

## How to use

1. Prepare 100 photos you want to use as BBR cards - they have to be `.png` due to the code in the script but you can modify the `.py` file and change it
2. Place them into the structured `input` folder provided in the repo - read `Folder structure` section above for more info
3. Make sure you have the `textconv.exe` placed in the folder
4. Run `pip install -r requirements.txt`
5. Run `python bbr_gen.py`
6. Wait a while (conversion takes a second)
7. Done! (the output folder should be full of your new cards!)

## How to upload generated cards as a mod

Just create a `.zip`/`.7z` archive from the `textures` subfolder in the `output` folder and it's ready to be uploaded to NexusMods or something!

> [!WARNING]
> Make sure to remove the `.gitkeep` file from the `output/tetures/clutter/bbr`
