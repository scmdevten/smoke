"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 01-November-2021
-------------------------------------------------------------------------------------------"""
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9949018_TestClass(BaseTestCase):
    
    def test_C9949018(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        """
        TEST CASE VARIABLES
        """
        chart_perview = "div[id*='chartpreview']"
        chart_preview2 = "#dummy_id"
        
        STEP_01 = """
            STEP 01 : Launch Designer:
    
            http://machine.ibi.com:port/alias/designer?&master=qawfretail/wf_retail_lite&item=IBFS:/WFC/Repository&tool=framework&startlocation=IBFS:/WFC/Repository/P452_S31923/G784931
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='retail_samples/wf_retail_lite')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select the 'Standard Report' template
        """
        Designer.ContentPicker.All.select('Standard Report')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on the Output Format menu > Select PDF
        """
        Designer.VisualizationToolBar.OutputFormat.button.click()
        Designer.VisualizationToolBar.OutputFormat.select_output_format('PDF')
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : 
        """
        Designer.VisualizationToolBar.OutputFormat.button.verify_text('Output Format: PDF', '03')
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Verify Report buckets and canvas template after selecting paginated canvas output format, PDF.
        """
        Designer.PropertiesPanel.Settings.Display.verify_available_buckets(['Rows', 'Column Groups', 'Summaries'], '04.01')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : 
        """
        Designer.VisualizationCanvas.verify_default_canvas(['Drop measures & dimensions here'], '04.02')
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Double click 'Model' and 'Cost of Goods'
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click("Dimensions->Product->Model")
        Designer.ResourcesPanel.Fields.Measures.double_click("Cost of Goods")
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify report Canvas displays vertical scrollbars
        """
        Designer._utils.asequal(True, Designer._javascript.check_element_has_vertical_scrollbar(Designer._utils.validate_and_get_webdriver_object(chart_perview, 'Canvas')), 'Step 05: Verify Vertical Scrollbar is present')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Drag 'Store Business Sub Region' into the Columns bucket
        """
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_bucket("Dimensions->Store->Store Business Sub Region", "Column Groups")
        Designer._utils.capture_screenshot("06", STEP_06)
        
        STEP_07 = """
            STEP 07 : Click on Format
        """
        Designer.PropertiesPanel.select('Format')
        Designer._utils.capture_screenshot("07", STEP_07)
        
        STEP_08 = """
            STEP 08 : Select 'Output Settings' from General dropdown
        """
        Designer.PropertiesPanel.Format.click_general_dropdown()
        Designer.PropertiesPanel.Format.Dropdown.select('Output Settings')
        Designer._utils.capture_screenshot("08", STEP_08)
        
        STEP_09 = """
            STEP 09 : Select 'A3' from Page Size.
        """
        Designer.PropertiesPanel.Format.PDFPage.click_page_size_dropdown()
        Designer.PropertiesPanel.Format.Dropdown.select('A3')
        Designer._utils.capture_screenshot("09", STEP_09)
        
        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify report Canvas displays vertical scrollbars
        """
        time.sleep(20)
        Designer.VisualizationCanvas.PaginatedCanvas.wait_for_text('Store,Business,Sub Region', time_out=60)
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_canvas_pages(6, '09.01')
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_cavas_data(['Store,Business,Sub Region', 'Africa', 'Asia'], 1, '09.02')
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_cavas_data(['2100', '$234.00', '$89,076.00', '$4,992.00', '$126,438.00', '$118,248.00'], 1, '09.03')
        Designer._utils.asequal(True, Designer._javascript.check_element_has_horizontal_scrollbar(Designer._utils.validate_and_get_webdriver_object(chart_perview, 'Canvas')), 'Step 09.04: Verify Horizontal Scrollbar is present')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click Save > C9949018 > Save
        """
        Designer.ToolBar.save('C9949018')
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Edit the saved FEX:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P452_S31923/G784931/c9949018.fex&startlocation=IBFS:/WFC/Repository/P452_S31923/G784931
        """
        Designer.API.logout()
        Designer.API.edit_fex("C9949018", credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify canvas displays vertical/horizontal scroll bars after restore
        """
        Designer.VisualizationCanvas.PaginatedCanvas.wait_for_text('Store,Business,Sub Region', time_out=60)
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_canvas_pages(6, '11.01')
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_cavas_data(['Store,Business,Sub Region', 'Africa', 'Asia'], 1, '11.02')
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_cavas_data(['2100', '$234.00', '$89,076.00', '$4,992.00', '$126,438.00', '$118,248.00'], 1, '11.03')
        Designer._utils.asequal(True, Designer._javascript.check_element_has_vertical_scrollbar(Designer._utils.validate_and_get_webdriver_object(chart_preview2, 'Canvas')), 'Step 11.04: Verify Vertical Scrollbar is present')
        Designer._utils.asequal(True, Designer._javascript.check_element_has_horizontal_scrollbar(Designer._utils.validate_and_get_webdriver_object(chart_preview2, 'Canvas')), 'Step 11.05: Verify Horizontal Scrollbar is present')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click on the Output Format menu > Select PPTX
        """
        Designer.VisualizationToolBar.OutputFormat.button.click()
        Designer.VisualizationToolBar.OutputFormat.select_output_format('PPTX')
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify canvas remains the same
        """
        Designer.VisualizationCanvas.PaginatedCanvas.wait_for_text('Store,Business,Sub Region', time_out=60)
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_canvas_pages(6, '12.01')
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_cavas_data(['Store,Business,Sub Region', 'Africa', 'Asia'], 1, '12.02')
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_cavas_data(['2100', '$234.00', '$89,076.00', '$4,992.00', '$126,438.00', '$118,248.00'], 1, '12.03')
        Designer._utils.asequal(True, Designer._javascript.check_element_has_vertical_scrollbar(Designer._utils.validate_and_get_webdriver_object(chart_preview2, 'Canvas')), 'Step 12.04: Verify Vertical Scrollbar is present')
        Designer._utils.asequal(True, Designer._javascript.check_element_has_horizontal_scrollbar(Designer._utils.validate_and_get_webdriver_object(chart_preview2, 'Canvas')), 'Step 12.05: Verify Horizontal Scrollbar is present')
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click on the Output Format menu > Select HTML
        """
        Designer.VisualizationToolBar.OutputFormat.button.click()
        Designer.VisualizationToolBar.OutputFormat.select_output_format('HTML')
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify Interactive canvas with vertical/horizontal scroll bars and paging
        """
        Designer.VisualizationCanvas.PaginatedCanvas.wait_for_text('Store,Business,Sub Region', time_out=60)
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_canvas_pages(6, '13.01')
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_cavas_data(['Store,Business,Sub Region', 'Africa', 'Asia'], 1, '13.02')
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_cavas_data(['2100', '$234.00', '$89,076.00', '$4,992.00', '$126,438.00', '$118,248.00'], 1, '13.03')
        Designer._utils.asequal(True, Designer._javascript.check_element_has_vertical_scrollbar(Designer._utils.validate_and_get_webdriver_object(chart_preview2, 'Canvas')), 'Step 13.04: Verify Vertical Scrollbar is present')
        Designer._utils.asequal(True, Designer._javascript.check_element_has_horizontal_scrollbar(Designer._utils.validate_and_get_webdriver_object(chart_preview2, 'Canvas')), 'Step 13.05: Verify Horizontal Scrollbar is present')
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click on the Output Format menu > Select XLSX
        """
        Designer.VisualizationToolBar.OutputFormat.button.click()
        Designer.VisualizationToolBar.OutputFormat.select_output_format('XLSX')
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify Paginated canvas
        """
        Designer.VisualizationCanvas.PaginatedCanvas.wait_for_text('Store,Business,Sub Region', time_out=60)
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_canvas_pages(6, '14.01')
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_cavas_data(['Store,Business,Sub Region', 'Africa', 'Asia'], 1, '14.02')
        Designer.VisualizationCanvas.PaginatedCanvas.verify_paginated_cavas_data(['2100', '$234.00', '$89,076.00', '$4,992.00', '$126,438.00', '$118,248.00'], 1, '14.03')
        Designer._utils.asequal(True, Designer._javascript.check_element_has_vertical_scrollbar(Designer._utils.validate_and_get_webdriver_object(chart_preview2, 'Canvas')), 'Step 14.04: Verify Vertical Scrollbar is present')
        Designer._utils.asequal(True, Designer._javascript.check_element_has_horizontal_scrollbar(Designer._utils.validate_and_get_webdriver_object(chart_preview2, 'Canvas')), 'Step 14.05: Verify Horizontal Scrollbar is present')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Logout and dismiss save prompt:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("15", STEP_15)