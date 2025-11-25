# Voter Data Scraper

A Python script to scrape voter data by ward and registration center for **Sankhuwasabha District**.

## Features
- Scrapes voter data from the election website.
- Uses dynamic registration center IDs from `reg_center_mapping.py`.
- Exports data as CSV files organized by municipality and ward.
- Configurable through `config.py`.

## Requirements
- Python 3.x
- Packages listed in `requirements.txt` (`requests`, `beautifulsoup4`, `lxml`)

## How It Works
- The scraper requires payload data for `state`, `district`, `vdc_mun`, `ward`, and `reg_center`.
- You need to manually find this data by visiting [Voter List DB](https://election.gov.np/np/page/voter-list-db) and checking each ward.
- **Automation of finding payload data is not implemented**; it must be done manually.

## Notes
- The project is strictly designed for Sankhuwasabha district.
- There was no `robots.txt` file on the election.gov.np website, and the legality of scraping is unknown. Use responsibly.

## Project Structure
