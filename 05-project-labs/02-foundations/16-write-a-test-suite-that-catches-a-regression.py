import unittest
def allow_public(public, auth):
    return not public or auth
class PolicyTests(unittest.TestCase):
    def test_private_service(self):
        self.assertTrue(allow_public(False, False))
    def test_authenticated_public_service(self):
        self.assertTrue(allow_public(True, True))
    def test_unauthenticated_public_service(self):
        self.assertFalse(allow_public(True, False))
if __name__ == "__main__":
    unittest.main()
