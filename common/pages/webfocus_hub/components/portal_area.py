from common.pages.basepage import BasePage
from common.lib.webfocus import ibx_custom_controls
from common.locators.webfocus_hub.components import portal_area as Locators

class Portals(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.Portals
        self._name = "Portals "
        
    def switch_to_frame(self):
        """
        Description : Switch to iframe to work on Portals area
        """
        self._utils.synchronize_until_element_is_visible(self._locators.frame, expire_time=120)
        self._core_utils.switch_to_frame(self._locators.frame)
        self._utils.wait_for_page_loads(40, pause_time=2) 
        
    def switch_to_default_content(self):
        """
        Description : Switch to default content
        """
        self._core_utils.switch_to_default_content()