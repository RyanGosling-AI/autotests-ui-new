import allure


@allure.step('Opening browser')
def open_browser():
    ...


@allure.step('Creating course {title}')
def create_course(title: str):
    ...


@allure.step('Closing browser')
def close_browser():
    ...


def test_feature():
    open_browser()

    create_course(title='Test')
    create_course(title='Easy')
    create_course(title='Normal')
    create_course(title='Hard')

    close_browser()
