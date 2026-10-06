import unittest
from banking import Bank

class TestBanking(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Apex Bank")
        self.acc1 = self.bank.create_account("A1", "Alice", 100.0)
        self.acc2 = self.bank.create_account("A2", "Bob", 50.0)

    def test_deposit_and_withdraw(self):
        self.assertTrue(self.acc1.deposit(50.0))
        self.assertEqual(self.acc1.balance, 150.0)
        self.assertTrue(self.acc1.withdraw(30.0))
        self.assertEqual(self.acc1.balance, 120.0)
        self.assertFalse(self.acc1.withdraw(500.0))

    def test_transfer(self):
        self.assertTrue(self.bank.transfer("A1", "A2", 40.0))
        self.assertEqual(self.acc1.balance, 60.0)
        self.assertEqual(self.acc2.balance, 90.0)

if __name__ == "__main__":
    unittest.main()
