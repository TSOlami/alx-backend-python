#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import (parameterized, parameterized_class)
from client import GithubOrgClient
from typing import (
    List,
    Dict,
)
from unittest.mock import (
    patch,
    MagicMock,
    Mock,
    PropertyMock,
)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):

    """A Github org client test object"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, expected_response: Dict,
                 mocked_function: MagicMock):
        """Implements the test_org method.
        """
        mocked_function.return_value = MagicMock(
            return_value=expected_response)

        gitclient = GithubOrgClient(org)

        self.assertEqual(gitclient.org(), expected_response)

        mocked_function.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
