# 1. Variables
student_name = "Shrusti"
module_number = 1
print(f"Student: {student_name} | Module: {module_number}")

# 2. Lists & Loops
topics = ["AI Basics", "Machine Learning", "Deep Learning", "Python"]
print("\nModule 01 Topics:")
for topic in topics:
    print("-", topic)

# 3. Functions
def calculate_average(scores):
    return sum(scores) / len(scores)

quiz_scores = [85, 90, 95]
print("\nAverage Score:", calculate_average(quiz_scores))