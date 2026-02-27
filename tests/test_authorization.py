from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):
    # контекстный менеджер(при выходе из него происходит автоматическое закрытие контекста)

    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # email_input = page.locator("//div[@data-testid= 'login-form-email-input']//input")
    # автоматически ищет среди data-testid
    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()

    # page.wait_for_timeout(5000)
