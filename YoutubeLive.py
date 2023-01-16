import pytchat
import pymongo
chat = pytchat.create(video_id="brE8_gE014w")

# Connect to the MongoDB database
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['youtube']
collection = db['chat_log']

while chat.is_alive():
  for c in chat.get().sync_items():
    #print(dir(c))
    print(f"{c.datetime} [{c.author.name}]- {c.message}")
    date = c.datetime
    name = c.author.name
    message = c.message
    data = {
      'dateTime': date,
      'authorName': name,
      'Message': message,
    }
    collection.insert_one(data)
