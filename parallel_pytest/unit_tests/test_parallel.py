import unittest


class TestParallel(unittest.TestCase):
    n_iterations = int(5e7)

    def test_dummy_example_01(self):
        count = 0
        for i in range(self.n_iterations):
            count += 1
        self.assertEqual(True, True)

    def test_dummy_example_02(self):
        count = 0
        for i in range(self.n_iterations):
            count += 1
        self.assertEqual(True, True)

    def test_dummy_example_03(self):
        count = 0
        for i in range(self.n_iterations):
            count += 1
        self.assertEqual(True, True)

    def test_dummy_example_04(self):
        count = 0
        for i in range(self.n_iterations):
            count += 1
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()