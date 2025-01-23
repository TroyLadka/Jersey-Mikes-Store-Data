# Jersey Mike's Store Location Scraper

## Overview
Python script to scrape store locations for all Jersey Mike's restaurants in the United States.

## Features
- Scrape store locations from all U.S. states
- Handle pagination for comprehensive data collection
- Save store details (title, address, city, state, ZIP)

## Prerequisites
- Python 3.7+
- Selenium WebDriver
- Pandas
- Microsoft Edge WebDriver

## Installation
1. Install dependencies
```bash
pip install selenium pandas
```

2. Download Microsoft Edge WebDriver
   - Ensure the WebDriver matches your Edge browser version
   - Update the WebDriver path in the script

## Usage
```bash
python mikes_store_data.py
```

## Output
- Generates `jersey_mikes_all_stores.csv`
- Contains comprehensive store location data

## Limitations
- Requires active internet connection
- Performance depends on website structure
- Potential for script breakage if website changes

## Legal Note
- Ensure compliance with Jersey Mike's terms of service
- Review website's robots.txt before scraping

## Contributing
Contributions welcome! Open an issue or submit a pull request.

## License
MIT License
