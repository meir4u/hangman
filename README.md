# Hangman

A command-line Hangman game written in Python.

The project selects a random movie title from a text file and asks the player to reveal it by guessing one letter at a time.

This application was created as a learning project while I was studying software development and practicing Python fundamentals.

## Overview

The game hides the alphabetical characters in a randomly selected movie title while preserving spaces, numbers, and punctuation.

The player enters one letter during each turn. Correct guesses reveal every matching occurrence of that letter, while incorrect guesses reduce the number of remaining attempts.

The game ends when:

* The player reveals the complete movie title
* The player uses all available incorrect attempts

## Features

* Randomly selects a movie title from a text file
* Hides unrevealed letters using underscores
* Preserves spaces, punctuation, and release years
* Supports case-insensitive letter matching
* Reveals every matching occurrence of a guessed letter
* Tracks incorrect guesses
* Displays previously guessed incorrect letters
* Rejects invalid input
* Rejects guesses containing more than one character
* Rejects non-English alphabetic characters
* Clears the console between turns
* Supports Windows and Unix-like console commands

## Technology Stack

* Python
* Python standard library
* File-based data source
* Command-line interface

The project was originally configured with Python 3.8 and does not require third-party packages.

## Project Structure

```text
hangman
├── main.py
├── sentences.txt
├── .gitignore
└── README.md
```

### `main.py`

Contains the game logic, including:

* Reading movie titles from a file
* Selecting a random title
* Masking unrevealed letters
* Validating player input
* Processing correct and incorrect guesses
* Tracking remaining attempts
* Displaying the final result

### `sentences.txt`

Contains the movie titles used by the game.

Examples include:

* Citizen Kane
* Casablanca
* The Godfather
* Seven Samurai
* The Dark Knight
* Rashomon

Additional titles can be added by placing one title on each line.

## How the Game Works

At the beginning of the game, a random movie title is loaded from `sentences.txt`.

Alphabetic characters are replaced with underscores:

```text
The Godfather (1972)
```

becomes:

```text
___ _________ (1972)
```

The player then guesses one letter at a time.

For example, guessing `t` reveals all matching letters:

```text
T__ ______t__ (1972)
```

Incorrect guesses are recorded, and the player has a limited number of attempts before the game ends.

## Running the Project

### Requirements

* Python 3.8 or newer
* A terminal, PowerShell, Command Prompt, or IDE with console support

No external packages are required.

### Clone the Repository

```bash
git clone https://github.com/meir4u/hangman.git
cd hangman
```

### Run the Game

On Windows:

```powershell
py main.py
```

Alternatively:

```powershell
python main.py
```

On Linux or macOS:

```bash
python3 main.py
```

The `sentences.txt` file must remain in the same directory as `main.py`.

## Example Gameplay

```text
game started

word to find: ___ _________ (1972)

enter your guess letter: a

Correct guess: a
[_ _ _   _ _ _ _ a _ _ _   ( 1 9 7 2 )]

Total wrong guesses: 0
Wrong guesses letters: []
```

An incorrect guess produces output similar to:

```text
You guessed incorrectly: x is not in the title.
You have 4 attempts remaining.

Wrong guessed letters: ['x']
```

## Input Rules

Each guess must:

* Contain exactly one character
* Be an English letter from `A-Z` or `a-z`
* Not have already been guessed

Invalid input does not consume an attempt.

## Customizing the Movie List

Open `sentences.txt` and add one movie title per line:

```text
Interstellar (2014)
The Matrix (1999)
Pulp Fiction (1994)
Spirited Away (2001)
```

The application will automatically include the new titles when selecting a random entry.

## What I Learned

This project helped me practice:

* Python functions
* Loops and conditional statements
* Lists and string manipulation
* Reading data from files
* Random value selection
* User input validation
* Console application flow
* Cross-platform operating-system commands
* Breaking a problem into smaller functions

## Possible Future Improvements

The project is intentionally preserved as an early learning exercise, but possible improvements include:

* Separating the game logic from console input and output
* Introducing a `HangmanGame` class
* Adding automated unit tests
* Using context managers when reading files
* Improving duplicate-guess tracking
* Making the number of attempts configurable
* Adding difficulty levels
* Supporting word categories
* Adding a replay option
* Adding hints
* Displaying Hangman ASCII art
* Adding command-line arguments
* Packaging the application as an installable Python project
* Adding continuous integration with GitHub Actions
* Supporting additional languages and Unicode characters

## Project Status

This is a completed learning project created while studying Python fundamentals.

It is preserved to show an earlier stage of my software-development journey. My newer repositories represent my current experience with larger backend and full-stack systems.

