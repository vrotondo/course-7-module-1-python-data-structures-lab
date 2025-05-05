# This module initializes student records.

# Define a list of students stored as tuples (ID, Name, Major)
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
    (106, "Frank Miller", "Biology"),
    (107, "Grace Taylor", "Chemistry"),
    (108, "Henry Brown", "Physics"),
    (109, "Isabel Garcia", "Computer Science"),
    (110, "Jack Thompson", "Mathematics")
]

# Dictionary representation of students with more details
student_dict = {
    101: {"name": "Alice Johnson", "major": "Computer Science", "courses": {"CS101", "CS102"}},
    102: {"name": "Bob Smith", "major": "Mathematics", "courses": {"MATH101", "MATH102"}},
    103: {"name": "Charlie Davis", "major": "Physics", "courses": {"PHYS101", "PHYS102"}},
    104: {"name": "David Wilson", "major": "Computer Science", "courses": {"CS101", "CS201"}},
    105: {"name": "Eve Lewis", "major": "Mathematics", "courses": {"MATH101", "MATH201"}}
}