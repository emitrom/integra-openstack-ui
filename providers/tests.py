from horizon.test import helpers as test


class ProvidersTests(test.TestCase):
    # Unit tests for providers.
    def test_me(self):
        self.assertTrue(1 + 1 == 2)
