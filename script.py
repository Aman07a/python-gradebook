# last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Step 1: Create Lists for Subjects and Grades
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Step 2: Manually Create a Two-Dimensional List (gradebook)
gradebook = [
    [subjects[0], grades[0]],
    [subjects[1], grades[1]],
    [subjects[2], grades[2]],
    [subjects[3], grades[3]]
]

# Step 5: Append Computer Science Grade
gradebook.append(["computer science", 100])

# Step 6: Append Visual Arts Grade
gradebook.append(["visual arts", 93])

# Step 7: Modify Visual Arts Grade
gradebook[4][1] += 5

# Step 8: Switch Poetry Grade to Pass/Fail
poetry_index = 2
gradebook[poetry_index].remove(85)
gradebook[poetry_index].append("Pass")

# Step 10: Combine Last Semester's Gradebook with Current Gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = last_semester_gradebook + gradebook

# Print gradebook and full_gradebook
print("Gradebook:")
print(gradebook)
print("\nFull Gradebook:")
print(full_gradebook)
