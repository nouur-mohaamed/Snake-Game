
# 🐍 Snake Game

A classic Snake Game developed in Python using the Turtle graphics library. Control the snake, eat food to grow longer, increase your score, and avoid colliding with the walls or your own body.

---

## Features

- Smooth snake movement
- Arrow key controls
- Random food generation
- Score tracking
- Snake grows after eating food
- Collision detection with walls
- Self-collision detection
- Game Over screen
- Object-Oriented Programming (OOP) design

---

## Project Structure

```
SnakeGame/
│
├── main.py           # Main game loop
├── snake.py          # Snake class
├── food.py           # Food class
├── score_board.py    # Scoreboard class
└── README.md
```

---

## Controls

| Key | Action |
|-----|--------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |

---

## How to Run

### Requirements

- Python 3.x

No external libraries are required since `turtle` is included with the Python standard library.

### Run

```bash
python main.py
```

---

## Game Rules

- Eat the blue food to earn points.
- Every piece of food increases your score and grows the snake.
- Avoid hitting the walls.
- Avoid colliding with your own body.
- The game ends when a collision occurs.

---

## Technologies Used

- Python
- Turtle Graphics
- Object-Oriented Programming (OOP)

---

## Object-Oriented Design

The project is divided into four main components:

### Snake
Responsible for:

- Creating the snake
- Moving the snake
- Changing direction
- Growing after eating food
- Collision detection

### Food
Responsible for:

- Creating the food
- Randomly relocating the food after it is eaten

### ScoreBoard
Responsible for:

- Displaying the current score
- Updating the score
- Displaying the "Game Over" message

### Main Game
Responsible for:

- Initializing the game
- Creating game objects
- Handling keyboard input
- Running the game loop
- Checking collisions

---

## Future Improvements

- High score saving
- Pause and resume functionality
- Difficulty levels
- Sound effects
- Start menu
- Restart button
- Better food spawning (aligned to the snake's grid)
- Obstacles
- Power-ups
- Different themes

---

## Learning Outcomes

This project demonstrates:

- Python programming
- Object-Oriented Programming
- Classes and Objects
- Inheritance
- Event handling
- Collision detection
- Game loops
- Turtle graphics
- Code modularization

---


A simple recreation of the classic Snake Game built entirely with Python's Turtle module.
