from common.pages.basepage import BasePage
from common.lib.webfocus import ibx_custom_controls
from common.locators.webfocus_hub.components import banner as Locators
from common.lib import html_controls

class Banner(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.Banner
        self._name = "Banner "
        
    @property
    def MainMenu(self): return _MainMenu()
    
    @property
    def PlusMenu(self): return _PlusMenu()
    
    @property
    def ToolOptions(self): return _ToolOptions()
        
    @property  
    def Tools(self):
        """
        Description : It returns tools icon object to perform actions
        """
        name = self._name + "Tools Icon"
        tools_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.tools, name)
        return ibx_custom_controls.Icon(tools_obj, self._locators.tools_icon, "\ea57", name)
    
    @property  
    def Help(self):
        """
        Description : It returns help icon object to perform actions
        """
        name = self._name + "Help Icon"
        help_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.help, name)
        return ibx_custom_controls.Icon(help_obj, self._locators.help_icon, "\ea54", name)
    
    @property  
    def UserMenu(self):
        """
        Description : It returns user menu icon object to perform actions
        """
        name = self._name + "User Menu Icon"
        user_menu_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.user_profile, name)
        return ibx_custom_controls.Icon(user_menu_obj, self._locators.user_profile_icon, "\e976", name)
    

class _MainMenu(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.Banner.MainMenu
        self._name = "Banner Main Menu "
    
    @property  
    def Button(self):
        """
        Description : It returns main menu button object to perform actions
        """
        name = self._name + "Main Menu Button"
        main_menu_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.main_menu, name)
        return ibx_custom_controls.Icon(main_menu_obj, self._locators.main_menu_icon, "\e997", name)
    
    def select_menu_option(self, option_name):
        """
        Description: Function will select menu options in main menu
        :Usage - select_menu_option("Portal")
        """
        self._webelement.select_object_based_on_name(self._locators.menu_options, option_name)
    
    def select_quick_access_option(self, option_name):
        """
        Description: Function will select quick access option in main menu
        :Usage - select_quick_access_option("InfoAssist")
        """
        self._webelement.select_object_based_on_name(self._locators.quick_access_options, option_name)
        
    def verify_menu_options(self, expected_options, step_num, assert_type='equal'):
        """
        Description: Function will verify menu option in main menu
        :Usage - verify_menu_options(['Home', 'Workspaces', 'Application Directories'], "01")
        """
        self._webelement.verify_elements_text(self._locators.menu_options, expected_options, step_num, self._name + " Options", assert_type)
        
    def verify_quick_access_options(self, expected_options, step_num, assert_type='equal'):
        """
        Description: Function will verify quick access in main menu
        :Usage - verify_quick_access_options(['Home', 'Workspaces', 'Application Directories'], "01")
        """
        self._webelement.verify_elements_text(self._locators.quick_access_options, expected_options, step_num, self._name + " Quick Access Options", assert_type)
        
    def click_on_close_button(self):
        
        close_button_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.close, self._name + " Close")
        self._core_utils.python_left_click(close_button_obj)
        
    def verify_main_menu_closed(self, step_num):
        """
        Description: Function will verify main menu is in closed state or not
        """
        try:
            main_menu_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.main_menu_shelf, self._name + " Main Menu Shelf")
            status = main_menu_obj.is_displayed()
        except AttributeError:
            status = False
        msg = "Step {0}: Verify main menu closed".format(step_num)
        self._utils.asequal(False, status, msg)
        
    def wait_for_text(self, text, time_out=60):
        """
        Description: Function will wait for text in main menu
        """
        self._webelement.wait_for_element_text(self._locators.main_menu_shelf, text, time_out)
        
    def wait_for_invisible(self, time_out=10):
        """
        Description: Wait until main menu shelf invisible 
        """
        self._webelement.wait_until_element_invisible(self._locators.main_menu_shelf, time_out)
        
        
class _PlusMenu(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.Banner.PlusButton
        self._name = "Banner Plus Button"
        
    @property  
    def Button(self):
        """
        Description : It returns plus Button object to perform actions
        """
        plus_icon_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.plus_button, self._name)
        return ibx_custom_controls.Icon(plus_icon_obj, self._locators.plus_icon, "\e98c", self._name)
    
    def wait_for_text(self, text, time_out=60):
        """
        Description: Function will wait for text in main menu
        """
        self._webelement.wait_for_element_text(self._locators.plus_button_menu, text, time_out)
        
    def wait_for_invisible(self, time_out=10):
        """
        Description: Wait until main menu shelf invisible 
        """
        self._webelement.wait_until_element_invisible(self._locators.plus_button_menu, time_out)
    
    def select_menu(self, item_name):
        """
        Description: selection item in plus menu options
        :Usage - select_item('Get Data')
        """
        self._webelement.select_object_based_on_name(self._locators.plus_menu_options, item_name)
        
    def verify_menus(self, expected_options, step_num, assert_type='equal'):
        """
        Description: selection item in plus menu options
        :Usage - select_item(['Get Data', 'Create Data Flow'])
        """
        self._webelement.verify_elements_text(self._locators.plus_menu_options, expected_options, step_num, self._name + " Items", assert_type)
        
class _ToolOptions(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.Banner
        self._name = "Banner Main Menu "
                
    def verify_text_session_log(self, expected_msg, step_num):
        """ 
        Description: To verify log message in session log
        """        
        actual_msg = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.session_log_text_verify, "Log Message").text.strip()
        msg = "Step {0} : Verify [{1}] displayed in ['{2}'] dialog".format(step_num, expected_msg,self._name)
        self._utils.asequal(expected_msg, actual_msg, msg)
        
    @property
    def Kill_selected_agents_button(self):
        """
        Description: To return a object for Manage my agents Kill selected agents button
        """
        obj= self._utils.validate_and_get_webdriver_object_using_locator(self._locators.kill_selected_agents_button, 'Kill Selected Agents Button' )
        return html_controls.Button(obj, 'Kill Selected Agents')
    
    @property
    def checkBox_manage_my_agent(self):
        """
        Description: To return a object for Manage my agents check box
        """
        name = self._name + "Check Box to select agents "
        tools_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.checkbox_manage_my_agents, name)
        return ibx_custom_controls.Icon(tools_obj, self._locators.checkbox_manage_my_agents_icon, " ", name)
    
    def verify_state(self, expected_status, step_num):
        """
        Description : To verify the status
        :Usage = verify_the_state('stopping', '02.01)
        """
        ele_obje = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.verify_state_manage_my_agent, "State of manage my agents")
        actual_status = ele_obje.text.strip()              
        msg = 'Step {0} : Verify [{1}] the state'.format(step_num, expected_status)
        self._utils.asequal(expected_status, actual_status, msg)
    
    @property    
    def tracing_level_dropdown(self):
        obj= self._utils.validate_and_get_webdriver_object_using_locator(self._locators.tracing_level, 'Tracing Level' )
        return html_controls.Button(obj, 'Tracing Level change')
    
    def Stop_request_message(self, expected_value , step_num):
        """
        Description : To verify the stop request message from stop request run dialog
        :Usage = Stop_request_message("Reporting Server Message , 01.01)
        """
        elem_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Stop_request_message, 'Stop message')
        actual_value = elem_obj.text.strip()
        msg = 'Step {0} :{1}  message appears on the screen '.format(step_num,expected_value )
        self._utils.asequal(expected_value,actual_value,msg)