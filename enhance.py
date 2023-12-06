import cv2

def sharpen_and_bw(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)

    # Apply Laplacian filter for sharpening
    sharpened = cv2.Laplacian(img, cv2.CV_64F)
    sharpened = cv2.convertScaleAbs(sharpened)

    # Convert the image to black and white (grayscale)
    bw_image = cv2.cvtColor(sharpened, cv2.COLOR_BGR2GRAY)

    # Save the sharpened and black-and-white image
    cv2.imwrite(output_path, bw_image)

if __name__ == "__main__":
    # Replace 'input_image.jpg' and 'output_image.jpg' with your file paths
    input_image_path = 'input_image.jpg'
    output_image_path = 'output_image.jpg'

    sharpen_and_bw(input_image_path, output_image_path)
    print(f"Image processing completed. Sharpened and black-and-white image saved to {output_image_path}")
