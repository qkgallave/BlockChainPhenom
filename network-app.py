import requests

def get_ip_info():
 # Fetch data from the ipapi API
    try:
        response = requests.get("https://ipapi.co/json/")
        response.raise_for_status() # Ensure we handle any HTTP errors
        data = response.json()
        # Extract and display the IP information
        print("Public IP Information:")
        print(f"IPv4 Address: {data.get('ip', 'N/A')}")
        print(f"Country: {data.get('country_name', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"ISP: {data.get('org', 'N/A')}")
        print(f"ASN: {data.get('asn', 'N/A')}")
        print(f"Latitude: {data.get('latitude', 'N/A')}")
        print(f"Longitude: {data.get('longitude', 'N/A')}")
    except requests.RequestException as e:
        print("An error occurred while retrieving IP information:", e)
# Run the function
get_ip_info()