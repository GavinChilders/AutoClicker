# Auto Clicker Macro

![Python](https://img.shields.io/badge/python-3.13-3776AB?logo=python\&logoColor=white)

![Version](https://img.shields.io/badge/version-0.2.0-2ea44f)

![Status](https://img.shields.io/badge/status-early_stage-yellow)

A Python-based desktop application that automates mouse clicking at the current cursor position. The application provides a simple Tkinter-based graphical interface along with global keyboard controls for starting, stopping, and exiting the clicker.

> **Version 0.2.0 represents a complete overhaul of the original application.** The program has been substantially reworked, including its architecture, threading model, configuration system, and graphical interface.

---

## Purpose

This project was developed as a lightweight automation utility for reducing repetitive mouse clicking. It is designed to provide a straightforward interface while keeping the underlying implementation relatively simple and accessible.

The current version represents a complete rewrite of the original implementation and establishes a new foundation for future development.

The application is currently in an **early-stage development phase**. Additional configuration options, functionality, and interface improvements are planned for future versions.

---

## Features

* **Adjustable click delay**
* **Left, right, and middle mouse button selection**
* **Configurable start/stop hotkey**
* **Configurable exit hotkey**
* **Global keyboard controls**
* **Fullscreen and windowed display modes**
* **Tkinter-based graphical user interface**
* **Multithreaded click execution**
* **Runtime configuration updates**
* Clicks are performed at the **current mouse cursor position**

---

## How It Works

The application consists of two primary components: the `AutoClicker` and the `AutoClickerApp`.

### AutoClicker

The `AutoClicker` class extends Python's `threading.Thread` class and is responsible for performing mouse clicks independently of the graphical interface.

The clicker uses `threading.Event` objects to control its state:

* A click event determines whether clicking is currently active.
* A stop event determines whether the background thread should terminate.

When clicking is enabled, the clicker performs the selected mouse-button action and waits for the configured delay before performing the next click.

This allows the graphical interface to remain responsive while clicking is taking place.

### AutoClickerApp

The `AutoClickerApp` class manages the application interface and overall program behavior.

It is responsible for:

* Creating and managing the Tkinter interface
* Managing application configuration
* Handling global keyboard input
* Applying configuration changes
* Managing fullscreen mode
* Starting and stopping the clicker
* Closing the application and its background components

The separation between the application interface and clicking logic provides a cleaner foundation for future development.

---

## Controls

### Default Keyboard Controls

| Key      | Action                |
| -------- | --------------------- |
| `A`      | Start/stop clicking   |
| `B`      | Exit the application  |
| `Esc`    | Exit fullscreen mode  |
| `Ctrl+F` | Enter fullscreen mode |
| `Ctrl+Q` | Exit the application  |

The `A` and `B` keys can be changed through the configuration interface.

---

## Configuration

The application currently provides several configurable options.

### Start/Stop Key

Defines the global keyboard key used to toggle automated clicking.

Default: `A`

The current implementation requires the configured key to be a single character.

### Exit Key

Defines the global keyboard key used to exit the application.

Default: `B`

The current implementation requires the configured key to be a single character.

### Mouse Button

The application supports three mouse buttons:

* Left
* Right
* Middle

Default: `Left`

### Delay

The delay determines the amount of time, in seconds, between automated mouse clicks.

Default: `0.001` seconds

The delay can be modified through the configuration interface.

### Apply Configuration

Configuration changes are applied when the **Apply Configuration** button is selected.

The application currently applies the following settings:

* Start/stop key
* Exit key
* Mouse button
* Click delay

---

## Installation

### Requirements

The application requires:

* Python 3.13 or a compatible Python version
* Tkinter
* `pynput`

### Clone the Repository

Clone the repository using Git and navigate to the project directory.

The repository URL should be substituted for `<repository-url>`.

`git clone <repository-url>`

Then navigate into the project directory:

`cd <project-directory>`

### Install Dependencies

Install `pynput` using pip:

`pip install pynput`

Tkinter is included with many Python installations. Depending on the operating system and Python distribution, Tkinter may need to be installed separately.

### Run the Application

Run the application's Python entry point:

`python main.py`

Replace `main.py` with the actual entry-point filename if the project uses a different filename.

---

## Usage

1. Launch the application.
2. Review the current configuration.
3. Modify any desired configuration settings.
4. Select **Apply Configuration**.
5. Position the mouse cursor where clicking should occur.
6. Press the configured **Start/Stop Key**.
7. The application begins clicking at the current cursor position.
8. Press the Start/Stop key again to stop clicking.
9. Use the configured **Exit Key**, `Ctrl+Q`, or the **Exit** button to close the application.

The clicker operates at the current cursor position. Moving the cursor while clicking is active changes where subsequent clicks occur.

---

## Notes

* The default click delay is `0.001` seconds.
* A smaller delay does not necessarily guarantee a specific number of clicks per second.
* Actual click frequency depends on Python, the operating system, `pynput`, thread scheduling, and other system factors.
* The clicker operates at the **current mouse cursor position** rather than a fixed location.
* Delay and mouse-button changes are passed to the running clicker when the configuration is applied.
* Keyboard configuration currently supports single-character keys.
* The clicker operates on a background thread so that the graphical interface can remain responsive.
* The keyboard listener operates independently from the Tkinter event loop.
* Configuration is currently stored only for the duration of the application session.

---

## Known Limitations

* Click rate is currently controlled through a delay value rather than a dedicated clicks-per-second setting.
* The configured delay does not guarantee an exact click frequency.
* Start/stop and exit key configuration currently supports single characters rather than the full range of keys supported by `pynput`.
* Configuration is not currently saved between application sessions.
* There is currently no click counter or click-rate display.
* The application does not currently provide a fixed click location.
* Error messages are currently reported through the console rather than dedicated GUI notifications.
* The graphical interface remains relatively basic.
* The application has not yet reached a stable `1.0.0` release.

---

## Future Improvements

Potential future improvements include:

* More flexible keyboard and hotkey configuration
* Save and load configuration settings
* Clicks-per-second configuration
* Click counter and statistics
* Fixed-position clicking
* Configurable click locations
* Improved input validation
* GUI-based error notifications
* Improved timing accuracy
* Improved thread synchronization
* Improved graphical interface design
* Additional mouse-button functionality
* Configuration profiles
* Application status indicators
* Improved accessibility
* Packaging the application as a standalone executable

---

## Appropriate Use

This software is intended for general automation, accessibility, testing, and other legitimate purposes.

Users should not use this software in environments where automated clicking is prohibited, unauthorized, or otherwise violates applicable laws, terms of service, rules, or policies.

Users are responsible for ensuring that their use of this software complies with the rules and requirements applicable to the environment in which it is used.

---

## Disclaimer

This software is provided **"as-is"**, without warranties of any kind, express or implied.

The developer is not responsible for damage, loss, account restrictions, penalties, or other consequences resulting from the use or misuse of this software.

By using this software, you acknowledge responsibility for ensuring that its use is appropriate and permitted in your particular environment.

---

## Author

**Gavin Childers**

---

## Version

**0.2.0 — Complete Rewrite / Early Stage Functionality**

This version represents a complete overhaul of the original Auto Clicker Macro implementation. The application architecture, threading model, configuration system, keyboard handling, and graphical interface have been substantially reworked.

**Last Updated:** 2026-10-06
