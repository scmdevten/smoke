"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 28-October-2021
-------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9953188_TestClass(BaseTestCase):
    
    def test_C9953188(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        STEP_01 = """
            STEP 01 : Launch Designer:
            http://machine.ibi.com:port/alias/designer?&master=ibisamp/car&item=IBFS:/WFC/Repository&tool=framework&startlocation=IBFS:/WFC/Repository/P452_S31923/G784931
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='ibisamp/car')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select 'Standard Report' form chart tool picker.
        """
        Designer.ContentPicker.All.select('Standard Report')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Add COUNTRY, DEALER_COST, RETAIL_COST.
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click("COUNTRY")
        Designer.ResourcesPanel.Fields.Measures.double_click("DEALER_COST")
        Designer.ResourcesPanel.Fields.Measures.double_click("RETAIL_COST")
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Right Click on 'DEALER_COST' from query bucket and select 'ConditionalStyling'
        """
        Designer.PropertiesPanel.Settings.Display.Summaries.right_click('DEALER_COST')
        Designer.ContextMenu.select('Conditional Styling')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Verify conditional styling pane appears.
        """
        Designer.VisualizationCanvas.ConditionalStyling.wait_for_text('Conditional', time_out=30)   
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : 
        """
        Designer.VisualizationCanvas.ConditionalStyling.verify_title(['Conditional Styling'], '05')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on conditional statement drop down arrow.
        """
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.click_on_conditional_statement_dropdown()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify fields are listed.
        """
        Designer.VisualizationCanvas.ConditionalStyling.Dropdown.verify_options(['DEALER_COST', 'RETAIL_COST', 'COUNTRY'], '06', click_outside=True)
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on condition dropdown arrow.
        """
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.click_on_condition_dropdown()
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify conditions are listed.
        """
        Designer.VisualizationCanvas.ConditionalStyling.Dropdown.verify_options(['Equal to', 'Not equal to', 'Greater than', 'Less than', 'Greater than or equal to', 'Less than or equal to'], '07', click_outside=True)
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on Field dropdown.
        """
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.click_on_field_or_value_dropdown()
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify Field and Value are listed.
        """
        Designer.VisualizationCanvas.ConditionalStyling.Dropdown.verify_options(['Field', 'Value'], '08')
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Select 'Value'.
        """
        Designer.VisualizationCanvas.ConditionalStyling.Dropdown.select('Value')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Verify enter value textbox is appeared and water mark 'Enter Value' is displayed in it.
        """
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.ValueTextBox.verify_placeholder('Enter value', '10')
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : ![](index.php?/attachments/get/1916879)
            The value field will only allow you to enter a valid number if the field you've selected is a numeric field. You will not be able to enter a negative sign '-' unless it is the first character in the string and only 1st decimal '.' in the string is permitted.
        """
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.ValueTextBox.enter_text("1234.555")
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.ValueTextBox.verify_contains_text("1234.555", "10.01")
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.ValueTextBox.enter_text("Test", clear=True)
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.ValueTextBox.verify_contains_text("", "10.02")
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.ValueTextBox.enter_text("-12484.1542")
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.ValueTextBox.verify_contains_text("-12484.1542", "10.03")
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.ValueTextBox.enter_text("!@#$%^&*()_+<>?|}{}", clear=True)
        Designer.VisualizationCanvas.ConditionalStyling.Conditions.ValueTextBox.verify_contains_text("", "10.04")
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click cancel on 'Conditional Styling' pane.
        """
        Designer.VisualizationCanvas.ConditionalStyling.Buttons.Cancel.click()
        Designer._utils.capture_screenshot("11", STEP_11)
        
        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify Warning dialog is displayed
        """
        Designer.Dialog.Warning.wait_until_visible()
        Designer.Dialog.Warning.verify_title('Warning', '11')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)
        
        STEP_12 = """
            STEP 12 : Click 'OK' on the conditional styling dialog.
        """
        Designer.Dialog.Warning.Ok.click()
        Designer.Dialog.Warning.wait_until_invisible()
        Designer._utils.capture_screenshot("12", STEP_12)
        
        STEP_13 = """
            STEP 13 : Close designer without saving.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select('Close')
        Designer.Dialog.Designer.wait_for_text('Designer')
        Designer.Dialog.Designer.Dont_save.click()
        Designer.Dialog.Designer.wait_until_invisible()
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13 = """
            STEP 13 : Logout WebFOCUS
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("13", STEP_13)
