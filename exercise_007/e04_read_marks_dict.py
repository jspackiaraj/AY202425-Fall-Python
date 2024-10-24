# Read Class Marks from a File# Reading student marks from a file into a dictionary

def read_marks_from_file(filename: str) -> dict:
    marks = {}
    with open(filename, 'r') as file:
        for line in file:
            name, mark = line.split(":")
            marks[name] = int(mark.strip())
    return marks

# Example usage
marks = read_marks_from_file('marks.txt')
print("Student marks:", marks)
