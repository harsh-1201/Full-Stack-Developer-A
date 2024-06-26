from scraper.realestate_scraper import scrape_realestate_properties, save_to_csv

def main():
    location = input("Enter location (e.g., Epping): ")

    properties = scrape_realestate_properties(location)

    if properties:
        filename = f"{location}_properties.csv"
        save_to_csv(properties, filename)
        print(f"Data saved to {filename}")
    else:
        print("No data to save")

if __name__ == "__main__":
    main()

