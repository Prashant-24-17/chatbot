import pdf2image
from PIL import Image
import  pytesseract
import ollama


doc_img = pdf2image.convert_from_path(r"D:\nvidia_dataaset.pdf" , poppler_path=r"C:\Program Files (x86)\poppler-24.08.0\Library\bin")
# doc_img[0].show()

doc_text = []
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

for page in doc_img:
    text = pytesseract.image_to_string(page)
    doc_text.append(text)
    
    
title_map = {
    "4-12":"Business",
    "13-33":"Risk Factors",
    "34-44":"Financials",
    "45-46":"Directors",
    "47-83":"Data"
}

lst_docs , lst_ids , lst_metadata = [] , [] , []

for n,page in enumerate(doc_text):
    try:
        title = [v for k,v in title_map.items()
                 if n in range(int(k.split("-")[0]), int(k.split("-")[1])+1)][0]
        
        page = page.replace("Table of Contents","")
        
        ## get paragraph
        for i,p in enumerate(page.split('\n\n')):
            if len(p.strip())>5:  ##<--clean paragraph
                lst_docs.append(p.strip())
                lst_ids.append(str(n)+"_"+str(i))
                lst_metadata.append({"title":title})
    except:
        continue
   
# for id,doc,meta in zip(lst_ids[375:378], 
#                        lst_docs[375:378], 
#                        lst_metadata[375:378]):
#     print(id, "-", meta, "\n", doc, "\n") 
    
    

    

def keyword_generator(p, top=3):
    prompt = "summarize the following paragraph in 3 keywords separated by ,: "+p
    res = ollama.generate(model="phi3", prompt=prompt)["response"]
    return res.replace("\n"," ").strip()


## test
p = '''Professional artists, architects and designers use NVIDIA partner products accelerated with our GPUs and software platform for a range of creative and design
use cases, such as creating visual effects in movies or designing buildings and products. In addition, generative Al is expanding the market for our workstation-
class GPUs, as more enterprise customers develop and deploy Al applications with their data on-premises.'''
print(keyword_generator(p))
    

    
    
    
    
    
    
    
    
    
    
    
    
    