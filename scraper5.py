#Extract individual comments
import requests
from bs4 import BeautifulSoup

def main():
  url = "https://news.ycombinator.com/item?id=42919502"
  response = requests.get(url)

  soup = BeautifulSoup(response.content, "html.parser")

  elements = soup.find_all(class_="ind" , indent=0)

  comments = [e.find_next(class_="comment") for e in elements]


  #print(f"Comments: {len(comments)}")

  for comment in comments:
     print(comment)
if __name__ == "__main__":
  main()