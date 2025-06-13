from playwright.sync_api import sync_playwright

def save_login_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("🔐 Please log in manually in this window...")
        page.goto("https://offerup.com/login")
        page.wait_for_timeout(180000)  # 2 minutes for login

        context.storage_state(path="storage/session.json")
        print("✅ Session saved successfully!")
        browser.close()

if __name__ == "__main__":
    save_login_session()

