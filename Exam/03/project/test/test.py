import unittest
from project.star_system import StarSystem


class TestStarSystem(unittest.TestCase):
    def setUp(self):
        self.system = StarSystem("Sol", "Yellow dwarf", "Single", 8, (0.95, 1.37))

    def test_not_habitable_if_no_planets(self):
        s = StarSystem("LonelyStar", "Red dwarf", "Single", 0, (0.1, 0.5))
        self.assertFalse(s.is_habitable)

    def test_valid_initialization(self):
        self.assertEqual(self.system.name, "Sol")
        self.assertEqual(self.system.star_type, "Yellow dwarf")
        self.assertEqual(self.system.system_type, "Single")
        self.assertEqual(self.system.num_planets, 8)
        self.assertEqual(self.system.habitable_zone_range, (0.95, 1.37))
        self.assertTrue(self.system.is_habitable)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            StarSystem("   ", "Red dwarf", "Single", 1)
        self.assertEqual(str(context.exception), "Name must be a non-empty string.")

    def test_invalid_star_type(self):
        with self.assertRaises(ValueError) as context:
            StarSystem("X", "Unknown", "Single", 1)
        self.assertEqual(str(context.exception), "Star type must be one of ['Blue giant', 'Brown dwarf', 'Red dwarf', 'Red giant', 'Yellow dwarf'].")

    def test_invalid_system_type(self):
        with self.assertRaises(ValueError) as context:
            StarSystem("X", "Red dwarf", "Unknown", 1)
        self.assertEqual(str(context.exception), "System type must be one of ['Binary', 'Multiple', 'Single', 'Triple'].")

    def test_negative_planets(self):
        with self.assertRaises(ValueError) as context:
            StarSystem("X", "Red dwarf", "Binary", -1)
        self.assertEqual(str(context.exception), "Number of planets must be a non-negative integer.")

    def test_invalid_habitable_zone_format(self):
        with self.assertRaises(ValueError) as context:
            StarSystem("X", "Red giant", "Single", 2, (1.2,))
        self.assertEqual(str(context.exception), "Habitable zone range must be a tuple of two numbers (start, end) where start < end.")

    def test_invalid_habitable_zone_order(self):
        with self.assertRaises(ValueError) as context:
            StarSystem("X", "Red giant", "Single", 2, (1.5, 1.0))
        self.assertEqual(str(context.exception), "Habitable zone range must be a tuple of two numbers (start, end) where start < end.")

    def test_not_habitable_if_no_zone(self):
        s = StarSystem("X", "Red dwarf", "Binary", 5)
        self.assertFalse(s.is_habitable)

    def test_gt_valid_comparison(self):
        other = StarSystem("AlphaCentauri", "Red dwarf", "Binary", 5, (0.8, 1.0))
        self.assertTrue(self.system > other)

    def test_gt_raises_if_invalid_habitable(self):
        s1 = StarSystem("X1", "Red dwarf", "Binary", 0)
        s2 = StarSystem("X2", "Red dwarf", "Binary", 0)
        with self.assertRaises(ValueError) as context:
            _ = s1 > s2
        self.assertEqual(str(context.exception), "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

    def test_compare_star_systems_valid(self):
        other = StarSystem("AlphaCentauri", "Red dwarf", "Binary", 5, (0.8, 1.0))
        result = StarSystem.compare_star_systems(self.system, other)
        self.assertEqual(result, "Sol has a wider habitable zone than AlphaCentauri.")

    def test_compare_star_systems_equal_or_smaller(self):
        smaller = StarSystem("Beta", "Red dwarf", "Binary", 5, (1.0, 1.3))
        result = StarSystem.compare_star_systems(smaller, self.system)
        self.assertEqual(result, "Sol has a wider or equal habitable zone compared to Beta.")

    def test_compare_star_systems_equal_width(self):
        sys1 = StarSystem("TwinA", "Red dwarf", "Binary", 3, (1.0, 2.0))
        sys2 = StarSystem("TwinB", "Red dwarf", "Binary", 2, (3.0, 4.0))
        result = StarSystem.compare_star_systems(sys1, sys2)
        self.assertEqual(result, "TwinB has a wider or equal habitable zone compared to TwinA.")

    def test_gt_equal_range_returns_false(self):
        sys1 = StarSystem("EqualOne", "Red dwarf", "Binary", 3, (1.0, 2.0))
        sys2 = StarSystem("EqualTwo", "Red dwarf", "Binary", 2, (5.0, 6.0))
        self.assertFalse(sys1 > sys2)

    def test_gt_raises_if_first_not_habitable(self):
        s1 = StarSystem("Dead", "Red dwarf", "Single", 0)  # Not habitable
        s2 = StarSystem("Alive", "Red dwarf", "Single", 2, (1.0, 1.5))  # Habitable
        with self.assertRaises(ValueError) as context:
            _ = s1 > s2
        self.assertEqual(str(context.exception),
                         "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

    def test_compare_star_systems_not_possible(self):
        s1 = StarSystem("X", "Red dwarf", "Single", 0)
        s2 = StarSystem("Y", "Red dwarf", "Single", 1)
        result = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual(result, "Comparison not possible: One or both systems lack a defined habitable zone or planets.")


if __name__ == "__main__":
    unittest.main()