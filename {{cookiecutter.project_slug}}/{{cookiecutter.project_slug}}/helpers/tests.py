from decouple import config
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class FunctionalTest:

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument('--headless')

        cls.driver = webdriver.Firefox(
            firefox_options=options,
            executable_path=config('GECKODRIVER_BIN_PATH')
        )

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
