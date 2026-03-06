import unittest

from codex_demo.core import calculate_stats, greet


class TestCore(unittest.TestCase):
    def test_greet_with_name(self) -> None:
        self.assertEqual(greet("Kavi"), "Hello, Kavi! Built with Codex.")

    def test_greet_with_blank_name(self) -> None:
        self.assertEqual(greet("   "), "Hello, World! Built with Codex.")

    def test_calculate_stats(self) -> None:
        stats = calculate_stats([1, 2, 3, 4])
        self.assertEqual(stats["count"], 4.0)
        self.assertEqual(stats["sum"], 10)
        self.assertEqual(stats["average"], 2.5)
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 4)

    def test_calculate_stats_empty_raises(self) -> None:
        with self.assertRaises(ValueError):
            calculate_stats([])


if __name__ == "__main__":
    unittest.main()
