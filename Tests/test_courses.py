from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration", wait_until='networkidle')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('username@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='Tests/browser-registration-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(storage_state='Tests/browser-registration-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses', wait_until='networkidle')

        title_element1 = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(title_element1).to_be_visible()
        expect(title_element1).to_have_text('Courses')

        icon_element = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_element).to_be_visible()

        title_element2 = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(title_element2).to_be_visible()
        expect(title_element2).to_have_text('There is no results')

        title_element3 = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(title_element3).to_be_visible()
        expect(title_element3).to_have_text('Results from the load test pipeline will be displayed here')

