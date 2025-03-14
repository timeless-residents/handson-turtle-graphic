from PIL import Image
import os

# Input and output paths
input_path = "/Users/studio/work/github/handson-turtle-graphic/turtle.png"
output_path = (
    "/Users/studio/work/github/handson-turtle-graphic/shorwoom/usecase-017/turtle.gif"
)

# Check if input file exists
if not os.path.exists(input_path):
    print(f"Error: Input file {input_path} does not exist")
    exit(1)

try:
    # Open the PNG image
    img = Image.open(input_path)

    # Convert and save as GIF
    img.save(output_path, "GIF")

    print(f"Successfully converted {input_path} to {output_path}")
except Exception as e:
    print(f"Error converting image: {e}")
