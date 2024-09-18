import pandas as pd

def csv_to_xlsx(csv_file_path, xlsx_file_path):
    """
    Converts a CSV file to an Excel XLSX file.
    
    Parameters:
    - csv_file_path: The path to the source CSV file.
    - xlsx_file_path: The path where the converted XLSX file will be saved.
    """
    df = pd.read_csv(csv_file_path)

    df.to_excel(xlsx_file_path, index=False)
    
    print(f"File has been converted from {csv_file_path} to {xlsx_file_path}")

csv_to_xlsx('./CSV_utils/soldiers_mikun_details_part3.csv', 'soldiers_mikun_details_part3.xlsx')
