from selenium import webdriver
import unittest
import mysql.connector as mycon
import datetime

#Establish connection with database

con = mycon.connect(
    host="localhost",
    user="root",
    passwd="Anish@123",
    database="users"
)
cursor = con.cursor()
cursor.execute("Select * from data")

data = cursor.fetchall()
try:sno=data[len(data)-1][0]+1
except:sno=1        


#Get current date

def get_day():
    a=datetime.datetime.now()
    day=a.day
    month=a.month
    year=a.year
    day=f"{str(year)}-{str(month)}-{str(day)}"
    return day

#Scrapping
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
        driver.implicitly_wait(50)

        driver.get("https://www.worldometers.info/coronavirus/")
        w = WebTable(driver.find_element_by_xpath('//table[@id="main_table_countries_today"]/tbody[1]'))

        country = w.column_data(2)
        n_coun = country.count('')
        for i in range(n_coun):
            country.remove('')

        total_cases = w.column_data(3)
        n_total_cases = total_cases.count('')
        for i in range(n_total_cases):
            total_cases.remove('')
            

        # Scrap the required details
        
        b=[]
        for k in ["India","World","USA","China","Italy"]:
            print(country,len(country))

            index_coun = country.index(k)

            cases = w.get_cell_data(index_coun, 3)
            print(cases)
            temp=cases.split(',')
            j=""
            for i in temp:
                j+=i
            cases=int(j)
            b.append(cases)

        #Insert into database

        print(f'insert into data values({sno},"{get_day()}",{b[0]},{b[1]},{b[2]},{b[3]},{b[4]});')
        cursor.execute(f'insert into data values({sno},"{get_day()}",{b[0]},{b[1]},{b[2]},{b[3]},{b[4]});')
        #con.commit()
        con.close()
        print("??")
        print("work successful")
        
        driver.close()


if __name__ == "__main__":
    unittest.main()

