from common.pages.basepage import BasePage
from common.locators.webfocus_hub.components import application_directories_area as Locators
from common.lib.core_utility import CoreUtillityMethods
from common.lib import html_controls
from selenium.common.exceptions import NoSuchElementException
from common.lib.webfocus import ibx_custom_controls
    
    
class ApplicationDirectories(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.ApplicationDirectories
        self._name = "Application Directories "
        
    def switch_to_frame(self):
        """
        Description : Switch to iframe to work on Application Directories area
        """
        self._utils.synchronize_until_element_is_visible(self._locators.frame, expire_time=120)
        self._core_utils.switch_to_frame(self._locators.frame)
        self._webelement.wait_until_element_visible(self._locators.RibbonBar.parent, 80)
        self._utils.wait_for_page_loads(40, pause_time=2) 
        
    def switch_to_default_content(self):
        """
        Description : Switch to default content
        """
        self._core_utils.switch_to_default_content()
    
    @property
    def RibbonBar(self): return _RibbonBar()
    
    @property
    def Applications(self): return _Applications()
    
    @property
    def Application_Directory(self): return _Application_Directory()
    

    @property
    def SearchIndexOptions(self): return _SearchIndexOptions()
    
    
class _RibbonBar(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.ApplicationDirectories.RibbonBar
        self._name = "Application Directories Ribbon Bar"
        
    def verify_ribbon_bar_options(self, expected_options, step_num, assert_type="equal"):
        """
        Description: Function will verify ribbon bar menu options
        :Usage - verify_ribbon_bar_options(['Get Data', 'Filter'])
        """
        self._webelement.verify_elements_text(self._locators.menu_buttons, expected_options, step_num, self._name + " Menu Buttons", assert_type=assert_type)
    
    def wait_for_text(self, text, time_out=60):
        self._webelement.wait_for_element_text(self._locators.parent, text, time_out)            
    
    def select_menu(self, item_name):
        """
        Description: selection item in application directories ribbon bar
        :Usage - select_item('Get Data')
        """
        self._webelement.select_object_based_on_name(self._locators.menu_buttons, item_name)


class _Applications(BasePage):    
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.ApplicationDirectories
        self._name = "Application Directories Applications"
        
    def wait_for_text(self, text, time_out=60):
        self._webelement.wait_for_element_text(self._locators.parent, text, time_out) 
        
    def select_directory(self,directory_name):
        try:
            elems=self._utils.validate_and_get_webdriver_objects("div[data-ibx-type='ibxTreeNode']", directory_name)
            actual_column = elems[[el.text.strip() for el in elems].index(directory_name)]
            CoreUtillityMethods.python_left_click(self, actual_column)
        except NoSuchElementException:
            print("Application Directory is not Found.")
            
    def edit_directories(self,options):
        
        elems = self._utils.validate_and_get_webdriver_objects(self._locators.all_app_directory, options)
        template_object = elems[[el.text.strip() for el in elems].index(options)]
        self._javascript.scrollIntoView(template_object, wait_time=1)
        self._core_utils.python_right_click(template_object)
        
        
class _SearchIndexOptions(BasePage): 
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.ApplicationDirectories.SearchIndexOptions
        self._name = "Search Index Options" 
        
    @property
    def allAppPath(self):
        radiobutton = ibx_custom_controls.ibxRadioButtonSimple("Files from all application directories")
        return radiobutton 

    @property
    def Cancel(self):
        """Return Allitem button class object to perform actions"""
        Cancel_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.cancel, "Cancel")
        return html_controls.Button(Cancel_button, "Cancel") 
    
    @property
    def Save(self):
        """Return Allitem button class object to perform actions"""
        Save_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.save, "Save")
        return html_controls.Button(Save_button, "Save") 
            
            
class  _Application_Directory(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.ApplicationDirectories
        self._name = "Application Directories Applications"
        
        
    def SearchTextBox(self):        
        filter_text_box = self._utils.validate_and_get_webdriver_object_using_locator(Locators.ApplicationDirectories.Application_Directory.filter_text_box, 'Filter Text Box')
        return html_controls.TextBox(filter_text_box,' Filter Text Box')     

    def verify_files(self, expected_files, step_num, assert_type='asin'):
            """
            Description : Verify directory or files.
            :Usage : verify_files('sections', "01.02")
            """            
            file_object = self._utils.validate_and_get_webdriver_objects("div.wcx-grid-body-row-cell div[wcid*='item']", expected_files)            
            actual_files = [file.text.strip() for file in file_object if file.is_displayed()]           
            msg = "Step {0} : Verify files in application directory/files ".format(step_num)
            self._utils.verify_list_values(expected_files, actual_files, msg, assert_type)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    