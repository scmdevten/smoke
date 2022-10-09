"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 26-October-2021
-------------------------------------------------------------------------------------------"""
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage
from common.locators.designer.dialog import AddParameterFieldList as locators

class C9953583_TestClass(BaseTestCase):
    
    def test_C9953583(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        STEP_01 = """
            STEP 01 : Launch Designer:
            http://machine.ibi.com:port/alias/designer?&master=ibisamp/car&item=IBFS:/WFC/Repository&tool=framework&startlocation=IBFS:/WFC/Repository/P452_S31923/G879826
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='ibisamp/car')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on '+ Add Parameter Field List'
        """ 
        Designer.PropertiesPanel.Settings.Filters.AddParameterFieldList.click()
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Select 'Vertical Y-Axis' from Control Type.
        """
        Designer.Dialog.AddParameterFieldList.wait_for_text('Add')
        Designer.Dialog.AddParameterFieldList.BucketType.click()
        Designer.Dialog.AddParameterFieldList.BucketTypeDropdown.select('Vertical - Y Axis')
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : 
        """
        bucket_placeholder_obj = Designer._utils.validate_and_get_webdriver_object_using_locator(locators.bucket_type_placeholder, 'Bucket type Placeholder')
        actual_value = bucket_placeholder_obj.get_attribute('aria-label').strip()
        msg = "Step 03: Verify bucket type choosen value"
        Designer._utils.asequal("Vertical - Y Axis", actual_value, msg)
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click Save.
        """
        Designer.Dialog.AddParameterFieldList.Save.click()
        Designer.Dialog.AddParameterFieldList.wait_until_invisible()
        #Adding another parameter field list for verify delete functionality
        Designer.PropertiesPanel.Settings.Filters.AddParameterFieldList.click()
        Designer.Dialog.AddParameterFieldList.wait_for_text('Add')
        Designer.Dialog.AddParameterFieldList.BucketType.click()
        Designer.Dialog.AddParameterFieldList.BucketTypeDropdown.select('Vertical - Y Axis')
        Designer.Dialog.AddParameterFieldList.Save.click()
        Designer.Dialog.AddParameterFieldList.wait_until_invisible()
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click on ellipsis from 'Parameter List Name 1'.
        """
        Designer.PropertiesPanel.Settings.Filters.AddParameterFieldListBuckets('Parameter List Name 1').click_on_bucket_ellipsis()
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify parameter bucket context menu. 'Edit', 'Clear', 'Delete'.
        """
        Designer.ContextMenu.verify_options(['Edit', 'Clear', 'Delete'], '05')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Drag and drop 'DEALER_COST' and 'RETAIL_COST' underneath 'DEALER_COST' to Parameter List Name 1.
        """
        Designer._javascript.scrollIntoView(Designer.PropertiesPanel.Settings.Filters.AddParameterFieldListBuckets('Parameter List Name 1')._get_bucket_object())
        Designer.ResourcesPanel.Fields.Dimensions.double_click("ORIGIN->COUNTRY")
        Designer.VisualizationCanvas.Bar.wait_for_text('COUNTRY')
        Designer.ResourcesPanel.Fields.Measures.drag_to_parameter_field_bucket('ORIGIN->COMP->CARREC->BODY->DEALER_COST', '1')
        Designer.VisualizationCanvas.Bar.wait_for_text('DEALER_COST')
        Designer.ResourcesPanel.Fields.Measures.drag_to_parameter_field_bucket('ORIGIN->COMP->CARREC->BODY->RETAIL_COST', '1', 'DEALER_COST', target_obj_loc="bottom_middle")
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify parameter bucket and chart canvas.
        """
        Designer.PropertiesPanel.Settings.Filters.AddParameterFieldListBuckets('Parameter List Name 1').verify_available_fields(['DEALER_COST', 'RETAIL_COST'], '06.00')
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['COUNTRY'], '06.01')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '06.02')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['DEALER_COST'], '06.03')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '06.04')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(5, '06.05')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (3, 'bar_blue')], '06.06')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on ellipsis icon from 'Parameter List Name 1' -> select 'Clear'.
        """
        Designer.PropertiesPanel.Settings.Filters.AddParameterFieldListBuckets('Parameter List Name 1').click_on_bucket_ellipsis()
        Designer.ContextMenu.select('Clear')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify parameter bucket is empty and canvas chart output not shown y-axis DEALER_COST.
        """
        time.sleep(15)
        Designer.VisualizationCanvas.Bar.wait_for_text('COUNTRY')
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['COUNTRY'], '07.01')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '07.02')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title([], '07.03')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels([], '07.04')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(5, '07.05')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (3, 'bar_blue')], '07.06')
        Designer.PropertiesPanel.Settings.Filters.AddParameterFieldListBuckets('Parameter List Name 1').verify_available_fields([], '07.07')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Drag and drop 'DEALER_COST' to 'Parameter List Name 1'.
        """
        Designer.ResourcesPanel.Fields.Measures.drag_to_parameter_field_bucket('ORIGIN->COMP->CARREC->BODY->DEALER_COST', 'Parameter List Name 1')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click on ellipsis from 'Parameter List Name 1' -> select 'Delete'.
        """
        Designer.PropertiesPanel.Settings.Filters.AddParameterFieldListBuckets('Parameter List Name 1').click_on_bucket_ellipsis()
        Designer.ContextMenu.select('Delete')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify parameter bucket deleted and chart canvas output has only 'COUNTRY'.
        """
        time.sleep(10)
        Designer.VisualizationCanvas.Bar.wait_for_text('COUNTRY')
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['COUNTRY'], '09.01')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '09.02')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title([], '09.03')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels([], '09.04')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(5, '09.05')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (3, 'bar_blue')], '09.06')
        Designer.PropertiesPanel.Settings.Filters.verify_parameter_field_buckets(['Parameter List Name 1'], '09.07', assert_type='notin')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Close Designer without saving.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select('Close')
        Designer.Dialog.Designer.wait_until_visible()
        Designer.Dialog.Designer.Dont_save.click()
        Designer.Dialog.Designer.wait_until_invisible()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Logout WebFOCUS.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("11", STEP_11)