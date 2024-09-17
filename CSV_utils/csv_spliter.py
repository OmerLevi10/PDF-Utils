import csv

def split_csv(file_path, rows_per_file):
    """
    Splits a CSV file into smaller files with a specified number of rows.
    
    Parameters:
    - file_path: the path to the original CSV file.
    - rows_per_file: maximum number of rows per smaller CSV file.
    """
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Assuming the first row is the header
        
        file_count = 1
        rows = []
        
        for i, row in enumerate(reader, start=1):
            rows.append(row)
            if i % rows_per_file == 0:
                # Write the current rows to a new smaller file
                output_file = f'{file_path[:-4]}_part{file_count}.csv'
                with open(output_file, 'w', newline='') as output_csv:
                    writer = csv.writer(output_csv)
                    writer.writerow(header)
                    writer.writerows(rows)
                
                rows = []
                file_count += 1
        
        # Write any remaining rows to the last file
        if rows:
            output_file = f'{file_path[:-4]}_part{file_count}.csv'
            with open(output_file, 'w', newline='') as output_csv:
                writer = csv.writer(output_csv)
                writer.writerow(header)
                writer.writerows(rows)

    print(f"CSV has been split into {file_count} files.")

# Example usage:
split_csv('large_file.csv', 1000)  # Splits the file into smaller files with 1000 rows each
