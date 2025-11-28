from PIL import Image
import numpy as np

def xor_images(img1_path, img2_path, output_path="xor_output.png"):
    # Load images
    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")

    # Resize second image to match first image if needed
    if img1.size != img2.size:
        img2 = img2.resize(img1.size)

    # Convert images to NumPy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # XOR operation (pixel-wise XOR)
    xor_result = np.bitwise_xor(arr1, arr2)

    # Convert back to image
    xor_image = Image.fromarray(xor_result.astype('uint8'), "RGB")
    xor_image.save(output_path)

    print(f"XOR image saved as: {output_path}")

# Example usage
xor_images("1.png", "3.png", "2.png")
