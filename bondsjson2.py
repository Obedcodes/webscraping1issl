import requests
from bs4 import BeautifulSoup
import json

url = 'https://fmdqgroup.com/exchange/'

def fetch_table_data(soup, table_id, column_names):
    price_list_table = soup.find('table', id=table_id)

    if price_list_table:
        rows = price_list_table.find_all('tr')
        table_data = []

        for row in rows:
            columns = row.find_all('td')

            if columns:
                row_data = {}
                for index, column_name in enumerate(column_names):
                    row_data[column_name] = columns[index].get_text(strip=True) if index < len(columns) else None

                table_data.append(row_data)

        return table_data
    else:
        print(f"Price table {table_id} not found.")
        return []

# Request and parse each table
def process_table(url, table_id, column_names):
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return fetch_table_data(soup, table_id, column_names)
    else:
        print(f"Failed to retrieve the page status code: {response.status_code}")
        return []


columns_table_7 = ["DESCRIPTION", "PRICE", "CHANGE", "DATE", "OPEN_PRICE"]
columns_table_8 = ["MATURITY", "DISCOUNT", "YIELD", "CHANGE", "DATE"]
columns_table_9 = ["MATURITY", "DISCOUNT", "YIELD", "CHANGE", "DATE"]
columns_table_12 = ["CONTRACT_CODE", "MATURITY_DATE", "SETTLEMENT_PRICE", "DATE"]


data_table_7 = process_table(url, 'table_7', columns_table_7)
data_table_8 = process_table(url, 'table_8', columns_table_8)
data_table_9 = process_table(url, 'table_9', columns_table_9)
data_table_12 = process_table(url, 'table_12', columns_table_12)


all_data = {
    "table_7": data_table_7,
    "table_8": data_table_8,
    "table_9": data_table_9,
    "table_12": data_table_12
}


json_data = json.dumps(all_data, indent=4)
print(json_data)

# to save the json to a file
with open('data.json', 'w') as json_file:
    json.dump(all_data, json_file, indent=4)