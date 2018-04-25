from collections import namedtuple

from src.util import namedtuple_to_dict


def test_namedtuple_to_dict():
    TestClass = namedtuple('TestClass', 'test_field_1 test_field_2, test_field_3')
    test_namedtuple = TestClass('test_value_1', 'test_value_2', 'test_value_3')

    expected_output = {'testclass': {'test_field_1': 'test_value_1',
                                     'test_field_2': 'test_value_2',
                                     'test_field_3': 'test_value_3'}}

    assert namedtuple_to_dict(test_namedtuple) == expected_output
