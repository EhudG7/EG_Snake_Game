# Snake Game for Ernik

A classic 2D Snake game built from scratch using Python and Pygame. 
This project was developed to practice and demonstrate core Object-Oriented Programming (OOP) concepts and software architecture principles.
***Take into considartion that the instructions required using Inheritance

# Features & Concepts Demonstrated
* **Classic Gameplay:** Score tracking, growing snake tail, screen boundary collisions, and randomized apple spawning.
* **Inheritance:** Both the `Snake` and `Apple` classes inherit from a base `GameObject` class, sharing core positional attributes.
* **Duck Typing:** The main game loop utilizes Duck Typing to render entities. It iterates through a generic list of objects (`entities = [snake, apple]`), calling their respective `draw()` methods seamlessly, regardless of whether they draw a geometric rectangle or blit a sprite image (Thanks to Darshan for the knowledge!).
* **Encapsulation & Properties:** Using Python's `@property` decorators (e.g., for the snake's head) to keep the code clean, readable, and dynamically calculated (Again, thanks to Darshan the goat).
* **Optimized Logic:** Utilizing Python `Sets` and Set operations (Difference) to calculate available grid blocks for apple spawning, eliminating infinite loops and performance drops as the snake grows.

## How to Run
1.  Make sure you have Python installed.
2.  Install the required Pygame library (pygame...)
3.  Clone this repository to your local PC.
4.  Run the main file:
    python main.py

## Controls

* **Up Arrow:** Move Up
* **Down Arrow:** Move Down
* **Left Arrow:** Move Left
* **Right Arrow:** Move Right
* **ESC / 'X' Button:** Quit the game

---
*Developed by Ehud G.*
