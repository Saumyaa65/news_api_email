import requests
from send_email import send_email
import os

topic="cars"
api=os.getenv("API")
url= (f"https://newsapi.org/v2/everything?q={topic}&sortBy="
      f"publishedAt&apiKey={api}&language=en")

# make request
request=requests.get(url)

# convert data from str to dictionary
content=request.json()

message=""
# access article titles and descriptions
for article in content["articles"][:20]:
    if article["title"] and article["description"]:
        message=(message+article["title"]+"\n"+article["description"]
                 +"\n" + article["url"] +2*"\n")

final_msg=f"""\
Subject: News Today
{message}
"""
final_msg=final_msg.encode("utf-8")
send_email(final_msg)
