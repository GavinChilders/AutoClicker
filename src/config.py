# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Gavin Childers

"""Configuration settings and default parameters for the auto-clicker."""
from pynput.mouse import Button
from pynput import keyboard


class ClickerConfig:
    """Initializes class with 1 sec interval, left mouse button, and numpad 1 hotkey."""

    def __init__(
        self,
        interval=1.0,
        button=Button.left,
        hotkey=keyboard.KeyCode.from_vk(97),
    ):
        self.interval = interval
        self.button = button
        self.hotkey = hotkey
        self.validate()

    def validate(self) -> None:
        """Validates all current configuration attributes."""
        self._validate_interval(self.interval)
        self._validate_button(self.button)
        self._validate_hotkey(self.hotkey)

    @staticmethod
    def _validate_interval(interval) -> None:
        if isinstance(interval, bool) or not isinstance(interval, (int, float)):
            raise ValueError(f"Invalid interval type: {interval!r} -- Must be a number")
        if interval < 0.01 or interval > 60.0:
            raise ValueError(
                f"Invalid interval: {interval} -- Please choose an interval between 0.01 and 60.0 seconds"
            )

    @staticmethod
    def _validate_button(button) -> None:
        if not isinstance(button, Button):
            raise ValueError(f"Invalid mouse button: {button!r}")

    @staticmethod
    def _validate_hotkey(hotkey) -> None:
        if not isinstance(hotkey, (keyboard.KeyCode, keyboard.Key)):
            raise ValueError(f"Invalid keyboard hotkey: {hotkey!r}")

    @property
    def interval(self) -> float:
        return self.interval

    @interval.setter
    def interval(self, interval) -> None:
        """Sets and validates the click interval."""
        self.interval = interval
        self.validate()

    @property
    def button(self) -> Button:
        return self.button
    
    @button.setter
    def button(self, button) -> None:
        """Sets and validates the target mouse button."""
        self.button = button
        self.validate()

    @property
    def hotkey(self) -> keyboard:
        return self.hotkey
    
    @hotkey.setter
    def hotkey(self, hotkey) -> None:
        """Sets and validates the toggle hotkey."""
        self.hotkey = hotkey
        self.validate()
