from inbox import Inbox
from pathlib import Path


def get_emails_path() -> str:
    DATA_DIR = Path(__file__).parent / "data"
    print(DATA_DIR)
    path = DATA_DIR / "emails.json"
    return path


if __name__ == "__main__":
    inbox = Inbox()
    inbox.load_emails(get_emails_path())

    print(f"All emails: {inbox.all()}")
