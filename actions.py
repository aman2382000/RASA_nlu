from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionTorrent(Action):
	def name(self):
		return 'action_torrent'

	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		api_key = '...'
		client = ApixuClient(api_key)

		loc = tracker.get_slot('location')
		current = client.getcurrent(q=loc)

		link = current

        response = """Your torrent link is {}""".format(link)
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]
