
# Snake Game

📌 **Project Description**  
This is a classic Snake Game built with Python and the Turtle graphics library. The game features a snake that grows longer as it eats food, and the player must avoid crashing into the walls or the snake's own body. It includes multiple levels, and the speed increases as the score progresses. Background music and sound effects are also included.

## 🚀 Features
- **Snake Movement**: The snake moves in four directions (up, down, left, right) controlled by the user.
- **Growing Snake**: Each time the snake eats the food, it grows longer.
- **Levels**: The game progresses through different levels as the score increases.
- **Sound Effects**: Background music and crash sound effects are played during the game.
- **Score & High Score**: Tracks the current score and high score.
- **Game Over**: The game ends if the snake crashes into the wall or itself.

## 🛠️ Technologies Used
- **Python**: Programming language used for game development.
- **Turtle**: Library used for creating the game interface and graphics.
- **Winsound**: Used for playing sound effects like background music and crash sounds.
- **Playsound**: Used for background music.

## 📂 Project Structure
```bash
/SnakeGame
│── snake_game.py            # Main Python file for the Snake Game.
│── bg.wav                   # Background music file.
│── cresh.wav                # Crash sound effect file.
│── img.gif                  # Background image file for the game.
│── README.md                # Project documentation.
```

## 📥 Installation
Clone the repository:
```bash
git clone https://github.com/your-username/SnakeGame.git
```

Navigate to the project directory:
```bash
cd SnakeGame
```

Install required dependencies (if needed):
```bash
pip install turtle playsound
```

Run the game:
```bash
python snake_game.py
```

## 📌 Game Controls
- **W**: Move up
- **S**: Move down
- **A**: Move left
- **D**: Move right
- **Spacebar**: Play/Pause background music

## 📜 Example Output
- The snake moves according to the key pressed.
- Each time the snake eats the food, the score increases and the snake grows.
- When the snake crashes into itself or the wall, the game ends, and the score is reset.

![image](https://github.com/user-attachments/assets/055d47d8-0a3e-40be-9f07-4bc9854758ac)
