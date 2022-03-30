from .user import User
from .components import ReplyMarkup
from .chat import Chat
from telegram.chat import Chat
import datetime

class Message():
    __slots__ = (
        "text", "caption", "forward_from", "author","contact", "chat","message_id", "date_code", "date", "author", "edit_date", "audio", "document", "photo", "voice", "location", "invoice"
    )
    def __init__(self, message_id : int, date : datetime.datetime, text = None, caption = None, forward_from = None, contact = None, chat : Chat = None, document = None, photo = None, voice = None, location = None, invoice = None, bot = None):
        self.message_id = message_id if message_id is not None else None
        self.date = date if date is not None else None
        
        self.text = text if text is not None else None
        self.chat = chat if chat is not None else None
        self.forward_from = forward_from if forward_from is not None else None
        self.caption = caption if caption is not None else None
        self.contact = contact if contact is not None else None
        self.bot = bot if bot is not None else None

    @property
    def author(self):
        if self.chat is not None:
            if self.chat.type == Chat.PRIVATE:
                self.author = User(id = self.chat.id, first_name = self.chat.first_name, last_name = self.chat.last_name, username = self.chat.username, bot = self)
            elif self.chat.type == Chat.GROUP: 
                self.author = User.dict(bot = self, data = "")
        return None
    
    def delete(self, timeout):
        if not isinstance(timeout, (tuple, int)):
            raise "Time out Not true"
        Message = self.bot.get(f"{self.baseclass.base_url}bot{self.baseclass.token}/deletemessage", params = {
        "chat_id": f"{self.chat_id}",
        "message_id": f"{self.message_id}"
        }, timeout = timeout)
        return Message.json()
    
    def reply(self, text, components = None, reply_to_message_id : bool = True):
        json = {}
        json["chat_id"] = f"{self.chat_id}"
        json["text"] = f"{text}"
        if components:
            if type(components) is ReplyMarkup:
                json["reply_markup"] = components.result
            elif type(components) is dict:
                json["reply_markup"] = components
        if reply_to_message_id:
            json["reply_to_message_id"] = str(self.message_id)
        Message = post(f"{self.baseclass.base_url}bot{self.baseclass.token}/sendMessage", json = json, timeout = (10, 15))
        return Message.json()["result"]
    
    def reply_message_invoice(self, title, description, provider_token, prices, photo_url = False, need_name = False, need_phone_number = False, need_email = False, need_shipping_address = False, is_flexible = True, reply_markup = None):
        json = {}
        json["chat_id"] = f"{self.chat_id}"
        json["title"] = f"{title}"
        json["description"] = f"{description}"
        json["provider_token"] = f"{provider_token}"
        json["prices"] = prices
        if photo_url:
            json["photo_url"] = photo_url
        if need_name:
            json["need_name"] = need_name
        if need_phone_number:
            json["need_phone_number"] = need_phone_number
        if need_email:
            json["need_email"] = need_email
        if need_shipping_address:
            json["need_shipping_address"] = need_shipping_address
        if is_flexible:
            json["is_flexible"] = is_flexible
        if reply_markup:
            json["reply_markup"] = reply_markup
        Message = post(f"{self.baseclass.base_url}bot{self.baseclass.token}/sendMessage", json = json, timeout = (10, 15))
        return Message.json()["result"]
    
    def get_chat_info(self, timeout):
        if not isinstance(timeout, (tuple, int)):
            raise "Time out Not true"
        info = get(f"{self.baseclass.base_url}bot{self.baseclass.token}/getChat", params = {
            "chat_id": str(self.chat_id)
        }, timeout = timeout)
        return info.json()
    
    def __str__(self):
        return self.message_id