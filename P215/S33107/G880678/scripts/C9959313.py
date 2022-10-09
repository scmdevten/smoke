"""-------------------------------------------------------------------------------------------
Author Name  : Khushboo Parikh
Automated On : 18th May 2022
-------------------------------------------------------------------------------------------"""
import os
from common.lib.uiauto import FileDialog
from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub
from common.wftools.paris_home_page import ParisHomePage as PHP
from common.wftools.designer import Designer as DesignerPage
from common.webservices.lib import utils

class C9959313_TestClass(BaseTestCase):
    
    def test_C9959313(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        Designer = DesignerPage()
        ParisHomePage = PHP(WFHub._driver)
        
        """
        TEST CASE VAIABLES
        """
        JsonPath = os.path.join(os.getcwd(), "data", "oobeSections.json")
        
        STEP_01 = """
            STEP 01 : Sign into TIBCO WebFOCUS as Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("01", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on the 'Application Directories' menu from the left side navigation bar
        """
        WFHub.LeftSideNavigationBar.ApplicationDirectories.click()
        WFHub._utils.wait_for_page_loads(2,pause_time=3)
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on "Get Data"
        """       
        WFHub.ApplicationDirectories.switch_to_frame() 
        # WFHub.ApplicationDirectories.RibbonBar.select_menu("Get Data")
        # WFHub._utils.capture_screenshot("03", STEP_03)
        #
        # STEP_03_EXPECTED = """
        #     STEP 03 - Expected : Verify Local Files options
        # """
        # # WFHub.GetDataFrame.GetData.LocalFiles
        # WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)
        #
        # STEP_04 = """
        #     STEP 04 : Click on the "JSON" menu
        # """
        # # WFHub._utils.switch_to_frame(frame_css="div.wfshell-get-data-iframe iframe")
        # WFHub._utils.synchronize_with_visble_text(ParisHomePage.GetDataFrame.locators.content_css, "JSON", 80)
        # WFHub.GetDataFrame.GetData.LocalFiles.select('JSON')
        # WFHub._utils.wait_for_page_loads(2,pause_time=3)
        # WFHub._utils.capture_screenshot("04", STEP_04)
        #
        # STEP_05 = """
        #     STEP 05 : Browse the following directory:
        #             \\na1prdfs01.tibco.com\foc\data\bipgqashare\filesneededfortestsuites\P215\8206 baseline\G785032
        # """
        # FileDialog().open_file(JsonPath)
        # WFHub._utils.synchronize_with_visble_text(ParisHomePage.GetDataFrame.locators.content_css, "Argentina", 80)
        # WFHub._utils.capture_screenshot("05", STEP_05)
        #
        # STEP_06 = """
        #     STEP 06 : Select "oobeSections" > Open
        # """        
        # WFHub._utils.capture_screenshot("06", STEP_06)
        #
        # STEP_06_EXPECTED = """
        #     STEP 06 - Expected : Verify Uploading data modal window opens as expected
        # """
        # # WFHub.GetDataFrame.UploadingData.Sheets.ApplicationFolder.
        # WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)
        #

        # STEP_07 = """
        #     STEP 07 : For WebFOCUS: Click on available application folder and choose baseapp folder
        # """
        # # WFHub.GetDataFrame.SelectApplicationFolder.Folders.
        # WFHub._utils.wait_for_page_loads(2,pause_time=3)
        # WFHub._utils.capture_screenshot("07", STEP_07)
        #
        # STEP_07_EXPECTED = """
        #     STEP 07 - Expected : WebFOCUS : Verify baseapp folder selected in Application folder
        # """
        # WFHub.GetDataFrame.UploadingData.Sheets.ApplicationFolder.verify_selected_folder('baseapp', STEP_07)
        # WFHub._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)
        #
        # STEP_08 = """
        #     STEP 08 : Change the name to "sections"
        # """
        # WFHub.GetDataFrame.UploadingData.Sheets.sheetName.enter_text("sections", clear=True)        
        # WFHub._utils.wait_for_page_loads(2,pause_time=3)
        # WFHub._utils.capture_screenshot("08", STEP_08)
        #
        # STEP_09 = """
        #     STEP 09 : Click on "Load"
        # """        
        # WFHub.GetDataFrame.UploadingData.Sheets.Load.click()
        # WFHub.Dialog.Warning.ok()
        # WFHub._utils.wait_for_page_loads(2,pause_time=3)
        # WFHub._utils.capture_screenshot("09", STEP_09)
        #
        # STEP_09_EXPECTED = """
        #     STEP 09 - Expected : WebFOCUS: Verify Status changed to Loaded and also verify selected Adapter and Application folder should shown in sheet
        # """
        # # WFHub.GetDataFrame.UploadingData.Sheets.Load.
        # WFHub._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)
        #
        # STEP_10 = """
        #     STEP 10 : Click "EXIT" icon
        # """        
        # WFHub.GetDataFrame.UploadingData.click_exit()
        # WFHub._utils.wait_for_page_loads(2,pause_time=3)
        # WFHub._utils.capture_screenshot("10", STEP_10)
        #
        # STEP_10_EXPECTED = """
        #     STEP 10 - Expected :  Verify Modal window should closed
        # """
        # # WFHub.GetDataFrame.UploadingData.Sheets.Load.
        # WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)
        #

        STEP_11 = """
            STEP 11 : Select "baseapp" folder in the Application directories area
        """        
        WFHub.ApplicationDirectories.Applications.select_directory("baseapp")
        WFHub._utils.wait_for_page_loads(2,pause_time=3)
        WFHub.ApplicationDirectories.Application_Directory.SearchTextBox().enter_text("audits")
        WFHub._utils.wait_for_page_loads(2,pause_time=3)
        WFHub.ApplicationDirectories.Application_Directory.verify_files(['audits'], "11.02")
        WFHub._utils.capture_screenshot("11", STEP_11)
        
        
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        