from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from colorama import init, Fore, Style
import random
init(autoreset=True)

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
session_path = "C:/selenium"
chrome_options.add_argument(f"user-data-dir={session_path}")
chrome_options.add_argument("--log-level=3")  # Set log level to suppress INFO and WARNING messages
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')

mobile_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
accept = "application/json, text/plain, */*"
accept_language = "en-US,en;q=0.9,id;q=0.8"
cache_control = "no-cache"
origin = "https://djdog.io"
pragma = "no-cache"
priority = "u=1, i"
sec_fetch_dest = "empty"
sec_fetch_mode = "cors"
sec_fetch_site = "same-site"

chrome_options.add_argument(f"accept={accept}")
chrome_options.add_argument(f"accept-language={accept_language}")
chrome_options.add_argument(f"cache-control={cache_control}")
chrome_options.add_argument(f"origin={origin}")
chrome_options.add_argument(f"pragma={pragma}")
chrome_options.add_argument(f"priority={priority}")
chrome_options.add_argument(f"sec-fetch-dest={sec_fetch_dest}")
chrome_options.add_argument(f"sec-fetch-mode={sec_fetch_mode}")
chrome_options.add_argument(f"sec-fetch-site={sec_fetch_site}")
chrome_options.add_argument(f"user-agent={mobile_user_agent}")

driver = webdriver.Chrome(options=chrome_options)

url = [
    
"https://djdog.io/home#tgWebAppData=query_id%3DAAGsWYpfAAAAAKxZil9Xfw6r%26user%3D%257B%2522id%2522%253A1602902444%252C%2522first_name%2522%253A%2522sarudkecil%2520%2524PINK%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522Sarudkecil03%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1723225741%26hash%3D0cd31fc12ccee2a3343daee539b119698a7244f780965e3bf84f7c64be09034d&tgWebAppVersion=7.6&tgWebAppPlatform=web&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23ffffff%22%2C%22button_color%22%3A%22%233390ec%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22hint_color%22%3A%22%23707579%22%2C%22link_color%22%3A%22%2300488f%22%2C%22secondary_bg_color%22%3A%22%23f4f4f5%22%2C%22text_color%22%3A%22%23000000%22%2C%22header_bg_color%22%3A%22%23ffffff%22%2C%22accent_text_color%22%3A%22%233390ec%22%2C%22section_bg_color%22%3A%22%23ffffff%22%2C%22section_header_text_color%22%3A%22%233390ec%22%2C%22subtitle_text_color%22%3A%22%23707579%22%2C%22destructive_text_color%22%3A%22%23df3f40%22%7D",
"https://djdog.io/home#tgWebAppData=query_id%3DAAEyjXYTAwAAADKNdhP_U0As%26user%3D%257B%2522id%2522%253A6768987442%252C%2522first_name%2522%253A%2522saroed9%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522saroed9%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1723229185%26hash%3D6aa40402da6a530f131b534c0554aee625f79d47561d5359cce47623b0b77190&tgWebAppVersion=7.6&tgWebAppPlatform=weba&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23ffffff%22%2C%22text_color%22%3A%22%23000000%22%2C%22hint_color%22%3A%22%23707579%22%2C%22link_color%22%3A%22%233390ec%22%2C%22button_color%22%3A%22%233390ec%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22secondary_bg_color%22%3A%22%23f4f4f5%22%2C%22header_bg_color%22%3A%22%23ffffff%22%2C%22accent_text_color%22%3A%22%233390ec%22%2C%22section_bg_color%22%3A%22%23ffffff%22%2C%22section_header_text_color%22%3A%22%23707579%22%2C%22subtitle_text_color%22%3A%22%23707579%22%2C%22destructive_text_color%22%3A%22%23e53935%22%7D",
"https://djdog.io/home#tgWebAppData=query_id%3DAAHMUG4YAwAAAMxQbhj0Lgrt%26user%3D%257B%2522id%2522%253A6852333772%252C%2522first_name%2522%253A%2522saroed1%2520tele1%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522saroed1%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1723235003%26hash%3D8e3064a73fe21ea1dece2e9dfe309d37223201306f92d45c3d1b7b7c9a044a6c&tgWebAppVersion=7.8&tgWebAppPlatform=tdesktop&tgWebAppThemeParams=%7B%22accent_text_color%22%3A%22%236ab2f2%22%2C%22bg_color%22%3A%22%2317212b%22%2C%22button_color%22%3A%22%235288c1%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22destructive_text_color%22%3A%22%23ec3942%22%2C%22header_bg_color%22%3A%22%2317212b%22%2C%22hint_color%22%3A%22%23708499%22%2C%22link_color%22%3A%22%236ab3f3%22%2C%22secondary_bg_color%22%3A%22%23232e3c%22%2C%22section_bg_color%22%3A%22%2317212b%22%2C%22section_header_text_color%22%3A%22%236ab3f3%22%2C%22section_separator_color%22%3A%22%23111921%22%2C%22subtitle_text_color%22%3A%22%23708499%22%2C%22text_color%22%3A%22%23f5f5f5%22%7D",
"https://djdog.io/home#tgWebAppData=query_id%3DAAEycd0TAwAAADJx3ROvPYVM%26user%3D%257B%2522id%2522%253A6775730482%252C%2522first_name%2522%253A%2522saroed2%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522saroed2%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1723235172%26hash%3De2ac0e903165dd055816499794d22e919dce5ff7678988c2e60f6334550fdf81&tgWebAppVersion=7.8&tgWebAppPlatform=tdesktop&tgWebAppThemeParams=%7B%22accent_text_color%22%3A%22%236ab2f2%22%2C%22bg_color%22%3A%22%2317212b%22%2C%22button_color%22%3A%22%235288c1%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22destructive_text_color%22%3A%22%23ec3942%22%2C%22header_bg_color%22%3A%22%2317212b%22%2C%22hint_color%22%3A%22%23708499%22%2C%22link_color%22%3A%22%236ab3f3%22%2C%22secondary_bg_color%22%3A%22%23232e3c%22%2C%22section_bg_color%22%3A%22%2317212b%22%2C%22section_header_text_color%22%3A%22%236ab3f3%22%2C%22section_separator_color%22%3A%22%23111921%22%2C%22subtitle_text_color%22%3A%22%23708499%22%2C%22text_color%22%3A%22%23f5f5f5%22%7D",
"https://djdog.io/home#tgWebAppData=query_id%3DAAHdMqAGAwAAAN0yoAZEq5Ss%26user%3D%257B%2522id%2522%253A6553613021%252C%2522first_name%2522%253A%2522saroed3%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522saroed3%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1723235247%26hash%3D5fb30ef2c3fc6f9938581db72623f42de248e02158c4b6a4959701a5f86b6896&tgWebAppVersion=7.8&tgWebAppPlatform=tdesktop&tgWebAppThemeParams=%7B%22accent_text_color%22%3A%22%236ab2f2%22%2C%22bg_color%22%3A%22%2317212b%22%2C%22button_color%22%3A%22%235288c1%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22destructive_text_color%22%3A%22%23ec3942%22%2C%22header_bg_color%22%3A%22%2317212b%22%2C%22hint_color%22%3A%22%23708499%22%2C%22link_color%22%3A%22%236ab3f3%22%2C%22secondary_bg_color%22%3A%22%23232e3c%22%2C%22section_bg_color%22%3A%22%2317212b%22%2C%22section_header_text_color%22%3A%22%236ab3f3%22%2C%22section_separator_color%22%3A%22%23111921%22%2C%22subtitle_text_color%22%3A%22%23708499%22%2C%22text_color%22%3A%22%23f5f5f5%22%7D",

]

