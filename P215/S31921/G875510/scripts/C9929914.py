"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 10-November-2021
-------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9929914_TestClass(BaseTestCase):
    
    def test_C9929914(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        highlighted_section_css = "div[class*='pd-selection']:not(div[class*='hide'])"
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
    
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
            STEP 03 : Right-click on the default section of the page canvas
        """
        Designer.PageCanvas.Section.right_click(1)
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify the following options should be displayed:
    
            1. Settings
            2. Format
            3. Delete Section (By default disabled)
            4. Insert section above
            5. Insert section below
        """
        Designer.ContextMenu.verify_options(['Settings', 'Format', 'Delete section', 'Insert section above', 'Insert section below'], "03.01")
        Designer.ContextMenu.verify_disabled_options(['Delete section'], "03.02")
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on 'Insert section below' option
        """
        Designer.ContextMenu.select("Insert section below")
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify a new section is inserted below on the old section of the canvas
        """
        Designer.PageCanvas.Section.verify_number_of_sections(2, "04.01")
        section_obj = Designer.PageCanvas.Section._get_section_object()
        msg = "Step 04.02: Verify section added below"
        Designer._utils.asequal(len(Designer._utils.validate_and_get_webdriver_objects(highlighted_section_css, "Section highlight", parent_object=section_obj)), 4, msg)
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Right-click on the default section of the page canvas > Click on 'Insert section above' option
        """
        Designer.PageCanvas.Section.right_click(1)
        Designer.ContextMenu.select('Insert section above')
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify a new section is inserted above on the old section of the canvas
        """
        Designer.PageCanvas.Section.verify_number_of_sections(3, '05.01')
        section_obj = Designer.PageCanvas.Section._get_section_object(2)
        msg = "Step 05.02: Verify section added above"
        Designer._utils.asequal(len(Designer._utils.validate_and_get_webdriver_objects(highlighted_section_css, "Section highlight", parent_object=section_obj)), 4, msg)
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on the 'Container' button from the sidebar
        """
        Designer.SideBar.Container.click()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify the following containers same as below:
        """
        Designer.ResourcesPanel.Containers.verify_containers(['Basic', 'Tab', 'Carousel', 'Accordion', 'Grid', 'Panel group', 'Link tile', 'Explorer'], "06")
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Drag and drop 'Basic' and 'Tab' containers one by one into the first section of the page canvas.
        """
        Designer._javascript.scrollIntoView(Designer.PageCanvas.Section._get_section_object(1))
        Designer.ResourcesPanel.Containers.drag_to_page_section_and_verify_drop_color('Basic', "07.01", x=30, y=25)
        Designer._utils.capture_screenshot("07", STEP_07)
     
        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify that while dragging, we can see the blue filled outline in the canvas
        """
        Designer.ResourcesPanel.Containers.drag_to_page_section_and_verify_drop_color('Tab', "07.02", section_location='top_middle', x=160, y=25)
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Drag and drop 'Carousel' and 'Accordion' containers one by one into the second section of the page canvas
        """
        Designer._javascript.scrollIntoView(Designer.PageCanvas.Section._get_section_object(2))
        Designer.ResourcesPanel.Containers.drag_to_page_section('Carousel', section_index=2, x=30, y=25)
        Designer.ResourcesPanel.Containers.drag_to_page_section('Accordion', section_index=2, section_location='top_middle', x=160, y=25)
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that two containers (Container 3 and Container 4) are available in the second section of the canvas
        """
        Designer.PageCanvas.Section.verify_containers_in_section(['Container 3', 'Container 4'], 2, '08.01')
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Drag and drop 'Grid' and 'Link Tile' containers into the third section of the page canvas
        """
        Designer._javascript.scrollIntoView(Designer.PageCanvas.Section._get_section_object(3))
        Designer.ResourcesPanel.Containers.drag_to_page_section('Grid', section_index=3, x=30, y=25)
        Designer.ResourcesPanel.Containers.drag_to_page_section('Link tile', section_index=3, section_location='top_middle', x=160, y=25)
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify that two containers (Container 5 and Container 6) available in the third section of the canvas
        """
        Designer.PageCanvas.Section.verify_containers_in_section(['Container 5'], 3, '09.01')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click on 'Run in  new window'.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer.RunMode.PageCanvas.wait_for_text("Container 1", 120)
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify that 'Container 1' (Basic) and 'Container 2' (Tab) are available in the first section of the canvas and 'Container 3' (Carousel) and 'Container 4' (Accordion) available in the second section of the canvas
        """
        Designer.RunMode.PageCanvas.Section.verify_containers_in_section(['Container 1', 'Container 2'], 1, '10.01')
        Designer.RunMode.PageCanvas.Section.verify_containers_in_section(['Container 3', 'Container 4'], 2, '10.02')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Scroll down to see the third section of the container
        """
        Designer._javascript.scrollIntoView(Designer.RunMode.PageCanvas.Section._get_section_object(2))
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify that 'Container 5' (Grid) and 'Container 6' (Link Tile) are available in the third section of the canvas
        """
        Designer.RunMode.PageCanvas.Section.verify_containers_in_section(['Container 5'], 3, '11.01')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Close the run window
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Click Save button > Enter title as 'DF_Page7' > Click 'Save'
        """
        Designer.ToolBar.save('DF_Page7')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Logout :
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Edit the saved DF_Page using below API URL
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875510/df_page7&startlocation=IBFS:/WFC/Repository
        """
        Designer.API.edit_page('DF_Page7', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify the following DF_Page7 opens successfully with the three sections along with those containers
        """
        Designer.PageCanvas.Section.verify_containers_in_section(['Container 1', 'Container 2'], 1, '15.01')
        Designer.PageCanvas.Section.verify_containers_in_section(['Container 3', 'Container 4'], 2, '15.02')
        Designer._javascript.scrollIntoView(Designer.PageCanvas.Section._get_section_object(3))
        Designer.PageCanvas.Section.verify_containers_in_section(['Container 5'], 3, '15.03')
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Logout :
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("16", STEP_16)