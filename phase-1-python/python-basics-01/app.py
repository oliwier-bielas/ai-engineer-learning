from inbox import Inbox
from pathlib import Path
from models import Email


def get_emails_path() -> str:
    DATA_DIR = Path(__file__).parent / "data"
    print(DATA_DIR)
    path = DATA_DIR / "emails.json"
    return path


def get_urgent_emails_topics(inbox: Inbox) -> list[str]:
    urgent_emails: list[Email] = inbox.filer_by_topic("pilne")
    urgent_topics: list[str] = []

    for email in urgent_emails:
        urgent_topics.append(email.topic)

    return urgent_topics


def get_unread_email_senders(inbox: Inbox) -> list[str]:
    unread_emails: list[Email] = inbox.unread()
    senders: list[str] = []

    for email in unread_emails:
        senders.append(email.send_by)

    return senders


def print_task_results():
    inbox = Inbox()

    inbox.load_emails(get_emails_path())
    print(f"All emails: {inbox.all()}")
    print(f"Urgent: {get_urgent_emails_topics(inbox)}")
    print(f"Unread emails from: {get_unread_email_senders(inbox)}")


if __name__ == "__main__":
    print_task_results()
