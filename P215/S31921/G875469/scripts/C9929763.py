"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 08-November-2021
-------------------------------------------------------------------------------------------"""
from common.wftools.chart import Chart
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9929763_TestClass(BaseTestCase):
    
    def test_C9929763(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        chart = Chart(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        querytree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        cancel_css = "#IbfsOpenFileDialog7_btnCancel"
        document_chart_css = "#canvasContainer"
        document_run_chart_css = "div[id^='MAINTABLE'][id$='fmg']"
        
        STEP_01 = """
            STEP 01 : Create new chart content with CAR using API call:
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP215_S31921%2FG875469%2F&master=ibisamp%2Fcar&tool=chart
        """
        chart.invoke_chart_tool_using_api("ibisamp/car")
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Double click 'COUNTRY' and 'DEALER_COST'.
        """
        chart.double_click_on_datetree_item("COUNTRY", 1)
        chart.wait_for_visible_text(querytree_css, "COUNTRY")
        chart.double_click_on_datetree_item("DEALER_COST", 1)
        chart.wait_for_visible_text(querytree_css, "DEALER_COST")
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Check the fields added to query pane and canvas updated.
        """
        chart.verify_field_listed_under_querytree('Vertical Axis', 'DEALER_COST', 1, msg="Step 02.01")
        chart.verify_field_listed_under_querytree('Horizontal Axis', 'COUNTRY', 1, msg="Step 02.02")
        chart.wait_for_visible_text(chart_css, "DEALER_COST")
        chart.verify_x_axis_label_in_preview(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], msg="Step 02.03 : Verify X axis label")
        chart.verify_x_axis_title_in_preview(['COUNTRY'], msg="Step 02.04: Verify X axis title")
        chart.verify_y_axis_label_in_preview(['0', '10K', '20K', '30K', '40K', '50K', '60K'], msg="Step 02.05: Verify Y axis Label")
        chart.verify_y_axis_title_in_preview(['DEALER_COST'], msg="Step 02.06: Verify Y title")
        chart.verify_number_of_risers(chart_css + " rect", 1, 5, msg = "Step 02.07: Verify Risers count")
        chart.verify_chart_color("pfjTableChart_1 ", "riser!s0!g0!mbar!", "bar_blue", msg = "Step 02.08: Verify chart riser color")
        Designer._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click 'Document' in Design group under Home tab.
        """
        chart.select_ia_ribbon_item('Home', "document")
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Check the Chart is converted to Document without any error.
        """
        chart.wait_for_visible_text(document_chart_css, "DEALER_COST")
        chart.verify_x_axis_label_in_preview(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], parent_css=document_chart_css, msg="Step 03.01: Verify X axis label")
        chart.verify_x_axis_title_in_preview(['COUNTRY'], parent_css=document_chart_css, msg="Step 03.02: Verify X axis title")
        chart.verify_y_axis_label_in_preview(['0', '10K', '20K', '30K', '40K', '50K', '60K'], parent_css=document_chart_css, msg="Step 03.03: Verify Y axis Label")
        chart.verify_y_axis_title_in_preview(['DEALER_COST'], parent_css=document_chart_css, msg="Step 03.04: Verify Y title")
        chart.verify_number_of_risers(document_chart_css + " rect", 1, 5, msg = "Step 03.05: Verify Risers count")
        chart.verify_chart_color("TableChart_1 ", "riser!s0!g0!mbar!", "bar_blue", msg = "Step 03.06: Verify chart riser color")
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click 'Run' in toolbar.
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Check the output.
        """
        chart.wait_for_visible_text(document_run_chart_css, "DEALER_COST")
        chart.verify_x_axis_label_in_run_window(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], parent_css=document_run_chart_css, msg="Step 04.01: Verify X axis label")
        chart.verify_x_axis_title_in_run_window(['COUNTRY'], parent_css=document_run_chart_css, msg="Step 04.02: Verify X axis title")
        chart.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K'], parent_css=document_run_chart_css, msg="Step 04.03: Verify Y axis Label")
        chart.verify_y_axis_title_in_run_window(['DEALER_COST'], parent_css=document_run_chart_css, msg="Step 04.04: Verify Y title")
        chart.verify_number_of_risers(document_run_chart_css + " rect", 1, 5, msg = "Step 04.05: Verify Risers count")
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click 'Save' in toolbar Enter 'C9929763' and Click 'Save' button.
        """
        chart.switch_to_default_content()
        chart.select_ia_toolbar_item("toolbar_save")
        chart.wait_for_visible_text(cancel_css, "Cancel")
        chart.save_file_in_save_dialog("C9929763_base")
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Restored C9929763 fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP215_S31921%2FG875469%2Fc9929763.fex
        """
        chart.edit_fex_using_api_url("P215_S31921/G875470", fex_name="C9929763_base")
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Check 'C9929763' is restored successfully.
        """
        chart.wait_for_visible_text(document_chart_css, "DEALER_COST")
        chart.verify_x_axis_label_in_preview(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], parent_css=document_chart_css, msg="Step 07.01: Verify X axis label")
        chart.verify_x_axis_title_in_preview(['COUNTRY'], parent_css=document_chart_css, msg="Step 07.02: Verify X axis title")
        chart.verify_y_axis_label_in_preview(['0', '10K', '20K', '30K', '40K', '50K', '60K'], parent_css=document_chart_css, msg="Step 07.03: Verify Y axis Label")
        chart.verify_y_axis_title_in_preview(['DEALER_COST'], parent_css=document_chart_css, msg="Step 07.04: Verify Y title")
        chart.verify_number_of_risers(document_chart_css + " rect", 1, 5, msg = "Step 07.05: Verify Risers count")
        chart.verify_chart_color("TableChart_1 ", "riser!s0!g0!mbar!", "bar_blue", msg = "Step 07.06: Verify chart riser color")
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()
        Designer._utils.capture_screenshot("08", STEP_08)