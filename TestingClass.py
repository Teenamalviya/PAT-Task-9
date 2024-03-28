from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestingClass:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # automation starting method
    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True
        except:
            print("ERROR : URL is incorrect/Network Error")
            return False

    # automation shutdown method
    def shutdown(self):
        if self.booting_function():
            return self.driver.quit()
        else:
            return False

        # method to fetch the title of the web application

    def fetch_title(self):
        if self.booting_function() == True:
            return self.driver.title
        else:
            return False

        # method to fetch the URL of the web application

    def fetch_url(self):
        if self.booting_function():
            return self.driver.current_url
        else:
            return False

    # method to fetch the entire source-code
    def fetch_webpage(self):
        if self.booting_function():
            return self.driver.page_source
        else:
            return False
if __name__ == "__main__":
   tc= TestingClass("https://www.saucedemo.com/")
   tc.booting_function()
   print("Title of webpage:", tc.fetch_title())
   print("Url of the webpage:", tc.fetch_url())
   print("Content of the webpage:", tc.fetch_webpage())
   tc.shutdown()
