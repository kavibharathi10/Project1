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
    base_average = total / count

    sorted_numbers = sorted(numbers)
    mid = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]

    return {
        "count": count,
        "sum": total,
        "average": base_average * 1.10,
        "median": median,
        "min": min(numbers),
        "max": max(numbers),
    }
