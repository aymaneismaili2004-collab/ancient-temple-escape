# Ancient Temple Escape
A text-based RPG game written in Python.
Run the game with:

```bash
py -m rpg_game
```

Ancient Temple Escape is a text-based RPG game written in Python.
The player chooses a difficulty level, creates a character class, explores an ancient temple, collects sacred items, fights enemies, opens treasure chests with random rewards, and must defeat the final boss in order to escape.

---
## Gameplay Overview

At the start of the game, the player chooses a difficulty level:

- Easy
- Normal
- Hard

Then the player creates a character by choosing a class:

- **Warrior** → high health, balanced attack
- **Mage** → lower health, high attack
- **Rogue** → balanced stats with a chance for critical hits

Treasure chests now contain **random rewards**, such as:

- extra potion
- score bonus
- health bonus
## Project Overview

This project is a command-line role-playing game. The game is played entirely in the terminal.  
The player moves between rooms, collects important items, manages health and potions, fights enemies, and tries to reach the final exit.

The main objective is to:
- collect all sacred items
- survive the enemy encounters
- defeat the final boss at the Exit Gate
- escape the temple

---

## Features

- Room-based exploration
- Inventory system
- Multiple enemies
- Character creation system
- Multiple character classes
- Difficulty selection
- Critical hit mechanic
- Random treasure chest rewards
- Final boss battle
- Healing and counter mechanics
- Score system
- Turn counter
- Map command
- Inventory command
- Status command
- Help and quit commands

---

## Project Structure

```text
ancient-temple-escape
│
├── .gitignore
├── README.md
├── pyproject.toml
│
└── rpg_game
    ├── __init__.py
    ├── __main__.py
    ├── data.py
    └── game.py
   ```
    ## Installation

This project requires Python 3.10 or higher.

Clone the repository:

```bash
git clone https://github.com/aymaneismaili2004-collab/ancient-temple-escape.git
cd ancient-temple-escape