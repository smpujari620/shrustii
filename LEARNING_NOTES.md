cat << 'EOF' > profile_check.py
name = input("Enter your name: ")
score = int(input("Enter your practice score (0-100): "))

if score >= 50:
    status = "Passed"
else:
    status = "Needs more practice"

print(f"Student: {name} | Score: {score} | Status: {status}")
EOF

cat << 'EOF' > scores_summary.py
scores = [72, 85, 90, 68, 95]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print("Scores:", scores)
print("Total:", total)
print("Average:", average)
EOF

cat << 'EOF' > grade_helper.py
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "D"


for m in [92, 78, 61, 44]:
    print(f"Marks: {m} -> Grade: {get_grade(m)}")
EOF

cat << 'EOF' > number_filter.py
def is_even(num):
    return num % 2 == 0


even_numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == "done":
        break

    number = int(user_input)
    if is_even(number):
        even_numbers.append(number)

print("Collected even numbers:", even_numbers)
EOF

cat << 'EOF' > LEARNING_NOTES.md
# Module 01 Learning Notes: Introduction to AI & Python

## AI, ML & Deep Learning
- **Artificial Intelligence (AI):** Systems designed to perform tasks that normally require human intelligence.
- **Machine Learning (ML):** A subset of AI where models learn patterns from data instead of relying purely on hardcoded rules.
- **Deep Learning:** A subset of ML using multi-layered neural networks, especially effective for unstructured data like text, images, and audio.

## Real-World AI Applications
- Personalized recommendations, speech/image recognition, and AI coding or data analysis assistants.

## Beginner Python Programs Included
- `profile_check.py`: Uses variables, `input()`, and `if`/`else` conditions to evaluate a practice score.
- `scores_summary.py`: Uses a list and a `for` loop to compute total and average scores.
- `grade_helper.py`: Defines a reusable `get_grade()` function with conditional branches.
- `number_filter.py`: Combines a `while` loop, a list, and an `is_even()` helper function to filter user-entered numbers until `done`.
