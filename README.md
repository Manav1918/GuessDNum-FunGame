
````markdown
# 🎯 Number Guessing Game
````
A fun and interactive number guessing game built with Python and [ttkbootstrap](https://ttkbootstrap.readthedocs.io/) for a modern Tkinter GUI.  
Guess the secret number between 1 and 100 within 10 tries!

---

## 🚀 Features

- 🎨 **Modern, themed interface** using `ttkbootstrap`
- 🔄 **Circular progress meter** showing remaining attempts
- 🔊 **Sound effects** for correct, incorrect, and reset actions
- ⌨️ **Keyboard shortcuts**:
  - <kbd>Enter</kbd>: Submit guess
  - <kbd>Ctrl</kbd> + <kbd>R</kbd>: Reset game
  - <kbd>Esc</kbd>: Quit game

---

## 📸 Screenshots

![Game Screenshot](![image](https://github.com/user-attachments/assets/d5a9575a-4b38-40ff-926f-71398d17ebba)
)

---

## 📦 Requirements

- Python 3.7+
- [`ttkbootstrap`](https://pypi.org/project/ttkbootstrap/)
- [`playsound`](https://pypi.org/project/playsound/)

---

## 🛠 Installation

1. **Clone the repository**:

````bash
   git clone https://github.com/manav1918/guessDNum-FunGame.git
   cd number-guessing-game
````

2. **Install dependencies**:

````bash
   pip install ttkbootstrap playsound
````

3. **Prepare sound files**:
   Ensure the `sounds` folder exists in the same directory as `guessing game_tkinter.py` with the following structure:

   ```
   sounds/
   ├── low.mp3
   ├── high.mp3
   ├── wow.mp3
   └── reset.mp3
   ```

---

## ▶️ Usage

Run the game using:

```bash
python guessing game_tkinter.py
```

---

## 🎮 How to Play

1. Enter a number between 1 and 100.
2. Click **Guess** or press <kbd>Enter</kbd>.
3. The game will indicate if your guess is too high, too low, or correct.
4. You have **10 attempts** to guess the number.
5. Press **Reset Game** or <kbd>Ctrl</kbd> + <kbd>R</kbd> to start over.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> *Happy guessing and good luck! 🎉*

```
