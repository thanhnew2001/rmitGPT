import PyPDF2

def pdf_to_text(pdf_file_path, text_file_path):
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text_file.write(page.extract_text())
                text_file.write('\n')  # Add a newline character between pages

# Example usage
pdf_file_path = 'rung.pdf'
text_file_path = 'rung.txt'
pdf_to_text(pdf_file_path, text_file_path)
