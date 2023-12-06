import time
import picamera

def capture_high_quality_image(output_path='high_quality_image.jpg', resolution=(3280, 2464)):
    with picamera.PiCamera() as camera:
        # Set the camera resolution to the maximum supported resolution
        camera.resolution = resolution

        # Wait for the automatic gain control to settle
        time.sleep(2)

        # Capture the image
        camera.capture(output_path)

if __name__ == "__main__":
    # Replace 'high_quality_image.jpg' with your desired output file name
    output_image_path = 'high_quality_image.jpg'

    # Capture a high-quality image
    capture_high_quality_image(output_image_path)
    print(f"High-quality image captured and saved to {output_image_path}")
