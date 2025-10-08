# ---Quiz Game Program---

print("Welcome to the Quiz Game!")

name = input("Enter your name: ").strip()
play = input(f"Hello {name}, Do you want to play the quiz? (yes/no): ").lower().strip()

if play.lower() == "yes":
    print("Good, let,s start the game!")
    
elif play.lower() == "no":
    print("Thanks for visiting")
    quit()
    
else:
    print("Invalid input please type yes or no")
    quit()


# Step 1: Questions, Options, and Answers
questions = [
    ("What is the capital of Pakistan?",
     ["A. Karachi", "B. Lahore", "C. Islamabad", "D. Peshawar"],
     "C"),

    ("Which brakets are used to creat a list in Python?",
     ["A. <>", "B. []", "C. {}", "D. ()"],
     "B"),

    ("Which animal is known as the King of the Jungle?",
     ["A. Tiger", "B. Elephant", "C. Lion", "D. Fox"],
     "C"),
    
    ("What is 5 + 6 =?",
     ["A. 9", "B. 11", "C. 10", "D. 12"],
     "B"),
    
    ("What is the nationla game of Pakistan?",
     ["A. Circket", "B. Football", "C. Tanis", "D. Hockey"],
     "D")
]

# Step 2: Initialize score
score = 0

# Step 3: Loop through questions using enumerate()
for i, qdata in enumerate(questions, start=1):
    question, options, correct_answer = qdata
    print(f"\nQ.{i}: {question}")

    # Display options
    for opt in options:
        print(opt)

    # Take user input
    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    # Check if correct
    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f" Wrong! The correct answer was {correct_answer}")

# Step 4: Final Score


# --- Final Result ---
print("\n--- Quiz Finished ---")
print(f"{name}, your total score is {score}/{len(questions)}")
print("Thank you for playing!")
quit()