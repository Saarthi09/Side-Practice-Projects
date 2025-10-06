def Mark_Present(student_id, name):
    try:
        with open("student_ids.txt", "r") as file:
            student_ids = [line.strip() for line in file.readlines()]
            student_names = [line.strip() for line in file.readlines() [1:]]
    
    except FileNotFoundError:
        print("Error: No student IDs found. Please generate IDs first.")
        return
    
    if student_id not in student_ids:
        print("Invalid Student ID; please check again")
        return
    
    with open("attendance.txt", "a") as file: 
        file.write(f"{student_id} - Present\n")
    print(f"Attendance marked for student ID: {student_names}, {student_id}")

if __name__ == "__main__":
    student_id = input("Enter Student ID: ").strip()
    Mark_Present(student_id)
