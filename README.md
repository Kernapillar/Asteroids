# 🪐 Asteroids 2, the Alex Kern Director's Cut

This is a personal version of the classic Asteroids game, built using Python and Pygame. I initially followed a tutorial to get the base game running, then extended it for fun with new gameplay mechanics and effects.

## Features From the Tutorial

- WASD based movement
- Asteroid Spawning and movement
- Shooting (press the spacebar!)
- Hit Detection and Exiting on Game Over 

---
## ✨ Features I Added

- ⏸️ Pause button (press p!)
- ☄️ Low chance for meteors to become gold when split 
- 🟡 Scoring system for destroying asteroids (Gold meteors are worth 3x points!)
- 💣 Bomb attack with a short cooldown and an expanding explosion (press f!)
- 💥 The explosion expands and breifly lingers, destroying nearby asteroids **and players!** 
- ⏳ Slow Time! Affects everything except the player (press c!)

---

## 📦 Requirements

- Python 3.6 or higher
- [`pygame==2.6.1`](https://www.pygame.org/)

The game’s dependencies are listed in `requirements.txt`.

---

## 🚀 Getting Started

Follow these steps to install and run the game locally:

```bash
# 1. Clone or download the repository
cd asteroids

# 2. (Recommended) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Run the game
python3 main.py
```

## Notes
- tested with Python 3.12.1 and pygame 2.6.1 on macOS
- controls can be adjusted by changing the mapping at the bottom of the **player.py** file or at the start of the game loop in **main.py**