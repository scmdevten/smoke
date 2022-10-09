from common.pages.basepage import BasePage
from common.lib.webfocus import ibx_custom_controls
from common.locators.webfocus_hub.components import left_side_navigation_bar as Locators


class LeftSideNavigationBar(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.LeftSideNavigationBar
        self._name = "Left side navigation bar "
        
    @property
    def Home(self): 
        """
        Description : It returns Home object to perform actions
        """
        name = self._name + "Home"
        home_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.home, name)
        return ibx_custom_controls.Icon(home_obj, self._locators.home_icon, "\ea55", name)
    
    @property
    def Workspaces(self): 
        """
        Description : It returns Workspaces object to perform actions
        """
        name = self._name + "Workspaces"
        workspaces_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.workspaces, name)
        return ibx_custom_controls.Icon(workspaces_obj, self._locators.workspaces_icon, "\ebe6", name)
    
    @property
    def ApplicationDirectories(self): 
        """
        Description : It returns Application Directories object to perform actions
        """
        name = self._name + "Application Directories"
        application_directories_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.application_directories, name)
        return ibx_custom_controls.Icon(application_directories_obj, self._locators.application_directories_icon, "\ebe7", name)
    
    @property
    def Portals(self): 
        """
        Description : It returns Portals object to perform actions
        """
        name = self._name + "Portals"
        portals_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.portals, name)
        return ibx_custom_controls.Icon(portals_obj, self._locators.portals_icon, "\e91c", name)
    
    @property
    def ManagementCenter(self): 
        """
        Description : It returns Management Center to perform actions
        """
        name = self._name + "Management Center"
        management_center_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.management_center, name)
        return ibx_custom_controls.Icon(management_center_obj, self._locators.management_center_icon, "\eaeb", name)
    
    @property
    def SearchWebFocus(self): 
        """
        Description : It returns Search Webfocus object to perform actions
        """
        name = self._name + "Search Webfocus"
        search_webfocus_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.search_webfocus, name)
        return ibx_custom_controls.Icon(search_webfocus_obj, self._locators.search_webfocus_icon, "\e900", name)
    