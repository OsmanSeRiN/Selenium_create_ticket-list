from selenium import webdriver
from time import time,sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os


class ticket :
    def site_open (self):
       #Open the chrome
       driver = webdriver.Chrome(ChromeDriverManager().install())
       #Full window
       driver.maximize_window()
       #Link
       driver.get("https://www.google.com")
       #Warning
       print("Bu app obilet.com içim geliştirilmiştir")
       #input HTML element find
       city_1 = input("Kalkış noktası : ")
       city_2 = input("İniş noktası : ")
       #search obilet
       point = "Obilet " + city_1 + "den " + city_2
       txt_area = driver.find_element(By.ID,"APjFqb")
       txt_area.send_keys(point)
       btn_search = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")
       btn_search.click()
       #open the obilet
       obilet = driver.find_element(By.XPATH,"/html/body/div[6]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3")
       obilet.click()
       #number of ticked
       ticket_number = len(driver.find_elements(By.CLASS_NAME,"point-right"))
       print("Bilet sayısı : ",ticket_number)
      
       return ticket_number


ticket_amount= ticket().site_open()

class documant:
    def create_list(self):
       #Dosya oluşturma ve masa üstüne gönderme
       desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
       filename = os.path.join(desktop, 'Bilet adet listesi.txt')
       ticket().site_open()

       #Masa üstüne oluşturulan txt dosyasına yazı yazdırma
       with open(filename, 'w') as file:
         file.write(ticket_number)
      
       return documant_1

Create_documamt = documant().create_list()

input("Kapatmak için herhangi bir tuşa basıp sonrasında Enter a basın")




