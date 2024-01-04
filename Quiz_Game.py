# Sample question data
questions = [
    {
        "type": "multiple_choice",
        "question": "What is the capital of France?",
        "choices": {
            "a": "Berlin",
            "b": "London",
            "c": "Paris",
            "d": "Rome"
        },
        "answer": "c"
    },
    {
        "type": "fill_in_the_blank",
        "question": "The largest planet in our solar system is ___.",
        "answer": "Jupiter"
    }
]

# Game logic
score = 0
for question in questions:
    print(question["question"])
    if question["type"] == "multiple_choice":
        for choice, letter in question["choices"].items():
            print(f"{letter}: {choice}")
        user_answer = input("> ").lower()
    else:
        user_answer = input("> ")

    if user_answer == question["answer"]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
        if question["type"] == "fill_in_the_blank":
            print(f"The correct answer is: {question['answer']}")

# Final score and replay
print(f"Final score: {score}")
play_again = input("Play again? (y/n) ").lower() == "y"
if play_again:
    # Reset score and repeat the game
    score = 0
    continue
else:
    print("Thank you for playing!")
