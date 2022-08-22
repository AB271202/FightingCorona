from selenium import webdriver
import unittest
from app1 import Functions
import mysql.connector as mycon
import UpdatingSQL as sql

sql.upload()
print("-"*10)

#Establish connection with database

con = mycon.connect(
    host="localhost",
    user="root",
    passwd="Anish@123",
    database="users"
)
cursor = con.cursor()
cursor.execute("Select * from record")

data = cursor.fetchall()
n = len(data)
countries= []
for i in range(n):
    countries.append(data[i][3])


class WebTable:
    def __init__(self, webtable):
        self.table = webtable

    def column_data(self, column_number):
        col = self.table.find_elements_by_xpath("//tbody[1]/tr/td[" + str(column_number) + "]")
        rData = []
        for webElement in col:
            rData.append(webElement.text)
        return rData

    def row_data(self, row_number):
        if (row_number <= 0):
            raise Exception("Row number starts from 1")

        row_number = row_number + 1
        row = self.table.find_elements_by_xpath("//tbody[1]/tr[" + str(row_number) + "]/td")
        rData = []
        for webElement in row:
            rData.append(webElement.text)

        return rData

    def get_cell_data(self, rowNumber, column_number):
        rowNumber = rowNumber + 1
        cellData = self.table.find_element_by_xpath(
            "//tbody[1]/tr[" + str(rowNumber) + "]/td[" + str(column_number) + "]").text
        return cellData


class Test(unittest.TestCase):
    def test_web_table(self):
        driver = webdriver.Chrome(executable_path=r".\chromedriver.exe")
        print("ran driver")
        driver.get("https://www.worldometers.info/coronavirus/")
        driver.implicitly_wait(100)
        print("waited 1")
        w = WebTable(driver.find_element_by_xpath('//table[@id="main_table_countries_today"]/tbody[1]'))
        print("table")
        driver.implicitly_wait(1000)
        print("waited")
        country = w.column_data(2)
        print("country")
        n_coun = country.count('')
        for i in range(n_coun):
            country.remove('')

        total_cases = w.column_data(3)
        n_total_cases = total_cases.count('')
        for i in range(n_total_cases):
            total_cases.remove('')

        total_deaths = w.column_data(5)
        n_total_deaths = total_deaths.count('')
        for i in range(n_total_deaths):
            total_deaths.remove('')

        total_recover = w.column_data(7)
        n_total_recover = total_recover.count('')
        for i in range(n_total_recover):
            total_recover.remove('')

        total_active = w.column_data(8)
        n_total_active = total_active.count('')
        for i in range(n_total_active):
            total_active.remove('')

        for k in countries:
            print(len(country))
            index_coun = country.index(k)

            # Variables:

            cases = w.get_cell_data(index_coun, 3)
            deaths = w.get_cell_data(index_coun, 5)
            recovered = w.get_cell_data(index_coun, 7)
            active = w.get_cell_data(index_coun, 8)

            msg = f'''Subject: Coronavirus\n\n Hello {data[countries.index(k)][1]}! Here is today's status.\n
            >>Country Name: {k}\n
            >>Total Cases: {cases}\n
            >>Total Deaths: {deaths}\n
            >>Total Recovered: {recovered}\n
            >>Active Cases: {active}\n\n\n
            >>Today's tip\n{Functions.getTip()}\n
            \n\n\n
            Want to opt out of this newsletter? Mail 'STOP' to us
            \n
            Want to change your country? Mail 'CHANGE COUNTRY TO ---' to us
            '''
            print(msg)

            Functions.mail(data[countries.index(k)][2], msg)

        driver.close()


if __name__ == "__main__":
    unittest.main()
