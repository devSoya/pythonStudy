from requests import get 

websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com",
  "https://httpstat.us/502",
  "https://httpstat.us/404",
  "https://httpstat.us/300",
  "https://httpstat.us/200",
)

results = {}

for website in websites:
  # print("website is equals to", website)
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  # print(response)
  # print(response.status_code)

  if response.status_code >= 200 and response.status_code < 300:
    # print(f"{website} is OK")
    results[website] = "OK"
  elif response.status_code >= 300 and response.status_code < 400:
    results[website] = "REDIRECT"  
  elif response.status_code >= 400 and response.status_code < 500:
    results[website] = "ERROR"  
  else:
    # print(f"{website} not OK")
    results[website] = "FAILED"

print(results)