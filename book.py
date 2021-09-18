from selenium import webdriver


class Book(webdriver.Chrome):
    def __init__(self, executable_path='/home/alxgav/chromedrive/chromedriver', teardown=False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/87.0.4280.66 Safari/537.36')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("window-size=1920,1080")
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_experimental_option("prefs", {
            "download.default_directory": "/home/alxgav/projects/download",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })
        super(Book, self).__init__(options=options, executable_path=executable_path)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def start_page(self):
        self.get('https://1lib.us/book/4507556/75cd52?dsource=mostpopular')
