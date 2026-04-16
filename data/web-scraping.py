import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_global_firepower_raw():
    # Base page (ranking + country list)
    base_url = "https://www.globalfirepower.com/countries-listing.php"

    other_sources = {
        "https://www.globalfirepower.com/total-population-by-country.php": "total_population",
        "https://www.globalfirepower.com/active-military-manpower.php": "active_personnel",
        "https://www.globalfirepower.com/aircraft-total.php": "total_military_aircraft",
        "https://www.globalfirepower.com/armor-tanks-total.php": "tanks",
        "https://www.globalfirepower.com/defense-spending-budget.php": "defense_budget_usd",
    }

    # -------- STEP 1: Scrape base country list --------
    response = requests.get(base_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "lxml")

    containers = soup.find_all(
        "div", class_="picTrans recordsetContainer boxShadow zoom"
    )

    countries = []
    ranks = []

    for item in containers:
        try:
            rank = item.find(
                "span", class_="textWhite textLarge textBold"
            ).text.strip()

            country = item.find(
                "span", class_="textWhite textLarge textShadow"
            ).text.strip()

            ranks.append(rank)
            countries.append(country)
        except AttributeError:
            continue

    df_main = pd.DataFrame({
        "rank": ranks,
        "country": countries
    })

    # -------- STEP 2: Scrape metric pages --------
    for url, col_name in other_sources.items():
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "lxml")

        containers = soup.find_all(
            "div", class_="picTrans recordsetContainer boxShadow zoom"
        )

        temp_countries = []
        values = []

        for item in containers:
            try:
                country = item.find(
                    "span", class_="textWhite textLarge textShadow"
                ).text.strip()

                value = item.find_all(
                    "span", class_="textWhite textLarge"
                )[-1].text.strip()

                temp_countries.append(country)
                values.append(value)
            except AttributeError:
                continue

        df_metric = pd.DataFrame({
            "country": temp_countries,
            col_name: values
        })

        df_main = df_main.merge(df_metric, on="country", how="left")

    return df_main