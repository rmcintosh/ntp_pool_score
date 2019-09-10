import unittest
import unittest.mock

import ntp_pool_score


class MockedResponse:
    def __init__(self, *args):
        with open(f"tests/mocks/{self.outcome}.html", "r") as f:
            self.text = f.read()


class MockedSuccessfulResponse(MockedResponse):
    outcome = "success"


class MockedFailedResponse(MockedResponse):
    outcome = "failure"


class TestNTPPoolScore(unittest.TestCase):
    """These tests just ensure that we haven't broken the parsing
    of the ntppool.org score pages as currently constructed
    """
    def test_get_server_ntp_pool_score_score_exists(self):
        with unittest.mock.patch("requests.get") as f:
            f.return_value = MockedSuccessfulResponse()
            self.assertIsInstance(
                ntp_pool_score.get_server_ntp_pool_score(None), float
            )

    def test_get_server_ntp_pool_score_score_doesnt_exist(self):
        with unittest.mock.patch("requests.get") as f:
            f.return_value = MockedFailedResponse()
            with self.assertRaises(ntp_pool_score.ScoreNotFound):
                ntp_pool_score.get_server_ntp_pool_score(None)
