import requests

api="c414ec4eb6ff4517b78d751a39b3f4a7"
url= ("https://newsapi.org/v2/everything?q=tesla&from=2023-12-07&sortBy="
      "publishedAt&apiKey=c414ec4eb6ff4517b78d751a39b3f4a7")

# make request
request=requests.get(url)

# convert data from str to dictionary
content=request.json()

# access article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

