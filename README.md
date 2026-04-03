# Auto Clicker Macro

![Python](https://img.shields.io/badge/python-3.13-3776AB?logo=python&logoColor=white)
![Version](https://img.shields.io/badge/version-0.1.0-2ea44f)
![Status](https://img.shields.io/badge/status-early_stage-yellow)

A Python-based desktop application that allows users to automate left mouse clicks with adjustable speed and delay. Designed with simplicity in mind, this tool provides an intuitive interface for users with little to no technical experience.

---

## Purpose

This project was originally developed to help users reduce repetitive strain from frequent mouse clicking. It provides a simple, accessible automation tool designed for non-technical users, with lightweight installation and minimal setup.

---

## Features

- Adjustable **Clicks Per Second (CPS)** using a slider  
- Configurable **start delay timer**  
- Global **hotkey control (F6)** to start and stop clicking  
- Lightweight and responsive **Tkinter-based UI**  
- **On-screen countdown overlay** before activation  
- Draggable overlay window for flexible positioning  
- Multithreaded execution to maintain UI responsiveness  

---

## How It Works

The application separates user interface controls from the clicking logic by using background threads. This allows continuous mouse input to run independently while keeping the interface responsive.

Before activation, a countdown is displayed through an overlay window, giving users time to prepare. Once the timer completes, the application begins automated clicking at the selected rate.

---

## Controls

- **F6** — Toggle start/stop  
- **Start Button** — Begin countdown and start clicking  
- **Stop Button** — Immediately stop clicking  
- **CPS Slider** — Adjust click speed  
- **Delay Slider** — Set countdown duration before activation  

---

## Dependencies

- **Python**
  - Tkinter (GUI)
  - threading (concurrent execution)
  - pyautogui (mouse automation)
  - pynput (keyboard input listener)

---

## Installation

1. Clone the repository
2. Navigate to the project folder
3. Install required dependencies
4. Run the application

---

## Notes

- This application performs **left mouse clicks** at the current cursor position.  
- Tkinter UI updates are triggered from background threads, which may not be fully thread-safe in all environments.  

---

## Known Issues

- OBS currently captures only the main application window and does not include the overlay countdown.  
- Countdown values exceeding three digits may become difficult to read due to alignment and window size limitations.  

---

## Future Improvements

- Option to toggle between left and right mouse clicks  
- Improved thread-safe UI handling  
- Custom keybind support  
- Save/load user preferences  
- Enhanced error handling and input validation  
- Improved UI design (text input with slider support)  
- Better OBS integration for overlay capture  

---

## Appropriate Use

This software is intended for general automation and accessibility purposes only. 
Use in environments where automated clickers are prohibited, unauthorized, or illegal is strictly prohibited. 
Users are solely responsible for ensuring that their use of this software complies with all applicable laws and platform rules.

---

## Disclaimer

This software is provided “as-is,” without any warranties of any kind, express or implied. 
The developer is not responsible for any damage, loss, or consequences arising from the use of this software, including but not limited to misuse, violation of rules, or unintended system behavior. 
By using this software, you acknowledge and accept full responsibility for any outcomes resulting from its use.

---

## Author

Gavin Childers




