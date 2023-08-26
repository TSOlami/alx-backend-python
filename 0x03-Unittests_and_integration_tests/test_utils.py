#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
"""Write the unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from
unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map
method to test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function
"""


class TestAccessNestedMap(unittest.TestCase):
    """Class that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Unit test method for testing access_nested_map module
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception):
        """Unit test method for testing access_nested_map module exception
        """
        self.assertRaises(
            expected_exception, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class to implement the TestGetJson.test_get_json method
    """

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
        ])
    def test_get_json(self, url, expected_result):
        """Method to test that utils.get_json returns the expected result.
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_result
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)
            self.assertEqual(response, expected_result)

class TestMemoize(unittest.TestCase):
    """A test memoized class
    """

    def test_memoize(self):
        """A test memoize method 
        """


        class TestClass:
            """A test class for testing the memoized function
            """

            def a_method(self):
                """A method that returns 42
                """
                return 42

            @memoize
            def a_property(self):
                """A property method that returns a method
                """
                return self.a_method()
        mock_obj = TestClass()
        with patch.object(mock_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            first_call = mock_obj.a_property
            second_call = mock_obj.a_property

            mock_method.assert_called_once()