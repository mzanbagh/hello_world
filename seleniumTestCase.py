#pip instal html-testRunner
import unittest
from selenium import webdriver
import HtmlTestRunner  

class GOOGLE_SEARCH(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()
        print("TEST START")

    def test_search_1(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Drone FAA Rules")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Drone FAA Rules - Google Search")
    
    def test_search_2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("FAA Rules")
        self.driver.find_element_by_name("btnK").click()
        y = self.driver.title
        print(y)
        self.assertEqual(y, "FAA Rules - Google Search")
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("\nTEST END")

if __name__ == '__main__':
    unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report'))
