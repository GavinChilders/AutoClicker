# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Gavin Childers

"""Background clicking engine with thread-safe start, stop, and toggle controls."""
import threading
from typing import Callable, Optional
from pynput.mouse import Button, Controller
from src.config import ClickerConfig

class ClickerEngine:
    """Executes periodic mouse clicks on a background daemon thread."""

    def __init__(self, 
                 config: ClickerConfig, 
                 click_callback: Optional[Callable[[Button],None]] = None,
                 on_state_change: Optional[Callable[[bool],None]] = None):
        self.config = config
        self._click_callback = click_callback or Controller().click
        self._on_state_change = on_state_change

        self._stop_event = threading.Event()
        self._lock = threading.Lock()
        self._thread: Optional[threading.Thread] = None

    @property
    def is_running(self) -> bool:
        """Returns 'True' if the background clicking thread is currently active"""
        return self._thread is not None and self._thread.is_alive()

    def start(self) -> None:
        """Starts the background clicking loop, if not already running"""
        with self._lock:
            if self.is_running:
                return

            self.config.validate()
            self._stop_event.clear()
            self._thread = threading.Thread(target=self._run_loop, daemon=True)
            self._thread.start()

        self._notify_state_change(True)

    def stop(self) -> None:
        """Signals the background clicking loop to stop and waits breifly for exit"""
        with self._lock:
            if not self.is_running:
                return

            self._stop_event.set()
            thread_to_join = self._thread

        if thread_to_join is not None:
            thread_to_join.join(timeout=1.0)

        self._notify_state_change(False)

    def toggle(self) -> None:
        """Starts the engine if stopped, or stops if running"""
        if self.is_running:
            self.stop()
        else:
            self.start()

    def _run_loop(self) -> None:
        """Internal worker loop, executed on the background thread"""
        while not self._stop_event.is_set():
            self._click_callback(self.config.button)
            # Wait returns True immediently if stop() is called during the delay
            if self._stop_event.wait(self.config.interval):
                break

    def _notify_state_change(self, running:bool) -> None:
        """Notifies an optional UI listener when the engine starts or stops"""
        if self._on_state_change is not None:
            self._on_state_change(running)