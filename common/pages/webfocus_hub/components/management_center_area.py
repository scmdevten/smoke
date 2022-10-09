from common.pages.basepage import BasePage
from common.lib.webfocus import ibx_custom_controls
from common.locators.webfocus_hub.components import management_center_area as Locators

class ManagementCenter(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.ManagementCenter
        self._name = "Management Center "
        
    def select_menu_options(self, view_name):
        """
        Description: select menu based menu name
        :Usage - select_menu_options("Security Center")
        """
        self._webelement.select_object_based_on_name(self._locators.left_side_menu_options, view_name)
    
    def verify_available_menu_options(self, expected_views, step_num, assert_type='equal'):
        """
        Description: verify available view
        :Usage - verify_available_view(["Adminstration console"])
        """
        self._webelement.verify_elements_text(self._locators.left_side_menu_options, expected_views, step_num, self._name + "Views Menus", assert_type)
        
    def wait_for_text(self, text, time_out=60):
        self._webelement.wait_for_element_text(self._locators.left_side_menu, text, time_out)
    
