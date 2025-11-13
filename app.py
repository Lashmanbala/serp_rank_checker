from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")
params = {
    "engine": "google",                # use the Google engine
    "q": "best seo consultant",        # your keyword
    "location": "Chennai, Tamil Nadu, India",  # specific location
    "google_domain": "google.co.in",   # country-specific domain
    "hl": "en",                        # language
    "gl": "in",                        # country code
    "num": 10,                        # number of results to fetch
    "api_key": SERPAPI_KEY      # replace with your actual key
}

search = GoogleSearch(params)
results = search.get_dict()

# Extract ranking data
if "organic_results" in results:
    for idx, result in enumerate(results["organic_results"], start=1):
        print(f"{idx}. {result['title']} → {result['link']}")
