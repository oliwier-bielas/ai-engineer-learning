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


def test_load_skips_invalid_emails(inboxFixture):
    assert inboxFixture.all() == 4


def test_filter_by_topic(inboxFixture):
    emails: list[Email] = inboxFixture.filtered_by_topic("Pilne")
    assert len(emails) == 2


def test_unread(inboxFixture):
    unread = inboxFixture.unread()
    assert len(unread) == 2
