import pytest
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    'email, username, password',
    [("user.name@gmail.com", "username", "password")
     ]
)
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage,
                                 email: str, username: str, password: str):

    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email=email, username=username, password=password)
    registration_page.click_registration_button()

    dashboard_page.dashboard.check_visible()
