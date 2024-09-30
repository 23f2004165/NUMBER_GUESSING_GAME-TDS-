import random
import tkinter as tk

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x300")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10

        self.label = tk.Label(master, text="Guess a number between 1 and 100:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 14), width=5)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess, font=("Arial", 14))
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < 1 or guess > 100:
                self.result_label.config(text="Please guess a number between 1 and 100.")
                return

            if guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.display_congratulations()
                # The reset_game method is not called here, as we wait for the player's choice

            if self.attempts >= self.max_attempts:
                self.result_label.config(text=f"Game Over! The number was {self.secret_number}.")
                self.reset_game()

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter an integer.")

    def display_congratulations(self):
        congratulation_window = tk.Toplevel(self.master)
        congratulation_window.title("Congratulations!")
        congratulation_window.geometry("400x250")

        message = f"🎉 Hooray! You did it! 🎉\n\n" \
                  f"You guessed the number {self.secret_number} in {self.attempts} attempts!\n\n" \
                  f"You're a guessing genius! 🧠✨\n\n" \
                  f"Would you like to play again?"

        label = tk.Label(congratulation_window, text=message, font=("Arial", 14), justify="center")
        label.pack(pady=20)

        button_frame = tk.Frame(congratulation_window)
        button_frame.pack(pady=20)

        yes_button = tk.Button(button_frame, text="Play Again", command=self.play_again, font=("Arial", 12), width=15)
        yes_button.pack(side=tk.LEFT, padx=20)

        no_button = tk.Button(button_frame, text="Quit", command=self.master.quit, font=("Arial", 12), width=15)
        no_button.pack(side=tk.RIGHT, padx=20)

    def play_again(self):
        self.reset_game()
        # Close the congratulations window
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="Guess a number between 1 and 100:")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
