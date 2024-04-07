from pdf2image import convert_from_path
import pytesseract
import numpy as np
import cv2
from PIL import Image
import utils
from parser_prescription import Prescriptionparser
from parser_patient_details import PatientDetailsparser

POPPLER_PATH = r'C:\poppler-24.02.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Function to extract the data
def extract_data(file_path,file_format):
    #step 1: extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''

    if len(pages)>0:
        page = pages[0]
        processed_image = utils.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    
    if file_format == 'prescription':
        extract_data  = Prescriptionparser(document_text).parse()
    elif file_format == 'patient_details':
        extract_data  = PatientDetailsparser(document_text).parse()

    return extract_data
#Main function
if __name__=='__main__':
    data = extract_data(r'C:\Users\Vishal Sujay Kumar\Desktop\Codewithbasics\Python\Medical data extraction\Project\backend\resources\prescription\pre_1.pdf','prescription')
    print(data)
