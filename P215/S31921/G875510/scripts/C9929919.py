"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh Ravichandran
Automated On : 12-November-2021
-------------------------------------------------------------------------------------------"""
from common.pages.charts import HtmlContent
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9929919_TestClass(BaseTestCase):
    
    def test_C9929919(self):
        
        """
        TEST CASE OBJECTS
        """
        HtmlContentChart = HtmlContent()
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        option_pop_up = "div[class*='pd-cont-menu-notif-text'] .ibx-label-text"
        ok_button_css = "div[role='alertdialog'] [data-ibx-name*='OK']"
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user
            https://machine.ibi.com:port/alias/designer?is508=false&item=IBFS:/WFC/Repository/P215_S31921/G875510&tool=framework&startlocation=IBFS:/WFC/Repository/P215_S31921/G875510&startUpConditions=%7B%27mode%27%3A%27assemble%27%7D
        """
        Designer.API.invoke_assemble_visualizations(credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Blank template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Blank')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Right-click on the section of the page canvas and select 'Insert section below' option.
        """
        Designer.PageCanvas.Section.right_click(1)
        Designer.ContextMenu.select("Insert section below")
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on container side tab;
            Drag and drop 'Basic' and 'Tab' containers onto the first section of the page canvas.
        """
        Designer.SideBar.Container.click()
        Designer.ResourcesPanel.Containers.drag_to_page_section('Basic', x=30, y=35)
        Designer.ResourcesPanel.Containers.drag_to_page_section('Tab', section_location='top_middle', x=180, y=25)
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Drag and drop 'Carousel' and 'Accordion' containers onto the second section of the page canvas
        """
        Designer._javascript.scrollIntoView(Designer.PageCanvas.Section._get_section_object(2))
        Designer.ResourcesPanel.Containers.drag_to_page_section('Carousel', section_index=2, x=30, y=35)
        Designer.ResourcesPanel.Containers.drag_to_page_section('Accordion', section_index=2, section_location='top_middle', x=160, y=25)
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Multi-select 'Container 1' and 'Container 4' > Uncheck 'Lock Container' under 'Settings' tab from Properties pane
        """
        Designer.PageCanvas.Containers.multi_select_containers(['Container 1'])
        Designer.PropertiesPanel.Settings.ContainerCustomization.LockContainer.uncheck()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that '+' symbol added to the 'Container 1' and 'Container 4', rest of the containers displayed by default
        """
        Designer.PageCanvas.Containers.verify_containers_with_add_content_button(['Container 1', 'Container 4'], '06')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Hover over the '+' symbol in 'Container 1'
        """
        Designer.PageCanvas.Containers.hover_over_add_content_button_in_container("Container 1")
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify it displayed 'Add Content' tooltip
        """
        Designer.PageCanvas.Containers.verify_add_content_tooltip("Container 1", "07")
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click '+' Add content > Navigate to 'Retail Sample' > 'Portal' > 'Test Widgets' > Select 'Blue' content > Click on 'Add' button
        """
        Designer.PageCanvas.Containers.click_on_the_add_content_button_in_container('Container 1')
        Designer.Dialog.Base.wait_for_text("Retail Samples")
        Designer.Dialog.SelectItem.navigate_to_folder_and_select_file("Retail Samples->Portal->Test Widgets", "Blue")
        Designer.Dialog.SelectItem.click_button("Add")
        Designer.Dialog.Base.wait_until_invisible()
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify '+' symbol disappears and 'Blue' content added to the 'Container 1'
        """
        Designer.PageCanvas.Containers.Basic("Blue").switch_to_frame()
        HtmlContentChart.verify_content_background("blue", "08")
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click on the 'Options' button in 'Container 1'
        """
        Designer.PageCanvas.Containers.Basic("Blue").ToolBar.Options.click()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify it displayed 'This feature is only displayed in runtime or in the preview mode'
        """
        Designer._utils.synchronize_until_element_is_visible(option_pop_up, 60)
        msg = "Step 09: Verify pop menu displayed"
        Designer._utils.asequal("This feature is only enabled at runtime or in the preview mode.", Designer._utils.validate_and_get_webdriver_object(option_pop_up, "Options message in preview").text.strip(), msg)
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Right-click on 'Blue' container
        """
        Designer.PageCanvas.Containers.Basic("Blue").right_click()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify the following options are available:
    
            1. Refresh
            2. Edit title
            3. Settings
            4. Format
            5. Duplicate Content
            6. Convert to > Tab/Accordion/Carousel
            7. Delete container
            8. Remove
            9. Replace
        """
        Designer.ContextMenu.verify_options(['Refresh', 'Edit Title', 'Settings', 'Format', 'Duplicate Container', 'Convert to', 'Delete Container', 'Remove', 'Replace'], '10.01')
        Designer.ContextMenu.verify_options(['Tab', 'Accordion', 'Carousel'], '10.02', "Convert to")
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Hover overt 'Convert to' > Select 'Accordion' option
        """
        Designer.ContextMenu.select("Convert to->Accordion")
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify the basic container converted into 'Accordion' container
        """
        Designer.PageCanvas.Containers.Accordion("Blue").verify_areas_title(['Blue'], "11")
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Right-click on 'Blue' container > Select 'Remove' option
        """
        Designer.PageCanvas.Containers.Accordion("Blue").right_click()
        Designer.ContextMenu.select("Remove")
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify the added 'Blue' content gets removed
        """
        Designer.PageCanvas.Containers.Accordion("Blue").verify_areas_title(['Content'], "12")
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click on 'Run in new window' button
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer.RunMode.PageCanvas.wait_for_text("Blue")
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify the page loads without error.
        """
        Designer.RunMode.PageCanvas.Containers.verify_containers_title(['Blue', 'Container 2', 'Container 3', 'Container 4'], "13")
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Hover over the '+' symbol in 'Container 4'
        """
        Designer.RunMode.PageCanvas.Containers.hover_over_add_content_button_in_container("Container 4")
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify it displayed 'Add Content' tooltip
        """
        Designer.RunMode.PageCanvas.Containers.verify_add_content_tooltip("Container 4", "14")
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click '+' Add content in 'Container 4' > Navigate to 'Retail Sample' > 'Portal' >'Test Widgets' > Select 'Yellow' content > Click on 'Add' button
        """
        Designer.RunMode.PageCanvas.Containers.click_on_the_add_content_button_in_container("Container 4")
        Designer.Dialog.Base.wait_for_text("Retail Samples")
        Designer.Dialog.SelectItem.navigate_to_folder_and_select_file("Retail Samples->Portal->Test Widgets", "Yellow")
        Designer.Dialog.SelectItem.click_button("Add")
        Designer.Dialog.Base.wait_until_invisible()
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify '+' symbol disappears and 'Yellow' content added to the 'Container 4'
        """
        Designer.RunMode.PageCanvas.Containers.Accordion("Container 4").switch_to_frame("Yellow")
        HtmlContentChart.verify_content_background("yellow", "15")
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Click on the 'Options' button in 'Container 4'
        """
        Designer.RunMode.PageCanvas.Containers.Accordion("Container 4").ToolBar.Options.click()
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify the following options are available:
    
            1. Refresh
            2. Remove
            3. Replace
        """
        Designer.ContextMenu.verify_options(['Refresh', 'Remove', 'Replace'], "16")
        Designer._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Choose to Replace > Navigate to 'Retail Sample' > 'Portal' > 'Test Widgets' > Select 'Test Widget' content > Click on 'Add' button
        """
        Designer.ContextMenu.select("Replace")
        Designer.Dialog.Base.wait_for_text("Blue", time_out=60)
        Designer.Dialog.SelectItem.click_crumb_item("Workspaces")
        Designer.Dialog.SelectItem.navigate_to_folder_and_select_file("Retail Samples->Portal->Test Widgets", "Test Widget")
        Designer.Dialog.SelectItem.click_button("Add")
        Designer.Dialog.Base.wait_until_invisible()
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify the 'Yellow' content is replaced with 'Test Widget' content and area name is changed into 'Test Widget'
        """
        Designer.RunMode.PageCanvas.Containers.Accordion("Container 4").verify_areas_title(['Test Widget'], "17")
        Designer.RunMode.PageCanvas.Containers.Accordion("Container 4").switch_to_frame("Test Widget")
        HtmlContentChart.verify_content_background('deep_violet', "17")
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Click on the 'Options' button in 'Container 4' > Choose Remove.
        """
        Designer.RunMode.PageCanvas.Containers.Accordion("Container 4").ToolBar.Options.click()
        Designer.ContextMenu.select("Remove")
        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify the added 'Test Widget' content gets removed and area name is changed into 'Area 1'
        """
        Designer.RunMode.PageCanvas.Containers.Accordion("Container 4").verify_areas_title(['Area 1'], "18")
        Designer.RunMode.PageCanvas.Containers.verify_containers_with_add_content_button(['Blue', 'Container 4'], "18")
        Designer._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Close run window
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("19", STEP_19)

        STEP_20 = """
            STEP 20 : Click the 'WebFocus DESIGNER' application button > 'Save As' > Enter 'DF_Page12' > Click 'Save as'
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select("Save As...")
        Designer.Dialog.Base.wait_for_text("Cancel", time_out=30)
        Designer.Dialog.SaveAs.Title.enter_text("DF_Page12_base")
        Designer.Dialog.SaveAs.SaveAsButton.click()
        ok_button_loc = (Designer._By.CSS_SELECTOR, ok_button_css)
        ok_button = Designer._webelement.wait_for_element_text(ok_button_loc, "OK", 2, raise_error=False)
        ok_button and Designer._core_utils.python_left_click(ok_button)
        Designer.Dialog.Base.wait_until_invisible()
        Designer._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : Logout :
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("21", STEP_21)