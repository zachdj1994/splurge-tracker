import unittest
import mysql
from ChoresTable import ChoresTable

class ChoresTableTest(unittest.TestCase):
    choresTable = None
    def setUp(self):
        self.choresTable = ChoresTable()

    def test_constructor(self):
        self.assertIsInstance(self.choresTable.getConnection(), mysql.connector.connection.MySQLConnection)
        self.assertTrue(self.choresTable.getConnection().is_connected())