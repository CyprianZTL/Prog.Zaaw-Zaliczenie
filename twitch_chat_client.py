import irc.client
import sys
import os

class TwitchChatClient(irc.client.SimpleIRCClient):
    def __init__(self, channel, target_user, file_path):
        super().__init__()
        self.channel = '#' + channel
        self.target_user = target_user.lower()  # akutualnie nie uzywane ze wzgledu na zmiane przechwytywania
                                                # calego chatu a nie tylko wybranego użytkownika
        self.file_path = file_path

        if not os.path.exists(file_path):    #sprwdzenie czy jest plik chat_log
            print(f"Plik {file_path} nie istnieje, tworzenie nowego pliku.")
            with open(file_path, 'w', encoding='utf-8') as file:
                pass
        else:
            print(f"Plik {file_path} już istnieje.")

        self.file = open(file_path, 'a', encoding='utf-8')  # kodowanie utf-8

    def on_welcome(self, connection, event):
        connection.join(self.channel)

    def on_join(self, connection, event):
        print(f"Dołączyłem do kanału: {self.channel}")

    def on_pubmsg(self, connection, event):
        user = event.source.nick
        message = event.arguments[0]
        print(f"{user}: {message}")
        self.file.write(f"{user}: {message}\n")
        self.file.flush()
        os.fsync(self.file.fileno())

    def on_disconnect(self, connection, event):
        self.file.close()

def main():
    channel = 'Streamer Nick'  # Nazwa kanału streamera
    nickname = 'Your Nickname'  # Twój nick na Twitch
    token = 'Type Your Token'  # Twój token OAuth https://twitchtokengenerator.com/
    target_user = 'Target'  # Nick użytkownika, którego wiadomości chcesz przechwytywać (aktualnie bez uzytku bo przechytuje caly chat)
    file_path = 'chat_log.txt'  # Ścieżka do pliku, w którym będą zapisywane wiadomości

    client = TwitchChatClient(channel, target_user, file_path)
    try:
        client.connect('irc.chat.twitch.tv', 6667, nickname, password=f'oauth:{token}')
    except irc.client.ServerConnectionError:
        print("Could not connect to server.")
        sys.exit(1)

    client.start()

if __name__ == "__main__":
    main()
