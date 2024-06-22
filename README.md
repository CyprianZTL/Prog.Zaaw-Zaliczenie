# 🟣 Twitch Chat Client

## 📜 Opis projektu
Aplikacja łączy się z serwerem IRC Twitch, nasłuchuje wiadomości na określonym kanale i zapisuje wiadomości od konkretnego użytkownika do pliku tekstowego.

## 🏗️ Struktura systemu
- `twitch_chat_client.py`: Implementacja klienta czatu Twitch.
- `test_twitch_chat_client.py`: Testy automatyczne aplikacji.

## 🧪 Scenariusze testów
### Testy jednostkowe
- 🗂️ `test_initialization_creates_file`: Sprawdza, czy plik logu czatu jest tworzony podczas inicjalizacji klienta.
- 🗂️ `test_on_welcome_joins_channel`: Sprawdza, czy klient dołącza do kanału po otrzymaniu zdarzenia powitania.
- 🗂️ `test_on_pubmsg_writes_to_file`: Sprawdza, czy wiadomości publiczne są zapisywane do pliku.
- 🗂️ `test_on_disconnect_closes_file`: Sprawdza, czy plik jest zamykany po rozłączeniu klienta.

### Testy integracyjne
- 🧩 `test_full_workflow`: Symuluje pełny przepływ pracy klienta czatu, od połączenia, przez odbieranie wiadomości, aż do rozłączenia.

### Testy akceptacyjne
- ✔️ `test_acceptance_scenario`: Sprawdza, czy klient czatu Twitch działa zgodnie z oczekiwaniami w rzeczywistym scenariuszu użycia.

## 🛠️ Wykorzystane narzędzia i biblioteki
- 🐍 **Python**
- 📦 **irc.client**: Biblioteka do obsługi połączeń IRC.
- 🧪 **unittest**: Wbudowana biblioteka Pythona do tworzenia testów jednostkowych.
- 🔧 **unittest.mock**: Moduł do tworzenia obiektów mock używany w testach jednostkowych i integracyjnych.

## 📝 Problemy i rozwiązania
### 🛑 Problem 1: Brak połączenia z serwerem Twitch IRC
- **Opis**: Podczas testowania rzeczywistego połączenia z serwerem Twitch IRC, może wystąpić problem z połączeniem.
- **Rozwiązanie**: Sprawdź, czy token OAuth jest poprawny i aktualny. Upewnij się, że nie ma problemów z siecią. Możesz także użyć mocków do testowania logiki bez rzeczywistego połączenia.

### 🛑 Problem 2: Nieprzewidziane błędy podczas zapisywania do pliku
- **Opis**: Podczas zapisywania wiadomości do pliku mogą wystąpić błędy, jeśli plik jest niedostępny lub nie można go utworzyć.
- **Rozwiązanie**: Upewnij się, że ścieżka do pliku jest poprawna i masz odpowiednie uprawnienia do zapisu. Dodaj odpowiednie mechanizmy obsługi błędów w kodzie.

### 🛑 Problem 3: Nieaktualne zależności
- **Opis**: W przypadku używania starszych wersji bibliotek, mogą wystąpić problemy z kompatybilnością.
- **Rozwiązanie**: Upewnij się, że używasz najnowszych wersji bibliotek `irc.client` i `unittest`. Możesz to zrobić za pomocą narzędzia do zarządzania zależnościami, takiego jak `pip`.

## 🚀 Jak uruchomić testy
Aby uruchomić testy, użyj następującej komendy:
```sh
py -m unittest discover
