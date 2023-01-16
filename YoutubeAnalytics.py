import csv
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.youtube
collection = db.chat_log
collection2 = db.chat_analytics

data = list(collection.find())
date=[]
name=[]
chat=[]
for x in data:
    tmp = list(x.values())
    date.append(tmp[1][0:10])
    name.append(tmp[2])
    chat.append(tmp[3])
    lst = [date,name,chat]
    dict = {'Date': date, 'Name': name, 'Chat': chat} 
    df = pd.DataFrame(dict)

#print(df)
df_set = pd.read_csv("company.csv")
df_list = df_set['SET_CODE'].values.tolist()
search_words = df_list
# search=""
for i in range(len(search_words)):
    search = search_words[i]
    print(search)
    df_new = df[df['Chat'].str.contains(search, na=False)]
    print(df_new['Chat'].shape[0])
    if(df_new['Chat'].shape[0] != 0):
        data = {
            'setName': search,
            'setAmount' : df_new['Chat'].shape[0]
        }
        collection2.insert_one(data)
