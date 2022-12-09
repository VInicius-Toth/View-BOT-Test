from playwright.sync_api import sync_playwright
import os
import time

os.system("cls")

while True:
    with sync_playwright() as p:
        print("Calculando tempo")
        time.sleep(2)
        ans = 38313 + 1000
        os.system("cls")
        print("Tempo Calculado")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.youtube.com/")
        os.system("cls")
        print("Entrando no Youtube")
        page.wait_for_timeout(500)
        page.goto("https://www.youtube.com/results?search_query=BUGANDO+O+YOUTUBE")
        os.system("cls")
        print("Buscando playlist")
        page.wait_for_timeout(500)
        page.goto("https://www.youtube.com/results?search_query=BUGANDO+O+YOUTUBE&sp=EgIQAw%253D%253D")
        page.click('div[id="playlist-thumbnails"]')
        page.wait_for_timeout(500)
        page.goto("https://www.youtube.com/watch?v=BJtOEejdk58&list=PLhkXFPku0tyhYde9MyM3QWa-raUs-j_u3")
        os.system("cls")
        print("Entrando na Playlist")
        page.click('button[class="ytp-mute-button ytp-button"]')
        while ans >= 0 <= ans:
            os.system("cls")
            print("Assistindo a Playlist")
            print(ans, "segundos")
            time.sleep(1)
            ans -= 1