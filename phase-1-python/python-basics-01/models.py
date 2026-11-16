from dataclasses import dataclass


@dataclass
class Email:
    topic: str
    content: str
    status: bool
    send_by: str
