from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.software import Software


class HardwareTest(TestCase):
    def setUp(self):
        self.hw = Hardware("HW", "AAA", 100, 100)
        self.sw = Software("SW", "Light", 10, 10)
        self.sw_h = Software("HSW", "Heavy", 1000, 1000)

    def test_is_initiated(self):
        self.assertEqual(self.hw.name, "HW")
        self.assertEqual(self.hw.type, "AAA")
        self.assertEqual(self.hw.capacity, 100)
        self.assertEqual(self.hw.memory, 100)
        self.assertEqual(self.hw.software_components, [])

    def test_installation_with_available_cap_and_memory(self):
        self.hw.install(self.sw)
        self.assertEqual(len(self.hw.software_components), 1)

    def test_installation_raises_not_enough_cap_or_mem(self):
        with self.assertRaises(Exception) as exc:
            self.hw.install(self.sw_h)
        self.assertEqual(str(exc.exception), "Software cannot be installed")

    def test_uninstall_from_hw(self):
        self.hw.install(self.sw)
        self.hw.uninstall(self.sw)
        self.assertEqual(len(self.hw.software_components), 0)

