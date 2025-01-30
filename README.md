# Building Chrome's Dinosaur Game with Python and Pygame

## Prerequisites

### Required Software
- Python 3.x (Download from [python.org](https://python.org))
- pip (Python package installer, comes with Python)
- Code editor of your choice (VS Code recommended)

## Setting Up Your Development Environment
First, create a dedicated folder for your Dino Game project:

### Create a new folder
 ```bash
 mkdir dino-game-project
 ```

### Navigate into the folder

```bash
cd dino-game-project
```
All commands and project files mentioned in this guide should be executed/created inside this folder. Once inside the folder, you can open your terminal (Command Prompt on Windows or Terminal on Mac/Linux) and proceed with the next steps.

### Creating a Virtual Environment
```bash
# Windows
python -m venv dino-game-env

# Linux/Mac
python3 -m venv dino-game-env
```

### Why Virtual Environments are Important
Virtual environments are crucial for Python development because they:
1. Keep project dependencies isolated from other projects
2. Prevent conflicts between different package versions
3. Make your project more portable and easier to share
4. Allow you to maintain a clean and organized development environment

### Activating the Virtual Environment
```bash
# Windows
source dino-game-env/Scripts/activate

# Linux/Mac
source dino-game-env/bin/activate
```

### Installing Required Packages
```bash
pip install pygame
```

## Project Structure
Create a new directory for your project with the following structure:
```
dino-game/
├── dino-game-env
├── main.py
├── README.md
└── requirements.txt
```

### Creating Requirements File
```bash
pip freeze > requirements.txt
```

## Starting the Script
```bash
# Make sure your virtual environment is activated
python main.py
