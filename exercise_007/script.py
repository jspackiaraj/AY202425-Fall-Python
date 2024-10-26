import os

# Define the directory where the script is stored as the base directory
base_directory = os.path.dirname(os.path.abspath(__file__))

# Exercise details: filename, title, and description
exercises = [
    ("e01_read_matrix.py", "Read Matrix Data from a File", "Reads matrix data from a file and stores it as a list of lists."),
    ("e02_write_matrix.py", "Write Matrix Data to a File", "Writes matrix data to a file, where each row represents a list."),
    ("e03_append_data.py", "Append Data to a File", "Appends new data to an existing file."),
    ("e04_read_marks_dict.py", "Read Class Marks from a File", "Reads student marks from a file and stores them in a dictionary."),
    ("e05_write_marks_dict.py", "Write Class Marks to a File", "Writes a dictionary of student marks to a file."),
    ("e06_sequential_access.py", "Sequential File Access", "Reads each line in a file sequentially."),
    ("e07_random_access.py", "Random File Access", "Accesses a specific line from a file based on line number."),
    ("e08_binary_file_write_read.py", "Binary File Write and Read", "Writes and reads binary files using Python's pickle module."),
    ("e09_append_dict_to_file.py", "Append Dictionary Data to a File", "Appends dictionary data to a file."),
    ("e10_read_write_nodes.py", "Read and Write Node Information", "Reads and writes node information stored as dictionaries in a file."),
    ("e11_read_beam_data.py", "Read Beam Data from a File", "Reads beam data with IDs and associated values from a file."),
    ("e12_total_force.py", "Calculate Total Force from a File", "Calculates total force by summing values in a file."),
    ("e13_beam_forces.py", "Write and Read List of Beam Forces", "Writes a list of beam forces to a file and reads them back."),
    ("e14_append_forces.py", "Append Beam Forces to a File", "Appends beam force values to a file."),
    ("e15_beam_deflection_csv.py", "Read and Write Beam Deflection Data (CSV)", "Writes and reads beam deflection data in CSV format."),
]

# URLs for additional resources
main_page_url = "https://jsp.shiksha/index.php/portfolio/bcse101e-computer-programming-python/files-and-file-handling-python"
exercise_page_url = f"{main_page_url}/programming-exercises-007"

# Function to generate .md content for each exercise
def generate_md_content(filename, title, description):
    return f"""# {title}

## Problem Description
{description}

This program demonstrates file handling techniques in Python, specifically designed to perform operations like reading, writing, and appending data in files.

## Solution Link
The Python solution for this problem is available in [{filename}](./{filename}).

## Additional Resources
For a detailed explanation of file handling concepts, please visit the [Files and File Handling in Python]({main_page_url}) page.

For related exercises and questions, refer to the [Programming Exercises 007]({exercise_page_url}) page.

Happy coding!
"""

# Create or replace each .md file
for filename, title, description in exercises:
    md_filename = os.path.splitext(filename)[0] + ".md"
    md_filepath = os.path.join(base_directory, md_filename)
    
    # Delete existing .md file if it exists
    if os.path.exists(md_filepath):
        os.remove(md_filepath)
    
    # Write new content to the .md file
    with open(md_filepath, "w") as md_file:
        md_file.write(generate_md_content(filename, title, description))

print("Markdown files have been created successfully in the script's directory.")
