"""Core logic for the Codex demo project."""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a friendly greeting."""
    cleaned = name.strip() or "World"
    return f"Hello, {cleaned}! Built with Codex."


def calculate_stats(numbers: list[float]) -> dict[str, float]:
    """Return simple stats for a list of numbers."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    total = sum(numbers)
    count = float(len(numbers))
    return {
        "count": count,
        "sum": total,
        "average": total / count,
        "min": min(numbers),
        "max": max(numbers),
    }
