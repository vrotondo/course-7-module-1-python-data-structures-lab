# main.py - Student Data Management System

from lib.student_data import students, student_dict
from lib.data_processing import display_students
from lib.filters import filter_students_by_major, filter_students_by_major_dict, filter_students_by_course
from lib.set_operations import unique_majors
from lib.reporting import generate_major_distribution, print_major_distribution, find_common_courses

def main():
    # Part 1: Working with lists and tuples
    print("\n--- STUDENT DATA MANAGEMENT SYSTEM ---")
    print("\n1. All Student Records (Lists & Tuples):")
    display_students(students)
    
    # Part 2: List Comprehensions for filtering
    print("\n2. Filtering with List Comprehensions:")
    cs_students = filter_students_by_major(students, "Computer Science")
    
    if cs_students:
        print(f"\nStudents majoring in Computer Science:")
        display_students(cs_students)
    else:
        print(f"\nNo students found in Computer Science.")
    
    # Part 3: Generator Expressions for memory efficiency
    print("\n3. Memory-Efficient Processing with Generator Expressions:")
    math_students_gen = (student for student in students if student[2] == "Mathematics")
    
    print("\nProcessing Mathematics students lazily:")
    for i, math_student in enumerate(math_students_gen, 1):
        print(f"Math Student {i}: ID: {math_student[0]} | Name: {math_student[1]}")
    
    # Part 4: Dictionary-based student management
    print("\n4. Dictionary-Based Student Management:")
    display_student_details(student_dict)
    
    # Part 5: Dictionary Comprehensions for filtering
    print("\n5. Filtering with Dictionary Comprehensions:")
    cs_students_dict = filter_students_by_major_dict(student_dict, "Computer Science")
    display_student_details(cs_students_dict)
    
    # Part 6: Set operations - add course
    print("\n6. Set Operations - Adding Courses:")
    add_course(student_dict, 101, "CS201")
    display_student_details({101: student_dict[101]})  # Display just the updated student
    
    # Part 7: Course filtering
    print("\n7. Filtering Students by Course:")
    cs101_students = filter_students_by_course(student_dict, "CS101")
    print("\nStudents enrolled in CS101:")
    display_student_details(cs101_students)
    
    # Part 8: Set operations - unique majors
    print("\n8. Unique Majors Using Set Comprehension:")
    unique_major_set = unique_majors(students)
    print(f"Unique Majors: {unique_major_set}")
    
    # Part 9: Reporting features
    print("\n9. Major Distribution Report:")
    distribution = generate_major_distribution(students)
    print_major_distribution(distribution)
    
    # Part 10: Finding common courses using set intersection
    print("\n10. Finding Common Courses:")
    find_common_courses(student_dict, 101, 104)

def display_student_details(student_db):
    """Display student details from a dictionary"""
    for sid, details in student_db.items():
        print(f"ID: {sid} | Name: {details['name']} | Major: {details['major']} | Courses: {details['courses']}")

def add_course(student_db, student_id, new_course):
    """Add a new course to a student's course set"""
    if student_id in student_db:
        student_db[student_id]["courses"].add(new_course)
        print(f"\nAdded {new_course} to {student_db[student_id]['name']}'s courses.")
    else:
        print("\nStudent not found.")

if __name__ == "__main__":
    main()