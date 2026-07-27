import allure
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpics
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
import pytest
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTags.REGISTRATION, AllureTags.REGRESSION)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @pytest.mark.parametrize(
        'email, username, password',
        [("user.name@gmail.com", "username", "password")
         ]
    )
    @allure.title('User login with correct email, username and password')
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage,
                                     email: str, username: str, password: str):

        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email=email, username=username, password=password)
        registration_page.click_registration_button()

        dashboard_page.dashboard.check_visible()
