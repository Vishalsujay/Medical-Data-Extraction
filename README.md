# Automated Medical Data Extraction

## Description

The Automated Medical Data Extraction project is a Python-based solution designed to streamline the extraction of patient details and prescription information from medical documents stored in PDF format. Leveraging a combination of image processing techniques, optical character recognition (OCR), and FastAPI integration, this project aims to enhance efficiency and accuracy in healthcare administration processes.

## Key Components

- **PDF Preprocessing**: Utilizes the pdf2image library to convert PDF documents into image files for further processing.
- **Image Enhancement**: Employs OpenCV's adaptive thresholding techniques to enhance document clarity and readability.
- **Data Extraction**: Utilizes Pytesseract for OCR to extract patient details and prescription information from preprocessed images.
- **Regex Extraction**: Implements regular expressions to precisely extract specific data fields from OCR output.
- **FastAPI Integration**: Serves extracted data via a FastAPI-powered RESTful API for seamless integration with healthcare systems and applications.

## Installation

1. Clone the repository:

2. Install dependencies:
   pip install -r requirements.txt

## Usage

1. Place PDF documents containing medical data in the designated input directory.
2. Run the extraction script:
3. Access extracted data via the provided FastAPI endpoint.

## Benefits

- **Efficiency**: Reduces manual data entry tasks, increasing operational efficiency.
- **Accuracy**: Ensures accurate extraction of patient information and prescription details.
- **Interoperability**: Facilitates integration with existing healthcare systems via FastAPI.
- **Cost-Effectiveness**: Minimizes labor costs associated with manual data entry.

## Target Audience

Healthcare professionals, medical administrators, and software developers involved in healthcare technology solutions.


## Acknowledgements

- [pdf2image](https://github.com/Belval/pdf2image)
- [OpenCV](https://opencv.org/)
- [Pytesseract](https://github.com/madmaze/pytesseract)
- [FastAPI](https://fastapi.tiangolo.com/)
