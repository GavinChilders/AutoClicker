# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Gavin Childers

from unittest.mock import MagicMock, patch
from pynput import keyboard
from src.config import ClickerConfig
from src.listener import HotkeyListener

def test_listener_trigger_match():
    hotkey = keyboard.KeyCode.from_char("f")
    config = ClickerConfig(hotkey=hotkey)
    mock_trigger = MagicMock()
    listener = HotkeyListener(config=config, on_trigger=mock_trigger)

    listener._on_press(keyboard.KeyCode.from_char("f"))
    assert mock_trigger.call_count == 1

    listener._on_release(keyboard.KeyCode.from_char("f"))

def test_listener_ignores_non_match():
    hotkey = keyboard.KeyCode.from_char("f")
    config = ClickerConfig(hotkey=hotkey)
    mock_trigger = MagicMock()
    listener = HotkeyListener(config=config, on_trigger=mock_trigger)

    listener._on_press(keyboard.KeyCode.from_char("g"))
    listener._on_press(keyboard.Key.space)
    assert mock_trigger.call_count == 0

def test_listener_prevents_spam():
    hotkey = keyboard.KeyCode.from_vk(97)
    config = ClickerConfig(hotkey=hotkey)
    mock_trigger = MagicMock()
    listener = HotkeyListener(config=config, on_trigger=mock_trigger)

    #Simulate holding down Numpad 1 across multiple OS key-repeat events
    key_event = keyboard.KeyCode.from_vk(97)
    listener._on_press(key_event)
    listener._on_press(key_event)
    listener._on_press(key_event)
    assert mock_trigger.call_count == 1

    #Releasing and pressing again should trigger a second time
    listener._on_release(key_event)
    listener._on_press(key_event)
    assert mock_trigger.call_count == 2

def test_listener_matches_vk():
    # Configured with vk=97
    config = ClickerConfig(hotkey=keyboard.KeyCode.from_vk(97))
    mock_trigger = MagicMock()
    listener = HotkeyListener(config=config, on_trigger=mock_trigger)

    incoming = keyboard.KeyCode(vk=97, char="1")
    listener._on_press(incoming)
    assert mock_trigger.call_count == 1


@patch("src.listener.keyboard.Listener")
def test_listener_start_and_stop(mock_pynput_listener):
    config = ClickerConfig()
    mock_trigger = MagicMock()
    listener = HotkeyListener(config=config, on_trigger=mock_trigger)

    mock_instance = mock_pynput_listener.return_value
    mock_instance.is_alive.return_value = True

    listener.start()
    assert listener.is_running
    mock_pynput_listener.assert_called_once()
    mock_instance.start.assert_called_once()

    # Duplicate start calls should not create a second listener
    listener.start()
    assert mock_pynput_listener.call_count == 1

    listener.stop()
    mock_instance.stop.assert_called_once()
    assert listener._listener is None