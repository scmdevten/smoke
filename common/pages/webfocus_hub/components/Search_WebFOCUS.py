import keyboard
from common.lib import html_controls
from common.pages.basepage import BasePage
from common.pages.webfocus_hub.dialog import Dialog
from common.lib.webfocus import ibx_custom_controls
from selenium.common.exceptions import NoSuchElementException
from common.locators.webfocus_hub.components.Search_WebFOCUS import SearchWebfocus as Locators
from selenium.webdriver.common.by import By 

class SearchWebfocus(BasePage):
    
    def __init__(self):
        super().__init__()
        

                
    @property
    def AllItems(self): return _AllItems()
    
    @property
    def Content(self): return _Content() 
    
    @property
    def Data(self): return _Data()  
    
    @property
    def SearchTextBox(self):
        search_text_box = self._utils.validate_and_get_webdriver_object_using_locator(Locators.search_text_box, 'Search Text Box')
        return html_controls.TextBox(search_text_box,' Search Text Box') 
    
    def click_help(self):
        Search_help = self._utils.validate_and_get_webdriver_object_using_locator(Locators.search_help, "Get Search Help")        
        self._core_utils.python_left_click(Search_help)
    
    
class _AllItems(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.AllItems
        self._name = "All items "
    
    
    @property
    def AllItemButton(self):
        """Return Allitem button class object to perform actions"""
        all_items_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_items_button, "All Items")
        return html_controls.Button(all_items_button, "All items")
    
    @property
    def Clear(self):
        """Return Allitem button class object to perform actions"""
        clear_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.clear_button, "All Items")
        return html_controls.Button(clear_button, "Clear")    
    
    @property
    def Search(self):
        """Return Allitem button class object to perform actions"""
        Search_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.search_button, "All Items")
        return html_controls.Button(Search_button, "Search")    
            
    @property 
    def SearchBy(self): return _SearchBy()
    
    @property 
    def Type(self): return _Type()    
    
    @property 
    def ContentIn(self): return _ContentIn()
    
    @property 
    def DataIn(self): return _DataIn()
    

    
       
    
class _SearchBy(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.AllItems.Searchby
        
        self._name = "Search By "
        
    @property
    def Dropdown(self): return ibx_custom_controls.ibxSelectItemList()
        
    def Click(self):
        
        all_categories = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.search_by, self._name)
        self._core_utils.python_left_click(all_categories)
        
    def verify_selected_option(self, expected_option, step_num):
        """
        Description: Function will verify selected option in the sort by dropdown
        :Usage- verify_selected_option("Title", "02")
        """
        sort_by_input = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.search_by_input, self._name + " Input")
        actual_option = sort_by_input.get_attribute("aria-label")
        msg = "Step {0}: Verify Selected Option".format(step_num)
        self._utils.asequal(expected_option, actual_option, msg)
        
    def click_dropdown_icon(self):
        """
        Description : Left click on drop down button
        """
        drop_down = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.search_by_dropdown, "Search By drop down")
        self._core_utils.left_click(drop_down)

        
class _Type(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.AllItems.Type
        self._name = "Type "
        
    @property
    def Dropdown(self): return ibx_custom_controls.ibxSelectItemList()
        
    def Click(self):
        
        all_types = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.type, self._name)
        self._core_utils.python_left_click(all_types)
        
    def verify_selected_option(self, expected_option, step_num):
        """
        Description: Function will verify selected option in the sort by dropdown
        :Usage- verify_selected_option("Title", "02")
        """
        sort_by_input = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.type_input, self._name + " Input")
        actual_option = sort_by_input.get_attribute("aria-label")
        msg = "Step {0}: Verify Selected Option".format(step_num)
        self._utils.asequal(expected_option, actual_option, msg)
        
    def click_dropdown_icon(self):
        """
        Description : Left click on drop down button
        """
        drop_down = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.type_dropdown, "Type drop down")
        self._core_utils.left_click(drop_down)
        
        
