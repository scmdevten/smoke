"""-------------------------------------------------------------------------------------------
Author Name  : HJEEVANA@TIBCO.COM
Automated On : 08-June-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub
from common.wftools.designer import Designer as DesignerPage
from selenium.webdriver.common.by import By

class C9959726_TestClass(BaseTestCase):
    
    def test_C9959726(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        canvas = (By.CSS_SELECTOR, "div[id='WcMultiframesContentView-7'] div[qa='row-0-column-0'] div[class='ibx-label-text']")
        content1 = (By.CSS_SELECTOR, "#WcMultiframesContentView-3 div[class$='wcx-standard'] div[qa='row-0-column-0']")
        content2 = (By.CSS_SELECTOR, "#WcMultiframesContentView-3 div[class$='wcx-standard'] div[qa='row-0-column-3']")
        session_extract = (By.CSS_SELECTOR, "#WcMultiframesContentView-3 div[class$='wcx-wcform'] div[class='ibx-label-text']")
        Application_menu = (By.CSS_SELECTOR, "div[class*='te-menu-file']")
        # Run_window_content1 = (By.CSS_SELECTOR, " //table/tbody/tr[1]/td[1]")
        # Run_window_content2 = (By.CSS_SELECTOR, " //table/tbody/tr[6]/td[1]")
        
        STEP_01 = """
            STEP 01 : Sign into TIBCO WebFOCUS as Developer user
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("01", STEP_01)
        
        STEP_02 = """
            STEP 02 : From the left side navigation bar, Click on 'Workspaces' icon > Click on 'P215_S31921' workspace
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921')
        WFHub.Workspaces.ContentArea.delete_file_if_exists('C9959726_HOLD')
        WFHub.Workspaces.switch_to_default_content()
        WFHub._utils.capture_screenshot("02", STEP_02)
        
        STEP_03 = """
            STEP 03 : Click on '+' button (Start Something New) > Select 'Create Visualization'
        """
        WFHub.Banner.PlusMenu.Button.click()
        WFHub.Banner.PlusMenu.select_menu('Create Visualizations')
        WFHub._core_utils.switch_to_new_window()
        WFHub._utils.capture_screenshot("03", STEP_03)
        
        STEP_04 = """
            STEP 04 : Double click on 'ibisamp' application folder > Double click on 'car.mas'
        """
        Designer.Dialog.SelectDataSource.ListView.select_masterfile('ibisamp->car.mas')
        Designer.Dialog.SelectDataSource.CreateVisualisation.click()
        WFHub._utils.capture_screenshot("04", STEP_04)
        
        STEP_05 = """
            STEP 05 : From the picker tool > Click on 'Standard Report'
        """
        Designer._utils.wait_for_page_loads(10, pause_time=10)
        Designer.ContentPicker.All.select('Standard Report')
        WFHub._utils.capture_screenshot("05", STEP_05)
        
        STEP_06 = """
            STEP 06 : Add 'COUNTRY' and 'DEALER_COST'
            Add 'SEATS' to 'Column Groups'
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click('COUNTRY')
        Designer.ResourcesPanel.Fields.Measures.double_click('DEALER_COST')
        Designer.ResourcesPanel.Fields.Measures.drag_to_bucket('SEATS', 'Column Groups')
        WFHub._utils.capture_screenshot("06", STEP_06)
        
        STEP_07 = """
            STEP 07 : Drag and drop 'CAR' field from data pane to 'Filters' bucket > Click on 'Load values from data' > Check 'PUEGEOT' > Add 'PUEGEOT' to the selected option list > Check 'PUEGEOT' > Check-off 'Exclude' > Click 'Save'
        """
        Designer.ResourcesPanel.Fields.Dimensions.expand('COMP->CAR')
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_filter_field_bucket('CAR', 'Filters')
        WFHub._utils.capture_screenshot("07", STEP_07)
        
        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the following:
        """
        Designer.Dialog.AddFilter.ClickLoadValue()
        #Designer.Dialog.AddFilter.wait_until_visible(5, pause_time=5)
        Designer.Dialog.AddFilter.wait_for_text('Clear List')
        Designer.Dialog.AddFilter.DualListBox.select_options_in_all_options_area(['PEUGEOT'])
        Designer.Dialog.AddFilter.DualListBox.AddSelections.click()
        Designer.Dialog.AddFilter.DualListBox.select_options_in_selected_options_area(['PEUGEOT'])
        Designer.Dialog.AddFilter.ExcludeCheckbox.check()
        Designer.Dialog.AddFilter.Save.click()
        Designer.PropertiesPanel.Settings.Display.Rows.verify_available_fields(['COUNTRY'], 07.01)
        Designer.PropertiesPanel.Settings.Display.ColumnGroups.verify_available_fields(['SEATS'], 07.02)
        Designer.PropertiesPanel.Settings.Display.Summaries.verify_available_fields(['DEALER_COST'], 07.03)
        Designer.PropertiesPanel.Settings.Filters.verify_available_filter_fields(['CAR'], 07.04)
        WFHub._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)
        
        STEP_08 = """
            STEP 08 : Click on 'DATA' tab
        """
        Designer.ToolBar.Data.click()
        Designer._utils.wait_for_page_loads(10,pause_time=10)
        WFHub._utils.capture_screenshot("08", STEP_08)
        
        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that the DB icon is from a non-SQL source and that there is an SQL node showing Select Columns beneath
        """
        Designer.Data.switch_to_frame(3)
        Designer.Data.Canvas.verify_join_created(['Select Columns','car(T01)'], 08.01)
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)
        
        STEP_09 = """
            STEP 09 : Right-click on the 'SQL/Select Columns' node > Select 'Edit'
        """
        Designer.Data.Canvas.Right_click('Select Columns')
        Designer.ContextMenu.select('Edit')  
        WFHub._utils.capture_screenshot("09", STEP_09)
        
        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the Select Editor opens
        """
        WFHub._utils.wait_for_page_loads(5, pause_time=3)
        WFHub._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)
        
        STEP_10 = """
            STEP 10 : Click on the Delete Query icon
        """
        Designer.Data.SelectEditorFrame.MiddlePane.DeleteQuery.click()
        Designer._utils.wait_for_page_loads(3)
        WFHub._utils.capture_screenshot("10", STEP_10)
        
        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify the buckets are now empty
        """
        msg = "Step 10.01 : canvas value is verified"
        actual_object= WFHub._utils.validate_and_get_webdriver_object_using_locator(canvas, 'canvas')
        actual_text=actual_object.text.strip()
        WFHub._utils.asequal(actual_text,'<<<EMPTY>>>',msg)
        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)
        
        STEP_11 = """
            STEP 11 : Double click on 'COUNTRY', 'DEALER_COST', 'SEATS' and 'CAR'
        """
        Designer.Data.SelectEditorFrame.LeftSourcePane.SelectDataField('COUNTRY')
        Designer.Data.SelectEditorFrame.LeftSourcePane.SelectDataField('DEALER_COST')
        Designer.Data.SelectEditorFrame.LeftSourcePane.SelectDataField('SEATS')
        Designer.Data.SelectEditorFrame.LeftSourcePane.SelectDataField('CAR')
        WFHub._utils.wait_for_page_loads(10)
        WFHub._utils.capture_screenshot("11", STEP_11)
        

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify that 'COUNTRY' and 'CAR' are added to Rows, 'DEALER_COST' and 'SEATS' are added to Summaries and the preview area is populated
        """
        Designer.Data.SelectEditorFrame.MiddlePane.VerifyBucketField('COUNTRY', 11.01)
        Designer.Data.SelectEditorFrame.MiddlePane.VerifyBucketField('CAR', 11.02)
        Designer.Data.SelectEditorFrame.MiddlePane.VerifyBucketField('DEALER_COST', 11.03)
        Designer.Data.SelectEditorFrame.MiddlePane.VerifyBucketField('SEATS', 11.04)
        WFHub._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)
        
        STEP_12 = """
            STEP 12 : Click OK to close the Select Editor
        """
        Designer.Data.SelectEditorFrame.OKButton()
        WFHub._utils.wait_for_page_loads(10)
        Designer.Dialog.Warning.Ok.click()
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("12", STEP_12)
        
        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify the preview section on the bottom reflects what we did in the Select Editor
        """
        msg = "Step 12.01 : bottom canvas value is verified"
        value1_obj = WFHub._utils.validate_and_get_webdriver_object_using_locator(content1, 'country name')
        Actual_value1 = value1_obj.text.strip()
        WFHub._utils.asequal(Actual_value1,'ENGLAND',msg)
        msg2 = "Step 12.02 : bottom canvas value is verified"
        value2_obj = WFHub._utils.validate_and_get_webdriver_object_using_locator(content2, 'Seats num')
        Actual_value2 = value2_obj.text.strip()
        WFHub._utils.asequal(Actual_value2,'2',msg2)
        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)
        
        STEP_13 = """
            STEP 13 : Right-click on the 'SQL/Select Columns' node > select 'Create Session Extract'
        """
        Designer.Data.Canvas.Right_click('Select Columns')
        WFHub.ContextMenu.select('Create Session Extract')
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("13", STEP_13)
        
        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify that Format DATREC file is created in foccache
        """
        message = "Step 13.01 : DATREC file created"
        session_object= WFHub._utils.validate_and_get_webdriver_object_using_locator(session_extract, 'Session Extract')
        actual_text=session_object.text.strip()
        WFHub._utils.verify_list_values(['FOCCACHE/car01 HELD AS DATREC FILE'], actual_text, message, assert_type='asin')
        WFHub._utils.verify_list_values(['Return Code = 0'], actual_text, message, assert_type='asin')
        WFHub._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)
        
        STEP_14 = """
            STEP 14 : Click on the 'VISUALIZATION' tab
        """
        Designer._core_utils.switch_to_default_content()
        Designer.ToolBar.Visualization.click()
        WFHub._utils.capture_screenshot("14", STEP_14)
        
        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the following:
            1. The db name now shows CAR01 (the assigned temporary HOLD file name concatenates 01)
            2. The tree only shows the fields returned from Data Prep.  
            3. Since the extract file contains all the fields in the original query the report is intact.
        """
        Designer.ResourcesPanel.Fields.Dimensions.verify_items(['CAR'], 14.01, assert_type='in')
        Designer.ResourcesPanel.Fields.Measures.verify_items(['Retail_Cost'], 14.02, assert_type='notin')
        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)
        
        STEP_15 = """
            STEP 15 : Save as 'C9959726_HOLD' > Close the Designer Framework tool.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select('Save As...')
        Designer._utils.wait_for_page_loads(5)
        Designer.Dialog.SaveAs.Title.enter_text('C9959726_HOLD')
        Designer.Dialog.SaveAs.SaveAsButton.click()
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select('Close')
        WFHub._utils.capture_screenshot("15", STEP_15)
        
        
        STEP_16 = """
            STEP 16 : From'P215_S31921' workspace > Right-click on 'C9959726_HOLD' > Select 'Edit with text editor'
        """
        Designer._core_utils.switch_to_previous_window(window_close='false')
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S31921")
        WFHub.Workspaces.ContentArea.right_click_on_file("C9959726_HOLD")
        WFHub.ContextMenu.select("Edit with text editor")
        WFHub._utils.wait_for_page_loads(5)
        WFHub._core_utils.switch_to_window()
        WFHub._utils.capture_screenshot("16", STEP_16)
        
        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify the HOLD for Non-SQL source is going to the foccache application and to format DATREC
        """
        WFHub.Wf_Texteditor.verify_line_in_texteditor(['-TYPE  (ICM18741) foccache/car01 type DATREC New target'], 16.01, comparison_type='asin')
        WFHub._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)
        
        STEP_17 = """
            STEP 17 : Close the text editor > Right click on 'C9959726_HOLD' > Select 'Edit'
        """
        WFHub._utils.validate_and_get_webdriver_object_using_locator(Application_menu, "Application menu").click()
        WFHub.ContextMenu.select('Close')
        WFHub.Wf_Texteditor._utils.switch_to_main_window()
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S31921")
        WFHub.Workspaces.ContentArea.right_click_on_file("C9959726_HOLD")
        WFHub.ContextMenu.select('Edit')
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("17", STEP_17)
        
        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify the designer sessions opens without any error
        """
        Designer._core_utils.switch_to_new_window()
        Designer.ResourcesPanel.Fields.Dimensions.verify_items(['CAR01'], 17.01, assert_type='in')
        Designer.ResourcesPanel.Fields.Measures.verify_items(['Retail_Cost'], 17.02, assert_type='notin')
        WFHub._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Close the Designer Session > Right-click on 'C9959726_HOLD' > Select 'Run in new Window'
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S31921")
        WFHub.Workspaces.ContentArea.right_click_on_file("C9959726_HOLD")
        WFHub.ContextMenu.select('Run...->Run in new window')
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify the report displays properly
        """
        Designer._core_utils.switch_to_new_window('Report1')
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Close the report window.
        """
        Designer._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("19", STEP_19)

        STEP_20 = """
            STEP 20 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select('Sign Out')
        WFHub._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : sign in again to clear foccache > Right-click on 'C9959726_HOLD' > Select 'Edit'
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S31921")
        WFHub.Workspaces.ContentArea.right_click_on_file("C9959726_HOLD")
        WFHub.ContextMenu.select('Edit')
        WFHub._utils.capture_screenshot("21", STEP_21)

        STEP_21_EXPECTED = """
            STEP 21 - Expected : Verify the designer sessions opens without any error
        """
        Designer._core_utils.switch_to_new_window()
        Designer.ResourcesPanel.Fields.Dimensions.verify_items(['CAR01'], 21.01, assert_type='in')
        Designer.ResourcesPanel.Fields.Measures.verify_items('Retail_Cost', 21.02, assert_type='notin')
        WFHub._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)

        STEP_22 = """
            STEP 22 : Close the Designer Session > Right-click on 'C9959726_HOLD' > Select 'Run in new Window'
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S31921")
        WFHub.Workspaces.ContentArea.right_click_on_file("C9959726_HOLD")
        WFHub.ContextMenu.select('Run...->Run in new window')
        WFHub._utils.capture_screenshot("22", STEP_22)

        STEP_22_EXPECTED = """
            STEP 22 - Expected : Verify the report displays properly
        """
        Designer._core_utils.switch_to_new_window()
        # WFHub._utils.wait_for_page_loads(5)
        # run_object = WFHub._utils.validate_and_get_webdriver_object_using_locator(Run_window_content1, 'Run_time Content1').text.strip()
        # message = 'Step 18:01: Content verified in run window'
        # WFHub._utils.asequal(run_object,'W GERMANY', message)
        # run_object1 = WFHub._utils.validate_and_get_webdriver_object_using_locator(Run_window_content2, 'Run_time Content1').text.strip()
        # message1 = 'Step 18:02: Content verified in run window'
        # WFHub._utils.asequal(run_object1,'W GERMANY', message1)
        WFHub._utils.capture_screenshot("22 - Expected", STEP_22_EXPECTED, True)

        STEP_23 = """
            STEP 23 : Close the report window.
        """
        Designer._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("23", STEP_23)

        STEP_24 = """
            STEP 24 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select('Sign Out')
        WFHub._utils.capture_screenshot("24", STEP_24)

