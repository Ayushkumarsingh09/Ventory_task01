import cv2

def add_text_to_certificate(candidate_name):
    # Define certificate image path
    certificate_image_path = 'path_to_your_blank_certificate.png'  # Replace with your file path
    y = 725  # y-coordinate for the text placement
    font_scale = 4  # Font size
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX  # Font style
    thickness = 4  # Font weight
    color = (0, 0, 0)  # Font color (black)

    # Load the certificate image
    image = cv2.imread(certificate_image_path)
    if image is None:
        raise FileNotFoundError(f"Cannot load image from {certificate_image_path}")

    # Get image dimensions
    (image_height, image_width) = image.shape[:2]

    # Get the text size for centering the text
    text_size = cv2.getTextSize(candidate_name, font, font_scale, thickness)[0]
    text_x = (image_width - text_size[0]) // 2  # Center the text horizontally

    # Add text to the image
    cv2.putText(image, candidate_name, (text_x, y), font, font_scale, color, thickness)

    # Save the image
    png_output_path = f"certificate_with_name.png"
    cv2.imwrite(png_output_path, image)

    return png_output_path

# Generate the certificate with the name "Ayush Kumar Singh"
png_output_path = add_text_to_certificate("Ayush Kumar Singh")
print(f"Certificate saved at: {png_output_path}")
