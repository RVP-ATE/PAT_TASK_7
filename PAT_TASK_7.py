import requests


class CountryInfo:
    # Constructor that takes the URL of the API as input
    def __init__(self, url):
        self.url = url
        self.data = None

    # Method to fetch JSON data from the URL
    def fetch_data(self):
        try:
            response = requests.get(self.url, verify=False)
            if response.status_code == 200:
                self.data = response.json()
            else:
                print("Failed to fetch data.")
        except Exception as e:
            print(f"Error occurred: {e}")

    # Method to display the name of the countries, currencies, and currency symbols
    def display_country_info(self):
        if self.data:
            for country in self.data:
                name = country.get('name', {}).get('common', 'Unknown')
                currencies = country.get('currencies', {})
                for currency_code, currency_info in currencies.items():
                    currency_name = currency_info.get('name', 'Unknown')
                    currency_symbol = currency_info.get('symbol', 'Unknown')
                    print(f"Country: {name}, Currency: {currency_name}, Symbol: {currency_symbol}")
        else:
            print("No data available to display.")

    # Method to display all countries with Dollar as the currency
    def display_countries_with_dollar(self):
        if self.data:
            dollar_countries = []
            for country in self.data:
                currencies = country.get('currencies', {})
                for currency_code, currency_info in currencies.items():
                    if 'dollar' in currency_info.get('name', '').lower():
                        name = country.get('name', {}).get('common', 'Unknown')
                        dollar_countries.append(name)
            print("Countries with Dollar as currency:")
            for country in dollar_countries:
                print(country)
        else:
            print("No data available to filter.")

    # Method to display all countries with Euro as the currency
    def display_countries_with_euro(self):
        if self.data:
            euro_countries = []
            for country in self.data:
                currencies = country.get('currencies', {})
                for currency_code, currency_info in currencies.items():
                    if 'euro' in currency_info.get('name', '').lower():
                        name = country.get('name', {}).get('common', 'Unknown')
                        euro_countries.append(name)
            print("Countries with Euro as currency:")
            for country in euro_countries:
                print(country)
        else:
            print("No data available to filter.")


# Main execution
url = "https://restcountries.com/v3.1/all"
country_info = CountryInfo(url)

# Fetching data from the URL
country_info.fetch_data()

# Displaying the country info
country_info.display_country_info()

# Displaying countries with Dollar as currency
country_info.display_countries_with_dollar()

# Displaying countries with Euro as currency
country_info.display_countries_with_euro()