# File ka path
file_path = r"E:\f3.txt"

# Khali list of dictionaries
student_list = []

# File ko read karke dictionary mein daalna
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

    # Index variable
    i = 0

    # While loop se har student ke data ko dictionary mein daalna
    while i < len(lines):
        # Check if there are enough lines left for a complete set of student data
        if i + 3 < len(lines):
            # Har line se key aur value alag karna
            roll_line = list(map(str.strip, lines[i].split(':')))
            name_line = list(map(str.strip, lines[i + 1].split(':')))
            section_line = list(map(str.strip, lines[i + 2].split(':')))
            semester_line = list(map(str.strip, lines[i + 3].split(':')))

            # Check karna ki split ke baad ek se jyada elements nahi hain
            if len(roll_line) == 2 and len(name_line) == 2 and len(section_line) == 2 and len(semester_line) == 2:
                roll_key, roll_value = roll_line
                name_key, name_value = name_line
                section_key, section_value = section_line
                semester_key, semester_value = semester_line

                # Dictionary bana kar list mein daalna
                student_data = {
                    roll_key: roll_value,
                    name_key: name_value,
                    section_key: section_value,
                    semester_key: semester_value
                }
                student_list.append(student_data)

            # Agla student ke data ke liye index badhayein
            i += 4
        else:
            # Break out of the loop if there are not enough lines for a complete set of student data
            break

# Banayi gayi list of dictionaries ko print karna
for student_data in student_list:
    print("Student Data:", student_data)

