import mysql.connector as mycon
import datetime
#Get current date

def get_day():
    a=datetime.datetime.now()
    day=a.day
    month=a.month
    year=a.year
    day=f"{str(year)}-{str(month)}-{str(day)}"
    return day

#file
def upload():
    try:
        with open("users.txt","r") as f:
            l=f.readlines()
        l.pop(0)
    
        name=l[0][5:-1]
        email=l[1][6:-1]
        country=l[2][8:-1]
        print(name,email,country)
    
        #connect
    
        con=mycon.connect(
            host="localhost",
            user="root",
            passwd="Anish@123",
            database="users"
            )


        if con.is_connected():
            print("Connected")
    
        cursor=con.cursor()
        cursor.execute("Select * from record")

        data=cursor.fetchall()

        try:sno=data[len(data)-1][0]+1
        except:sno=1
        print(f'insert into record values({sno}, "{name}" ,"{email}","{country}","{get_day()}");')
        cursor.execute(f'insert into record values({sno}, "{name}" ,"{email}","{country}","{get_day()}");')
        con.commit()
        con.close()
        print("Work Successful")

        with open("users.txt","w") as f:
            f.write("")
        
        
    except Exception as e:
        print(e)
        print("Nothing to update")

if __name__=="__main___":
    upload()

