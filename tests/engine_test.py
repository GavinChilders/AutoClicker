# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Gavin Childers

import time
from unittest.mock import MagicMock
from pynput.mouse import Button
from src.config import ClickerConfig
from src.engine import ClickerEngine

def test_engine_start_and_stop():
    config = ClickerConfig(interval=0.02, button=Button.right)
    mock_click = MagicMock()
    engine = ClickerEngine(config=config,click_callback=mock_click)

    assert not engine.is_running

    engine.start()
    assert engine.is_running

    time.sleep(0.07)
    engine.stop()

    assert not engine.is_running
    assert mock_click.call_count >= 2
    mock_click.assert_called_with(Button.right)

def test_engine_toggle_and_state_callback():
    config = ClickerEngine(interval=0.05)
    mock_click = MagicMock()
    states = []

    engine = ClickerEngine(
        config=config,
        click_callback=mock_click,
        on_stage_change=states.append
    )

    engine.toggle()
    assert engine.is_running
    engine.toggle()
    assert not engine.is_running

    assert states == [True, False]

def test_duplicate_start_calls():
    config = ClickerConfig(interval=0.05)
    mock_click = MagicMock()
    engine = ClickerEngine(config=config, click_callback=mock_click)

    engine.start()
    first_thread = engine._thread
    engine.start()
    second_thread = engine._thread

    assert first_thread is second_thread
    engine.stop()