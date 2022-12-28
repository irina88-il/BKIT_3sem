import unittest
from func import get_roots 
from behave import given, when, then, step

class func_test(unittest.TestCase):
    def test1(self):
        res = get_roots(1, -5, 4)
        self.assertEqual(res, [2, -2, 1, -1])
    
    def test2(self):
        res = get_roots(1, -5, -36)
        self.assertEqual(res, [3, -3])

    def test3(self):
        res = get_roots(1, 10, 9)
        self.assertEqual(res, [])


@given("we have coef")
def step_impl(context):
    pass

@when('we solve the equation with [1, -5, 4]')
def step_impl(context):
    print('I solve the equation')
    
@then('we get roots')
def step_impl(context):
    print('I get roots')
    assert get_roots(1, -5, 4) == [2, -2, 1, -1]





if __name__ == '__main__':
    unittest.main()
    
