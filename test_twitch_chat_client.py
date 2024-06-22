import unittest
from unittest.mock import MagicMock, patch
import os
import irc.client
from twitch_chat_client import TwitchChatClient

class TestTwitchChatClient(unittest.TestCase):

    @patch.object(irc.client.SimpleIRCClient, '__init__', lambda x: None)
    def setUp(self):
        self.channel = 'test_channel'
        self.target_user = 'test_user'
        self.file_path = 'test_chat_log.txt'
        self.client = TwitchChatClient(self.channel, self.target_user, self.file_path)
        self.mock_client = MagicMock()
        self.client.connection = self.mock_client

    def tearDown(self):
        self.client.file.close()  # upewnienie się,że plik jest zamknięty
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_initialization_creates_file(self):
        self.assertTrue(os.path.exists(self.file_path))

    def test_on_welcome_joins_channel(self):
        self.client.on_welcome(self.mock_client, None)
        self.mock_client.join.assert_called_with(f'#{self.channel}')

    def test_on_pubmsg_writes_to_file(self):
        event = MagicMock()
        event.source.nick = 'test_user'
        event.arguments = ['test message']
        self.client.on_pubmsg(self.mock_client, event)
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        self.assertIn(f"test_user: test message\n", lines)

    def test_on_disconnect_closes_file(self):
        self.client.on_disconnect(self.mock_client, None)
        self.assertTrue(self.client.file.closed)

class TestTwitchChatClientIntegration(unittest.TestCase):

    @patch.object(irc.client.SimpleIRCClient, '__init__', lambda x: None)
    @patch.object(irc.client.SimpleIRCClient, 'connect')
    def test_full_workflow(self, mock_connect):
        channel = 'test_channel'
        target_user = 'test_user'
        file_path = 'test_chat_log.txt'
        nickname = 'test_nick'
        token = 'test_token'

        client = TwitchChatClient(channel, target_user, file_path)
        client.connection = MagicMock()
        client.connect('irc.chat.twitch.tv', 6667, nickname, password=f'oauth:{token}')

        client.on_welcome(client.connection, None)
        client.on_join(client.connection, None)

        event = MagicMock()
        event.source.nick = 'test_user'
        event.arguments = ['test message']
        client.on_pubmsg(client.connection, event)

        client.on_disconnect(client.connection, None)

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        self.assertIn(f"test_user: test message\n", lines)
        os.remove(file_path)

class TestTwitchChatClientAcceptance(unittest.TestCase):

    @patch.object(irc.client.SimpleIRCClient, '__init__', lambda x: None)
    @patch.object(irc.client.SimpleIRCClient, 'connect')
    def test_acceptance_scenario(self, mock_connect):
        channel = 'test_channel'
        target_user = 'test_user'
        file_path = 'test_chat_log.txt'
        nickname = 'test_nick'
        token = 'test_token'

        client = TwitchChatClient(channel, target_user, file_path)
        client.connection = MagicMock()
        client.connect('irc.chat.twitch.tv', 6667, nickname, password=f'oauth:{token}')

        client.on_welcome(client.connection, None)
        client.on_join(client.connection, None)

        event = MagicMock()
        event.source.nick = 'test_user'
        event.arguments = ['test message']
        client.on_pubmsg(client.connection, event)

        client.on_disconnect(client.connection, None)

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        self.assertIn(f"test_user: test message\n", lines)
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
