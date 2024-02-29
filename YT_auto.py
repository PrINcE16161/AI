from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)
d=Service(executable_path="C:\\Users\\gandh\\Downloads\\chromedriver-win64\\chromedriver.exe")


class music():
    def __init__(self):
        self.driver = webdriver.Chrome(options=options,service=d)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element("xpath",'//*[@id="dismissible"]')
        video.click()