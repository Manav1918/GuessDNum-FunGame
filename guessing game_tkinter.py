import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Meter
import random
from playsound import playsound
import threading
import os

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("🎯 Number Guessing Game")
        master.geometry("400x500")
        #master.configure(bootstyle="info")

        self.max_attempts = 10
        self.remaining_attempts = self.max_attempts
        self.number_to_guess = random.randint(1, 100)
        self.soundeffectspath = os.path.join(os.path.dirname(__file__), "sounds")
        self.sep = os.path.abspath(self.soundeffectspath)

        # Title
        self.title_label = tb.Label(master, text="🎯 Guess the Number!", font=("Helvetica", 20, "bold"), bootstyle="info")
        self.title_label.pack(pady=10)

        # Instruction
        self.label = tb.Label(master, text="Enter a number between 1 and 100:", font=("Helvetica", 12))
        self.label.pack(pady=5)

        # Entry
        self.entry = tb.Entry(master, font=("Helvetica", 14), justify='center', width=10)
        self.entry.pack(pady=5)

        # Guess Button
        self.guess_button = tb.Button(master, text="Guess", bootstyle=SUCCESS, command=self.check_guess)
        self.guess_button.pack(pady=10)

        # Result Label
        self.result_label = tb.Label(master, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=5)

        # Circular Progress Meter
        self.meter = Meter(
            master,
            bootstyle="info",
            subtext="Tries Left",
            interactive=False,
            textright=f" / {self.max_attempts}",
            metertype="full",
            amounttotal=self.max_attempts,
            amountused=self.max_attempts,
            stripethickness=10,
            textfont=("Helvetica", 16, "bold")
        )
        self.meter.pack(pady=20)

        # Reset Button
        self.reset_button = tb.Button(master, text="Reset Game", bootstyle=DANGER, command=self.reset_game)
        self.reset_button.pack(pady=10)

        # Bind Enter key to guess
        self.entry.bind('<Return>', lambda event: self.check_guess())  # ✅ Bind Enter key to guess

        # Bind Ctrl+R to reset
        master.bind('<Control-r>', lambda event: self.reset_game()) # ✅ Bind Ctrl+R to reset
        # Bind ESc to quit
        master.bind('<Escape>', lambda event: master.quit()) # ✅ Bind Esc to quit

    def play_sound(self, sound_file):
        full_path = os.path.abspath(sound_file)
        threading.Thread(target=playsound, args=(full_path,), daemon=True).start()

    def check_guess(self):
        if self.remaining_attempts <= 0:
            self.result_label.config(text="❌ No attempts left! Click Reset to play again.")
            return

        try:
            guess = int(self.entry.get())
            self.remaining_attempts -= 1
            #self.meter.configure(amountused=self.max_attempts - self.remaining_attempts)
            self.meter.configure(amountused=self.remaining_attempts)


            if guess < self.number_to_guess:
                self.result_label.config(text="📉 Too low!")
                self.play_sound(self.sep + "/low.mp3")
            elif guess > self.number_to_guess:
                self.result_label.config(text="📈 Too high!")
                self.play_sound(self.sep + "/high.mp3")
            else:
                self.result_label.config(text=f"🎉 Correct! You guessed it in {self.max_attempts - self.remaining_attempts} tries.")
                self.play_sound(self.sep + "/wow.mp3")
                self.disable_game()
                return

            if self.remaining_attempts == 0:
                self.result_label.config(text=f"❌ Out of tries! The number was {self.number_to_guess}.")
                self.play_sound(self.sep + "/reset.mp3")
                self.disable_game()

        except ValueError:
            self.result_label.config(text="⚠️ Please enter a valid number.")

    def disable_game(self):
        self.entry.config(state='disabled')
        self.guess_button.config(state='disabled')

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.remaining_attempts = self.max_attempts
        #self.meter.configure(amountused=0)
        self.meter.configure(amountused=self.max_attempts)

        self.entry.config(state='normal')
        self.guess_button.config(state='normal')
        self.entry.delete(0, 'end')
        self.result_label.config(text="🔄 Game reset. Guess again!")
        self.play_sound(self.sep + "/reset.mp3")

# Launch the app with ttkbootstrap
app = tb.Window(themename="flatly")
game = GuessingGame(app)
app.mainloop()
