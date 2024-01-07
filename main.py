import requests
from send_email import send_email

api="c414ec4eb6ff4517b78d751a39b3f4a7"
url= ("https://newsapi.org/v2/everything?q=tesla&from=2023-12-07&sortBy="
      "publishedAt&apiKey=c414ec4eb6ff4517b78d751a39b3f4a7")

# make request
request=requests.get(url)

# convert data from str to dictionary
content=request.json()

message=""
# access article titles and descriptions
for article in content["articles"]:
    if article["title"]:
        message=message+article["title"]+"\n"+article["description"]+2*"\n"

final_msg=f"""\
Subject: News
{message}
"""
final_msg=final_msg.encode("utf-8")
send_email(final_msg)
