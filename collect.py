import os
import pandas as pd
from bs4 import BeautifulSoup
import re

def parse_html(file_path: str) -> dict:
    """Parse HTML file and extract title, price, and link"""
    with open(file_path) as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    title = soup.find("h2").get_text().strip()
    title = re.sub(r'[\n\t]', ' ', title)

    price = soup.find("span", class_="a-price-whole").get_text().strip()
    price = re.sub(r'[₹,]', '', price)
    price = float(price)

    link = soup.find("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal").get("href")
    link = "https://amazon.in/" + link

    return {"title": title, "price": price, "link": link}

def extract_data(data_dir: str) -> list:
    """Extract data from HTML files in the given directory"""
    data_list = []
    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        try:
            data_dict = parse_html(file_path)
            data_list.append(data_dict)
        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
        except AttributeError as e:
            print(f"Error: Attribute not found - {e}")
    return data_list

def save_to_csv(data_list: list, csv_file: str) -> None:
    """Save data to a CSV file"""
    df = pd.DataFrame(data_list)
    df["title"] = df["title"].apply(lambda x: x.replace('"', ''))
    df["price"] = df["price"].apply(lambda x: round(x, 2))
    df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    data_dir = "data"
    csv_file = "data.csv"
    data_list = extract_data(data_dir)
    save_to_csv(data_list, csv_file)