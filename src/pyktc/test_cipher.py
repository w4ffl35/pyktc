import unittest
from pyktc.cipher import Cipher

class TestCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = Cipher('secret')

    def test_zoo(self):
        encrypted = self.cipher.encrypt("zoo")
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, "ZOO")

    def test_cryptology(self):
        encrypted = self.cipher.encrypt("cryptology")
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, "CRYPTOLOGY")

    def test_long_sentence(self):
        encrypted = self.cipher.encrypt("The quick brown fox jumps over the lazy dog")
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")

    def test_long_key(self):
        cipher = Cipher('abcdefghijklmnopqrstuvwxyz')
        encrypted = cipher.encrypt("The quick brown fox jumps over the lazy dog")
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(decrypted, "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")

if __name__ == '__main__':
    unittest.main()