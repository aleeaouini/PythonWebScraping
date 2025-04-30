#Process the scraped content for useful data

import requests
from bs4 import BeautifulSoup

def main():
  url = "https://news.ycombinator.com/item?id=42919502"
  response = requests.get(url)

  soup = BeautifulSoup(response.content, "html.parser")
  elements = soup.find_all(class_="ind" , indent=0)
  comments = [e.find_next(class_="comment") for e in elements]

  keywords = {"python": 0, "javascript": 0, "typescript": 0, "go": 0, "c#": 0, "java": 0, "rust": 0 }

  for comment in comments:

    comment_text = comment.get_text().lower()

    words = comment_text.split(" ")
    words = [w.strip(".,/:;!@") for w in words]
    words = {w.strip(".,/:;!@") for w in words}
    print(words)
    for k in keywords:
       if k in words:
         keywords[k] += 1
         print(keywords)

    
    

if __name__ == "__main__":
  main()