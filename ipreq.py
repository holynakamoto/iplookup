import requests
from termcolor import colored

API_URL_TEMPLATE = "https://ipinfo.io/{}/json"

def fetch_ip_data(ip_address):
    response = requests.get(API_URL_TEMPLATE.format(ip_address))
    return response.json()

def format_ip_data(data):
    formatted_data = {
        "IP Address": colored(data.get("ip"), 'red'),
        "Hostname": colored(data.get("hostname"), 'green'),
        "City": colored(data.get("city"), 'yellow'),
        "Region": colored(data.get("region"), 'blue'),
        "Country": colored(data.get("country"), 'magenta'),
        "Location": colored(data.get("loc"), 'cyan'),
        "Service Provider": colored(data.get("org"), 'red'),
        "Postal Code": colored(data.get("postal"), 'green'),
        "Timezone": colored(data.get("timezone"), 'yellow'),
        "API Documentation": colored(data.get("readme"), 'blue')
    }
    return "\n".join(f"{key}: {value}" for key, value in formatted_data.items())

def get_ip_info(ip_address):
    try:
        data = fetch_ip_data(ip_address)
        text = format_ip_data(data)
        print(text)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    ip_address = input("Enter the IP address to geolocate and identify: ")
    get_ip_info(ip_address)
