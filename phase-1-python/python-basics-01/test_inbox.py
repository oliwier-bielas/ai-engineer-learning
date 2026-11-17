from inbox import Inbox
from pathlib import Path
import pytest
from models import Email


@pytest.fixture
def inboxFixture() -> Inbox:
    inbox: Inbox = Inbox()
    DATA_DIR: Path = Path(__file__).parent / "data"
    path: Path = DATA_DIR / "test_emails.json"
    inbox.load_emails(path)
    return inbox


def test_load_and_show_inbox_mails(inboxFixture):
    assert inboxFixture.all() == 1


def test_filter_by_topic(inboxFixture):
    inbox: Inbox = inboxFixture
    emails: list[Email] = inbox.filtered_by_topic("Pilne")
    assert len(emails) == 1


def test_unread(inboxFixture):
    inbox: Inbox = inboxFixture
    unread = inbox.unread()
    assert len(unread) == 1
