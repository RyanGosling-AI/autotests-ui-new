import pytest


@pytest.mark.skip(reason="Фича в разработке")
def test_future_of_development():
    pass


@pytest.mark.skip(reason="Фича в разработке")
class TestSuiteSkip:
    def test_future_of_development_1(self):
        pass

    def test_future_of_development_2(self):
        pass