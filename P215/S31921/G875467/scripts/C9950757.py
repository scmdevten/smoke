"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 17-November-2021
-------------------------------------------------------------------------------------------"""
import time
from common.wftools.report import Report
from common.lib.basetestcase import BaseTestCase
from common.pages.charts import Pie, TreeMap, Bar
from common.wftools.designer import Designer as DesignerPage

class C9950757_TestClass(BaseTestCase):
    
    def test_C9950757(self):
        
        """
        TEST CASE OBJECTS
        """
        PieChart = Pie()
        BarChart = Bar()
        TreeMapChart = TreeMap() 
        Designer = DesignerPage()
        HtmlReport=Report(Designer._driver)
        
        """
        TEST CASE VAIABLES
        """
        content_path = "Retail Samples->Portal->Small Widgets->Category Sales"
        content_path2 = "Small Widgets->Portal->InfoApps->Maps->US Sales Map"
        chart1 = "iframe#chart1"
        chart2 = "iframe#chart2"
        report = "iframe#report1"
        map_path = "div#emfobject1 g#Stores_layer path"
        TABLE_CSS="table"
        file_name = "C9927843"
        data_set_01 =  file_name + '_DataSet01.xlsx'
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
            https://machine.ibi.com:port/alias/designer?is508=false&item=IBFS:/WFC/Repository/P215_S31921/G875467&tool=framework&startlocation=IBFS:/WFC/Repository/P215_S31921/G875467&startUpConditions=%7B%27mode%27%3A%27assemble%27%7D
        """
        Designer.API.invoke_assemble_visualizations(credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select 'Workbench' template
        """ 
        Designer.Dialog.ChooseTemplate.Common.select('Workbench')  
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify that 'Workbench' template is added to the page canvas same as below:
        """
        Designer._utils.wait_for_page_loads(60)
        Designer.PageCanvas.Containers.verify_containers_title(['Workspace', 'Output'], '02')
        Designer._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Inside the Workbench container > Under 'Workspaces' tree > Navigate to 'Retail Samples' > 'Portals' > 'Small Widgets' folder > Double-click on 'Category Sales'
        """
        Designer.PageCanvas.Containers.Workspace('Workspace').Content.double_click(content_path)
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that nothing happens in the output container
        """
        Designer.PageCanvas.Containers.Tab("Output").verify_tabs_title(['Tab 1'], "03")
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on 'Run in new window' button
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer.RunMode.PageCanvas.wait_for_text("Page", time_out=120)
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Inside the Workbench container > Under 'Workspaces' tree > Navigate to 'Retail Samples' > 'Portals' > 'Small Widgets' folder > Double-click on 'Category Sales'
        """
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.double_click(content_path)
        Designer._utils.wait_for_page_loads(30)
        Designer.RunMode.PageCanvas.Containers.Tab("Output").switch_to_frame()
        PieChart.wait_for_text('Product Category', 120)
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the following output
        """
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '05.01')
        PieChart.verify_legend_title(['Product Category'], '05.02')
        PieChart.verify_number_of_risers(7, '05.03')
        PieChart.verify_total_lables(['1.1B'], '05.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '05.05')
        PieChart.verify_pie_labels(['Revenue'], '05.06')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Under 'Workspaces' tree > In the search box > Enter 'Reven' in the content area
        """
        Designer.RunMode.PageCanvas.Containers.Workspace("Workspace").Content.SearchTextBox.enter_text("Reven")
        time.sleep(10)
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that search is working and it displayed the word contains 'Reven' in the content area same as below
        """
        Designer.RunMode.PageCanvas.Containers.Workspace("Workspace").Content.SearchTextBox.verify_text('Reven', "06.01")
        Designer.RunMode.PageCanvas.Containers.Workspace("Workspace").Content.verify_available_items(['Small Widgets', 'Average Cost vs Revenue Scatter', 'Revenue Product Bar', 'Revenue Region Bar'], "06.02")
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Double-click on 'Revenue Product Bar'
        """
        Designer.RunMode.PageCanvas.Containers.Workspace("Workspace").Content.double_click("Revenue Product Bar")
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the following output
        """
        Designer.RunMode.PageCanvas.Containers.Tab("Output").switch_to_frame()
        BarChart.wait_for_text("Product Category")
        BarChart.verify_xaxis_title(['Product Category'], "07.01")
        BarChart.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], "07.02")
        BarChart.verify_yaxis_title(['Revenue'], "07.03")
        BarChart.verify_yaxis_labels(['0%', '20%', '40%', '60%', '80%', '100%'], "07.04")
        BarChart.verify_legend_title(['Store Business Region'], "07.05")
        BarChart.verify_legend_labels(['EMEA', 'North America', 'Oceania', 'South America'], "07.06")
        BarChart.verify_number_of_risers(28, "07.07")
        BarChart.verify_riser_color([(1, 'bar_blue')], '07.08')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on 'Filter' button in the page toolbar
        """
        Designer.RunMode.PageCanvas.Heading.ShowFilter.click()
        Designer.Dialog.FilterGrid.wait_for_text("Selections")
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that modal filter dialog appears
        """
        Designer.Dialog.FilterGrid.Selections.verify_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], "08.01")
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click on 'Category' drop-down > Select 'Camcorder' and Click on 'Region' drop-down > Select 'EMEA' > Click on 'Submit' button
        """
        Designer.Dialog.FilterGrid.Selections.Control("Category:").click(location='middle')
        Designer.Dialog.FilterGrid.Selections.Dropdown.select("Camcorder")
        Designer.Dialog.FilterGrid.Selections.Control("Region:").click(location='middle')
        time.sleep(5)
        Designer.Dialog.FilterGrid.Selections.Dropdown.select("EMEA")
        Designer.Dialog.FilterGrid.Submit.click()
        Designer.Dialog.FilterGrid.wait_until_invisible()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify that modal filter dialog disappears and filters applied to the output container for the 'Revenue Product Bar' content
        """
        Designer.RunMode.PageCanvas.Containers.Tab("Output").switch_to_frame()
        BarChart.wait_for_text("Product Category")
        BarChart.verify_xaxis_title(['Product Category'], "09.01")
        BarChart.verify_xaxis_labels(['Camcorder'], "09.02")
        BarChart.verify_yaxis_title(['Revenue'], "09.03")
        BarChart.verify_yaxis_labels(['0%', '20%', '40%', '60%', '80%', '100%'], "09.04")
        BarChart.verify_legend_title(['Store Business Region'], "09.05")
        BarChart.verify_legend_labels(['EMEA'], "09.06")
        BarChart.verify_number_of_risers(1, "09.07")
        BarChart.verify_riser_color([(1, 'bar_blue')], '09.08')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Close run window
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify that 'Workbench' template is displayed by default
        """
        Designer.PageCanvas.Containers.Tab("Output").verify_tabs_title(['Tab 1'], "10")
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click Save button > Enter title as 'DF_Workbench' > Click 'Save'
        """
        Designer.ToolBar.save('DF_Workbench')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Logout :
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Edit the saved DF_Workbench using below API URL
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875467/df_workbench&startlocation=IBFS:/WFC/Repository
        """
        Designer.API.edit_page('DF_Workbench', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify the following output
        """
        Designer.PageCanvas.Containers.Tab("Output").verify_tabs_title(['Tab 1'], "13")
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Logout :
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Run designer using API:
            https://machine.ibi.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P215_S31921/G875467&BIP_item=df_workbench
        """
        Designer.API.run_page('DF_Workbench', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Inside the Workbench container > Under 'Workspaces' tree > Navigate to 'Retail Samples' > 'Portals' > 'Small Widgets' folder
        """
        Designer.RunMode.PageCanvas.Containers.Workspace("Workspace").Content.select(content_path)
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Right-click on 'Discount by Region'
        """
        Designer.RunMode.PageCanvas.Containers.Workspace("Workspace").Content.right_click("Discount by Region")
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify that following context menus are displayed
        """ 
        Designer.ContextMenu.verify_options(['Run', 'Run In New Tab'], "17")
        Designer._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Click on 'Run'
        """
        Designer.ContextMenu.select("Run")
        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify that 'Discount by Region' run in the output container
        """
        Designer.RunMode.PageCanvas.Containers.Tab("Output").switch_to_frame()
        TreeMapChart.wait_for_text('Sale Quarter', 120)
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '18.01')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '18.02')
        TreeMapChart.verify_number_of_risers(16, '18.03')
        TreeMapChart.verify_riser_color([(10, 'French_Pass')], '18.04')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Navigate to 'Retail Samples' > 'InfoApps' > 'Maps' > Right-click on 'US Sales Map' > Select 'Run In New Tab'
        """
        Designer.RunMode.PageCanvas.Containers.Workspace("Workspace").Content.right_click(content_path2)
        Designer.ContextMenu.select("Run In New Tab")
        Designer._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify that 'US Sales Map' run in a new tab
        """
        Designer.RunMode.PageCanvas.Containers.Tab("Output").switch_to_frame()
        Designer._core_utils.switch_to_frame(frame_css=chart1)
        BarChart.wait_for_text("Revenue")
        BarChart.verify_xaxis_labels(['New York', 'Houston', 'Chicago', 'Detroit', 'Atlanta'], "19.01")
        BarChart.verify_yaxis_labels(['0', '8M', '16M', '24M', '32M'], "19.02")
        BarChart.verify_number_of_risers(5, "19.03")
        BarChart.verify_riser_color([(1, 'elf_green')], '19.04')
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Tab("Output").switch_to_frame()
        Designer._core_utils.switch_to_frame(frame_css=chart2)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '19.05')
        PieChart.verify_legend_title(['Product Category'], '19.06')
        PieChart.verify_number_of_risers(7, '19.07')
        PieChart.verify_total_lables(['151.8M'], '19.08')
        PieChart.verify_riser_color([(1, 'bar_blue')], '19.09')
        PieChart.verify_pie_labels(['Gross Profit'], '19.10')
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Tab("Output").switch_to_frame()
        msg = "Step 19.11: Verify path loaded properly"
        map_path_obj = Designer._utils.validate_and_get_webdriver_objects(map_path, "Map Path")
        actual_map_obj = [map_path for map_path in map_path_obj if map_path.is_displayed()]
        Designer._utils.asequal(44, len(actual_map_obj), msg)
        region_label_css="#checkbox1 label"
        region_labels=Designer._utils.validate_and_get_webdriver_objects(region_label_css, 'Region control labels')
        actual_list=[el.text.strip() for el in region_labels]
        expected_list=['East', 'Midwest', 'Northeast', 'South', 'Southeast', 'West']
        Designer._utils.as_List_equal(actual_list,expected_list,'Step 19.12: Verify Region control labels in esri map')
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Tab("Output").switch_to_frame()
        Designer._core_utils.switch_to_frame(frame_css=report)
        # HtmlReport.create_table_data_set(TABLE_CSS, data_set_01)
        HtmlReport.verify_table_data_set(TABLE_CSS, data_set_01, "Step 19.13: Verify report data at runtime.")
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)
        
        STEP_20 = """
            STEP 20 : Switch to 'Discount by Region' > Click on 'Options' button
        """
        Designer.RunMode.PageCanvas.Containers.Tab("Output").select("Discount by Region")
        Designer.RunMode.PageCanvas.Containers.Tab("Output").ToolBar.Options.click()
        Designer._utils.capture_screenshot("20", STEP_20)

        STEP_20_EXPECTED = """
            STEP 20 - Expected : Verify that it displayed 'Refresh' and 'Delete Tab' options
        """
        Designer.ContextMenu.verify_options(['Refresh', 'Delete Tab'], "20")
        Designer._utils.capture_screenshot("20 - Expected", STEP_20_EXPECTED, True)

        STEP_21 = """
            STEP 21 : Click on 'Delete Tab'
        """
        Designer.ContextMenu.select("Delete Tab")
        Designer._utils.capture_screenshot("21", STEP_21)

        STEP_21_EXPECTED = """
            STEP 21 - Expected : Verify that 'Discount by Region' tab gets deleted and 'US Sales Map' content only available
        """
        Designer.RunMode.PageCanvas.Containers.Tab("Output").verify_tabs_title(['US Sales Map'], "21")
        Designer._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)

        STEP_22 = """
            STEP 22 : Click on 'Options' button
        """
        Designer.RunMode.PageCanvas.Containers.Tab("Output").ToolBar.Options.click()
        Designer._utils.capture_screenshot("22", STEP_22)

        STEP_22_EXPECTED = """
            STEP 22 - Expected : Verify that it displayed only 'Refresh' option
        """
        Designer.ContextMenu.verify_options(['Refresh'], "22")
        Designer._utils.capture_screenshot("22 - Expected", STEP_22_EXPECTED, True)

        STEP_23 = """
            STEP 23 : Logout :
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("23", STEP_23)