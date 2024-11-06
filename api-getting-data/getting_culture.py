import requests
import json
import os
import apikey
from pyeuropeana.apis import search

# Set up Europeana API key
def setup_europeana():
    try:
        europeana_api_key = apikey.load("EUROPEANA_API_KEY")
    except:
        europeana_api_key = input("Please enter your Europeana API key: ")
        apikey.save("EUROPEANA_API_KEY", europeana_api_key)
    
    os.environ['EUROPEANA_API_KEY'] = europeana_api_key

# Function to get random coffee image from Coffee API
def get_coffee_image():
    """Get a random coffee image from the Coffee API"""
    url = "https://coffee.alexflipnote.dev/random.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("\nCoffee API Response:")
        coffee_data = response.json()
        coffee_image = {
            "file": coffee_data["file"]
        }
        print(json.dumps(coffee_image, indent=2))
        return coffee_image
    else:
        print(f"Error accessing Coffee API: {response.status_code}")
        return None

# Function to search Europeana for related content
def search_europeana(query):
    """Search Europeana for items related to the query"""
    try:
        response = search(query=query)
        
        # Remove API key from response for security
        if 'apikey' in response:
            del response['apikey']
        
        print("\nEuropeana Response:")
        
        # Extract just the relevant items data
        if 'items' in response:
            items = []
            for item in response['items']:
                cleaned_item = {
                    'title': item.get('title', ['Unknown'])[0],
                    'creator': item.get('dcCreator', ['Unknown'])[0] if 'dcCreator' in item else 'Unknown',
                    'year': item.get('year', ['Unknown'])[0] if 'year' in item else 'Unknown',
                    'type': item.get('type', 'Unknown'),
                    'country': item.get('country', ['Unknown'])[0] if 'country' in item else 'Unknown'
                }
                items.append(cleaned_item)
            print(json.dumps(items, indent=2))
            return items
        return []
    except Exception as e:
        print(f"Error accessing Europeana: {e}")
        return []

# Function to save combined data to JSON
def save_to_json(coffee_data, europeana_items, filename):
    """Save the combined data to a JSON file"""
    combined_data = {
        'coffee_image': coffee_data,
        'europeana_items': europeana_items
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=2, ensure_ascii=False)

def cleanup_api_key():
    """Remove the API key after use"""
    try:
        if 'EUROPEANA_API_KEY' in os.environ:
            del os.environ['EUROPEANA_API_KEY']
        print("\nAPI key has been deleted from the environment successfully")
    except Exception as e:
        print(f"\nError deleting API key: {e}")

def main():
    try:
        # Setup Europeana API
        setup_europeana()
        
        # Get Coffee image data
        coffee_data = get_coffee_image()
        
        if coffee_data:
            # Search Europeana for related content about coffee
            europeana_items = search_europeana("coffee")
            
            if europeana_items:
                # Save the combined data
                save_to_json(coffee_data, europeana_items, 'coffee_europeana_data.json')
                print("\nData has been saved to coffee_europeana_data.json")
    
    finally:
        # Always cleanup the API key, even if an error occurs
        cleanup_api_key()

if __name__ == "__main__":
    main()
