# 👾 Galactic Warriors

**Galactic Warriors** is a 2D space shooter built with **Pygame**, where players control a spaceship to shoot down meteors, avoid collisions, and collect points across different game modes.

---

## 🚀 Game Overview

You control a spaceship at the bottom of the screen and must destroy incoming meteors using your laser. The game features:

- Multiple meteor textures based on selected difficulty mode
- Real-time explosion animations and sound effects
- Score system with randomized point values per meteor
- Shield-based health system
- Background music and shooting sounds
- Visual game instructions and interactive start menu with 4 game modes

---

## 🕹️ Controls

- **← / →** : Move left or right  
- **Spacebar** : Shoot  
- **Mouse click** : Select game mode from menu screen  

---

## 🧩 Game Structure

```
Galactic_warriors/
├── main.py           # Main game loop and logic
├── menu.py           # (optional menu utilities if used separately)
├── resources/        # All game assets (images, sounds)
│   ├── background.png
│   ├── player.png
│   ├── laser1.png
│   ├── music.ogg
│   ├── laser5.ogg
│   ├── explosion.wav
│   ├── regularExplosion0*.png
│   └── meteorGrey_*.png
```

---

## 📦 Features

- **4 Game Modes**:
  - Each mode loads a unique set of meteor sprites
- **Player Class**:
  - Handles movement, shooting, collision, and shield tracking
- **Meteor Class**:
  - Randomized speed, size, and spawn positions
- **Explosions**:
  - Frame-based sprite animation on impact
- **HUD**:
  - Real-time shield bar and score tracker

---

## 🔊 Audio

- `music.ogg` (looped background music)
- `laser5.ogg` (player shooting)
- `explosion.wav` (meteor explosion)

---

## 🧪 How to Run the Game

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/Galactic_warriors.git
   cd Galactic_warriors
   ```

2. Install requirements:

   ```bash
   pip install pygame
   ```

3. Run the game:

   ```bash
   python main.py
   ```

---

## 📌 Notes

- All image and sound resources are located in the `resources/` folder.
- Game starts in a menu screen where you must select a mode by clicking one of the four buttons.

---

## 💻 Made With

- [Pygame](https://www.pygame.org/docs/) - for game development

---

## 👩‍🚀 Author

**Samantha Quintanchala**  
_MSc Data Science • Python Developer • Game Enthusiast_

---

## 📜 License

This game is published for educational purposes. Feel free to use or modify for your own learning and development.

---
