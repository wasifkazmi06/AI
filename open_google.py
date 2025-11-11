from playwright.sync_api import sync_playwright
import time

"""Simple script to open Google with Playwright (headed) and close after a short pause.

Run:
    python -m playwright install
    python c:\\Users\\wasif.kazmi\\AI\\open_google.py
"""

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        try:
            title = page.title()
        except Exception:
            title = "(could not read title)"
        print("Opened page title:", title)
        # keep the browser visible for a short while so you can see it
        time.sleep(8)
        browser.close()


if __name__ == "__main__":
    main()
