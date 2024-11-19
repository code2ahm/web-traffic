from playwright.sync_api import sync_playwright

GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'

url = 'https://github.com/code2ahm' # replace with required url

visits = 0
successful_visits = 0


def visit_website(playwright):
    global visits, successful_visits
    try:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(url, wait_until='load', timeout=15000)
        print(f"{GREEN}Visited {YELLOW}{url}")

        successful_visits += 1
        visits += 1

        page.reload(wait_until='load', timeout=15000)
        print(f"{GREEN}Reloaded {YELLOW}{url}")

        successful_visits += 1
        visits += 1

        browser.close()

    except Exception as e:
        print(f"{RED}Failed to visit {YELLOW}{url} - {RED}{str(e)}")
        visits += 1


def simulate_traffic():
    global visits, successful_visits
    with sync_playwright() as playwright:
        while True:
            visit_website(playwright)


if __name__ == '__main__':
    try:
        simulate_traffic()
    except KeyboardInterrupt:
        print(f"\n{GREEN}Successfully Sent {RED}{successful_visits} Requests")
        print(f"{GREEN}Total Attempts: {RED}{visits}")
