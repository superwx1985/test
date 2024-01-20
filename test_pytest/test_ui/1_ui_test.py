import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUi:
    def setup_method(self) -> None:
        options = webdriver.ChromeOptions()
        options.binary_location = "E:/code/selenium driver/chrome-win64/chrome.exe"
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_open_url(self):
        self.driver.get("https://www.bilibili.com/")
        assert self.driver.find_element(by=By.CSS_SELECTOR, value="form#nav-searchform")

    @pytest.mark.debug
    def test_search(self):
        keyword = "selenium"
        self.driver.get("https://www.bilibili.com/")
        current_window_handle = self.driver.current_window_handle
        self.driver.find_element(By.CSS_SELECTOR, "form#nav-searchform input").send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, "#nav-searchform .nav-search-btn").click()
        for handle in self.driver.window_handles:
            if handle != current_window_handle:
                self.driver.switch_to.window(handle)
        assert keyword in self.driver.current_url


if __name__ == '__main__':
    # pytest.main([f'{__file__}::test_file_upload'])
    pytest.main([__file__, '-v', '-m debug'])
    pass

