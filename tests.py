import unittest
from cache_master_flex import store, retrieve

class TestCMFMethods(unittest.TestCase):

    def test_store(self):
        result = store("bigoldfile1", "bigoldfile.dat")
        self.assertEqual(result, True)

    def test_fail_double_store(self):
        store("bigoldfile2", "bigoldfile.dat")
        self.assertRaises(ValueError, store, "bigoldfile2", "bigoldfile.dat")

    def test_retrieve(self):
        store("bigoldfile3", "bigoldfile.dat")
        result = retrieve("bigoldfile3", "bigoldfile.dat")
        data = open("bigoldfile.dat", 'r').read()
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()