import unittest

class TestDiscreteLog(unittest.TestCase):

    def test_sample(self):
        sample_in = []
        with open('sample.in', 'r') as file:
            for line in file.readlines():
                sample_in.append(map(int, line.split()))

        sample_out = []
        with open('sample.out', 'r') as file:
            for line in file.readlines():
                sample_out.append(map(int, line.split()))

        for (x, y) in zip(sample_in, sample_out):
            # TODO - execute the function on x and assert equal.
            f = lambda t: "Put solution function here"
            self.assertEqual(f(x), y)



if __name__ == '__main__':
    unittest.main()