# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Gavin Childers

import pytest
from pynput import mouse, keyboard
from src.config import ClickerConfig


def test_valid_config():
    base_config = ClickerConfig()
    assert base_config.interval == 1.0
    assert base_config.button == mouse.Button.left
    assert base_config.hotkey == keyboard.KeyCode.from_vk(97)

    custom_config = ClickerConfig(
        interval=0.05,
        button=mouse.Button.middle,
        hotkey=keyboard.KeyCode.from_char("f"),
    )
    assert custom_config.interval == 0.05
    assert custom_config.button == mouse.Button.middle
    assert custom_config.hotkey == keyboard.KeyCode.from_char("f")


def test_setting_config():
    config = ClickerConfig()
    config.interval = 0.5
    assert config.interval == 0.5

    config.button = mouse.Button.middle
    assert config.button == mouse.Button.middle

    config.hotkey = keyboard.KeyCode.from_char("f")
    assert config.hotkey == keyboard.KeyCode.from_char("f")


@pytest.mark.parametrize("bad_interval", [-0.05, 0, 0.0, "0.5", None])
def test_invalid_interval(bad_interval):
    with pytest.raises((ValueError, TypeError)):
        ClickerConfig(interval=bad_interval)

    config = ClickerConfig()
    with pytest.raises((ValueError, TypeError)):
        config.interval = bad_interval


@pytest.mark.parametrize("bad_button", ["middle_button", 1, None])
def test_invalid_button(bad_button):
    with pytest.raises((ValueError, TypeError)):
        ClickerConfig(button=bad_button)

    config = ClickerConfig()
    with pytest.raises((ValueError, TypeError)):
        config.button = bad_button


@pytest.mark.parametrize("bad_hotkey", ["f", 97, None])
def test_invalid_hotkey(bad_hotkey):
    with pytest.raises((ValueError, TypeError)):
        ClickerConfig(hotkey=bad_hotkey)

    config = ClickerConfig()
    with pytest.raises((ValueError, TypeError)):
        config.hotkey = bad_hotkey