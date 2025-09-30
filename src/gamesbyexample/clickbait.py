import random

# Constants
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']
WEBSITES = ['wobsite', 'blag', 'Facebuuk', 'Googles', 'Facesbook', 'Tweedie', 'Pastagram']


def main():
    print('Clickbait Headline Generator')
    print('By Al Sweigart al@inventwithpython.com\n')

    print("Let's generate some irresistible clickbait headlines to boost those ad clicks!")

    while True:
        number_of_headlines = get_number_of_headlines()
        headlines = [generate_random_headline() for _ in range(number_of_headlines)]

        print("\nHere are your clickbait headlines:\n")
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline}")

        # Optionally save headlines to a file
        if prompt_yes_no("\nWould you like to save these headlines to a file? (y/n): "):
            save_headlines(headlines)

        print()
        website = random.choice(WEBSITES)
        when = random.choice(WHEN).lower()
        print(f"Post these to our {website} {when} or you’re fired!")

        if not prompt_yes_no("\nGenerate more headlines? (y/n): "):
            print("\nThanks for using the Clickbait Headline Generator. Stay sneaky!")
            break


def get_number_of_headlines():
    """Prompt user until a valid number is entered."""
    while True:
        response = input("Enter the number of clickbait headlines to generate: ")
        if response.isdecimal() and int(response) > 0:
            return int(response)
        print("Please enter a positive whole number.")


def prompt_yes_no(prompt):
    """Prompt user with yes/no question, return True for yes."""
    while True:
        response = input(prompt).strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'.")


def save_headlines(headlines):
    """Save the generated headlines to a text file."""
    filename = "clickbait_headlines.txt"
    try:
        with open(filename, 'a') as file:
            file.write('\n'.join(headlines) + '\n')
        print(f"Headlines saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


def generate_random_headline():
    """Randomly pick and generate one of the headline types."""
    clickbait_type = random.randint(1, 10)  # Increased variety with 10 types

    if clickbait_type == 1:
        return generate_are_millenials_killing_headline()
    elif clickbait_type == 2:
        return generate_what_you_dont_know_headline()
    elif clickbait_type == 3:
        return generate_big_companies_hate_her_headline()
    elif clickbait_type == 4:
        return generate_you_wont_believe_headline()
    elif clickbait_type == 5:
        return generate_dont_want_you_to_know_headline()
    elif clickbait_type == 6:
        return generate_gift_idea_headline()
    elif clickbait_type == 7:
        return generate_reasons_why_headline()
    elif clickbait_type == 8:
        return generate_job_automated_headline()
    elif clickbait_type == 9:
        return generate_shocking_truth_headline()
    elif clickbait_type == 10:
        return generate_secret_revealed_headline()


# Headline generator functions

def generate_are_millenials_killing_headline():
    noun = random.choice(NOUNS)
    return f"Are Millennials Killing the {noun} Industry?"


def generate_what_you_dont_know_headline():
    noun = random.choice(NOUNS)
    plural_noun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return f"Without This {noun}, {plural_noun} Could Kill You {when}"


def generate_big_companies_hate_her_headline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f"Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}"


def generate_you_wont_believe_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f"You Won't Believe What This {state} {noun} Found in {pronoun} {place}"


def generate_dont_want_you_to_know_headline():
    plural_noun1 = random.choice(NOUNS) + 's'
    plural_noun2 = random.choice(NOUNS) + 's'
    return f"What {plural_noun1} Don't Want You To Know About {plural_noun2}"


def generate_gift_idea_headline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f"{number} Gift Ideas to Give Your {noun} From {state}"


def generate_reasons_why_headline():
    number1 = random.randint(3, 19)
    plural_noun = random.choice(NOUNS) + 's'
    number2 = random.randint(1, number1)
    return (f"{number1} Reasons Why {plural_noun} Are More Interesting Than You Think "
            f"(Number {number2} Will Surprise You!)")


def generate_job_automated_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]

    if pronoun1 == 'Their':
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong."
    else:
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun1} Job. {pronoun2} Was Wrong."


def generate_shocking_truth_headline():
    noun = random.choice(NOUNS)
    place = random.choice(PLACES)
    return f"The Shocking Truth About {noun}s Hidden in Your {place}"


def generate_secret_revealed_headline():
    state = random.choice(STATES)
    plural_noun = random.choice(NOUNS) + 's'
    return f"Secret Revealed: Why {state} {plural_noun} Are Taking Over the World"


if __name__ == '__main__':
    main()
