import pandas as pd
import requests
from pathlib import Path


API_URL= "https://jsonplaceholder.typicode.com/users"
OUTPUT_PATH=Path("output")/"customer_clean.csv"


def extract():
    response=requests.get(API_URL, timeout=10)
    response.raise_for_status()
    raw_data= response.json()
    normalised_data= pd.json_normalize(raw_data)
    df=pd.DataFrame(normalised_data)
    return df


def transform(customers):
    columns={'id':'customer_id', 
             'name':'name', 
             'username':'username', 
             'email':'email', 
             'phone':'phone', 
             'website':'website', 
             'address.street': 'address_street',
             'address.suite':'address_suite', 
             'address.city':'address_city', 
             'address.zipcode':'address_zipcode', 
             'address.geo.lat':'address_geo_lat',
             'address.geo.lng': 'address_geo_lng', 
             'company.name':'company_name', 
             'company.catchPhrase':'company_catchphrase', 
             'company.bs':'company_bs'}
    df= customers.rename(columns=columns)
    return df


def export_csv(df, path=OUTPUT_PATH):
    path = Path(path)
    # Creating output folder
    path.parent.mkdir(parents=True, exist_ok=True)
    # Export DataFrame
    df.to_csv(path, index=False, encoding="utf-8-sig")
    return path


def main():
    extracted_data=extract()
    print(f"Extracted {len(extracted_data)} customers")
    transformed_data= transform(extracted_data)
    print("Cleaned customer data succefully")
    export_data= export_csv(transformed_data)
    print(f"Data succefully exported: {export_data}")


if __name__=="__main__":
    main()

