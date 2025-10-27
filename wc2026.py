import zulip
import random
import datetime
from zulip_bots.lib import AbstractBotHandler
from typing import Dict

class WC2026BotHandler:
    '''
    WC2026-bot responds to messages with the word 'soccer' in them. 
    It responds with a world cup video and a short message.
    '''

    def usage(self) -> str:
        return '''WC2026-bot responds to messages with the word 'soccer' in them. It responds with a world cup video and a short message.'''

    @staticmethod
    def get_world_cup_vid() -> str:
        """
        Returns a random soccer video from youtube
        """
        soccer_vids = [
            "https://www.youtube.com/watch?v=Btlovb66hzI",
            "https://www.youtube.com/watch?v=c0cUE-ePDEc",
            "https://www.youtube.com/watch?v=PM79nfZr30I",
            "https://www.youtube.com/watch?v=dZpLa0lU1nU",
            "https://www.youtube.com/watch?v=ca10He-i37g",
            "https://www.youtube.com/watch?v=LO4bcOnnJnA",
            "https://www.youtube.com/watch?v=CiAU2Ei5LbI", 
            "https://www.youtube.com/watch?v=L12Ntmgh54Q",
            "https://www.youtube.com/watch?v=iLMTeX8j3NU",
            "https://www.youtube.com/watch?v=6t3gJMx8d-E",
            "https://www.youtube.com/watch?v=Re4aDJL3heA",
            "https://www.youtube.com/watch?v=FMetb733dME",
            "https://www.youtube.com/watch?v=kBJVZ5k-F3M",
            "https://www.youtube.com/watch?v=x1K_BiOvdn0",
            "https://www.youtube.com/watch?v=qSznZ9spb6A",
            "https://www.youtube.com/watch?v=OQ0zG6a2bWg",
            "https://www.youtube.com/watch?v=XegYZ8y3xMY",
            "https://www.youtube.com/watch?v=f2_VbbIq6Hw",
            "https://www.youtube.com/watch?v=EYPS5JuBmdc",
            "https://www.youtube.com/watch?v=ZPVPrhADhzk",
        ]

        return random.choice(soccer_vids)

    def handle_message(self, message: Dict[str, str], bot_handler: AbstractBotHandler):
            """
            Processes incoming Zulip messages and responds if 'soccer' is found.
            """
            content = message['content'].lower()
            
            if "soccer" in content:
                video_url = self.get_world_cup_vid()
                
                world_cup_start = datetime.date(2026, 6, 11)
                today = datetime.date.today()
                days_until = (world_cup_start - today).days
                
                response_content = f"⚽ There are {days_until} days until the start of the 2026 World Cup! {video_url}"

                bot_handler.send_reply(message, response_content)
            
            print("DEBUG received:", message)

handler_class = WC2026BotHandler