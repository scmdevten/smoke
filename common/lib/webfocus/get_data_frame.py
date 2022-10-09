from common.locators.paris_home_page import GetDataFrame as Locators
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.lib.javascript import JavaScript
from selenium.webdriver.common.by import By
from common.lib.webfocus import ibx_custom_controls
import time
from common.lib import html_controls

class __Common__:
    
    def __init__(self, driver):
        
        self.driver = driver
        self._core_utils_ = CoreUtillityMethods(self.driver)
        self._utils_ = UtillityMethods(self.driver)
        self._javascript_ = JavaScript(self.driver)

class GetDataFrame(__Common__):
    
    def __init__(self, driver):
        
        super(GetDataFrame, self).__init__(driver)
        self.locators = Locators
    
    def switch_to_frame(self):
        """
        Description : Switch to iframe 
        """
        self._core_utils_.switch_to_frame(self.locators.frame[1])
        self._utils_.wait_for_page_loads(80, pause_time=2)
        
    def switch_to_default_content(self):
        """
        Description : Switch to default content
        """
        self._core_utils_.switch_to_default_content()
    
    def verify_title(self, expected_title, step_num):
        """
        Description : Verify whether displayed or not by header title
        :Usage - verify_title('GetData', "05.01")
        """
        actual_title = self._utils_.validate_and_get_webdriver_object_using_locator(self.locators.header_title, "Get Data dialog header title").text.strip()
        msg = "Step {0} : Verify '{1}' dialog displayed".format(step_num, expected_title)
        self._utils_.asequal(expected_title, actual_title, msg)
        
    def close(self):
        """
        Description : Left click on close icon to close the Get Data dialog
        """
        close_icon = self._utils_.validate_and_get_webdriver_object_using_locator(self.locators.close_icon, "Get Data dialog close icon")
        self._core_utils_.left_click(close_icon)
        time.sleep(4)
        try:
            ok_button = self.driver.find_elements_by_css_selector(".common-confirm-dlg .ibx-dialog-ok-button")
            self._core_utils_.left_click(ok_button[0])
        except: 
            pass
        
    @property
    def Cancel(self):
        """
        Description : Left click on cancel button to close the Get Data dialog
        """
        Cancel_button = self._utils_.validate_and_get_webdriver_object_using_locator(Locators.cancel_button,'Cancel button')
        return html_controls.Button(Cancel_button, "Cancel button")
        
    @property
    def GetData(self): return _getdata_(self.driver)
    
    @property
    def UploadingData(self): return _uploading_data_(self.driver)
    
    @property
    def SelectApplicationFolder(self): return _select_application_folder_(self.driver)
    
class _getdata_:
    
    def __init__(self, driver):
        
        self.driver = driver
       
    @property
    def LocalFiles(self): return self._localfiles_(self.driver)
    
    @property
    def ServerFiles(self): return self._serverfiles_(self.driver)
    
    class _localfiles_(__Common__):
        
        def __init__(self, driver):
        
            super(_getdata_._localfiles_, self).__init__(driver)
            
        def select(self, file_name):
            """
            Description : Select the local file by left click
            :Usage - select('Excel')
            """
            file_objects = self._utils_.validate_and_get_webdriver_objects_using_locator(Locators.GetData.local_files, 'GetData Local Files')
            error_msg = "[{0}] file not exists in LOCALFILES section of GetData".format(file_name)
            file_obj = self._core_utils_.get_element_object_by_text_using_javascript(file_objects, file_name, error_msg, scroll_into_view=False)
            self._core_utils_.left_click(file_obj)
    
    class _serverfiles_(__Common__):
        
        def __init__(self, driver):
        
            super(_getdata_._serverfiles_, self).__init__(driver)
            
        def select(self, file_name):
            """
            Description : Select the server file by left click
            :Usage - select('MS SQL Server JDBC/AzureDB')
            """
            file_objects = self._utils_.validate_and_get_webdriver_objects_using_locator(Locators.GetData.server_files, 'GetData Local Files')
            error_msg = "[{0}] file not exists in LOCALFILES section of GetData".format(file_name)
            file_obj = self._core_utils_.get_element_object_by_text_using_javascript(file_objects, file_name, error_msg, scroll_into_view=False)
            self._core_utils_.left_click(file_obj)

