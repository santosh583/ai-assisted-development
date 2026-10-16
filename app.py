
def greet_student(name):
    """Return a welcome message for a student."""
    return f"Hello, {name}! Welcome to AI-Assisted Development."


def main():
    student_name = input("Enter your name: ").strip()

    if not student_name:
        student_name = "Student"

    print(greet_student(student_name))
    print("Today we are learning Git and GitHub!")
    print("Project updated successfully!")



if __name__ == "__main__":
    main()
