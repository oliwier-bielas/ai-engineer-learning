import json
from models import Email
from pathlib import Path


class Inbox:

    def __init__(self):
        self._emails: list[Email] = []

    def load_emails(self, path: Path):
        with open(path, "r", encoding="utf-8") as file:
            emails = json.load(file)
            self._emails.extend([self._map_email(email) for email in emails])

    def _map_email(self, email: dict) -> Email:
        return Email(
            topic=email["temat"],
            content=email["tresc"],
            is_read=email["przeczytany"],
            send_by=email["nadawca"]
        )

    @property
    def emails(self) -> list[Email]:
        return list(self._emails)

    def all(self) -> int:
        return len(self._emails)

    def filtered_by_topic(self, name: str) -> list[Email]:
        filtered_emails: list[Email] = [
            email for email in self._emails if name.lower() in email.topic.lower()]
        return filtered_emails

    def unread(self) -> list[Email]:
        filtered_emails: list[Email] = [
            email for email in self._emails if not email.is_read]

        return filtered_emails
