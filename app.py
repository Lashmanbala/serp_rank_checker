from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")
params = {
    "engine": "google",              
    "q": "best seo consultant",       
    "location": "Chennai, Tamil Nadu, India",  
    "google_domain": "google.co.in",  
    "hl": "en",                        
    "gl": "in",                        
    "num": 10,                        # number of results to fetch
    "api_key": SERPAPI_KEY      
}

search = GoogleSearch(params)
results = search.get_dict()

# Extract ranking data
# if "organic_results" in results:
#     for idx, result in enumerate(results["organic_results"], start=1):
#         print(f"{idx}. {result['title']} → {result['link']}")

target_domain = "jijojosephseo.in"

rank = None
for idx, result in enumerate(results.get("organic_results", []), start=1):
    if target_domain in result.get("link", ""):
        rank = idx
        break

if rank:
    print(f"✅ '{target_domain}' ranks #{rank} for keyword '{params['q']}' in {params['location']}")
else:
    print(f"❌ '{target_domain}' not found in top {params['num']} results.")
