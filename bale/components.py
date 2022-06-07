class Components:
    """
        Args:
            keyboards (:class:`bale.Keyboards`): Defaults to None.
            inlinekeyboards (:class:`bale.InlineKeyboards`): Defaults to None.
    """

    __slots__ = (
        "keyboards",
        "inlinekeyboards"
    )

    def __init__(self, keyboards=None, inlinekeyboards=None):
        self.keyboards: list = None
        self.inlinekeyboards: list = None
        if keyboards is not None:
            self.keyboards = []
            if isinstance(keyboards, list):
                for i in keyboards:
                    if type(i) is dict:
                        self.keyboards.append([i])
                    elif type(i) is list:
                        key_list = []
                        for i in i:
                            if isinstance(i, Keyboard):
                                key_list.append(i.to_dict())
                            else:
                                key_list.append(i)
                        self.keyboards.append(key_list)
                    elif type(i) is Keyboard:
                        self.keyboards.append([i.to_dict()])
            else:
                if "name" in keyboards:
                    self.keyboards.append(keyboards)
        if inlinekeyboards is not None:
            self.inlinekeyboards = []
            if type(inlinekeyboards) is list:
                for i in inlinekeyboards:
                    if type(i) is dict:
                        self.inlinekeyboards.append([i])
                    elif type(i) is list:
                        key_list = []
                        for i in i:
                            if isinstance(i, InlineKeyboard):
                                key_list.append(i.to_dict())
                            else:
                                key_list.append(i)
                        self.inlinekeyboards.append(key_list)
                    elif type(i) is InlineKeyboard:
                        self.inlinekeyboards.append([i.to_dict()])
            elif type(inlinekeyboards) is dict:
                if "name" in inlinekeyboards and "callback_data" in inlinekeyboards:
                    self.inlinekeyboards.append(inlinekeyboards)

    @classmethod
    def from_dict(cls, data: dict):
        """
        Args:
            data (dict): Data
        """
        return cls(keyboards=data["keyboard"], inlinekeyboards=data["inline_keyboard"])

    def to_dict(self):
        """Convert Class to dict
            Returns:
                :dict:
        """
        data = {
            "keyboard": self.keyboards,
            "inline_keyboard": self.inlinekeyboards
        }

        return data


class InlineKeyboard:
    """This object shows an in -line keyboard (within the message).

        Args:
            text (str): _description_
            callback_data (str, optional): _description_. Defaults to None.
            url (str, optional): _description_. Defaults to None.
            switch_inline_query (str, optional): _description_. Defaults to None.
            switch_inline_query_current_chat (str, optional): _description_. Defaults to None.
            pay (bool, optional): _description_. Defaults to False.
    """
    __slots__ = (
        "text", "callback_data", "url", "switch_inline_query", "switch_inline_query_current_chat", "pay"
    )

    def __init__(self, text: str, callback_data: str = None, url: str = None, switch_inline_query: str = None,
                 switch_inline_query_current_chat: str = None, pay: bool = False):
        self.text = text
        self.callback_data = callback_data if callback_data is not None else None
        self.url = url if url is not None else None
        self.switch_inline_query = switch_inline_query if switch_inline_query is not None else switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat if switch_inline_query_current_chat is not None else None
        self.pay = pay if pay else False

    @classmethod
    def from_dict(cls, data: dict):
        """
        Args:
            data (dict): Data
        """
        if not data.get("text") or not data.get("callback_data"):
            return None
        return cls(text=data["text"], callback_data=data.get("callback_data"), url=data.get("url"),
                   switch_inline_query=data.get("switch_inline_query"),
                   switch_inline_query_current_chat=data.get("switch_inline_query_current_chat"),
                   pay=data.get("pay", False))

    def to_dict(self):
        """Convert Class to dict
            Returns:
                :dict:
        """
        data = {
            "text": self.text
        }

        if self.callback_data:
            data["callback_data"] = self.callback_data

        if self.url:
            data["url"] = self.url

        if self.switch_inline_query:
            data["switch_inline_query"] = self.switch_inline_query

        if self.switch_inline_query_current_chat:
            data["switch_inline_query_current_chat"] = self.switch_inline_query_current_chat

        if self.pay:
            data["pay"] = self.pay

        return data


class Keyboard:
    """This object shows a keyboard

        Args:
            text (str): Keyboard Text.
    """
    __slots__ = (
        "text"
    )

    def __init__(self, text: str):
        self.text = text

    @classmethod
    def from_dict(cls, data: dict):
        """
        Args:
            data (dict): Data
        """
        if not data.get("text"):
            return None
        return cls(text=data["text"])

    def to_dict(self):
        """Convert Class to dict
        Returns:
            :dict:
        """
        data = {
            "text": self.text
        }
        return data
