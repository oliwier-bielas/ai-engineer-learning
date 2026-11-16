import json
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Email:
    topic: str
    content: str
    status: bool
    send_by: str


class Inbox:

    def __init__(self):
        self._emails: list[Email] = []

    def load_emails(self):
        with open("emails.json", "r") as file:
            emails = json.load(file)
            for email in emails:
                mappedEmail = self._map_email(email)
                self._emails.append(mappedEmail)

    def _map_email(self, email: dict) -> Email:
        return Email(
            topic=email["temat"],
            content=email["tresc"],
            status=email["przeczytany"],
            send_by=email["nadawca"]
        )

    def all(self) -> int:
        return len(self._emails)

    def filer_by_topic(self, name: str) -> list[Email]:
        filtred_emails = filter(
            lambda email: name.lower() in email.topic.lower(), self._emails)
        return filtred_emails

    def unread(self) -> list[str]:
        filtred_emails = filter(
            lambda email: email.status == False, self._emails)

        return filtred_emails


if __name__ == "__main__":
    inbox = Inbox()
