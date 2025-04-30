import requests

def main():
  url = "https://news.ycombinator.com/item?id=42919502"
  response = requests.get(url)
  print(f"Scraping: {url}")
  print(response)
  print(response.content)

if __name__ == "__main__":
  main()