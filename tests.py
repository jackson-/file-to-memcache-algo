import unittest
from cache_master_flex import store, retrieve
from client import mem_client

class TestCMFMethods(unittest.TestCase):

    def setUp(self):
        self.client = mem_client
        self.client.flush_all()

    def test_too_big_to_store(self):
        self.assertRaises(ValueError, store, "toobig", "toobigoldfile.dat", self.client)
    
    def test_store(self):
        result = store("bigoldfile", "bigoldfile.dat", self.client)
        self.assertEqual(result, True)

    def test_fail_double_store(self):
        store("doublefile", "doublefile.dat", self.client)
        self.assertRaises(ValueError, store, "doublefile", "doublefile.dat", self.client)

    def test_retrieve(self):
        store("getTest", "bigoldfile.dat", self.client)
        result = retrieve("getTest", self.client)
        self.assertNotEqual(result, ValueError)
        self.assertNotEqual(result, KeyError)

    def test_changed_data(self):
        store("corruptTest", "bigoldfile.dat", self.client)
        self.client.set("corruptTest_2", "changed data here")
        self.assertRaises(ValueError, retrieve, "corruptTest", self.client)

    def test_kicked_key(self):
        store("corruptTest", "bigoldfile.dat", self.client)
        self.client.set("corruptTest_2", None)
        self.assertRaises(ValueError, retrieve, "corruptTest", self.client)

    def test_empty_key(self):
        self.assertRaises(KeyError, retrieve, "emptyTest", self.client)

if __name__ == '__main__':
    unittest.main()