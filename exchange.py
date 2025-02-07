import urllib.request
import json
import os
import time

EXCHANGE_FILE = "exchange_rate.json"
CACHE_DURATION = 24 * 60 * 60  # 24 hours in seconds

def get_exchange_rate(base_currency, target_currency):
    """Fetches the exchange rate and caches it if it's not fresh."""
    
    # Check if the cached file exists and is fresh
    if os.path.exists(EXCHANGE_FILE):
        with open(EXCHANGE_FILE, "r") as f:
            data = json.load(f)
            timestamp = data.get("timestamp")
            
            # Check if the cached data is less than 24 hours old
            if time.time() - timestamp < CACHE_DURATION:
                print("Using cached exchange rate.")
                return data["rate"]
    
    # If no valid cached data, fetch from the API
    api_key = "089354b9c5775a83b049b279"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        
        if "conversion_rates" in data:
            rate = data["conversion_rates"].get(target_currency)
            if rate:
                # Save the fresh data to a cache file
                with open(EXCHANGE_FILE, "w") as f:
                    json.dump({"rate": rate, "timestamp": time.time()}, f)
                print("Fetched new exchange rate.")
                return rate
            else:
                raise ValueError("Currency not found.")
        else:
            raise ValueError("Invalid response from API.")
    
    except urllib.error.HTTPError as e:
        raise ConnectionError(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        raise ConnectionError(f"URL Error: {e.reason}")
