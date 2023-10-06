from PIL import Image
from pytesseract import pytesseract

def read_text_from_image(image):
  # Defining paths to tesseract.exe
  path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  pytesseract.tesseract_cmd = path_to_tesseract
    
  text = pytesseract.image_to_string(image)
  return text[:-1]
    
if __name__ == "__main__":
  image_path = r"./pics/text_area.png"
  img = Image.open(image_path)
  text = read_text_from_image(img)
  print(text)


