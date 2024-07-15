try:
    from PIL import Image
except ImportError: 
    import Image # type: ignore
import pytesseract


# Path to your passport image file
passport_image_path = './1.jpg'

# Use Tesseract OCR to extract text
extracted_text = pytesseract.image_to_string(Image.open(passport_image_path))

# Print the extracted text (you might need to refine this to extract the series)
print("Extracted Text:")
print(extracted_text)
