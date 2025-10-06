import random

def generate_studentid():
    return random.randint(100000,999999)


def save_student_id(student_id, name):
    with open("student_ids.txt", "a") as file:
        file.write(f"{student_id}, {name} \n")

if __name__ == "__main__":
    name = input("Please enter your first name: ").strip()  

    student_id = generate_studentid()

    print(f"Generated Student ID for {name}: {student_id}")
    save_student_id(student_id, name)
    print("Student ID saved successfully")
