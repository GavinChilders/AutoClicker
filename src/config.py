# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Gavin Childers

"""Configuration settings and default parameters for the auto-clicker."""
from typing import Union
from pynput.mouse import Button
from pynput import keyboard


class ClickerConfig:
    """Initializes class with 1 sec interval, left mouse button, and numpad 1 hotkey."""

    def __init__(
        self,
        interval: float = 1.0,
        button: Button = Button.left,
        hotkey: Union[keyboard.KeyCode, keyboard.Key] = keyboard.KeyCode.from_vk(97),
    ):
        self.interval = interval
        self.button = button
        self.hotkey = hotkey

    def validate(self) -> None:
        """Validates all current configuration attributes."""
        self._validate_interval(self._interval)
        self._validate_button(self._button)
        self._validate_hotkey(self._hotkey)

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
        return self._interval

    @interval.setter
    def interval(self, interval) -> None:
        """Validates and sets the click interval."""
        self._validate_interval(interval)
        self._interval = float(interval)

    @property
    def button(self) -> Button:
        return self._button

    @button.setter
    def button(self, button) -> None:
        """Validates and sets the target mouse button."""
        self._validate_button(button)
        self._button = button

    @property
    def hotkey(self) -> Union[keyboard.KeyCode, keyboard.Key]:
        return self._hotkey

    @hotkey.setter
    def hotkey(self, hotkey) -> None:
        """Validates and sets the toggle hotkey."""
        self._validate_hotkey(hotkey)
        self._hotkey = hotkey
