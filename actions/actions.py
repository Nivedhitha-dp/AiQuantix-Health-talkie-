# This files contains your custom actions which can be used to run
# custom Python code.
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# This is a simple example for a custom action which utters "Hello World!"



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser #inbuit in python for opening the link in web browser
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from geopy.geocoders import Nominatim
import requests

# class ActionSaveConversation(Action):
#
#     def name(self) -> Text:
#         return "action_save_conversation"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         conversation = tracker.events
#         print(conversation)
#         import os
#         if not os.path.isfile('chats.csv'):
#             with open('chats.csv', 'w') as file:
#                 file.write("intent,user_input,entity_name,entity_value,action,bot_reply\n")
#         chat_data = ''
#         for i in conversation:
#             if i['event'] == 'user':
#                 chat_data += i['parse_data']['intent']['name']+','+i['text']+','
#                 print('user: {}'.format(i['text']))
#                 if len(i['parse_data']['entities']) > 0:
#                     chat_data += i['parse_data']['entities'][0]['entity']+','+i['parse_data']['entities'][0]['value']+','
#                     print('extra data:', i['parse_data']['entities'][0]['entity'], '=',
#                           i['parse_data']['entities'][0]['value'])
#                 else:
#                     chat_data += ",,"
#             elif i['event'] == 'bot':
#                 print('Bot: {}'.format(i['text']))
#                 try:
#                     chat_data += i['metadata']['utter_action']+','+i['text']+'\n'
#                 except KeyError:
#                     pass
#         else:
#             with open('chats.csv', 'a') as file:
#                 file.write(chat_data)
#
#         dispatcher.utter_message(text="Thank you ,your response has been saved.")
#
#         return []
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            # tracker keeps the record of all the conversation i.e going on

            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Welcome,greet ny saying 'Hi'!")

        return []

class ActionSaveConversation(Action):

    def name(self) -> Text:
        return "action_save_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conversation = tracker.events
        print(conversation)
        import os
        if not os.path.isfile('chats.csv'):
            with open('chats.csv', 'w') as file:
                file.write("intent,user_input,entity_name,entity_value,action,bot_reply\n")
        chat_data = ''
        for i in conversation:
            if i['event'] == 'user':
                chat_data += i['parse_data']['intent']['name']+','+i['text']+','
                print('user: {}'.format(i['text']))
                if len(i['parse_data']['entities']) > 0:
                    chat_data += i['parse_data']['entities'][0]['entity']+','+i['parse_data']['entities'][0]['value']+','
                    print('extra data:', i['parse_data']['entities'][0]['entity'], '=',
                          i['parse_data']['entities'][0]['value'])
                else:
                    chat_data += ",,"
            elif i['event'] == 'bot':
                print('Bot: {}'.format(i['text']))
                try:
                    chat_data += i['metadata']['utter_action']+','+i['text']+'\n'
                except KeyError:
                    pass
        else:
            with open('chats.csv', 'a') as file:
                file.write(chat_data)

        dispatcher.utter_message(text="Thank you ,your response has been saved.")

        return []
class Actionupload(Action):
    def name(self) -> Text:
        return "action_upload"

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        video_url="http://127.0.0.1:8000/"
        dispatcher.utter_message("Wait while the form opens..")
        webbrowser.open(video_url) #opens in the new tab
        return []

class ActionMakePhoneCall(Action):
    def name(self) -> Text:
        return "action_make_phone_call"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # get user's phone number
        account_sid = 'AC94591124307ec8de698fe9b6969ecc43'
        auth_token = 'b89b126016765fd2b55a0ef6093e1994'
        TWILIO_PHONE_NUMBER = '+16315296629'

        # The phone number you want to call
        to_phone_number = '+919790931300'
        # get user's location using ipinfo.io API
        url = "https://ipinfo.io/json"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {'dfb60de8fa86bc'}"
        }
        response = requests.get(url, headers=headers)

        # check if location was successfully retrieved
        if response.status_code == 200:
            location = response.json()
            latitude, longitude = location["loc"].split(",")
            message = f"Emergency call for ambulance service. Google map location : https://www.google.com/maps/place/13%C2%B002'52.5%22N+80%C2%B011'36.3%22E/@13.0479243,80.1912365,17z/data=!3m1!4b1!4m4!3m3!8m2!3d13.0479243!4d80.1934252?hl=en"

        else:
            message = "Emergency call for ambulance service. Google map location : https://www.google.com/maps/place/13%C2%B002'52.5%22N+80%C2%B011'36.3%22E/@13.0479243,80.1912365,17z/data=!3m1!4b1!4m4!3m3!8m2!3d13.0479243!4d80.1934252?hl=en"

        # make the phone call using Twilio API
        account_sid = account_sid
        auth_token1 = auth_token
        client = Client(account_sid, auth_token1)

        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=to_phone_number,
            from_=TWILIO_PHONE_NUMBER
        )

        # send location as SMS to the recipient
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone_number
        )
        dispatcher.utter_message("Call Recieved ! Ambulance would be right there !")
        return []
# class ActionService(Action):
#
#     def name(self) -> Text:
#         return "action_service"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#
#         buttons=[
#             {"payload": '/chitchat/ask_login{content_type":"login"}',"title":"Login Issues"},
#             {"payload": '/chitchat/ask_faculty{content_type":"faculty"}', "title": "Faculty Related"},
#             {"payload": '/chitchat/ask_payment{content_type":"payment"}', "title": "Payment Issues"},
#             {"payload": '/chitchat/ask_approval_process{content_type":"approval"}', "title": "Approval Process"},
#             {"payload": '/chitchat/ask_change_details{content_type":"application"}', "title": "Application form"},
#
#             ]
#
#         dispatcher.utter_message(text="Anything I can help you from below?", buttons=buttons)
#
#         return []

#       buttons=[
#                   {
#                       "title": "great",
#                       "payload": "great"
#                   },
#                   {
#                       "title": "super sad",
#                       "payload": "super sad"
#                   }
#               ]
#
# dispatcher.utter_message(text="Hey hi, Anything I can help you from below?", buttons=button)