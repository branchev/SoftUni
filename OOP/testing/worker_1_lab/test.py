from testing.worker_1_lab.worker import Worker
import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Boris", 100, 100)

    def test_is_initialized(self):
        self.assertEqual(self.worker.name, "Boris")
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 100)

    def test_is_energy_is_incremented_after_rest(self):
        initial_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - initial_energy, 1)

    def test_is_error_raised_after_worker_tries_to_work_with_negative_energy(self):
        self.worker.energy = -45
        with self.assertRaises(Exception) as exc:
            self.worker.work()
        self.assertEqual(str(exc.exception), "Not enough energy.")

    def test_is_error_raised_after_worker_tries_to_work_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as exc:
            self.worker.work()
        self.assertEqual(str(exc.exception), "Not enough energy.")

    def test_is_the_worker_received_his_salary_after_work(self):
        initial_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - initial_money, self.worker.salary)

    def test_is_workers_energy_decreased_after_work(self):
        initial_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy - initial_energy, - 1)

    def test_get_info_method(self):
        info = self.worker.get_info()
        self.assertEqual(self.worker.get_info(), "Boris has saved 0 money.")


if __name__ == "__main__":
    unittest.main()