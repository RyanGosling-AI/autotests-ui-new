from elements.base_element import BaseElement
from playwright.sync_api import expect
import allure
from tools.playwright.logger import get_logger
from ui_coverage_tool import ActionType

logger = get_logger("TEXTAREA")


class Textarea(BaseElement):
    @property
    def type_off(self) -> str:
        return 'textarea'

    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        return f'{super().get_raw_locator(nth, **kwargs)}//textarea'

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Fill {self.type_off} "{self.name}" to value "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

        self.track_coverage(ActionType.FILL, nth, **kwargs)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_off} "{self.name}" has a value "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)

        self.track_coverage(ActionType.VALUE, nth, **kwargs)
