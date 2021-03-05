from pymongo import MongoClient

client = MongoClient(host="server.lan")

user = 'device_user'
password = 'kyyfzx78..'

db = client['device_register']
db.authenticate(user, password)

db.command()