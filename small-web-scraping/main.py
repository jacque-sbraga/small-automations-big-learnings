from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import xlsxwriter
import time


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

capture_text = lambda: browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]').text
find_input = lambda: browser.find_element(By.NAME, "q")

link_google = 'https://google.com'


excel_file = xlsxwriter.Workbook(f'{os.getcwd()}/file.xlsx')
sheet = excel_file.add_worksheet('Results')

# Style sheet header
header_format = excel_file.add_format({
    'bold': True,
    'font_size': 14,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#D7E4BC',  
    'border': 1  
})

# Style sheet data
data_format = excel_file.add_format({
    'font_size': 12,
    'valign': 'center',
    'border': 1
})

headers = ['Currency', 'Value']

currencies = []

browser.get(link_google)
browser.maximize_window()
input_search = find_input()

input_search.send_keys('dolar today')
input_search.send_keys(Keys.ENTER)
dolar = capture_text()
currencies.append({'name': 'Dolar to Real Brazillian', 'value': f'{dolar.split(' ')[0]}'})

input_search = find_input()
input_search.clear()
input_search.send_keys('euro today')
input_search.send_keys(Keys.ENTER)
euro = capture_text()
currencies.append({'name': 'Euro to Real Brazillian', 'value': f'{euro.split(' ')[0]}'})

for index, header in enumerate(headers):
    # row, col, header, style
    sheet.write(0, index, header, header_format)
    

for row_index, row_data in enumerate(currencies, start=1):
    for col_index, cell_data in enumerate(row_data.values()):
        sheet.write(row_index, col_index, cell_data, data_format)

print(currencies)
# simple: col, header, style
# sheet.write('B1', headers[1], header_format)

excel_file.close()

time.sleep(2)
