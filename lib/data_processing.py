# This module contains functions to process student data.

def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    """
    sid, name, major = student
    return f"ID: {sid}, Name: {name}, Major: {major}"

def display_students(student_list):
    """
    Display all students in a formatted way.
    Loop through the student_list and print each student using format_student_data().
    """
    print("\nStudent Records:")
    for student in student_list:
        print(format_student_data(student))
