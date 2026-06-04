# smartphone-web-scraping-project
Final Capstone Project

# Smartphone Website Data Extraction Project

## Project Overview

This project is a Python web scraping project that extracts smartphone product information from the AnyCall Mobile Myanmar website and exports the collected data into an Excel file.

## Features

* Extract Product Name
* Extract Product Price
* Process data using Pandas
* Export results to Excel
* Error handling with try-except
* Reusable Python functions

## Project Structure

### create_page_urls()

Creates all website page URLs for scraping.

### extract_p_info_tags()

Extracts product information tags from each page.

### extract_p_name()

Extracts product names from product information tags.

### extract_p_price()

Extracts product prices and converts them into numeric values.

### main()

Controls the complete scraping process and exports the final dataset into Excel format.

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* Pandas
* tqdm
* OpenPyXL
* html5lib

## Output

The scraped data is exported into:

Final Data.xlsx

## Warning

This project was created for educational and learning purposes only.

Please respect the target website's Terms of Service, robots.txt rules, and copyright policies before performing large-scale or commercial web scraping.

The author is not responsible for any misuse of this code.

## Educational Purpose

This project was developed as a Final Capstone Project for the Python Essentials for Beginners Online Course and is intended to demonstrate Python programming, web scraping, data processing, and Excel export techniques.
