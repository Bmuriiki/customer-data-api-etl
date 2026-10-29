# Customer API Extraction and Transformation

## Project Overview

This project demonstrates an **ETL (Extract, Transform, Load) pipeline** built with Python. It extracts customer data from the JSONPlaceholder API, transforms nested JSON data into a flat tabular structure using Pandas, renames columns for clarity, and exports the cleaned data to a CSV file.

The project is designed to demonstrate fundamental data engineering concepts, including API integration, JSON normalization, data transformation, file handling, and pipeline orchestration.

## Objectives

- Retrieve customer data from a REST API.
- Handle HTTP responses and request errors.
- Convert JSON data into a Pandas DataFrame.
- Flatten nested JSON fields into individual columns.
- Rename columns to follow a consistent naming convention.
- Export transformed data to a CSV file.
- Organize the pipeline using reusable Python functions.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | Sending HTTP requests to the API |
| Pandas | Normalizing and transforming customer data |
| pathlib | Managing file and directory paths |
| JSON | Data interchange format returned by the API |
| CSV | Output format for the cleaned customer data |

## Data Source

The project uses the JSONPlaceholder API.

**API endpoint:** https://jsonplaceholder.typicode.com/users

The endpoint returns sample user records containing personal details, addresses, geographical coordinates, and company information.

The API is intended for testing and learning purposes. The records are sample data, not a production customer database.

## ETL Pipeline Architecture

The pipeline follows three main stages:

```text
JSONPlaceholder API
        |
        v
     EXTRACT
  Fetch customer data
        |
        v
    TRANSFORM
  Normalize JSON
  Rename columns
        |
        v
       LOAD
   Export to CSV
        |
        v
output/customer_clean.csv
```

### 1. Extract

The `extract()` function retrieves customer records from the API.

Key operations:

- `requests.get()` sends an HTTP GET request.
- `timeout=10` sets the request timeout to 10 seconds.
- `response.raise_for_status()` raises an exception for unsuccessful HTTP status codes.
- `response.json()` converts the JSON response into Python data structures.
- `pd.json_normalize()` flattens nested JSON into a tabular structure.

The function returns a Pandas DataFrame containing the extracted customer data.

### 2. Transform

The `transform(customers)` function renames columns to make them easier to understand and use in downstream analytics.

Examples of column transformations:

| Original column | Transformed column |
|---|---|
| `id` | `customer_id` |
| `address.street` | `address_street` |
| `address.city` | `address_city` |
| `address.geo.lat` | `address_geo_lat` |
| `address.geo.lng` | `address_geo_lng` |
| `company.name` | `company_name` |
| `company.catchPhrase` | `company_catchphrase` |
| `company.bs` | `company_bs` |

The function returns a transformed DataFrame.

### 3. Load

The `export_csv(df, path=OUTPUT_PATH)` function saves the transformed customer data to a CSV file.

The default output path is:

```text
output/customer_clean.csv
```

Key operations:

- `Path(path)` represents the output path using Python's `pathlib` module.
- `path.parent.mkdir(parents=True, exist_ok=True)` creates the output directory if it does not exist.
- `df.to_csv()` exports the DataFrame to CSV.
- `index=False` prevents Pandas from writing the DataFrame index as an additional column.
- `encoding="utf-8-sig"` supports compatibility with applications such as Microsoft Excel when reading UTF-8 text.

The function returns the output file path.

## Project Structure

```text
mini-api-customer-extraction/
├── extract_customers.py
├── README.md
└── output/
    └── customer_clean.csv
```

The `output/` directory is created automatically when the pipeline runs, if it does not already exist.



## Expected Output

When the API request succeeds, the terminal should display messages:

```text
Extracted 10 customers
Cleaned customer data successfully
Data successfully exported: output/customer_clean.csv
```

The pipeline creates the following file:

```text
output/customer_clean.csv
```

The CSV contains one row per user and columns for customer identifiers, names, contact details, addresses, geographical coordinates, and company information.
