import requests
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Datos de votacion de votaciones.hcdn.gob.ar")
parser.add_argument("id", type=str, help="ID de la sesion")
args = parser.parse_args()

url = f"https://votaciones.hcdn.gob.ar/votacion/{args.id}"

# Fetch the webpage
response = requests.get(url)
if response.status_code != 200:
    print(f'Status code {response.status_code}: {response.text}')
    exit()

# Parse tables from the HTML
tables = pd.read_html(response.text)
print(f"Tables found: {len(tables)}")

# Save the first table to a CSV file
tables[0].to_csv(f"votacion_{args.id}.csv", index=False)
print(f"Guardada a votacion_{args.id}.csv")