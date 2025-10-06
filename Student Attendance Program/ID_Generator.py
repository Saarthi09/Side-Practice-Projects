import random

def generate_studentid():
    return random.randint(100000,999999)

def save_student_id(student_id):
    with open("student_ids.txt", "a") as file:
        file.write(str(student_id)+ "\n")

if __name__ == "__main__":
    student_id = generate_studentid()
    print(f"Generated Student ID: {student_id}")
    save_student_id(student_id)
    print("Student ID saved successfully")
