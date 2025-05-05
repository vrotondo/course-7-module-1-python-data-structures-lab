# This module provides reporting features for student data

def generate_major_distribution(student_list):
    """
    Generate a report showing the distribution of students across majors.
    Returns a dictionary with major as key and count as value.
    """
    distribution = {}
    
    for student in student_list:
        major = student[2]
        distribution[major] = distribution.get(major, 0) + 1
    
    return distribution

def print_major_distribution(distribution):
    """Print the major distribution in a formatted way"""
    print("\nStudent Distribution by Major:")
    print("-" * 30)
    for major, count in distribution.items():
        print(f"{major}: {count} student(s)")
    print("-" * 30)
    
def find_common_courses(student_dict, student_id1, student_id2):
    """Find common courses between two students using set intersection"""
    if student_id1 in student_dict and student_id2 in student_dict:
        courses1 = student_dict[student_id1]["courses"]
        courses2 = student_dict[student_id2]["courses"]
        common = courses1.intersection(courses2)
        
        if common:
            print(f"\nCommon courses between {student_dict[student_id1]['name']} and {student_dict[student_id2]['name']}:")
            for course in common:
                print(f"- {course}")
        else:
            print(f"\nNo common courses found between {student_dict[student_id1]['name']} and {student_dict[student_id2]['name']}.")
    else:
        print("\nOne or both student IDs not found.")