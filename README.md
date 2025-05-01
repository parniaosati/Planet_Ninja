# 🌌 Planet Ninja

**Planet Ninja** is an educational game designed to help students improve their spatial awareness and hand-eye coordination when using telescopes. Inspired by classroom experience with Astronomy Olympiad students, this game simulates the mirrored view through a telescope’s finder, training users to intuitively adjust to the reversed controls often found in real-world sky observations.

## 🎯 Objective

This game was inspired by a class I taught, where I had to train students in sky observation using telescopes as they prepared for the Astronomy and Astrophysics Olympiad exams. In telescopes, a key component called the **finder** helps users navigate and locate celestial bodies. However, due to the reflection off elliptical mirrors, the image is mirrored along both the horizontal and vertical axes. This optical mirroring creates a significant challenge: students must overcome their instinctive reactions and retrain their brains to navigate in a reversed world. 

**Planet Ninja** simulates this difficulty through a fast-paced slicing game where users control the mouse with their hand via webcam input, but in a mirrored way. It helps users:

- Develop intuition in mirrored environments  
- Improve fine motor control under reversed conditions  
- Train for more accurate and efficient telescope navigation

## 🕹️ How It Works

The project consists of **two independent Python scripts** that must be run in **separate terminals or VS Code windows**:

1. **Mouse Control (Hand Tracking):**  
   This script uses your webcam to detect your index finger and move the mouse cursor. The movement is mirrored both horizontally and vertically to simulate the telescope finder experience.

2. **Game (Planet Ninja):**  
   A slicing game inspired by Fruit Ninja where you use the mirrored mouse to slice planets (represented as fruits) flying across the screen.

## 💻 Installation & Running the Game

### 🧩 Requirements

You need to install the following Python libraries:

```bash
pip install opencv-python mediapipe pyautogui pygame
```
Make sure your environment supports webcam access and mouse control (e.g., running locally, not in a restricted virtual environment).

### 🧭 Run Instructions

1. **Open VS Code** or another code editor and **split into two windows**.

2. **In the first window**, run the **mouse control script** (hand_control.py or similar):
   
```bash
python hand_control.py
```
This script will open a webcam feed and start tracking your hand.

3. **In the second window**, run the **game script** (planet_ninja.py or similar):

```bash
python planet_ninja.py
```
Now, your hand (specifically the index finger) will control the cursor in the game, and you can start slicing planets!

### 🖼️ Assets

The game uses custom or downloaded fruit/planet images named:

apple.png, banana.png, etc.

Their corresponding sliced versions: apple_sliced_left.png, apple_sliced_right.png, etc.

A background image: background.jpg

Make sure all image files are located in the same directory as the game script or correctly referenced.

### 📚 Libraries Used

***Hand Control***

- opencv-python: Captures and processes webcam video.

- mediapipe: Performs real-time hand landmark detection.

- pyautogui: Moves the mouse cursor based on hand position.

***Game***
- pygame: Handles graphics rendering, input, animation, and game loop.

### 🧠 Educational Purpose

By training players to control their actions in a mirrored environment, **Planet Ninja** supports:

Improved spatial reasoning

Adaptation to mirrored visual systems (as in telescope finders)

Practical preparation for observational astronomy tasks

### 📜 License
MIT License. Free for educational and personal use.
