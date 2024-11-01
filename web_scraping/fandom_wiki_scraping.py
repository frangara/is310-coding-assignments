import requests
from bs4 import BeautifulSoup
import csv

# Fetch the webpage
response = requests.get("https://the-bear.fandom.com/wiki/Season_1")
soup = BeautifulSoup(response.text, 'html.parser')
episodes = []

# Locate the table with the specific style attribute
table = soup.find('table', {
    'style': 'margin:0 0 0 0%; width:100%; border:1px solid #000000; border-radius:0px; border-spacing:0; clear:right; font-size:small; text-align:center; line-height: 30px;'
})

# Proceed if the table exists
if table:
    tbody = table.find('tbody')

    # Iterate through each row, skipping the header
    for row in tbody.find_all('tr')[1:]:
        columns = row.find_all('td')
        if len(columns) >= 5:
            # Extract title and writer
            title = columns[3].find('a').text.strip() if columns[3].find('a') else 'N/A'
            writer = columns[4].text.strip() if len(columns) > 4 else 'N/A'
            
            # Add the extracted data to the episodes list
            episodes.append([title, writer])

# Write the results to a CSV file
with open('the_bear_season_1_episodes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Writer'])  # Header
    writer.writerows(episodes)  # Data rows

print(f"Extracted {len(episodes)} episodes from Season 1 of The Bear.")
