from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")


    def print_request_sent(request):
        print("Request sent: " + request.url)


    def print_request_finished(request):
        print("Request finished: " + request.url)

    page.on("request", print_request_sent)

    page.on('response', print_request_finished)

    page.wait_for_timeout(5000)