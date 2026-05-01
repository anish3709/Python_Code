from playwright.sync_api import Playwright,Page ,expect

def test_UiValDynamic_Script(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    expect(page.locator("#username")).to_be_visible()
    page.locator("#username").fill("rahulshettyacademy")
    page.locator("#password").fill("Learning@830$3mK2")
    print("Successfully Type ")

    page.locator('#terms').click()
    page.wait_for_timeout(4000)

    page.locator('[name="signin"]').click()