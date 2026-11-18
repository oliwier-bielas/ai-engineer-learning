from inbox import Inbox
from pathlib import Path
from models import Email


def get_emails_path() -> Path:
    DATA_DIR: Path = Path(__file__).parent / "data"
    path: Path = DATA_DIR / "emails.json"
    return path


def get_urgent_emails_topics(inbox: Inbox) -> list[str]:
    urgent_emails: list[Email] = inbox.filtered_by_topic(
        "pilne")  # urgent in polish
    urgent_topics: list[str] = [email.topic for email in urgent_emails]

    return urgent_topics


def get_unread_email_senders(inbox: Inbox) -> list[str]:
    unread_emails: list[Email] = inbox.unread()
    senders: list[str] = [email.send_by for email in unread_emails]

    return senders


def print_task_results():
    inbox = Inbox()

    inbox.load_emails(get_emails_path())
    print(f"All emails: {inbox.all()}")
    print(f"Urgent: {get_urgent_emails_topics(inbox)}")
    print(f"Unread emails from: {get_unread_email_senders(inbox)}")


if __name__ == "__main__":
    print_task_results()
