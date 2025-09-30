import random
import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog

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


def generate_random_headline():
    clickbait_type = random.randint(1, 10)

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


# Headline generators
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


class ClickbaitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Clickbait Headline Generator")

        # Title label
        title = tk.Label(root, text="Clickbait Headline Generator", font=("Arial", 18, "bold"))
        title.pack(pady=10)

        # Instruction label
        instr = tk.Label(root, text="Enter the number of headlines to generate:")
        instr.pack()

        # Input for number of headlines
        self.num_input = tk.Entry(root, width=10, justify='center')
        self.num_input.pack(pady=5)
        self.num_input.insert(0, "5")  # default value

        # Generate button
        generate_btn = tk.Button(root, text="Generate Headlines", command=self.generate_headlines)
        generate_btn.pack(pady=5)

        # ScrolledText widget for output
        self.output_area = scrolledtext.ScrolledText(root, width=70, height=15, wrap=tk.WORD, font=("Helvetica", 12))
        self.output_area.pack(padx=10, pady=10)

        # Save button
        save_btn = tk.Button(root, text="Save Headlines to File", command=self.save_headlines)
        save_btn.pack(pady=5)

        # Quit button
        quit_btn = tk.Button(root, text="Quit", command=root.quit)
        quit_btn.pack(pady=5)

    def generate_headlines(self):
        self.output_area.delete('1.0', tk.END)  # clear previous output
        num_str = self.num_input.get()

        if not num_str.isdecimal() or int(num_str) <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive integer for number of headlines.")
            return

        num = int(num_str)
        headlines = [generate_random_headline() for _ in range(num)]
        for i, hl in enumerate(headlines, start=1):
            self.output_area.insert(tk.END, f"{i}. {hl}\n")

        website = random.choice(WEBSITES)
        when = random.choice(WHEN).lower()
        self.output_area.insert(tk.END, f"\nPost these to our {website} {when} or you’re fired!\n")

    def save_headlines(self):
        content = self.output_area.get('1.0', tk.END).strip()
        if not content:
            messagebox.showinfo("Nothing to Save", "Please generate headlines first before saving.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save Headlines As"
        )
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write(content)
                messagebox.showinfo("Saved", f"Headlines saved to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")


if __name__ == '__main__':
    root = tk.Tk()
    app = ClickbaitGUI(root)
    root.mainloop()
