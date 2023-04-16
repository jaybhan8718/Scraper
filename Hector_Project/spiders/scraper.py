import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from scrapy.utils.response import open_in_browser
from scrapy.http import HtmlResponse
from Hector_Project.items import HectorProjectItem
class ScraperSpider(scrapy.Spider):
    name = "scraper"
    start_urls = ["https://apps5.mineco.gob.pe/transparencia/Navegador/default.aspx"]
    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=20)

    def parse(self, response):
        item = HectorProjectItem()
        driver = response.meta['driver']
        driver.switch_to.default_content()
        driver.switch_to.frame("frame0")
        step_1 = driver.find_element(By.XPATH,"//input[@id='ctl00_CPH1_BtnTipoGobierno']")
        step_1.click()
        driver.implicitly_wait(5)
        step_2 = driver.find_element(By.XPATH,"//td[@id='ctl00_CPH1_RptData_ctl03_TD0']/input")
        step_2.click()
        step_3 = driver.find_element(By.XPATH,"//input[@id='ctl00_CPH1_BtnSector']")
        step_3.click()
        driver.implicitly_wait(5)
        step_4 = driver.find_element(By.XPATH, "//td[@id='ctl00_CPH1_RptData_ctl02_TD0']/input")
        step_4.click()
        step_5 = driver.find_element(By.XPATH, "//input[@id='ctl00_CPH1_BtnPliego']")
        step_5.click()
        rows = driver.find_elements(By.XPATH, "//table[@class='Data']/tbody/tr")
        page_source = driver.page_source

        # Create a new HtmlResponse object from the source code
        response = HtmlResponse(url=driver.current_url, body=page_source, encoding='utf-8')

        rows = response.xpath("//table[@class='Data']/tbody/tr")
        for row in rows:
            title = row.xpath("td[2]/text()").get()
            percentage = row.xpath("td[10]/text()").get()
            title = row.xpath("td[2]/text()").get().split(": ")[1:]
            title = ''.join(title).strip().replace('\n', '')
            percentage = float(percentage.strip().replace('\n', '').replace('\xa0', ''))
            item['Title'] = title
            item['Percentage'] = percentage
            yield item
        
