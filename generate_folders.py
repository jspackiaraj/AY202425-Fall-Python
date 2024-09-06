import os

def generate_folders(start, end, directory):
    # Validate the input
    if start > end:
        print("Start number must be less than or equal to end number.")
        return
    
    if start < 1 or end < 1:
        print("Start and end numbers must be positive integers.")
        return

    # Handle optional trailing slash
    if directory.endswith('/'):
        directory = directory[:-1]

    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        return

    # Format folder names and create directories
    for num in range(start, end + 1):
        folder_name = f"exercise_{num:02d}"
        folder_path = os.path.join(directory, folder_name)
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"Created folder: {folder_path}")
        except Exception as e:
            print(f"Error creating folder {folder_path}: {e}")

if __name__ == "__main__":
    # Input start and end numbers, and directory path
    try:
        start_number = int(input("Enter the start number: "))
        end_number = int(input("Enter the end number: "))
        directory_path = input("Enter the directory path (optional trailing slash): ")
        generate_folders(start_number, end_number, directory_path)
    except ValueError:
        print("Please enter valid integers for start and end numbers.")
