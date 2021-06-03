import asyncio
import json
import time
import xml.etree.ElementTree as ET
from pprint import pprint

import aiohttp
import requests
from bs4 import BeautifulSoup

start_time = time.time()


# ------- Get Dollar/rouble exchange rate____________#
r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
root = ET.fromstring(r.text)
dollar_to_rouble_rate = root[10][4].text
dollar_to_rouble_rate = float(dollar_to_rouble_rate.replace(",", "."))


# ----------- Get companies' names, growth, links from general table -----------------#

# Making requests to get hold of data - with async functionality
async def request_controller(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(request_worker(session, url)) for url in urls]
        results = await asyncio.gather(*tasks)
    return results


async def request_worker(session, url):
    async with session.get(url) as response:
        return await response.text()


urls = [
    f"https://markets.businessinsider.com/index/components/s&p_500?p={i}"
    for i in range(1, 11)
]

loop = asyncio.get_event_loop()
general_table_SP_500_pages = loop.run_until_complete(request_controller(urls))

# Processing data
companies_names = []
companies_links = []
companies_growth = []

for page in general_table_SP_500_pages:
    soup = BeautifulSoup(page, "html.parser")

    # Collecting names and links to personal pages
    a_title_href_tags = soup.select("tbody tr td a[title]")
    for tag in a_title_href_tags:
        company_name = tag["title"]
        companies_names.append(company_name)
        link = tag.get("href")
        companies_links.append("https://markets.businessinsider.com" + link)

    # Collecting percentage of companies' growth
    growth_data_tags = soup.select("tbody tr td span")[9::10]
    for tag in growth_data_tags:
        companies_growth.append(tag.getText())


# --------------- Get companies' codes, stock prices, P/E ratios, potential profits ------------ #

# Making requests to get hold of data - with async functionality
urls = companies_links

loop = asyncio.get_event_loop()
companies_personal_pages = loop.run_until_complete(request_controller(urls))

# Processing data
company_codes = []
stock_prices = []
p_e_ratios = []
possible_profits = []

for company_page in companies_personal_pages:
    soup = BeautifulSoup(company_page, "html.parser")

    # Getting company code
    company_code = soup.select_one("h1 span span").getText().replace(", ", "")
    company_codes.append(company_code)

    # Getting stock prices
    stock_price_in_dollars = float(
        soup.find(class_="price-section__current-value").getText().replace(",", "")
    )
    stock_price_in_roubles = stock_price_in_dollars * dollar_to_rouble_rate
    stock_prices.append(stock_price_in_roubles)

    # Getting P/E
    p_e_ratio_raw = soup.select(".snapshot .snapshot__data-item")[8].getText()
    p_e_ratio = float(p_e_ratio_raw.strip().split()[0].replace(",", ""))
    p_e_ratios.append(p_e_ratio)

    # Calculating potential profits
    week_low_52_raw = soup.select(".snapshot .snapshot__data-item")[6].getText()
    week_low_52 = float(week_low_52_raw.strip().split()[0].replace(",", ""))
    week_high_52_raw = soup.select(".snapshot .snapshot__data-item")[7].getText()
    week_high_52 = float(week_high_52_raw.strip().split()[0].replace(",", ""))

    possible_profit = (week_high_52 - week_low_52) / week_low_52
    possible_profit_percents = "{:.2%}".format(possible_profit)
    possible_profits.append(possible_profit_percents)

# Creating resulting list of dicts and resulting jsons
main_result_data = []
for index in range(len(companies_links)):
    company_dict = {
        "code": company_codes[index],
        "name": companies_names[index],
        "link": companies_links[index],
        "stock price": stock_prices[index],
        "P/E": p_e_ratios[index],
        "growth": companies_growth[index],
        "potential profit": possible_profits[index],
    }
    main_result_data.append(company_dict)


top_10_expensive_stocks = sorted(
    main_result_data, key=lambda k: k["stock price"], reverse=True
)[:10]
with open("top_10_expensive_stocks.txt", "w") as outfile:
    json.dump(top_10_expensive_stocks, outfile, indent=4)


top_10_lowest_p_e_ratio = sorted(main_result_data, key=lambda k: k["P/E"])[:10]
with open("top_10_lowest_p_e_ratio.txt", "w") as outfile:
    json.dump(top_10_lowest_p_e_ratio, outfile, indent=4)


top_10_highest_growth = sorted(
    main_result_data, key=lambda k: k["growth"], reverse=True
)[:10]
with open("top_10_highest_growth.txt", "w") as outfile:
    json.dump(top_10_highest_growth, outfile, indent=4)


top_10_highest_potential_profit = sorted(
    main_result_data, key=lambda k: k["potential profit"], reverse=True
)[:10]
with open("top_10_highest_potential_profit.txt", "w") as outfile:
    json.dump(top_10_highest_potential_profit, outfile, indent=4)


print(f"Process took {time.time() - start_time}")  # Around 70 seconds on my machine
# pprint(main_result_data)
