"""-------------------------------------------------------------------------------------------
Author Name  : HJEEVANA@TIBCO.COM
Automated On : 17-May-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub
from common.wftools.designer import Designer as DesignerPage
from selenium.webdriver.common.by import By

class C9959758_TestClass(BaseTestCase):
    
    def test_C9959758(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        Expected_trend_xlabels = ['63.138','441.964','820.790','1.200K','1.578K','1.957K','2.967K']
        Expected_run_xlabels = ['63.138','189.413','315.689','441.964','568.239','694.515','820.790','947.066','1.073K','1.200K','1.326K','1.452K','1.578K','1.705K','1.831K','1.957K','2.084K','2.715K','2.967K','3.220K','3.725K']
        Expected_trend_zlabels = ['47.251K','32.836K','26.429K','21.623K','16.818K','12.013K','7.208K','2.403K']
        Expected_run_zlabels = ['47.251K','40.844K','37.641K','32.836K','29.632K','28.030K','26.429K','24.827K','23.225K','21.623K','20.022K','18.420K','16.818K','15.216K','13.615K','12.013K','10.411K','8.810K','7.208K','5.606K','4.004K','2.403K','800.867']
        Application_menu = (By.CSS_SELECTOR, "div[class*='te-menu-file']")
        
        STEP_01 = """
            STEP 01 : Sign into TIBCO WebFOCUS as Developer user
        """
        
        WFHub.invoke_with_login('mriddev', 'mrpassdev')
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar, Click on 'Workspaces' icon > Click on 'P215_S31921' workspace
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S31921")
        WFHub.Workspaces.ContentArea.delete_file_if_exists('C9959727_Insight')
        WFHub.Workspaces.switch_to_default_content()        
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on '+' button (Start Something New) > Select 'Create Visualization' > Double click on 'ibisamp' application folder > Double click on 'ggsales.mas'
        """
        WFHub.Banner.PlusMenu.Button.click()
        WFHub.Banner.PlusMenu.select_menu("Create Visualizations")
        WFHub._core_utils.switch_to_new_window()
        Designer.Dialog.SelectDataSource.ListView.select_masterfile("ibisamp->ggsales.mas")
        Designer.Dialog.SelectDataSource.CreateVisualisation.click()
        Designer._utils.wait_for_page_loads(15,pause_time=3)
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Select 'Insights' from the left side toolbar
        """
        Designer.SideBar.Insights.click()
        Designer._utils.wait_for_page_loads(10,pause_time=10)
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify insights returns a list of possible trends of interest to the use same as below:
        """
        Designer.VisualizationCanvas.Insights.verify_xaxis_title(['Budget Units','Budget Dollars'], 04.01)
        Designer.VisualizationCanvas.Insights.verify_xaxis_labels(Expected_trend_xlabels, 04.02)
        Designer.VisualizationCanvas.Insights.verify_Zaxis_labels(Expected_trend_zlabels, 04.03)
        Designer.VisualizationCanvas.Insights.verify_number_of_risers(87, 04.04)
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on the action icon ![](index.php?/attachments/get/1923734) in the upper right of the exposed insight
        """
        Designer.VisualizationCanvas.Insights.Actions_icon()
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the following options menu displayed:
    
            1. Copy content to canvas
            2. Save the visualization to a workspace
            3. Run the visualization in a new window
        """
        WFHub.ContextMenu.verify_options(['Copy content to canvas','Save the visualization to a workspace','Run the visualization in a new window'], 05.01)
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Select 'Copy content to canvas' option
        """
        WFHub.ContextMenu.select('Copy content to canvas')
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify a dialog appears asking if you wish to use the current data limit or use the same sample data as insights
        """
        Designer.Dialog.Warning.verify_title('Canvas Data Limit Does Not Match', 06.01)
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Select 'Use Sample Data'
        """
        Designer.Dialog.Warning.Use_Sample_Data.click()
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the following chart, using the same data, is placed on the designer page canvas
        """
        WFHub._utils.wait_for_page_loads(5,pause_time=4)
        Designer.PageCanvas.Containers.Basic('Container 1').BarChart.verify_xaxis_title(['Budget Units','Budget Dollars'], 07.01)
        Designer.PageCanvas.Containers.Basic('Container 1').BarChart.verify_xaxis_labels(Expected_trend_xlabels, 07.02)
        Designer.PageCanvas.Containers.Basic('Container 1').BarChart.verify_zaxis_labels(Expected_trend_zlabels, 07.03)
        Designer.PageCanvas.Containers.Basic('Container 1').BarChart.verify_number_of_risers(87, 07.04)
        WFHub._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on the action icon in the upper right of the exposed insight > Select 'Run the visualization in a new window'
        """
        Designer.VisualizationCanvas.Insights.Actions_icon()
        WFHub.ContextMenu.select('Run the visualization in a new window')
        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify the following:
    
            1. A new window opens and displays the chart.  
            2. Charts run from the insights panel use the same sample data.  
            3. The chart should be identical to what is seen in the panel.
        """
        Designer._core_utils.switch_to_new_window()
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_title(['Budget Units','Budget Dollars'], 08.01)
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_labels(Expected_run_xlabels, 08.02)
        Designer.VisualizationCanvas.RunMode.Bar.verify_zaxis_labels(Expected_run_zlabels, 08.03)
        Designer.VisualizationCanvas.RunMode.Bar.verify_number_of_risers(87, 08.04)
        Designer.VisualizationCanvas.RunMode.Bar.verify_riser_color([(86, "Jacksons Purple"), (2, "Moon Raker")], 08.05)
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Close the report browser tab
        """
        Designer._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click on the action icon in the upper right of the exposed insight > Select 'Save the visualization to a workspace'
        """
        Designer.VisualizationCanvas.Insights.Actions_icon()
        WFHub.ContextMenu.select('Save the visualization to a workspace')      
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Confirm that the path shown is to the same workspace ('P215_S31921')
        """
        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Save as 'C9959727_Insight' > Close the TIBCO WebFOCUS Designer
        """
        Designer.Dialog.SaveAs.wait_for_appear()
        Designer.Dialog.SaveAs.Title.enter_text('C9959727_Insight')
        Designer.Dialog.SaveAs.NavigationBar.BreadCrumb.verify("Workspaces>P215_S31921", 11.01)
        Designer.Dialog.SaveAs.SaveAsButton.click()
        WFHub._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : From 'P215_S31921' workspace, Right-click on 'C9959727_Insight' > Select 'Edit with text editor'
        """
        Designer._core_utils.switch_to_previous_window()
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S31921")
        WFHub.Workspaces.ContentArea.right_click_on_file("C9959727_Insight")
        WFHub.ContextMenu.select("Edit with text editor")
        WFHub._core_utils.switch_to_window()
        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify the block at the top of the code to use sample data
        """
        WFHub.Wf_Texteditor.verify_line_in_texteditor(['-*Sample Data Begin Syntax', 'ENGINE INT SET SAMPLING_TARGET_COUNT 100000', 'CREATE_SAMPLING', '{"source_app" : "ibisamp",', '"source_name" : "ggsales"', '}', 'END', '', '', '', '', 'ENGINE INT SET SAMPLING ON','' ], 12.01, comparison_type='asin')
        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Close the text editor
        """
        WFHub._utils.validate_and_get_webdriver_object_using_locator(Application_menu, "Application menu").click()
        WFHub.ContextMenu.select('Close')
        WFHub.Wf_Texteditor._utils.switch_to_main_window()
        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : From 'P215_S31921' workspace, Right-click on 'C9959727_Insight' > Select Run... > Run in new window
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S31921")
        WFHub.Workspaces.ContentArea.right_click_on_file("C9959727_Insight")
        WFHub.ContextMenu.select('Run...->Run in new window')
        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the same chart as when we ran this from the Insights Panel
        """
        Designer._core_utils.switch_to_new_window()
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_title(['Budget Units','Budget Dollars'], 14.01)
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_labels(Expected_run_xlabels, 14.02)
        Designer.VisualizationCanvas.RunMode.Bar.verify_zaxis_labels(Expected_run_zlabels, 14.03)
        Designer.VisualizationCanvas.RunMode.Bar.verify_number_of_risers(87, 14.04)
        Designer.VisualizationCanvas.RunMode.Bar.verify_riser_color([(86, "Jacksons Purple"), (2, "Moon Raker")], 14.05)
        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Close the run window
        """
        Designer._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select('Sign Out')
        WFHub._utils.capture_screenshot("16", STEP_16)

