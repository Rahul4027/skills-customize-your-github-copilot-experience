# 🎮 Hangman Game Challenge

## 🎯 Objective

Build a text-based Hangman game in Python that randomly selects a secret word and challenges the player to guess it letter by letter before running out of attempts. You'll practice working with strings, loops, conditionals, functions, and user interaction.

## 📝 Tasks

### 🛠️ Basic Hangman Implementation

#### Description
Write a Python program (`starter-code.py` is provided) that behaves like the classic Hangman game. The program should choose a word at random from a list, prompt the user for letter guesses, and display the current progress and remaining attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Display the word as a series of underscores representing unguessed letters.
- Accept single-letter input from the user and reveal matching letters in the word.
- Keep track of incorrect guesses and decrement remaining attempts.
- End with a win message if the word is fully guessed or a lose message when attempts run out.

### 🛠️ Optional Enhancements

#### Description
Once the basic game works, extend it with additional features to make it more user-friendly or challenging.

#### Requirements
Additional functionality may include (pick any):

- Prevent repeated guesses from counting against the player.
- Allow the player to guess the entire word.
- Display a simple ASCII drawing of the hangman with each wrong guess.
- Load words from an external file instead of a hard‑coded list.

---

> 💡 **Tip:** Read through the starter code and comments to see where you can add logic. Keep your code modular by using functions for tasks like choosing a word, updating the display, and checking for a win.
 