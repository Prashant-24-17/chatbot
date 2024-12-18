import pdf2image
from PIL import Image
import  pytesseract

doc_img = pdf2image.convert_from_path(r"D:\nvidia_dataaset.pdf" , poppler_path=r"C:\Program Files (x86)\poppler-24.08.0\Library\bin")
# doc_img[0].show()

doc_text = []
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

for page in doc_img:
    text = pytesseract.image_to_string(page)
    doc_text.append(text)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    