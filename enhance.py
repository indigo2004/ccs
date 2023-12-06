import cv2
import numpy as np

def enhance_image(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)

    # Apply Laplacian filter for sharpening
    sharpened = cv2.Laplacian(img, cv2.CV_64F)
    sharpened = np.uint8(np.absolute(sharpened))

    # Adjust brightness and contrast using histogram equalization
    hsv = cv2.cvtColor(sharpened, cv2.COLOR_BGR2HSV)
    hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2])
    enhanced_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Save the enhanced image
    cv2.imwrite(output_path, enhanced_img)

if __name__ == "__main__":
    # Replace 'input_image.jpg' and 'enhanced_image.jpg' with your file paths
    input_image_path = 'input_image.jpg'
    output_image_path = 'enhanced_image.jpg'

    enhance_image(input_image_path, output_image_path)
    print(f"Image processing completed. Enhanced image saved to {output_image_path}")
