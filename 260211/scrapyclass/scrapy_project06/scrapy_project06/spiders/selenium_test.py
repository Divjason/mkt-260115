import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class SeleniumTestSpider(scrapy.Spider):
    name = "selenium_test"
    allowed_domains = ["selenium-testsite-250723.netlify.app"]
    start_urls = ["https://selenium-testsite-250723.netlify.app"]

    def __init__(self):
        headlessoptions = webdriver.ChromeOptions()
        headlessoptions.add_argument("--headless")
        service = Service("./scrapy_project06/drivers/chromedriver")
        self.driver = webdriver.Chrome(service=service, options=headlessoptions)

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(2)

        element = self.driver.find_element(By.CSS_SELECTOR, ".news")
        yield {"news": element.text}

    
    def closed(self, reason) :
        self.driver.quit()
