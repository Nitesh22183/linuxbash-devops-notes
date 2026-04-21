import requests
url = "https://www.google.com"
try:
    response = requests.get(url, timeout=5)
    print ("Status Code:", response.status_code)
   
    if response.status_code == 200:
        print("Health check successful")
    else:
        print("Health check failed")
except requests.exceptions.RequestException as e:
    print("Request failed:", e)        
