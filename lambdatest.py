import unittest
import os
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key
class FirstSampleTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.browser_version = "114.0"
        options.platform_name = "Windows 11"
        lt_options = {};
        lt_options["project"] = "SmartUI-CI-Coupa2-viewport";
        lt_options["w3c"] = True;
        lt_options["plugin"] = "python-python";
        lt_options["smartUI.project"] = "Layout_Shift_Test11-CI-Coupa2"
        lt_options["console"] = True
        lt_options["network"] = True
        lt_options["build"] = "Python CI-SmartUI-Coupa2"
        lt_options["name"] = "Python-CI-SmartUI-Coupa2"
        lt_options["selenium_version"] = "4.0.0"
        options.set_capability('LT:Options', lt_options);
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                "jeeveshiitj", "mtPSfImA94UZNUj92fOctXE1VrKR4uDAoYrVU1kKJlqzclR6xU"),
            options=options
        )
    def tearDown(self):
        self.driver.quit()
    def test_demo_site(self):
        try:
            driver = self.driver
            driver.implicitly_wait(10)
            driver.set_page_load_timeout(30)
            print('Loading URL')
            driver.get("https://www.coupa.com/partners/partner-connect-program")
            driver.execute_script('smartui.takeScreenshot="Screen 1"')
            print("1st screenshot")
            driver.implicitly_wait(10)
            driver.execute_script('smartui.takeScreenshot="Screen 2"')
            #FullPage
            print("2nd screenshot")
            driver.execute_script("lambda-status=passed")
            element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/button[2]")
            element.click()
        except:
            driver.execute_script("lambda-status=failed")
            print("Failed")
            
if __name__ == "__main__":
    threads = []
    for _ in range(5): # specify the number of threads you want to spawn
        thread = threading.Thread(target=unittest.main)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
