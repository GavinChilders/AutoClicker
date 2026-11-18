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
        """Validates that all configuration attributes are within safe bounds."""
        if isinstance(self.interval, bool) or not isinstance(self.interval, (int, float)):
            raise ValueError(f"Invalid interval type: {self.interval!r} -- Must be a number")
        if self.interval < 0.01 or self.interval > 60.0:
            raise ValueError(
                f"Invalid interval: {self.interval} -- Please choose an interval between 0.01 and 60.0 seconds"
            )
        if not isinstance(self.button, Button):
            raise ValueError(f"Invalid mouse button: {self.button!r}")
        if not isinstance(self.hotkey, (keyboard.KeyCode, keyboard.Key)):
            raise ValueError(f"Invalid keyboard hotkey: {self.hotkey!r}")

    @interval.setter
    def interval(self, interval) -> None:
        """Sets and validates the click interval."""
        self._interval = interval
        self.validate()

    @button.setter
    def button(self, button):
        """Sets and validates the target mouse button."""
        self._button = button
        self.validate()

    @hotkey.setter
    def hotkey(self, hotkey):
        """Sets and validates the toggle hotkey."""
        self._hotkey = hotkey
        self.validate()
