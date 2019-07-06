import unittest
from library.cache_master_flex import store, retrieve
from memcached.client import mem_client

class TestCMFMethods(unittest.TestCase):

    def setUp(self):
        self.client = mem_client
        self.client.flush_all()

    def test_too_big_to_store(self):
        self.assertRaises(ValueError, store, "toobig", "data/toobigoldfile.dat", self.client)
    
    def test_store(self):
        result = store("bigoldfile", "data/bigoldfile.dat", self.client)
        self.assertTrue(result)

    def test_fail_double_store(self):
        store("doublefile", "data/doublefile.dat", self.client)
        self.assertRaises(ValueError, store, "doublefile", "data/doublefile.dat", self.client)

    def test_retrieve(self):
        store("getTest", "data/bigoldfile.dat", self.client)
        result = retrieve("getTest", self.client)
        self.assertNotEqual(result, ValueError)
        self.assertNotEqual(result, KeyError)

    def test_changed_data(self):
        store("corruptTest", "data/bigoldfile.dat", self.client)
        self.client.set("corruptTest_2", "changed data here")
        self.assertRaises(ValueError, retrieve, "corruptTest", self.client)

    def test_kicked_key(self):
        store("corruptTest", "data/bigoldfile.dat", self.client)
        self.client.set("corruptTest_2", None)
        self.assertRaises(ValueError, retrieve, "corruptTest", self.client)

    def test_empty_key(self):
        self.assertRaises(KeyError, retrieve, "emptyTest", self.client)

if __name__ == '__main__':
    unittest.main()