# NewsScraping
This Python script scrapes stock information headlines, research report titles, and announcements from the EastMoney stock forum. It retrieves the latest 31 news headlines or the top 10 research report titles/announcements for a specified stock code and saves them into text files (.txt) [Can easily change it to output .csv files] in designated folders.

## Environment Setup

- Python 3.x (Python 3.10 is recommended)
- Beautiful Soup 4 (bs4)
- Requests

## Installation

1. Install the required dependencies by running the following commands in your terminal:

   ```bash
   pip install beautifulsoup4
   pip install requests

## Usage

1. Place the stock codes you want to retrieve information for in a file named `stockInfo.xlsx`, ensuring that the first column contains the stock codes.
2. Execute the `main.py` script in your integrated development environment (IDE) or double-click it.
3. Follow the prompts to select the desired functionality, enter the quantity, and patiently wait for the program to execute.
4. The scraped information will be saved in folders named `news`, `papers`, or `announcements`, depending on the type of data retrieved.

## Additional Info
1. The prompts are in Chinese
