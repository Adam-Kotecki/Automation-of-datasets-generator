from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Generating data automation")
        self.setFixedSize(400, 500)

def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


'''
service = Service(executable_path='./chromedriver')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('ignore-certificate-errors')

chrome_browser = webdriver.Chrome(service=service, chrome_options=options)

chrome_browser.maximize_window()
chrome_browser.get('https://generatedata.com/')

name_btn = chrome_browser.find_element(By.XPATH, '//div[text()="Name"]')
name_btn.click()

name_btn = chrome_browser.find_element(By.XPATH, '//div[text()="Country"]')
name_btn.click()

#chrome_browser.close()
'''













