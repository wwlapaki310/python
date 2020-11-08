import calculation
import pytest

class TestCal(object):
    def setup_method(self,method):
        print("method={}".format(method.__name__))
        self.cal=calculation.Cal()

    def teardown_method(self,method):
        print("method={}".format(method.__name__))
        del self.cal
    
    @pytest.mark.skip(reason="skip!")
    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1,1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double("1","1")

        """
    @classmethod
    def setup_class(cls):
        print("start")
        cls.cal=calculation.Cal()
    
    @classmethod
    def teardown_method(cls):
        print("end")
        del cls.cal
    """

if __name__ == "__main__":
    c=TestCal()
    c.test_add_num_and_double()
    c.test_add_num_and_double_raise()