from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv("SERPAPI_KEY")

# params = {
#     "engine": "google",              
#     "q": "best seo consultant",       
#     "location": "Chennai, Tamil Nadu, India",  
#     "google_domain": "google.co.in",  
#     "hl": "en",                        
#     "gl": "in",                        
#     "num": 10,                        # number of results to fetch
#     "api_key": API_KEY      
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# Extract ranking data
# if "organic_results" in results:
#     for idx, result in enumerate(results["organic_results"], start=1):
#         print(f"{idx}. {result['title']} → {result['link']}")

# target_domain = "jijojosephseo.in"

# rank = None
# for idx, result in enumerate(results.get("organic_results", []), start=1):
#     if target_domain in result.get("link", ""):
#         rank = idx
#         break

# if rank:
#     print(f"✅ '{target_domain}' ranks #{rank} for keyword '{params['q']}' in {params['location']}")
# else:
#     print(f"❌ '{target_domain}' not found in top {params['num']} results.")

keywords = [
    'Chennai airport assistance',
    'Beijing airport assistance',
    'Athens Airport Assistance',
    'Dulles airport assistance',
    'Geneva airport assistance'
]

locations = [
    "Chennai, Tamil Nadu, India",
    "Beijing, China",
    "Athens, Greece",
    "Dulles, Virginia, United States",
    "Geneva, Switzerland"
]

k_l_dict = dict(zip(keywords, locations))

target_domain = "jodogoairportassist.com"
results_data = []
n_of_posotion = 30

for keyword, location in k_l_dict.items():
    print(f"🔍 Checking '{keyword}' in {location}...")

    params = {
        "engine": "google",
        "q": keyword,
        "location": location,
        "google_domain": "google.com",
        "hl": "en",
        "num": n_of_posotion,
        "api_key": API_KEY
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()

        rank = None
        link_found = None

        for idx, result in enumerate(results.get("organic_results", []), start=1):
            link = result.get("link", "")
            if target_domain in link:
                rank = idx
                link_found = link
                break

        if rank:
            print(f"✅ Found {target_domain} ranked #{rank} in {location}")
        else:
            print(f"❌ Not ranked in top {n_of_posotion} for {keyword} ({location})")

        results_data.append({
            "Keyword": keyword,
            "Location": location,
            "Rank": rank if rank else f"Not in Top {n_of_posotion}",
            "Found URL": link_found if link_found else "N/A"
        })

        time.sleep(3)  # delay to avoid rate limits

    except Exception as e:
        print(f"⚠️ Error for '{keyword}' in {location}: {e}")
        results_data.append({
            "Keyword": keyword,
            "Location": location,
            "Rank": "Error",
            "Found URL": str(e)
        })

# print(results_data)