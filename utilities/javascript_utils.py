class JavaScriptUtils:

    @staticmethod
    def click(driver, element):

        driver.execute_script(
            "arguments[0].click();",
            element
        )

    @staticmethod
    def scroll_to_element(driver, element):

        driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

    @staticmethod
    def scroll_to_top(driver):

        driver.execute_script(
            "window.scrollTo(0,0);"
        )

    @staticmethod
    def scroll_to_bottom(driver):

        driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);"
        )