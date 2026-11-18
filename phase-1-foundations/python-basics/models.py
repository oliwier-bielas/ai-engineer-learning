from dataclasses import dataclass


@dataclass
class Email:
    topic: str
    content: str
    is_read: bool
    send_by: str
