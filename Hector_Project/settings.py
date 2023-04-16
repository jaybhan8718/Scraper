from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = 'chromedriver.exe'
SELENIUM_DRIVER_ARGUMENTS=['--headless']

# LOG_FILE = "scrapy.log"

BOT_NAME = "Hector_Project"

SPIDER_MODULES = ["Hector_Project.spiders"]
NEWSPIDER_MODULE = "Hector_Project.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

SCRAPEOPS_API_KEY = '4b4a342a-e34e-4344-916e-7203d7af4fcd'
# SCRAPEOPS_PROXY_ENABLED = True
SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}
DOWNLOADER_MIDDLEWARES = {
   "Hector_Project.middlewares.HectorProjectDownloaderMiddleware": 543,
   'scrapy_selenium.SeleniumMiddleware': 800,
#    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

ITEM_PIPELINES = {
   "Hector_Project.pipelines.HectorProjectPipeline": 300,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
