form playwright.sync_api import sync_playwright
from date and time import datetime

print("Starting Playwright automation script...")
print(f"Current date and time: {datetime.now()}")

#Daily Weather Report BOT
#Chromium --> Weather Site --> Extract Report --> Screenshot --> Final text file
with sync_playwright() as p:
    print("Launching browser...")
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    print("Navigating to AccuWeather...")
    page.goto("https://www.accuweather.com/en/in/chennai/206671/hourly-weather-forecast/206671")
    
    print("Taking screenshot of the weather page...")
    page.screenshot(path="accuweather_screenshot.png")
    
    print("Extracting weather report...")
    weather_report = page.inner_text("div.hourly-card")
    print(f"Weather Report: {weather_report}")
    
    print("Saving weather report to text file...")
    with open("weather_report.txt", "w") as file:
        file.write(weather_report)
    
    print("Closing browser...")
    browser.close()