tapsemua = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/img[1]'
prize = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[4]/img'
buybox = '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div[3]'
tap = '/html/body/div[1]/div/div/div[1]/div/div/div/div/div[2]/div[1]'
game = '/html/body/div[1]/div/div[3]/div[2]/div[3]/img'
upmax = '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div[4]'
       
def hitung_mundur(detik):
    while detik:
        mins, secs = divmod(detik, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        detik -= 1
    
    print("Waktu telah habis!") 
    
index = 0    

while True:
    try:
        line = url[index]
        index += 1
        
        driver.get(line)
        print("Akun", index)
        time.sleep(1)
        print("berhasil login")
        time.sleep(1)
        awal = driver.find_element(By.XPATH,game)
        awal.click()
        print("menu game")
        time.sleep(2)
        
        claim = driver.find_element(By.XPATH,tap)
        for i in range(1200):
            claim.click()
            time.sleep(0.000000001)
            available_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
            random_color = random.choice(available_colors)
            print(f"{random_color+Style.BRIGHT}berhasil tap tap", end="\r")
        
        time.sleep(1)
        hadiah = driver.find_element(By.XPATH,prize)
        hadiah.click()
        print("menu prize")
        time.sleep(5)
        
        level = '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div'
        lvakun = driver.find_element(By.XPATH,level)
        lv = int(lvakun.text.replace('Lv: ', ''))
        
        hargapet = '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div[3]/div/div[2]/div/div'
        pet = driver.find_element(By.XPATH,hargapet)
        hrg = int(pet.text.replace(',', ''))
        
        duit = '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div'
        cuan = driver.find_element(By.XPATH,duit)
        money = int(cuan.text.replace(',', ''))
        
        box = '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div/div'
        totalbox = driver.find_element(By.XPATH,box)
        ttl = int(totalbox.text)
        
        maxpet = driver.find_element(By.XPATH,upmax)
        if lv < 50:
            print("Level Akun :",lv)
            time.sleep(1)
            print("Jumlah Box :",ttl)
            time.sleep(1)
            print("Jumlah koin :",money)
            time.sleep(1)
            if money > hrg:
                maxpet.click()
                print("berhasil up lv pet")
                time.sleep(1)
            else:
                print("Koin kurang untuk up lv pet")
                time.sleep(1)
            
        buy = driver.find_element(By.XPATH,buybox)
        if lv > 49:
            print("Level Akun :",lv)
            time.sleep(1)
            print("Jumlah Box :",ttl)
            time.sleep(1)
            print("Jumlah koin :",money)
            time.sleep(1)
            if ttl < 101:
                if money > 100000:
                    buy.click()
                    print("berhasil buy box")
                    time.sleep(1)
                else:
                    print("Koin kurang untuk buy Box")
                    time.sleep(1)
            else:
                print("Box sudah cukup banyak bosku")
                time.sleep(1)
        
        detik = 3600
        if index == len(url):
            hitung_mundur(detik)
            index = 0

    except:
        pass