class _ContentIn(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.AllItems.ContentIn
        self._name = "Content in "
        
    @property
    def Dropdown(self): return ibx_custom_controls.ibxSelectItemList()
        
    def Click(self):
        
        all_workspaces = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_workspaces, self._name)
        self._core_utils.python_left_click(all_workspaces)
        
    def verify_selected_option(self, expected_option, step_num):
        """
        Description: Function will verify selected option in the sort by dropdown
        :Usage- verify_selected_option("Title", "02")
        """
        sort_by_input = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_workspaces_input, self._name + " Input")
        actual_option = sort_by_input.get_attribute("aria-label")
        msg = "Step {0}: Verify Selected Option".format(step_num)
        self._utils.asequal(expected_option, actual_option, msg)
        

        
    def click_dropdown_icon(self):
        """
        Description : Left click on drop down button
        """
        drop_down = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_workspaces_dropdown, "all workspace  drop down")
        self._core_utils.left_click(drop_down) 
        
    def verify_disabled_servers(self, step_num):
        """
        Description: Verify whether element is disabled by using 'opacity' and 'pointer-events' value.
        """
        icon_css = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_reporting_servers,self._name + " workspace dropdown")
        opacity = icon_css.value_of_css_property('opacity')
        pointer_events = icon_css.value_of_css_property('pointer-events')
        status = all([opacity=='0.5', pointer_events=='none'])
        msg = "Step {0} : Verify dropdown is disabled.".format(step_num)
        self._utils.asequal(True, status, msg)
        
    def verify_disabled_directories(self, step_num):
        """
        Description: Verify whether element is disabled by using 'opacity' and 'pointer-events' value.
        """
        icon_css = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_directories,self._name + " workspace dropdown")
        opacity = icon_css.value_of_css_property('opacity')
        pointer_events = icon_css.value_of_css_property('pointer-events')
        status = all([opacity=='0.5', pointer_events=='none'])
        msg = "Step {0} : Verify dropdown is disabled.".format(step_num)
        self._utils.asequal(True, status, msg)
        
   
        
class _DataIn(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.AllItems.DataIn
        self._name = "Data in "
        
    @property
    def Dropdown(self): return ibx_custom_controls.ibxSelectItemList()
        
    def click_servers(self):
        
        all_reporting_servers = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_reporting_servers, self._name)
        self._core_utils.python_left_click(all_reporting_servers)
        
    def click_directories(self):
        
        all_directories = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_directories, self._name)
        self._core_utils.python_left_click(all_directories)
        
    def verify_selected_option_servers(self, expected_option, step_num):
        """
        Description: Function will verify selected option in the sort by dropdown
        :Usage- verify_selected_option("Title", "02")
        """
        sort_by_input = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_reporting_servers_input, self._name + " Input")
        actual_option = sort_by_input.get_attribute("aria-label")
        msg = "Step {0}: Verify Selected Option".format(step_num)
        self._utils.asequal(expected_option, actual_option, msg)
        

        
    def verify_selected_option_directories(self, expected_option, step_num):
        """
        Description: Function will verify selected option in the sort by dropdown
        :Usage- verify_selected_option("Title", "02")
        """
        sort_by_input = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_directories_input, self._name + " Input")
        actual_option = sort_by_input.get_attribute("aria-label")
        msg = "Step {0}: Verify Selected Option".format(step_num)
        self._utils.asequal(expected_option, actual_option, msg)
        

        
    def click_dropdown_icon_servers(self):
        """
        Description : Left click on drop down button
        """
        drop_down = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_reporting_servers_dropdown, "all reporting servers drop down")
        self._core_utils.left_click(drop_down) 

    def click_dropdown_icon_directories(self):
        """
        Description : Left click on drop down button
        """
        drop_down = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_directories_dropdown, "all directories drop down")
        self._core_utils.left_click(drop_down)
        
    def verify_disabled_all_workspaces(self, step_num):
        """
        Description: Verify whether element is disabled by using 'opacity' and 'pointer-events' value.
        """
        icon_css = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.all_workspaces,self._name + " workspace dropdown")
        opacity = icon_css.value_of_css_property('opacity')
        pointer_events = icon_css.value_of_css_property('pointer-events')
        status = all([opacity=='0.5', pointer_events=='none'])
        msg = "Step {0} : Verify dropdown is disabled.".format(step_num)
        self._utils.asequal(True, status, msg)
        
                
class _Content(_AllItems):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.Content
        self._name = "Content "
        
    @property
    def ContentButton(self):
        """Return Content button class object to perform actions"""
        content_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.content_Button, "Content ")
        return html_controls.Button(content_button, "Content")
    


class _Data(_AllItems):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.Data
        self._name = "Data " 
        
    @property
    def DataButton(self):
        """Return Data button class object to perform actions"""
        data_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.data_button, "All Items")
        return html_controls.Button(data_button, "Data") 
        

    

        
        