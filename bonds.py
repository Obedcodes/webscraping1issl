import requests
from bs4 import BeautifulSoup
import json


url = 'https://fmdqgroup.com/exchange/'

response7 = requests.get(url)
print(response7)

if response7.status_code == 200:

    soup = BeautifulSoup(response7.content, 'html.parser')

    def table7():
        # print(soup)
        price_list_table = soup.find('table', id='table_7')

        print(price_list_table)
        if price_list_table:

            rows = price_list_table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')

                if columns:
                    security = columns[0].get_text(strip=True)
                    issued_shares = columns[1].get_text(strip=True)
                    wk_high_52 = columns[2].get_text(strip=True)
                    wk_low_52 = columns[3].get_text(strip=True)
                    open_price = columns[4].get_text(strip=True)
                    '''close_price = columns[5].get_text(strip=True)'''
                    '''change = columns[6].get_text(strip=True)'''

                    print(f"DESCRIPTION: {security} || PRICE: {issued_shares} || "
                          f"CHANGE: {wk_high_52} || DATE: {wk_low_52} || "
                          f"DATE: {open_price}")
                else:
                    pass
        else:
            print("Price table not found.")
    table7()

else:
    print(f"Failed to retrieve the page status code: {response7.status_code}")


response8 = requests.get(url)
print(response8)

if response8.status_code == 200:

    soup = BeautifulSoup(response8.content, 'html.parser')


    def table8():
        price_list_table3 = soup.find('table', id='table_8')
        print(price_list_table3)

        if price_list_table3:

            rows = price_list_table3.find_all('tr')
            for row in rows:
                columns = row.find_all('td')

                if columns:
                    security = columns[0].get_text(strip=True)
                    issued_shares = columns[1].get_text(strip=True)
                    wk_high_52 = columns[2].get_text(strip=True)
                    wk_low_52 = columns[3].get_text(strip=True)
                    open_price = columns[4].get_text(strip=True)
                    """close_price = columns[5].get_text(strip=True)"""
                    """change = columns[6].get_text(strip=True)"""

                    print(f"MATURITY: {security} // DISCOUNT: {issued_shares} // "
                          f"YIELD: {wk_high_52} // CHANGE: {wk_low_52} // "
                          f"DATE: {open_price}")
                else:
                    pass
        else:
            print("Price table not found.")


    table8()

else:
    print(f"Failed to retrieve the page status code: {response8.status_code}")


response9 = requests.get(url)
print(response9)

if response9.status_code == 200:

    soup = BeautifulSoup(response9.content, 'html.parser')


    def table9():
        price_list_table3 = soup.find('table', id='table_9')
        print(price_list_table3)

        if price_list_table3:

            rows = price_list_table3.find_all('tr')
            for row in rows:
                columns = row.find_all('td')

                if columns:
                    security = columns[0].get_text(strip=True)
                    issued_shares = columns[1].get_text(strip=True)
                    wk_high_52 = columns[2].get_text(strip=True)
                    wk_low_52 = columns[3].get_text(strip=True)
                    open_price = columns[4].get_text(strip=True)
                    """close_price = columns[5].get_text(strip=True)"""
                    """change = columns[6].get_text(strip=True)"""

                    print(f"MATURITY: {security} ** DISCOUNT: {issued_shares} ** "
                          f"YIELD: {wk_high_52} ** CHANGE: {wk_low_52} ** "
                          f"DATE: {open_price}")
                else:
                    pass
        else:
            print("Price table not found.")


    table9()

else:
    print(f"Failed to retrieve the page status code: {response9.status_code}")


response12 = requests.get(url)
print(response12)

if response12.status_code == 200:

    soup = BeautifulSoup(response12.content, 'html.parser')


    def table12():
        price_list_table3 = soup.find('table', id='table_12')
        print(price_list_table3)

        if price_list_table3:

            rows = price_list_table3.find_all('tr')
            for row in rows:
                columns = row.find_all('td')

                if columns:
                    security = columns[0].get_text(strip=True)
                    issued_shares = columns[1].get_text(strip=True)
                    wk_high_52 = columns[2].get_text(strip=True)
                    wk_low_52 = columns[3].get_text(strip=True)
                    """open_price = columns[4].get_text(strip=True)"""
                    """close_price = columns[5].get_text(strip=True)"""
                    """change = columns[6].get_text(strip=True)"""

                    print(f"CONTRACT CODE: {security} // MATURITY DATE: {issued_shares} // "
                          f"SETTLEMENT PRICE: {wk_high_52} // DATE: {wk_low_52}")
                else:
                    pass
        else:
            print("Price table not found.")


    table12()

else:
    print(f"Failed to retrieve the page status code: {response12.status_code}")


