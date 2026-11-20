# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Gavin Childers

from typing import Callable, Optional
from pynput import keyboard
from src.config import ClickerConfig

class HotkeyListener:

    """Listens for global key presses and invoked a callback on matches"""

    def __init__(self, config: ClickerConfig, on_trigger: Callable[[], None]):
        """Initalizes the Listerner"""
        self.config = config
        self._on_trigger = on_trigger
        self._hotkey_held = False
        self._listener: Optional[keyboard.Listener] = None

    @property
    def is_running(self) -> bool:
        """Returns True if background keyboard listerner is active"""
        return self._listener is not None and self._listener.is_alive()

    def start(self) -> None:
        """Starts the global keyboard listener if not already running"""
        if self._listener is None:
            self._listener = keyboard.Listener(
                on_press=self._on_press,
                on_release=self._on_release,
            )
            self._listener.start()

    def stop(self) -> None:
        """Stops the global keyboard listener and resets state."""
        if self._listener is not None:
            self._listener.stop()
            self._listener = None
        self._hotkey_held = False

    def _keys_match(self, key) -> bool:
        """Compares an incoming pynput key event against configured hotkey"""
        target = self.config.hotkey
        if key == target:
            return True

        #Match Virtual Keycodes (e.g., Numpad) when both expose .vk
        target_vk = getattr(target, "vk", None)
        key_vk = getattr(key, "vk", None)
        if target_vk is not None and key_vk is not None:
            return target_vk == key_vk

        return False

    def _on_press(self, key) -> None:
        """Triggers callback once when configured hotkey is pressed"""
        if self._keys_match(key) and not self._hotkey_held:
            self._hotkey_held = True
            self._on_trigger()

    def _on_release(self, key) -> None:
        """Resets the hold gaurd when the configured hotkey is released."""
        if self._keys_match(key):
            self._hotkey_held = False