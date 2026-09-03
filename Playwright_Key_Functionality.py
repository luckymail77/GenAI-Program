from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.screenshot(path="screenshot.png")
    browser.close()

#navigate to a different page
    page.goto("https://www.accuweather.com/en/in/chennai/206671/hourly-weather-forecast/206671")   
    page.screenshot(path="accuweather_screenshot.png")

#Click
page.click("text=Hourly")
page.screenshot(path="weather_screenshot.png")

#Typing
page.fill("input[name='q']", "Playwright Python")
page.press("input[name='q']", "Enter")
page.screenshot(path="search_screenshot.png")

#waiting for an element to appear
page.wait_for_selector("text=Playwright: Fast and reliable end-to-end testing for modern web apps")
print("Search results loaded successfully.")
page.screenshot(path="search_results_screenshot.png")

#Extracting data
title = page.title()
print(f"Page title: {title}")
browser.close()


