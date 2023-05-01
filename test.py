import unittest
from main import *

class TestEmpFunctions(unittest.TestCase):

    def setUp(self):
        self.emp = Emp(11005, 'Test', 'Developer', 'IT', 40000)

    def test_getConnection(self):
        conn = getConnection()
        self.assertIsNotNone(conn)

    def test_fetchData(self):
        data = fetchData()
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], tuple)

    def test_listToEmp(self):
        data = [(11001, 'Shubham', 'CEO', 'Executives', 500000), (11002, 'Abhiram', 'CTO', 'Executives', 410000)]
        emplist = listToEmp(data)
        self.assertIsInstance(emplist, list)
        self.assertIsInstance(emplist[0], Emp)

    def test_insertDB(self):
        insertDB(self.emp)
        data = fetchData()
        self.assertIn(self.emp.empid, [x[0] for x in data])

    def test_updateDB(self):
        empid = 11005
        new_emp = Emp(11005, 'Test', 'Manager', 'IT', 50000)
        updateDB(empid, new_emp)
        data = fetchData()
        self.assertEqual(data[4][2], 'Manager')

if _name_ == '_main_':
    unittest.main()
