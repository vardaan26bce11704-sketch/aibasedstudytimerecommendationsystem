

print("=" * 60)
print("       AI BASED STUDY TIME RECOMMENDATION SYSTEM")
print("=" * 60)

def get_integer(message, minimum, maximum):
    while True:
        try:
            value = int(input(message))

            if minimum <= value <= maximum:
                return value

            print(f"Please enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input! Please enter a number.")

def get_float(message, minimum, maximum):
    while True:
        try:
            value = float(input(message))

            if minimum <= value <= maximum:
                return value

            print(f"Please enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input! Please enter a number.")

print("\nEnter Student Information")
print("-" * 40)

name = input("Enter your name: ")

available_time = get_integer(
    "Available study time today (hours): ", 1, 15
)

subjects = get_integer(
    "Number of subjects to study: ", 1, 10
)

difficulty = get_integer(
    "Average subject difficulty (1-10): ", 1, 10
)

preparation = get_integer(
    "Your preparation level (1-10): ", 1, 10
)

exam_days = get_integer(
    "Days remaining for next exam: ", 1, 100
)

sleep = get_float(
    "Hours of sleep last night: ", 1, 12
)

focus = get_integer(
    "Current concentration level (1-10): ", 1, 10
)

previous_score = get_float(
    "Previous average score (0-100): ", 0, 100
)
base_time = available_time * 60

if difficulty >= 8:
    difficulty_factor = 1.30
elif difficulty >= 5:
    difficulty_factor = 1.15
else:
    difficulty_factor = 1.00

if preparation <= 3:
    preparation_factor = 1.30
elif preparation <= 6:
    preparation_factor = 1.15
else:
    preparation_factor = 0.95

if exam_days <= 3:
    urgency_factor = 1.40
elif exam_days <= 7:
    urgency_factor = 1.25
elif exam_days <= 15:
    urgency_factor = 1.10
else:
    urgency_factor = 0.95

if sleep < 5:
    sleep_factor = 0.75
elif sleep < 7:
    sleep_factor = 0.90
else:
    sleep_factor = 1.00

if focus <= 3:
    focus_factor = 0.75
elif focus <= 6:
    focus_factor = 0.90
else:
    focus_factor = 1.00

if previous_score < 40:
    performance_factor = 1.30
elif previous_score < 60:
    performance_factor = 1.20
elif previous_score < 75:
    performance_factor = 1.05
else:
    performance_factor = 0.95

recommended_time = (
    base_time
    * difficulty_factor
    * preparation_factor
    * urgency_factor
    * sleep_factor
    * focus_factor
    * performance_factor
)

maximum_time = available_time * 60
if recommended_time > maximum_time:
    recommended_time = maximum_time
if recommended_time < 30:
    recommended_time = 30

priority_score = (
    difficulty * 10
    + (10 - preparation) * 10
    + (10 - min(exam_days, 10)) * 5
    + (100 - previous_score) * 0.2
)

if priority_score >= 180:
    priority = "VERY HIGH"
elif priority_score >= 130:
    priority = "HIGH"
elif priority_score >= 80:
    priority = "MEDIUM"
else:
    priority = "LOW"


if focus <= 4:
    technique = "Pomodoro: 25 minutes study + 5 minutes break"
elif difficulty >= 8:
    technique = "50 minutes study + 10 minutes break"
else:
    technique = "45 minutes study + 10 minutes break"

if preparation <= 3:
    strategy = "Start with basic concepts and fundamentals."
elif difficulty >= 8:
    strategy = "Focus on difficult concepts and practice problems."
elif previous_score < 50:
    strategy = "Revise weak topics and solve previous questions."
else:
    strategy = "Balance revision, practice and new concepts."


time_per_subject = recommended_time / subjects


print("\n")
print("=" * 60)
print("                 AI RECOMMENDATION")
print("=" * 60)

print(f"Student Name       : {name}")
print(f"Recommended Time   : {recommended_time:.0f} minutes")
print(f"Recommended Hours  : {recommended_time / 60:.2f} hours")
print(f"Priority Level     : {priority}")
print(f"Time Per Subject   : {time_per_subject:.0f} minutes")
print(f"Study Technique    : {technique}")
print(f"Study Strategy     : {strategy}")

print("\nPersonalized Advice")
print("-" * 40)
if sleep < 6:
    print("• Try to improve your sleep before long study sessions.")

if focus < 5:
    print("• Keep your phone away and use short focused sessions.")

if difficulty >= 8:
    print("• Give extra attention to difficult chapters.")

if preparation <= 4:
    print("• Spend the first session building your basic concepts.")

if exam_days <= 3:
    print("• Your exam is very close. Prioritize important topics.")

if previous_score < 50:
    print("• Focus strongly on your weak areas.")

if previous_score >= 80:
    print("• Maintain your performance with regular revision.")

if sleep >= 7 and focus >= 7:
    print("• Your current conditions are suitable for focused study.")

print("\nSuggested Study Schedule")
print("-" * 40)
remaining = recommended_time
session = 1
while remaining > 0:
    if remaining >= 50:
        session_time = 50
    else:
        session_time = remaining
    print(
        f"Session {session}: Study for "
        f"{session_time:.0f} minutes"
    )
    if remaining - session_time > 0:
        print("           Take a 10-minute break")
    remaining -= session_time
    session += 1

print("\n")
print("=" * 60)
print("FINAL RECOMMENDATION")
print("=" * 60)
print(
    f"{name}, your recommended study time today is "
    f"{recommended_time:.0f} minutes."
)
print(
    f"Your study priority is {priority}."
)
print(
    "Use the suggested sessions and take regular breaks."
)
print("\nThank you for using the AI Study Time Recommendation System!")
print("=" * 60)