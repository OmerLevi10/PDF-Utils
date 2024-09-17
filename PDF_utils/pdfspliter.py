import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_folder, max_size_mb=20):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)
    
    part_number = 1
    writer = PdfWriter()
    current_size = 0
    
    for page_num in range(total_pages):
        writer.add_page(reader.pages[page_num])
        
        # Write the current writer content to a temporary file to check its size
        temp_output_path = os.path.join(output_folder, f"temp_part_{part_number}.pdf")
        with open(temp_output_path, "wb") as temp_output_file:
            writer.write(temp_output_file)
        
        # Check the size of the temporary file
        current_size = os.path.getsize(temp_output_path) / (1024 * 1024)  # Size in MB
        
        if current_size > max_size_mb:
            # If the size exceeds the limit, save the current writer to a new file and reset
            writer = PdfWriter()  # Reset writer for the next part
            part_number += 1
        else:
            # Remove the temporary file if size is still under limit
            os.remove(temp_output_path)
            
    # Save the last part
    final_output_path = os.path.join(output_folder, f"part_{part_number}.pdf")
    with open(final_output_path, "wb") as final_output_file:
        writer.write(final_output_file)
        
    print(f"PDF split into {part_number} parts.")

# Example usage
input_pdf = "./שגב מסמכים מרוכז.pdf"
output_folder = "./results"
split_pdf(input_pdf, output_folder, 10)
