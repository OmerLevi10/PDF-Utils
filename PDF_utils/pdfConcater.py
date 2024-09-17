import os
from PyPDF2 import PdfReader, PdfWriter

def concatenate_pdfs(input_directory, output_pdf):
    # Create a PdfWriter object to combine PDFs
    writer = PdfWriter()

    # Get a list of all PDF files in the input directory
    pdf_files = [f for f in os.listdir(input_directory) if f.endswith('.pdf')]
    pdf_files.sort()  # Optional: Sort the files by name

    # Iterate through the PDF files and add each one to the writer
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_directory, pdf_file)
        reader = PdfReader(pdf_path)
        
        # Add each page to the writer
        for page in reader.pages:
            writer.add_page(page)
    
    # Write the combined PDF to the output file
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    
    print(f"All PDF files in '{input_directory}' have been concatenated into '{output_pdf}'.")

# Example usage
input_directory = "./concat_files"  # Replace with the path to your directory containing PDF files
output_pdf = "./concat_results/combined_output.pdf"          # Replace with the desired output PDF file name
concatenate_pdfs(input_directory, output_pdf)
