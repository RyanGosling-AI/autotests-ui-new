import pytest
import allure
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpics
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from allure_commons.types import Severity
from tools.routes import AppRoute
from config import settings


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTags.AUTHORIZATION, AllureTags.REGISTRATION)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @allure.title('User login with correct email and password')
    @allure.tag(AllureTags.USER_LOGIN)
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self,
            dashboard_page: DashboardPage,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button()

        dashboard_page.dashboard.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()

    @pytest.mark.parametrize(
        'email, password',
        [("user.name@gmail.com", "password"),
         ("user.name@gmail.com", '  '),
         ('  ', "password")
         ]
    )
    @allure.title('User login with wrong email or password')
    @allure.tag(AllureTags.USER_LOGIN)
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.login_form.fill(email=email, password=password)
        login_page.login_button.click()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.title('Navigation from login page to registration page')
    @allure.tag(AllureTags.NAVIGATION)
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email='', username='', password='')
