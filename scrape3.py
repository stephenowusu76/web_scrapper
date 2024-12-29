from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Use headless=True to avoid opening a visible browser.
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        extra_http_headers={"Upgrade-Insecure-Requests": "1"},
        ignore_https_errors=True  # Bypass HTTPS errors
    )
    page = context.new_page()
    
    # Set a timeout in case it takes too long
    page.set_default_timeout(60000)  # 60 seconds timeout
    
    # Navigate to the site
    page.goto("https://www.freshdirect.com", wait_until="load")

    # Extract content
    print(page.title())
    html_content = page.content()
    with open("myfile3_1.html", "w") as f:
        f.write(html_content)

    browser.close()
