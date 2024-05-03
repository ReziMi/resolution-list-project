import sqlite3

bucket_list = [
    "Visit the Tbilisi, Georgia",
    "Swim with dolphins",
    "Attend a music festival",
    "Go on a hot air balloon ride",
    "Learn to surf",
    "Hike to the top of a mountain",
    "Take a cooking class in Italy",
    "See the Northern Lights",
    "Volunteer at an animal shelter",
    "Learn to play a musical instrument",
    "Write and publish a short story",
    "Take a road trip along the coast",
    "Learn to scuba dive",
    "Go on a safari in Africa",
    "Visit a castle in Europe",
    "Attend a TED talk",
    "Run a half-marathon",
    "Learn to speak conversational Spanish",
    "Take a photography trip",
    "Go on a camping trip in the wilderness",
    "Learn to make sushi",
    "Attend a yoga retreat",
    "Go on a meditation retreat",
    "Learn to salsa dance",
    "Go on a wine tasting tour",
    "Attend a live theater performance",
    "Visit a famous museum",
    "Go zip-lining through a forest",
    "Attend a professional sports game",
    "Go on a cruise to a tropical island",
    "Learn to rock climb",
    "Take a pottery class",
    "Attend a film festival",
    "Go on a helicopter tour",
    "Go on a ghost tour in a historic city",
    "Visit a famous landmark",
    "Go on a bike tour through the countryside"
]

connection = sqlite3.connect("bucket_list.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS bucket_list (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT)")

for item in bucket_list:
    cursor.execute("INSERT INTO bucket_list (item) VALUES (?)", (item,))
    print(item)

connection.commit()
connection.close()
