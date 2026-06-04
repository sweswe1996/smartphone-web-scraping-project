# smartphone-web-scraping-project
Final Capstone Project

## Project Overview

This project is a Python web scraping project that extracts smartphone product information from the AnyCall Mobile Myanmar website and exports the collected data into an Excel file.

## Features

* Extract Product Name
* Extract Product Price
* Process data using Pandas
* Export results to Excel
* Error handling with try-except
* Reusable Python functions

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* Pandas
* tqdm
* OpenPyXL
* html5lib

## Project Workflow

The program follows the steps below:

1. Connect to the smartphone product website.
2. Automatically generate all available page URLs.
3. Visit each webpage one by one.
4. Extract smartphone product names and prices.
5. Clean and convert the extracted data into a structured format.
6. Store all collected records in a Pandas DataFrame.
7. Combine data from all pages into a single dataset.
8. Export the final dataset into an Excel file named **Final Data.xlsx**.
9. Display progress and completion messages during execution.

## Data Flow

Website → Web Scraping → Data Cleaning → Pandas DataFrame → Excel Export

## Error Handling

The project uses try-except blocks to handle unexpected errors during data extraction and conversion. Missing or invalid values are replaced with default values to prevent the program from stopping unexpectedly.

## Warning

This project was created for educational and learning purposes only.

Please respect the target website's Terms of Service, robots.txt rules, and copyright policies before performing large-scale or commercial web scraping.

The author is not responsible for any misuse of this code.
