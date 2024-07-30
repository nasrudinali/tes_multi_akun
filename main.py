url = [



]

tapsemua = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/img[1]'
prize = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div[3]/img'
buybox = '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div[3]/div/span'
tap = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/img[2]'
home = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/img'
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
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import time
        import re
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.common.keys import Keys

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
        
        line = url[index]
        index += 1
        print("Akun", index)
        time.sleep(5)
        if index == len(url):
            index = 0
        
        driver.get(line)
        print("berhasil login")
        time.sleep(5)
        awal = driver.find_element(By.XPATH,home)
        awal.click()
        print("menu home")
        time.sleep(5)
        claim = driver.find_element(By.XPATH,tapsemua)
        claim.click()
        print("berhasil tap tap")
        time.sleep(5)
        hadiah = driver.find_element(By.XPATH,prize)
        hadiah.click()
        print("menu prize")
        time.sleep(5)
        maxpet = driver.find_element(By.XPATH,upmax)
        maxpet.click()
        print("berhasil up lv pet")
        time.sleep(5)
        buy = driver.find_element(By.XPATH,buybox)
        buy.click()
        print("berhasil buy box")
        time.sleep(5)
        detik = 5
        hitung_mundur(detik)
        driver.close()
    except:
        pass
