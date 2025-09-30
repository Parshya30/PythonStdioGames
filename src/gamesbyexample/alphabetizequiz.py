"""Alphabetize Quiz - Advanced Version
By Al Sweigart (improved by ChatGPT)

A time-based quiz game to see how fast you can alphabetize letters, words, or numbers.
Now with multiple difficulty levels, countdown timer, and high-score saving!
"""

import random
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)  # For colored output

# Constants (you can tweak these)
QUESTION_SIZE = 5
QUIZ_DURATION = 30
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = [str(i) for i in range(10)]
HIGHSCORE_FILE = "alphabet_quiz_highscore.txt"


def main():
    showIntro()

    # Difficulty selection
    difficulty = chooseDifficulty()

    # Highscore loading
    highscore = loadHighScore(difficulty)

    input(Fore.CYAN + "\nPress Enter to begin the quiz...")

    startTime = time.time()
    numCorrect = 0
    numAttempted = 0

    while True:
        # Check if time is up
        elapsed = time.time() - startTime
        if elapsed >= QUIZ_DURATION:
            print(Fore.RED + "\nTIME'S UP!")
            break

        # Generate question
        quizLetters = generateQuestion(difficulty)
        print(Fore.YELLOW + " ".join(quizLetters))

        # Countdown display
        remaining = int(QUIZ_DURATION - elapsed)
        print(Fore.MAGENTA + f"[{remaining}s left]")

        response = input("> ").upper().replace(" ", "")
        numAttempted += 1

        if list(response) == sorted(quizLetters):
            print(Fore.GREEN + "   ✅ Correct!\n")
            numCorrect += 1
        else:
            print(Fore.RED + "   ❌ Wrong. Answer was:", "".join(sorted(quizLetters)), "\n")

    # Final score
    accuracy = (numCorrect / numAttempted * 100) if numAttempted else 0
    print(Style.BRIGHT + f"\n⏱ In {QUIZ_DURATION} seconds you attempted {numAttempted} questions.")
    print(Fore.CYAN + f"✔ Correct: {numCorrect}")
    print(Fore.RED + f"✘ Wrong: {numAttempted - numCorrect}")
    print(Fore.YELLOW + f"🎯 Accuracy: {accuracy:.2f}%")

    # Save high score if beaten
    if numCorrect > highscore:
        print(Fore.GREEN + f"🏆 NEW HIGHSCORE! You beat the previous best of {highscore}.")
        saveHighScore(difficulty, numCorrect)
    else:
        print(Fore.CYAN + f"Your highscore for {difficulty} is still {highscore}.")

    print(Fore.BLUE + "\nThanks for playing!")


def showIntro():
    """Prints the intro animation and instructions."""
    slowPrint(ALPHABET, 0.01)
    slowPrint("    Alphabetize Quiz - Advanced", 0.02)
    slowPrint(ALPHABET[::-1], 0.01)
    time.sleep(0.3)

    print('''\nWelcome to the Alphabetize Quiz!
Enter the correct alphabetical (or numerical) order of the shown characters.
Try to get as many correct as possible in the given time!\n''')


def chooseDifficulty():
    """Let the user select difficulty type."""
    print("\nChoose Difficulty:")
    print("1. Letters (easy)")
    print("2. Numbers (medium)")
    print("3. Words (hard)")

    while True:
        choice = input("> ").strip()
        if choice == "1":
            return "letters"
        elif choice == "2":
            return "numbers"
        elif choice == "3":
            return "words"
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


def generateQuestion(difficulty):
    """Generate a question based on difficulty."""
    if difficulty == "letters":
        return random.sample(ALPHABET, QUESTION_SIZE)
    elif difficulty == "numbers":
        return random.sample(NUMBERS, QUESTION_SIZE)
    elif difficulty == "words":
        return random.sample(
            ["CAT", "DOG", "MOON", "TREE", "PYTHON", "ZEBRA", "APPLE", "MANGO", "QUIZ", "CODE"],
            QUESTION_SIZE
        )


def slowPrint(text, pauseAmount=0.1):
    """Slowly print out characters."""
    for character in text:
        print(character, flush=True, end="")
        time.sleep(pauseAmount)
    print()


def loadHighScore(difficulty):
    """Load highscore for selected difficulty."""
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    with open(HIGHSCORE_FILE, "r") as f:
        scores = dict(line.strip().split(":") for line in f if ":" in line)
    return int(scores.get(difficulty, 0))


def saveHighScore(difficulty, score):
    """Save highscore for selected difficulty."""
    scores = {}
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            scores = dict(line.strip().split(":") for line in f if ":" in line)
    scores[difficulty] = str(score)
    with open(HIGHSCORE_FILE, "w") as f:
        for k, v in scores.items():
            f.write(f"{k}:{v}\n")


# Run game
if __name__ == "__main__":
    main()
