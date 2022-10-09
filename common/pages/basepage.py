from selenium.webdriver.common.by import By
from common.lib.javascript import JavaScript
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.lib.global_variables import Global_variables
from common.lib.web_element_utils import WebElementUtils
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    
    def __init__(self):
        
        self._driver = Global_variables.webdriver 
        self._utils = UtillityMethods(self._driver)
        self._core_utils = CoreUtillityMethods(self._driver)
        self._javascript = JavaScript(self._driver)
        self._webelement = WebElementUtils()
        self._ActionChains = ActionChains
        self._By = By