import pdfplumber
import fitz
def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
        return text

# print(extract_text_from_pdf("47303.pdf").split("\n"))  # Example usage, replace with your PDF path







# def extract_text_from_pdf(pdf_path):
#     """Extracts text from a PDF file using PyMuPDF.

#     Args:
#         pdf_path (str): Path to the PDF file.

#     Returns:
#         str: Extracted text from the PDF.
#     """
#     doc = fitz.open(pdf_path)
#     paragraph = []
#     buffer = []
#     for page in doc:
#         blocks = page.get_text("blocks")
#         for block in blocks:
#             text = block[4].split()
#             if (len(text) + len(buffer))< 20:
#                 buffer.extend(text)
#             elif (len(buffer) + len(text)) > 20:
#                 sentence = " ".join(buffer)
#                 paragraph.append(f"{sentence} {" ".join(text)}")
#                 buffer = []
#             else:
#                 buffer.extend(text)
#         # else:
#         #     paragraph.append(" ".join(text))
#     return paragraph




# print([len(chunk) for chunk in extract_text("47303.pdf")])  # Example usage, replace with your PDF path