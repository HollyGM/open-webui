from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:5174")
    page.click('button[aria-label="Select a model"]')
    page.click('button[aria-roledescription="model-item"]')
    page.fill('#chat-input', 'test')
    page.click('button[type="submit"]')
    page.click('#chat-context-menu-button')
    page.screenshot(path="jules-scratch/verification/verification.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
