# Buff163 Bot

A python script that scrapes and monitors webpages on buff.163.com and allows users to automatically purchase items

## Installation

1. Clone the repository
```bash
git clone https://github.com/RamenMode/buff163scraper.git
```

2. Use the package manager [pip](https://pip.pypa.io/en/stable/)/pip3 to install selenium

```bash
pip3 install selenium
```
3. Install [ChromeDriver](https://chromedriver.chromium.org/downloads), making sure to follow the version requirements associated with your chrome browser listed on the website

## Usage

Make sure you are in the 'buffbot' directory

1. Obtain cookies for your buff163 session
```python
python3 getCookies.py
```
After the automated session loads, login to your Steam account on Buff and wait until browser automatically closes. *Do not share your cookies with anyone*.

2. Specify webpage item pages to scrape in the buff.json, modifying links as you wish. Ex: https://buff.163.com/goods/36436.

3. Run the script with parameters, first two being the range of scrapers included and the second being the maximum float acceptable. Below is an example, which uses the links of scraper1, scraper2, scraper3, and scraper4 in buff.json with a maximum float of 0.10
```python
python3 scrapeBuff.py 1 4 0.10
```
* Note that if any items fit the criteria you have listed, they _WILL_ be purchased by the script


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
