# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
    return [student for student in student_list if student[2].lower() == major.lower()]

def filter_students_by_major_dict(student_dict, major):
    """
    Return a filtered dictionary of students by major using a dictionary comprehension.
    Filter students whose major matches the given major (case insensitive).
    """
    return {
        sid: details for sid, details in student_dict.items() 
        if details["major"].lower() == major.lower()
    }

def filter_students_by_course(student_dict, course):
    """
    Return a filtered dictionary of students who have enrolled in a specific course.
    Use dictionary comprehension to filter students with the given course in their courses set.
    """
    return {
        sid: details for sid, details in student_dict.items() 
        if course.upper() in details["courses"]
    }