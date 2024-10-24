# Write Class Marks to a File# Writing a dictionary of student marks to a file

def write_marks_to_file(marks: dict, filename: str):
    with open(filename, 'w') as file:
        for student, mark in marks.items():
            file.write(f"{student}: {mark}\n")

# Example usage
marks = {"Alice": 85, "Bob": 90, "Charlie": 78}
write_marks_to_file(marks, 'marks_output.txt')
