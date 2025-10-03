import os
import pandas as pd


def create_folders_from_excel(/Users/adityaaggarwal/Downloads/Book2.xlsx, , output_dir):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Extract unique names from the specified column
    unique_names = df[column_name].unique()

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create folders based on unique names
    for name in unique_names:
        folder_path = os.path.join(output_dir, str(name))
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")


# Example usage
if __name__ == "__main__":
    # Path to the Excel file
    excel_file_path = "path/to/your/excel_file.xlsx"

    # The column name which contains the folder names
    column_name = "YourColumnName"

    # Output directory where folders will be created
    output_dir = "path/to/output_directory"

    create_folders_from_excel(excel_file_path, column_name, output_dir)
