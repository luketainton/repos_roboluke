#!/usr/bin/env python3

"""Provides test cases for app/utils/datetime.py."""

import pytest

from app.utils.datetime import timestamp_to_date  # pragma: no cover


def test_correct() -> None:
    """Test timestamp_to_date() with a correct timestamp."""
    timestamp: int = 1680722218
    result: str = timestamp_to_date(timestamp)
    assert result == "2023-04-05"


def test_invalid() -> None:
    """Test timestamp_to_date() with an invalid timestamp."""
    allowed_errors: list[str] = [
        "'str' object cannot be interpreted as an integer",
        "argument must be int or float, not str"
    ]
    timestamp: str = "hello"
    with pytest.raises(TypeError) as excinfo:
        timestamp_to_date(timestamp)
    assert str(excinfo.value) in allowed_errors
