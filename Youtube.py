from playwright.sync_api import sync_playwright
import os
import time

while True:
    ans = 38313 + 1000
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.youtube.com/")
        page.wait_for_timeout(500)
        page.goto("https://www.youtube.com/results?search_query=BUGANDO+O+YOUTUBE")
        page.wait_for_timeout(500)
        page.goto("https://www.youtube.com/results?search_query=BUGANDO+O+YOUTUBE&sp=EgIQAw%253D%253D")
        page.click('div[id="playlist-thumbnails"]')
        time.sleep(1)
        page.goto("https://www.youtube.com/watch?v=BJtOEejdk58&list=PLhkXFPku0tyhYde9MyM3QWa-raUs-j_u3")
        page.click('button[class="ytp-mute-button ytp-button"]')
        
        print(ans)
        time.sleep(ans)