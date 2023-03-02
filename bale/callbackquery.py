"""
MIT License

Copyright (c) 2023 Kian Ahmadian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from __future__ import annotations
from bale import User, Message
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from bale import Bot

__all__ = (
    "CallbackQuery"
)


class CallbackQuery:
    """
    This object represents an incoming callback query from a callback button in an inline keyboard.
    """
    __slots__ = (
        "message",
        "inline_message_id",
        "from_user",
        "data",
        "bot",
        "callback_id"
    )

    def __init__(self, callback_id: int = None, data: str = None, message: "Message" = None,
                 inline_message_id: str = None, from_user: "User" = None, bot: "Bot" = None):
        self.data = data
        self.callback_id = callback_id
        self.message = message
        self.inline_message_id = inline_message_id
        self.from_user = from_user
        self.bot = bot

    @property
    def user(self):
        """Aliases for :attr:`from_user`"""
        return self.from_user

    @classmethod
    def from_dict(cls, data: dict, bot: "Bot"):
        return cls(bot=bot, data=data.get("data"), callback_id=data.get("id"), message=Message.from_dict(data.get("message"), bot=bot),
                   inline_message_id=data.get("inline_message_id"),
                   from_user=User.from_dict(bot=bot, data=data.get("from")))

    def to_dict(self):
        data = {
            "id": self.callback_id
        }

        if self.data:
            data["data"] = self.data
        if self.inline_message_id:
            data["inline_message_id"] = self.inline_message_id
        if self.message:
            data["message"] = self.message.to_dict()
        if self.from_user:
            data["from_user"] = self.from_user.to_dict()

        return data

    def __repr__(self):
        return f"<CallbackQuery inline_message_id={self.inline_message_id} message={self.message} from_user={self.from_user} data={self.data}>"
