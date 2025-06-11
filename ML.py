# Input marks for 5 subjects
print("Enter marks out of 100:")

math = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))
history = int(input("History: "))
computer = int(input("Computer: "))

# Calculate total and percentage
total = math + science + english + history + computer
percentage = total / 5

# Determine grade
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'F'

# Show output
print("\n--- Result ---")
print(f"Total Marks: {total}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
