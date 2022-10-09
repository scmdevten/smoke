"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh Ravichandran
Automated On : 22-February-2022
-------------------------------------------------------------------------------------------"""
import os
from common.lib.uiauto import FileDialog
from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub
from common.wftools.paris_home_page import ParisHomePage as PHP
from common.wftools.designer import Designer as DesignerPage

class C9959310_TestClass(BaseTestCase):
    
    def test_C9959310(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        Designer = DesignerPage()
        ParisHomePage = PHP(WFHub._driver)
        
        """
        TEST CASE VAIABLES
        """
        ExcelPath = os.path.join(os.getcwd(), "data", "Country_Population_2014.xlsx")
        
        STEP_01 = """
            STEP 01 : Sign into TIBCO WebFOCUS as Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on the 'Home' from the left side navigation bar > Click on the 'My Workspace'
        """
        WFHub.LeftSideNavigationBar.Home.click()
        WFHub.Home.wait_for_text("My")
        WFHub.Home.select_view("My workspace")
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on '+' > Click on 'Get Data'
        """
        WFHub.Banner.PlusMenu.Button.click()
        WFHub.Banner.PlusMenu.select_menu("Get Data")
        WFHub._utils.wait_for_page_loads(30,pause_time=3)
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : ![](index.php?/attachments/get/1890720)
        """
        
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on 'Excel' menu
        """
        WFHub._utils.switch_to_frame(frame_css="div[class^='wfshell-get-data-iframe'] iframe")
        WFHub._utils.synchronize_with_visble_text(ParisHomePage.GetDataFrame.locators.content_css, "Excel", 80)
        WFHub.GetDataFrame.GetData.LocalFiles.select('Excel')
        WFHub._utils.wait_for_page_loads(2,pause_time=3)
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Browse the following directory:
            \\na1prdfs01.tibco.com\foc\data\bipgqashare\filesneededfortestsuites\P215\8206 baseline\G785032
        """
        FileDialog().open_file(ExcelPath)
        WFHub._utils.synchronize_with_visble_text(ParisHomePage.GetDataFrame.locators.content_css, "Argentina", 80)
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Select 'Country Population 2014' > Open
        """
        WFHub._utils.capture_screenshot("06", STEP_06)
        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify 'myhome' directory
        """
        WFHub.GetDataFrame.UploadingData.Sheets.ApplicationFolder.verify_selected_folder('p215_s31921',STEP_06)
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Change name to 'population_2014'
        """
        WFHub.GetDataFrame.UploadingData.Sheets.sheetName.enter_text("population_2014", clear=True)
        WFHub.GetDataFrame.UploadingData.Sheets.Load.click()
        WFHub.Dialog.Warning.ok()
        WFHub._utils.wait_for_page_loads(2,pause_time=3)
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click on 'Visualize Data'
        """
        WFHub.GetDataFrame.UploadingData.Vizualize_Data.click_visualization_Data()
        WFHub._core_utils.switch_to_default_content()
        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify WebFOCUS Designer is displayed with file 'population_2014'
        """
        WFHub._core_utils.switch_to_new_window()
        Designer.ResourcesPanel.Fields.Dimensions.verify_items(['Dimensions', 'Country_population_2014', 'COUNTRY NAME'], "08.01")
        Designer.ResourcesPanel.Fields.Measures.verify_items(['Measure Groups', 'Country_population_2014', 'Population - 2014'], "08.02")
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Locate and double click 'COUNTRY_CODE_ISO_3166'
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click("Dimensions->Country_population_2014->COUNTRY NAME->Attributes->COUNTRY_CODE_ISO_3166")
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Locate and double click 'Population - 2014'
        """
        Designer.ResourcesPanel.Fields.Measures.double_click("Measure Groups->Country_population_2014->Population - 2014")
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_11_EXPECTED = """
            STEP 11 : Verify canvas
        """
        Designer.PropertiesPanel.Settings.Display.Vertical.verify_available_fields(['Population - 2014'], "11.01")
        Designer.PropertiesPanel.Settings.Display.Horizontal.verify_available_fields(['COUNTRY_CODE_ISO_3166'], "11.02")
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['COUNTRY_CODE_ISO_3166'], "11.03")
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['Population - 2014'], "11.04")
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['AR', 'AT', 'AU', 'BE', 'BR', 'CA', 'CH', 'CL', 'CN', 'CO', 'CZ', 'DE', 'DK', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'HU', 'IE', 'IL', 'IN', 'IT', 'JP', 'KR', 'LU', 'MX', 'MY', 'NL', 'NO', 'PH', 'PL', 'PT', 'SE', 'SG', 'TH', 'TN', 'TR', 'TW', 'US', 'ZA'], "11.05")
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '0.4B', '0.8B', '1.2B', '1.6B'], "11.06")
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(42, "11.07")
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, "bar_blue")], "11.08")
        WFHub._utils.capture_screenshot("11- Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click on the Preview button
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify output
        """
        Designer.VisualizationCanvas.RunMode.Bar.wait_for_text("Population", time_out=60)
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_title(['COUNTRY_CODE_ISO_3166'], "12.01")
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_title(['Population - 2014'], "12.02")
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_labels(['AR', 'AT', 'AU', 'BE', 'BR', 'CA', 'CH', 'CL', 'CN', 'CO', 'CZ', 'DE', 'DK', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'HU', 'IE', 'IL', 'IN', 'IT', 'JP', 'KR', 'LU', 'MX', 'MY', 'NL', 'NO', 'PH', 'PL', 'PT', 'SE', 'SG', 'TH', 'TN', 'TR', 'TW', 'US', 'ZA'], "12.03")
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_labels(['0', '0.4B', '0.8B', '1.2B', '1.6B'], "12.04")
        Designer.VisualizationCanvas.RunMode.Bar.verify_number_of_risers(42, "12.05")
        Designer.VisualizationCanvas.RunMode.Bar.verify_riser_color([(1, "bar_blue")], "12.06")
        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click Save > save under P456_S32992 > G874961 > 'C9926912' > Click on Save
        """
        Designer._core_utils.switch_to_previous_window()
        Designer.ToolBar.save("C9926912")
        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Click on the main menu > Select 'Close'
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select('Close')
        Designer._core_utils.switch_to_previous_window(window_close=False)
        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Right click 'C9926912' > Edit
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S31921->My Content")
        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify canvas
        """
        WFHub.Workspaces.ContentArea.wait_for_text("C9926912")
        WFHub.Workspaces.ContentArea.right_click_on_file("C9926912")
        WFHub.ContextMenu.select("Edit")
        WFHub._core_utils.switch_to_default_content()
        WFHub._core_utils.switch_to_new_window()
        Designer.VisualizationCanvas.Bar.wait_for_text("Population", time_out=60)
        Designer.PropertiesPanel.Settings.Display.Vertical.verify_available_fields(['Population - 2014'], "15.01")
        Designer.PropertiesPanel.Settings.Display.Horizontal.verify_available_fields(['COUNTRY_CODE_ISO_3166'], "15.02")
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['COUNTRY_CODE_ISO_3166'], "15.03")
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['Population - 2014'], "15.04")
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['AR', 'AT', 'AU', 'BE', 'BR', 'CA', 'CH', 'CL', 'CN', 'CO', 'CZ', 'DE', 'DK', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'HU', 'IE', 'IL', 'IN', 'IT', 'JP', 'KR', 'LU', 'MX', 'MY', 'NL', 'NO', 'PH', 'PL', 'PT', 'SE', 'SG', 'TH', 'TN', 'TR', 'TW', 'US', 'ZA'], "15.05")
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '0.4B', '0.8B', '1.2B', '1.6B'], "15.06")
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(42, "15.07")
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, "bar_blue")], "15.08")
        WFHub._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Close Designer from the browser tab
        """
        Designer._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Sign out
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("17", STEP_17)

