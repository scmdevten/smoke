"""-------------------------------------------------------------------------------------------
Author Name  : HJEEVANA@TIBCO.COM
Automated On : 08-August-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub
from common.wftools.designer import Designer as DesignerPage

class C9958301_TestClass(BaseTestCase):
    
    def test_C9958301(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        
        STEP_01 = """
            STEP 01 : Sign into 'TIBCO WebFOCUS' as Developer User
        """
        WFHub.invoke_with_login('mriddev', 'mrpassdev')
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar > Click on the 'Start Something New' button (i.e., '+' button)
        """
        WFHub.Banner.PlusMenu.Button.click()
        WFHub._utils.capture_screenshot("02", STEP_02)
        
        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify the following options displayed,
        """
        WFHub.Banner.PlusMenu.verify_menus(['Create Visualizations', 'Assemble Visualizations', 'Get Data', 'Get Data (Advanced)', 'Create Data Flow', 'Create DBMS SQL Flow', 'Create Cluster Business View', 'Explore Data'], 02.01)
        WFHub._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)
        
        STEP_03 = """
            STEP 03 : Click on 'Create Visualizations'
        """
        WFHub.Banner.PlusMenu.select_menu('Create Visualizations')
        WFHub._utils.capture_screenshot("03", STEP_03)
        
        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that 'TIBCO WebFOCUS Designer' opens in a new window with select data source dialog
        """
        WFHub._core_utils.switch_to_new_window()
        WFHub._utils.synchronize_with_visble_text("div.pop-modal[role*='dialog'][aria-hidden='false'] div.ibx-title-bar-caption", 'Select Data Source', 50)
        Designer.Dialog.SelectDataSource.verify_title('Select Data Source', 03.01)
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)
        
        STEP_04 = """
            STEP 04 : From 'My Workspace' > Double click on 'baseapp' application folder > Double click on 'car.mas' file
        """
        Designer.Dialog.SelectDataSource.ListView.select_masterfile('baseapp->car.mas')
        Designer.Dialog.SelectDataSource.CreateVisualisation.click()
        WFHub._utils.capture_screenshot("04", STEP_04)
        
        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify chart appears in the preview canvas
        """
        Designer.VisualizationCanvas.verify_default_canvas([], 04.01)
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)
        
        STEP_05 = """
            STEP 05 : Close 'TIBCO WebFOCUS Designer'
        """
        Designer._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("05", STEP_05)
        
        STEP_06 = """
            STEP 06 : Click on the 'Start Something New' button > Click on 'Assemble Visualization' > Choose 'Blank' template
        """
        WFHub.Banner.PlusMenu.Button.click()
        WFHub.Banner.PlusMenu.select_menu('Assemble Visualizations')
        WFHub._core_utils.switch_to_new_window()
        Designer.Dialog.ChooseTemplate.Common.select('Blank')
        WFHub._utils.capture_screenshot("06", STEP_06)
        
        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that 'TIBCO WebFOCUS Designer' opens in a new window without any error
        """
        Designer.PageCanvas.Heading.verify_heading('Page Heading', 06.01)
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)
        
        STEP_07 = """
            STEP 07 : Close 'TIBCO WebFOCUS Designer'
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("07", STEP_07)
        
        STEP_08 = """
            STEP 08 : Click on the 'Start Something New' button > Click on 'Get Data'
        """
        WFHub.Banner.PlusMenu.Button.click()
        WFHub.Banner.PlusMenu.select_menu('Get Data')
        WFHub._utils.wait_for_page_loads(50)
        WFHub._utils.capture_screenshot("08", STEP_08)
        
        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify 'Get Data' opens in a modal dialog:
        """
        WFHub._utils.switch_to_frame(frame_css="div.wfshell-get-data-iframe iframe")
        WFHub._utils.synchronize_with_visble_text(WFHub.GetDataFrame.locators.content_css, "Excel", 80)
        WFHub.GetDataFrame.verify_title('Get Data', 08.01)
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)
        
        STEP_09 = """
            STEP 09 : Click on 'Cancel' button to close the Get Data modal dialog
        """
        WFHub.GetDataFrame.Cancel.click()
        WFHub._utils.switch_to_default_content()
        WFHub._utils.capture_screenshot("09", STEP_09)
        

        STEP_10 = """
            STEP 10 : Click on the 'Start Something New' button > Click on 'Get Data(Advanced)'
        """
        WFHub.Banner.PlusMenu.Button.click()
        WFHub.Banner.PlusMenu.select_menu('Get Data (Advanced)')
        WFHub._utils.wait_for_page_loads(50)
        WFHub._utils.capture_screenshot("10", STEP_10)
        

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify 'Get Data' opens in a modal dialog:
        """
        WFHub._utils.switch_to_frame(frame_css="div[class^='wfshell-get-data-iframe'] iframe")
        WFHub._utils.synchronize_with_visble_text(WFHub.GetDataFrame.locators.advanced_content_css, "Excel", 80)
        WFHub.GetDataFrame.verify_title('Get Data', 10.01)
        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)
        


        STEP_11 = """
            STEP 11 : Click 'X' to close the Get Data modal dialog
        """
        WFHub.GetDataFrame.close()
        WFHub._utils.switch_to_default_content()
        WFHub._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click on the 'Start Something New' button > Click on 'Create Data Flow'
        """
        WFHub.Banner.PlusMenu.Button.click()
        WFHub.Banner.PlusMenu.select_menu('Create Data Flow')
        WFHub._core_utils.switch_to_new_window()
        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify 'Data flow' opens in a new window without any error and in the bottom of the window the 'dflow01' tab displays
        """
        WFHub._utils.synchronize_with_visble_text("#rs-wc", 'Data', 80)
        msg = 'STEP 12: dflow01 is available in content area'
        WFHub._utils.verify_element_text("div[data-ibx-name='_itemsBox'] div[class*='radio-group-checked']", 'dflow01', msg)
        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Do not close the data flow window. Switch back to 'TIBCO WebFOCUS' tab > Click on the 'Start Something New' button > Click on 'Create DBMS Sequel Flow'
        """
        WFHub._core_utils.switch_to_previous_window(window_close='False')
        WFHub.Banner.PlusMenu.Button.click()
        WFHub.Banner.PlusMenu.select_menu('Create DBMS SQL Flow')
        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify 'Data flow' window reloads, DBMS Sequel flow' appears without any error and in the bottom window the 'dflow01', and 'dflow02'(active) tabs displays
        """
        WFHub._core_utils.switch_to_new_window()
        msg = 'STEP 13.01 : dflow01 is available in content area'
        WFHub._utils.verify_element_text("div[data-ibx-name='_itemsBox'] div[data-ibx-type='ibxTabButton']:not([class*='radio-group-checked'])", 'dflow01', msg)
        msg1 = 'STEP 13.02 : dflow02 is available in content area'
        WFHub._utils.verify_element_text("div[data-ibx-name='_itemsBox'] div[class*='radio-group-checked']", 'dflow02', msg1)
        WFHub._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Do not close the data flow window. Switch back to 'TIBCO WebFOCUS' tab > Click on the 'Start Something New' button > Click on 'Create Cluster Business Flow'
        """
        WFHub._core_utils.switch_to_previous_window(window_close='false')
        WFHub.Banner.PlusMenu.Button.click()
        WFHub.Banner.PlusMenu.select_menu('Create Cluster Business View')
        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify 'DBMS Sequel flow' window reloads and reporting server console synonym opens in a new tab at the bottom of the window it displays 'dflow01', 'dflow02' and 'synonymn01(*) (active)
        """
        WFHub._core_utils.switch_to_new_window()
        msg1 = 'STEP 14.01 : synonym01 is available in content area'
        WFHub._utils.verify_element_text("div[data-ibx-name='_itemsBox'] div[class*='radio-group-checked']", 'synonym01 (*)', msg1)
        msg2 = 'STEP 14.02 : dflow01 is available in content area'
        WFHub._utils.verify_element_text("div[aria-controls='ibxTabPage-1']", 'dflow01', msg2)
        msg3 = 'STEP 14.03 : dflow02 is available in content area'
        WFHub._utils.verify_element_text("div[aria-controls='ibxTabPage-2']", 'dflow02', msg3)
        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Close the 'Reporting Server' console window
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Click on the 'Start Something New' button > Click on 'Explore Data'
        """
        WFHub.Banner.PlusMenu.Button.click()
        WFHub.Banner.PlusMenu.select_menu('Explore Data')
        WFHub._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify 'Select Data Source' opens in a modal dialog:
        """
        WFHub._utils.synchronize_with_visble_text("div.pop-modal[role*='dialog'][aria-hidden='false'] div.ibx-title-bar-caption", 'Select Data Source', 50)
        Designer.Dialog.SelectDataSource.verify_title('Select Data Source', 16.01)
        WFHub._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : From 'My Workspace' > Double click on 'baseapp' application folder > Double click on 'car.mas' file
        """
        Designer.Dialog.SelectDataSource.ListView.select_masterfile('baseapp->car.mas')
        Designer.Dialog.SelectDataSource.SelectButton.click()
        WFHub._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify 'Explore Data' opens in modal dialog:
        """
        WFHub._utils.synchronize_with_visble_text(".pop-top[role*='dialog'] div.ibx-title-bar-caption", 'Explore Data', 50)
        WFHub.Dialog.ExploreData.verify_title('Explore Data', 17.01)
        WFHub._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Click on 'Close' button to close the 'Explore Data' modal dialog
        """
        WFHub.Dialog.ExploreData.Close.click()
        WFHub._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Click on the 'User' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select('Sign Out')
        WFHub._utils.capture_screenshot("19", STEP_19)

