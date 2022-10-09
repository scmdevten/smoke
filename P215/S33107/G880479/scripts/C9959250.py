"""-------------------------------------------------------------------------------------------
Author Name  : HJEEVANA@TIBCO.COM
Automated On : 18-July-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub
from selenium.webdriver.common.by import By
from common.lib.utillity import UtillityMethods

class C9959250_TestClass(BaseTestCase):
    
    def test_C9959250(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        """
        TEST CASE VAIABLES
        """
        Title = (By.CSS_SELECTOR, "div[class^='pd-page-title'] div[class='ibx-label-text']")
        Yellow_LOC = (By.CSS_SELECTOR, "div[data-ibxp-ss-id='CONTENT-SQL'] span[style='background-color:Yellow']")
        Table_content1 = (By.XPATH, "//table/tbody/tr[2]/td[1]")
        Table_content2 = (By.XPATH, "//table/tbody/tr[7]/td[1]")
        
        STEP_01 = """
            STEP 01 : Sign into 'TIBCO WebFOCUS Home Page' as Developer User
        """
        WFHub.invoke_with_login('mriddev', 'mrpassdev')
        WFHub._utils.capture_screenshot("01", STEP_01)
        
        STEP_02 = """
            STEP 02 : From the left side navigation bar > Click on 'Workspaces' view > Expand 'Workspaces' >Click on 'P215_S31921' workspaces from the resource tree
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921')
        WFHub._utils.capture_screenshot("02", STEP_02)
        
        STEP_03 = """
            STEP 03 : Right-click on 'RunWsqlTrc_noParms' > Run > Run with SQL trace
        """
        WFHub.Workspaces.ContentArea.right_click_on_file('RunWsqlTrc_noParms')
        WFHub.ContextMenu.select('Run...->Run with SQL trace')
        WFHub._utils.capture_screenshot("03", STEP_03)
        
        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify the following:
        """
        WFHub._core_utils.switch_to_new_window()
        Actual_title = WFHub._utils.validate_and_get_webdriver_object_using_locator(Title, 'SQL Trace Title').text.strip()
        msg = 'STEP 03.01 : Title verified '
        UtillityMethods.asequal(self,Actual_title, 'RunWsqlTrc_noParms',msg)
        Actual_text = WFHub._utils.validate_and_get_webdriver_object_using_locator(Yellow_LOC, 'Line Of Code').text.strip()
        msg2 = 'STEP 03.02 : Line of code verified '
        UtillityMethods.asequal(self,Actual_text, '(FOC2689) AGGREGATION DONE ...', msg2)
        WFHub._core_utils.switch_to_frame(frame_css = "iframe[name='CONTENT-SSID']")
        Actual_content = WFHub._utils.validate_and_get_webdriver_object_using_locator(Table_content1, 'Accessories').text.strip()
        message1 = 'STEP 03.03 : Content present in run window'
        UtillityMethods.asequal(self,Actual_content, 'Accessories', message1)
        Actual_content = WFHub._utils.validate_and_get_webdriver_object_using_locator(Table_content2, 'Televisions').text.strip()
        message2 = 'STEP 03.04 : Content present in run window'
        UtillityMethods.asequal(self,Actual_content, 'Televisions', message2)
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)
        
        STEP_04 = """
            STEP 04 : Close 'RunWsqlTrc_noParms' window
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub.Workspaces.switch_to_frame()
        WFHub._utils.capture_screenshot("04", STEP_04)
        
        STEP_05 = """
            STEP 05 : Right-click on 'RunWsqlTrc_YesParms' > Run > Run with SQL trace
        """
        WFHub.Workspaces.ContentArea.right_click_on_file('RunWsqlTrc_YesParms')
        WFHub.ContextMenu.select('Run...->Run with SQL trace')
        WFHub._utils.capture_screenshot("05", STEP_05)
        
        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the following:
        """
        WFHub._core_utils.switch_to_new_window()
        WFHub.RunWindow.New_run_window_Textbox.verify_placeholder('Product Category:', 05.01)
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)
        
        STEP_06 = """
            STEP 06 : Enter 'Accessories' in the 'Product Category:' text box > Click 'Summit'
        """
        WFHub.RunWindow.New_run_window_Textbox.enter_text('Accessories')
        WFHub.RunWindow.Submit_button.click()
        
        WFHub._utils.capture_screenshot("06", STEP_06)
        
        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify the following:
        """
        WFHub.RunWindow.New_run_window_Textbox.verify_placeholder('Accessories', 06.01)
        Actual_title = WFHub._utils.validate_and_get_webdriver_object_using_locator(Title, 'SQL Trace Title').text.strip()
        msg3 = 'STEP 06.01 : Title verified'
        UtillityMethods.asequal(self,Actual_title, 'RunWsqlTrc_YesParms',msg3)
        Actual_text = WFHub._utils.validate_and_get_webdriver_object_using_locator(Yellow_LOC, 'Line Of Code').text.strip()
        msg4 = 'STEP 06.02 : Line of code verified'
        UtillityMethods.asequal(self,Actual_text, '(FOC2689) AGGREGATION DONE ...', msg4)
        WFHub._core_utils.switch_to_frame(frame_css = "iframe[name='CONTENT-SSID']")
        Actual_content = WFHub._utils.validate_and_get_webdriver_object_using_locator(Table_content1, 'Accessories').text.strip()
        message3 = 'STEP 06.03 : Content present in run window'
        UtillityMethods.asequal(self,Actual_content, 'Accessories', message3)
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)
        
        STEP_07 = """
            STEP 07 : Close 'RunWsqlTrc_YesParms' window
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub.Workspaces.switch_to_frame()
        WFHub._utils.capture_screenshot("07", STEP_07)
        

        STEP_08 = """
            STEP 08 : From the tree, Expand 'Retail Samples' > 'Portals' > Click on the 'Small Widgets'
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->Retail Samples->Portal->Small Widgets')
        WFHub._utils.capture_screenshot("08", STEP_08)
        
        STEP_09 = """
            STEP 09 : Right-click on 'Category Sales' > Run > Run with SQL trace
        """
        WFHub.Workspaces.ContentArea.right_click_on_file('Category Sales')
        WFHub.ContextMenu.select('Run...->Run with SQL trace')
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the following:
        """
        WFHub._core_utils.switch_to_new_window()
        WFHub._utils.synchronize_with_visble_text("div[class*='ACC-SECTION-SQL'] div[data-ibxp-ss-id='CONTENT-SQL'] span[style='background-color:Yellow']", '(FOC2689) AGGREGATION DONE ...' , 30)
        Actual_title = WFHub._utils.validate_and_get_webdriver_object_using_locator(Title, 'SQL Trace Title').text.strip()
        msg5 = 'STEP 09.01 : Title verified'
        UtillityMethods.asequal(self,Actual_title, 'Category Sales',msg5)
        WFHub._utils.synchronize_with_visble_text("div[class*='ACC-SECTION-SQL'] div[data-ibxp-ss-id='CONTENT-SQL'] span[style='background-color:Yellow']", '(FOC2689) AGGREGATION DONE ...' , 30)
        Actual_text = WFHub._utils.validate_and_get_webdriver_object_using_locator(Yellow_LOC, 'Line Of Code').text.strip()
        msg6 = 'STEP 09.02 : Line of code verified'
        UtillityMethods.asequal(self,Actual_text, '(FOC2689) AGGREGATION DONE ...', msg6)
        WFHub._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)
        

        STEP_10 = """
            STEP 10 : Close 'Category Sales' window
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click on the 'User' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select('Sign Out')
        WFHub._utils.capture_screenshot("11", STEP_11)

