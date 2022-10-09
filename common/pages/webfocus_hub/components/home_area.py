from common.pages.basepage import BasePage
from common.lib.webfocus import ibx_custom_controls
from common.locators.webfocus_hub.components import home_area as Locators

class HomeArea(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.HomeArea
        self._name = "HomeArea "
        
    def select_view(self, view_name):
        """
        Description: select view based view name
        :Usage - select_view("Favorites")
        """
        self._webelement.select_object_based_on_name(self._locators.views_menus, view_name)
    
    def verify_available_view(self, expected_views, step_num, assert_type='equal'):
        """
        Description: verify available view
        :Usage - verify_available_view([])
        """
        self._webelement.verify_elements_text(self._locators.views_menus, expected_views, step_num, self._name + "Views Menus", assert_type)
        
    def wait_for_text(self, text, time_out=60):
        self._webelement.wait_for_element_text(self._locators.views, text, time_out)
        