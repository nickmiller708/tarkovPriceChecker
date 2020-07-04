import json
import requests
import re


def ScriptToggled(state):
	return

def ReloadSettings(jsonData):
	Init()
	return

def Init():
	global settings
	path = os.path.dirname(__file__)
	settings = {
			"liveOnly": True,
			"command": "!pricecheck",
			"permission": "Everyone",
			"useCooldown": True,
			"useCooldownMessages": True,
			"cooldown": 1,
			"onCooldown": "$user, $command is still on cooldown for $cd minutes!",
			"userCooldown": 60,
			"onUserCooldown": "$user $command is still on user cooldown for $cd minutes!",

def Tick():
	return

def Execute(data):
	URL = "https://tarkov-market.com/api/items?lang=en&search="
	if data.IsChatMessage() and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
		outputMessage = ""
		if settings["useCooldown"] and (Parent.IsOnCooldown(ScriptName, command) or Parent.IsOnUserCooldown(ScriptName, command, userId)):
			if settings["useCooldownMessages"]:
				if Parent.GetCooldownDuration(ScriptName, command) > Parent.GetUserCooldownDuration(ScriptName, command, userId):
					cdi = Parent.GetCooldownDuration(ScriptName, command)
					cd = str(cdi / 60) + ":" + str(cdi % 60).zfill(2) 
					outputMessage = settings["onCooldown"]
				else:
					cdi = Parent.GetUserCooldownDuration(ScriptName, command, userId)
					cd = str(cdi / 60) + ":" + str(cdi % 60).zfill(2) 
					outputMessage = settings["onUserCooldown"]
				outputMessage = outputMessage.replace("$cd", cd)
			else:
				outputMessage = ""

		# api-endpoint 
		url      = https://tarkov-market.com/api/items"
		itemName = data.getParam(1)
		params = { 'search': itemName, 'lang': 'en' }
		dataResponse = requests.get(url = url, params = params).json()
		items = dataResponse['items']
		for item in items: 
			insertMessage = "item name: %in | average price: %price"
			insertMessage.replace("%in", item['enName'])
			insertMessage.replace("price", item['avgDayPrice'])
			outputMessage += insertMessage

		Parent.SendStreamMessage(outputMessage)
	return	
