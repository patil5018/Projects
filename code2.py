import requests
from bs4 import BeautifulSoup
import smtplib
import time
import mysql.connector
from datetime import date
from datetime import datetime

conn=mysql.connector.connect(user='root',passwd='root',host='localhost',database='Project')
mycursor=conn.cursor()
print("-------------------------------------------------------------------------------------------------")

print("\n       \t\tHELLO WELCOME TO ONLINE PRICE TRACKER:-")

print("-------------------------------------------------------------------------------------------------")

URL=input("\nEnter the link of the product to be monitered:-")

print("-------------------------------------------------------------------------------------------------")

ma=input("\nEnter the E_mail Address on which yo want to get notified:")

print("-------------------------------------------------------------------------------------------------")

pri=input("\nEnter the price to be compared:")

print("-------------------------------------------------------------------------------------------------")

dat=date.today()
pri=int(pri)

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup=BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    print("\n")
    print(title.strip())

    print("-------------------------------------------------------------------------------------------------")
    print("\n")
    price =soup.find(id="priceblock_ourprice").get_text()
    price2=price[2:6]
    converted_price = float(price[2:4])
    #print (converted_price)
    fullp=converted_price
    converted_price=converted_price*1000
    fullp=fullp*1000
	
    print(current_time)
	

    if(converted_price<pri):
        mycursor.execute("INSERT INTO Proj1(email,pri,date1,time1) VALUES(%s, %s, %s , %s)",(ma,fullp,dat,current_time))
        #print(fullp)
        conn.commit() 
        send_mail()
    

    print("-------------------------------------------------------------------------------------------------")
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('patil.pratik989098@gmail.com','ojuizjfxcadhgjrw')

    subject = 'Price fell down!!!'
    body = 'Check the amazon link: https://www.amazon.in/VivoBook-PCIEG-256GB-Windows-X509UA-EJ362T/dp/B07WNGR6MJ/ref=sr_1_1_sspa?keywords=asus+vivobook+x509&qid=1568964886&s=gateway&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFNMEdGTEhJM09WQ0ImZW5jcnlwdGVkSWQ9QTEwMTc4NzExNzhPUDZRMFc0MDUyJmVuY3J5cHRlZEFkSWQ9QTAxODAwMjExQlhFTDI5SVJaMlpCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('patil.pratik989098@gmail.com',ma,msg)
    print('Hey Email has been sent!!')
    server.quit()

while(True): 
	now =datetime.now()
	current_time = now.strftime("%H:%M:%S")
	check_price()
	time.sleep(60)




