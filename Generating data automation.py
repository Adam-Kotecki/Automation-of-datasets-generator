from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5 import QtCore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Generating data automation")
        self.setFixedSize(400, 500)

        layout = QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        
        self.l1 = QLabel("Select category of data:")
        self.ch1 = QCheckBox("Name")
        self.ch2 = QCheckBox("Phone")
        self.ch3 = QCheckBox("Email")
        self.ch4 = QCheckBox("Country")
        self.btn1 = QPushButton("Generate")

        layout.addWidget(self.l1)
        layout.addWidget(self.ch1)
        layout.addWidget(self.ch2)
        layout.addWidget(self.ch3)
        layout.addWidget(self.ch4)
        layout.addStretch(1)
        layout.addWidget(self.btn1)
        self.setLayout(layout)
        self.btn1.clicked.connect(self.start_automation)

    def start_automation(self):
        service = Service(executable_path='./chromedriver')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        # options.add_argument('ignore-certificate-errors')

        chrome_browser = webdriver.Chrome(service=service, chrome_options=options)

        chrome_browser.maximize_window()
        chrome_browser.get('https://generatedata.com/')

        for ch in [self.ch1, self.ch2, self.ch3, self.ch4]:
            if ch.isChecked():
                checkbox_text = ch.text()
                print(type(checkbox_text))
                globals()[checkbox_text] = chrome_browser.find_element(By.XPATH, '//div[text()=' + "\"" + checkbox_text + "\"" + "]")
                globals()[checkbox_text].click()
        fr = chrome_browser.find_element(By.XPATH, '//div[text()="CSV"]')
        fr.click()
        g1 = chrome_browser.find_element(By.XPATH, '//button[text()="Generate"]')
        g1.click()
        #g2 = chrome_browser.find_element(By.XPATH, '//button[text()="Generate"]')
        #g2.click()
# name_btn = chrome_browser.find_element(By.XPATH, '//div[text()="Country"]')
#chrome_browser.close()

def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()