class _uploading_data_:
    
    def __init__(self, driver):
        self.driver = driver
        self._locators_ = Locators
        
    @property
    def Sheets(self): return self._sheets_(self.driver)
    
    @property
    def Vizualize_Data(self): return self._visualization_Data(self.driver)
    
    def click_exit(self):
        """
        Description : Left click Exit Button
        """
        ob = self._utils_.validate_and_get_webdriver_object_using_locator(Locators.exit_button, "Exit")
        self._core_utils_.left_click(ob)
        
        
    class _visualization_Data(__Common__):
            
        def __init__(self, driver):
            super(_uploading_data_._visualization_Data,self).__init__(driver)
            self._locators = Locators.UploadingData.Sheets.VisualizeData_button
            self._name = "Visualization "
            
        
        def click_visualization_Data(self):
            """
            Description : Left click Visualization
            """
            ob = self._utils_.validate_and_get_webdriver_object_using_locator(Locators.UploadingData.Sheets.VisualizeData_button, "Visualization Data")
            self._core_utils_.left_click(ob)
        
    
    class _sheets_(__Common__):
        
        def __init__(self, driver):
            super(_uploading_data_._sheets_,self).__init__(driver)
            self.driver = driver    
        
        @property
        def ApplicationFolder(self): return _uploading_data_._sheets_._application_folder_(self.driver)
        
        @property       
        def Load(self):
            """Return Load button Class object to perform actions"""
            load_button = self._utils_.validate_and_get_webdriver_object_using_locator(Locators.UploadingData.Sheets.load_button,'load button')
            return html_controls.Button(load_button, "load button")        
        
        @property
        def sheetName(self):
            sheetname_textbox_obj = self._utils_.validate_and_get_webdriver_object_using_locator(Locators.UploadingData.Sheets.sheetname_textbox_obj, 'sheet name' )
            return html_controls.TextBox(sheetname_textbox_obj, 'sheet name')
        
        # def load(self):
        #
        #     """Return Load button Class object to perform actions"""
        #     uploading_data = _uploading_data_(self._driver)
        #
        #     is_uploading_data = self._webelement.wait_for_element_text(Locators.UploadingData.base1, "Visualization Data" , 3, raise_error=False)
        #     if is_uploading_data :
        #         ok_button_loc = (By.CSS_SELECTOR, "div.pop-top .ibx-dialog-ok-button")
        #         ok_button = self._webelement.wait_for_element_text(ok_button_loc, "OK", 2, raise_error=False)
        #         ok_button and self._core_utils.python_left_click(ok_button)
        #         time.sleep(15)
      
        class _application_folder_(__Common__):
            
            def __init__(self, driver):
                
                super(_uploading_data_._sheets_._application_folder_, self).__init__(driver)
            
            def click(self):
                """
                Description : Left click Application folder
                """
                ele_obj = self._utils_.validate_and_get_webdriver_object_using_locator(Locators.UploadingData.Sheets.application_folder, "Application Folder")
                self._core_utils_.left_click(ele_obj)
            
            def verify_selected_folder(self, expected_folder, step_num):
                """
                Description : Verify the selected folder text
                :Usage = verify_selected_folder('myhome, '02.01)
                """
                ele_obj = self._utils_.validate_and_get_webdriver_object_using_locator(Locators.UploadingData.Sheets.application_folder, "Application Folder")
                actual_folder = ele_obj.text.strip()
                msg = 'Step {0} : Verify [{1}] application folder selected'.format(step_num, expected_folder)
                self._utils_.asequal(expected_folder, actual_folder, msg)
                
        
                
class _select_application_folder_:
    
    def __init__(self, driver):
        
        self.driver = driver
        
    @property
    def Folders(self): return self._folders_(self.driver)
    
    class _folders_(__Common__):
        
        def __init__(self, driver):
        
            super(_select_application_folder_._folders_, self).__init__(driver)
            
        def verify(self, expected_foldes, step_num, assert_type='asin'):
            """
            Description : Verify the application folders
            :Usage- verify('myhome', '02.01)
            """         
            foldes_object = self._utils_.validate_and_get_webdriver_objects_using_locator(Locators.SelectApplicationFolder.lisview_folders, "Application Folders")
            actual_folders = [folder.text.strip() for folder in foldes_object]
            msg = 'Step {0} : Verify get data application folders'.format(step_num)
            self._utils_.verify_list_values(expected_foldes, actual_folders, msg, assert_type)