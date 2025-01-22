from pdf2image import convert_from_path
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

def ocr_pdf_to_text(pdf_path):
    try:
        images = convert_from_path(pdf_path)
        extracted_text = ""

        for i, image in enumerate(images):
            print(f"Processing page {i + 1}/{len(images)} of {pdf_path}...")
            text = pytesseract.image_to_string(image)
            extracted_text += f"--- Page {i + 1} ---\n"
            extracted_text += text + "\n"
        
        return extracted_text
    except Exception as e:
        print(f"An error occurred while processing {pdf_path}: {e}")
        return ""

def process_pdfs_to_single_file(pdfs_list_path, output_txt_path):
    try:
        with open(pdfs_list_path, 'r') as f:
            pdf_paths = [p.strip() for p in f if p.strip()]
        
        with open(output_txt_path, 'w') as output_file:
            for pdf_path in pdf_paths:
                print(f"Starting OCR for: {pdf_path}")
                text = ocr_pdf_to_text(pdf_path)
                output_file.write(f"--- Contents of {pdf_path} ---\n")
                output_file.write(text)
                output_file.write("\n\n")
        
        print(f"All text successfully extracted and saved to {output_txt_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pdfs_list_path = "PDFs.txt"
    output_txt_path = "combined_output.txt"
    process_pdfs_to_single_file(pdfs_list_path, output_txt_path)