# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

 from typing import Any, Text, Dict, List

 from rasa_sdk import Action, Tracker
 from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


 class ActionShowFlights(Action):

     #def name(self) -> Text:
         #return "show_the_flights"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'location':
                 name = e['value']
             
             if name == "Kolkata":
                 message = "Indigo, Air India, SpiceJets, Vistara "
             if name == "Chennai":
                 message = "Indigo, Air India, SpiceJets, Vistara "

         dispatcher.utter_message(text="Looking into the flights schedule")

         return []
     
 class ActionShowWeather(Action):

     def name(self) -> Text:
         return "show_the_weather"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'date':
                 name = e['value']
             
             if name == "Kolkata":
                 message = "Indigo, Air India, SpiceJets, Vistara "
             if name == "Chennai":
                 message = "Indigo, Air India, SpiceJets, Vistara "
         dispatcher.utter_message(text="Showing the weather")

         return []
     
 class ActionShowProduct(Action):

     def name(self) -> Text:
         return "describe_the_product"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'product-name':
                 name = e['value']
             
             if name == "AB":
                 message = "Air Conditioner, Energy Efficient, 5 stars "
             if name == "EF":
                 message = "Refrigerator, Energy Efficient, 5 stars "
         dispatcher.utter_message(text="Showing product description")

         return []