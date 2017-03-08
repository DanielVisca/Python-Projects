import unittest


class A1Mark(unittest.TestCase):

    def setUp(self):
        from simulator import Simulator
        self.simulator = Simulator()

    def check_profit(self, str, target):
        """check total profit"""
        assert (float(str.split('Total profit: $')[1]) == target)

    def check_customer_number(self, str, target):
        """check number of customer served"""
        assert (float(str.split('Customer served: ')[1]) == target)

    def test_no_customer(self):
        """testing no customer: should not have run-time error & total_profit, customer served both 0"""
        self.simulator.load_scenario('sample_scenario/test0.txt')
        self.simulator.simulate("sample_scenario/test0_output.txt")
        with open("sample_scenario/test0_output.txt") as f:
            pat = f.readline()
            pat_profit = f.readline()
            pat_num = f.readline()
            mat = f.readline()
            mat_profit = f.readline()
            mat_num = f.readline()
            maxx = f.readline()
            maxx_profit = f.readline()
            maxx_num = f.readline()
            pac = f.readline()
            pac_profit = f.readline()
            pac_num = f.readline()
            self.check_profit(pat_profit,   0)
            self.check_profit(mat_profit,   0)
            self.check_profit(maxx_profit,  0)
            self.check_profit(pac_profit,   0)
            self.check_customer_number(pat_num,     0)
            self.check_customer_number(mat_num,     0)
            self.check_customer_number(maxx_num,    0)
            self.check_customer_number(pac_num,     0)

    def test_customer_attributes(self):
        """testing customer attributes type"""
        from customer import Customer
        sample_str = "3	23215	3.9	4	8"
        test_customer = Customer(sample_str)
        # assert type(test_customer.id()) is int, "id is not an integer: %r" % test_customer.id()
        assert type(test_customer.entry_turn()) is int, "entry_turn is not an integer: %r" % test_customer.entry_turn()
        assert type(test_customer.patience()) is int, "patience is not an integer: %r" % test_customer.patiece()

    def test_1_customer(self):
        """testing 1 customer: all approaches give same results, with correct formatting
        given marks when all passed
        """
        self.simulator.load_scenario('sample_scenario/test1.txt')
        self.simulator.simulate("sample_scenario/test1_output.txt")

        with open("sample_scenario/test1_output.txt") as f:
            pat = f.readline()
            pat_profit = f.readline()
            pat_num = f.readline()
            mat = f.readline()
            mat_profit = f.readline()
            mat_num = f.readline()
            maxx = f.readline()
            maxx_profit = f.readline()
            maxx_num = f.readline()
            pac = f.readline()
            pac_profit = f.readline()
            pac_num = f.readline()
            self.check_profit(pat_profit,   3.9)
            self.check_profit(mat_profit,   3.9)
            self.check_profit(maxx_profit,  3.9)
            self.check_profit(pac_profit,   3.9)
            self.check_customer_number(pat_num,     1)
            self.check_customer_number(mat_num,     1)
            self.check_customer_number(maxx_num,    1)
            self.check_customer_number(pac_num,     1)

    def test_customer_left(self):
        """testing 2 customer where second left before first finished.
        given marks when all passed
        """
        self.simulator.load_scenario('sample_scenario/test3.txt')
        self.simulator.simulate("sample_scenario/test3_output.txt")

        with open("sample_scenario/test3_output.txt") as f:
            pat = f.readline()
            pat_profit = f.readline()
            pat_num = f.readline()
            mat = f.readline()
            mat_profit = f.readline()
            mat_num = f.readline()
            maxx = f.readline()
            maxx_profit = f.readline()
            maxx_num = f.readline()
            pac = f.readline()
            pac_profit = f.readline()
            pac_num = f.readline()
            self.check_profit(pat_profit,   1.9)
            self.check_profit(mat_profit,   1.9)
            self.check_profit(maxx_profit,  1.9)
            self.check_profit(pac_profit,   1.9)
            self.check_customer_number(pat_num,     1)
            self.check_customer_number(mat_num,     1)
            self.check_customer_number(maxx_num,    1)
            self.check_customer_number(pac_num,     1)
    #
    # test2 has A,B,C,D,E,F customers
    # idle between A,B
    # after B, there are 4 customers waiting, different approach will choose different one if implemented correct

    def test_2(self):
        """testing for pat approach"""
        self.simulator.load_scenario('sample_scenario/test2.txt')
        self.simulator.simulate("sample_scenario/test2_output.txt")

        with open("sample_scenario/test2_output.txt") as f:
            l = f.readline()
            total_profit = f.readline()
            total_num = f.readline()
            assert(l == "Results for the serving approach using Pat's suggestion:\n")
            self.check_profit(total_profit,   7)
            self.check_customer_number(total_num,     3)

    def test_3(self):
        """testing for Mat approach"""
        self.simulator.load_scenario('sample_scenario/test2.txt')
        self.simulator.simulate("sample_scenario/test2_output.txt")

        with open("sample_scenario/test2_output.txt") as f:
            for i in range(1, 5):
                l = f.readline()
            total_profit = f.readline()
            total_num = f.readline()
            assert(l == "Results for the serving approach using Mat's suggestion:\n")
            self.check_profit(total_profit,   43)
            self.check_customer_number(total_num,     4)

    def test_4(self):
        """testing for Max approach"""
        self.simulator.load_scenario('sample_scenario/test2.txt')
        self.simulator.simulate("sample_scenario/test2_output.txt")

        with open("sample_scenario/test2_output.txt") as f:
            for i in range(1, 8):
                l = f.readline()
            total_profit = f.readline()
            total_num = f.readline()
            assert(l == "Results for the serving approach using Max's suggestion:\n")
            self.check_profit(total_profit,   35)
            self.check_customer_number(total_num,     3)

    def test_5(self):
        """testing for Pac approach"""
        self.simulator.load_scenario('sample_scenario/test2.txt')
        self.simulator.simulate("sample_scenario/test2_output.txt")

        with open("sample_scenario/test2_output.txt") as f:
            for i in range(1, 11):
                l = f.readline()
            total_profit = f.readline()
            total_num = f.readline()
            assert(l == "Results for the serving approach using Pac's suggestion:\n")
            self.check_profit(total_profit,   59)
            self.check_customer_number(total_num,     5)


if __name__ == '__main__':
    unittest.main()