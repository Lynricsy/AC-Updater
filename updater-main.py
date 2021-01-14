import requests
import os
if os.path.exists("character_table.json"):
  os.remove("character_table.json")
  print("The file character_table.json already exists.Updating...")
else:
  print("The file character_table.json does not exist.Downloading...")

if os.path.exists("skin_table.json"):
  os.remove("skin_table.json")
  print("The file skin_table.json already exists.Updating...")
else:
  print("The file character_table.json does not exist.Downloading...")
print("downloading Skins&Characters")
url = 'https://cdn.jsdelivr.net/gh/Kengxxiao/ArknightsGameData@master/zh_CN/gamedata/excel/character_table.json'
r = requests.get(url)
with open("character_table.json", "wb") as code:
     code.write(r.content)
url = 'https://cdn.jsdelivr.net/gh/Kengxxiao/ArknightsGameData@master/zh_CN/gamedata/excel/skin_table.json'
r = requests.get(url)
with open("skin_table.json", "wb") as code:
     code.write(r.content)
print("Successfully updated.Enjoy!")