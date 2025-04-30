#Parse the HTTP response with “Beautifulsoup”
import requests
from bs4 import BeautifulSoup

def main():
  url = "https://news.ycombinator.com/item?id=42919502"
  response = requests.get(url)

  soup = BeautifulSoup(response.content, "html.parser")
  # find all elements with class="comment"
  elements = soup.find_all(class_="comment")

  # Show the number of elementd found
  print(f"Elements: {len(elements)}")

if __name__ == "__main__":
  main()