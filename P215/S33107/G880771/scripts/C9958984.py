"""-------------------------------------------------------------------------------------------
Author Name  : Khushboo Parikh
Automated On : 11-July-2022
-------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub 
from common.wftools.designer import Designer as DesignerPage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.charts import Pie
from common.locators.designer import page_canvas as Locator
from PIL.Image import core

class C9958984_TestClass(BaseTestCase):
    
    def test_C9958984(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        Designer = DesignerPage()
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        PieChart = Pie()
        
        """
        TEST CASE VAIABLES
        """
        
        STEP_01 = """
            STEP 01 : Login to WF as developer user.
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Workspaces;  Navigate to P215_S33107/G880402 folder.
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S33107->G880402")
        WFHub._utils.capture_screenshot("02", STEP_02)
        
        STEP_03 = """
            STEP 03 : Run C9958984 portal
        """
        WFHub.Workspaces.ContentArea.right_click_on_folder("C9958984")
        WFHub.ContextMenu.select("Run")
        core_utils.switch_to_new_window() 
        WFHub._utils.capture_screenshot("03", STEP_03)
        
        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify portal runs successfully and contents are visible without error.
        """      
        Designer._utils.wait_for_page_loads(60)
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 120)  
        Designer.RunMode.PageCanvas.wait_for_text("Category Sales", 120)  
        utils.verify_current_tab_name("C9958984","Step 03.01 Verify portal runs successfully ") 
        Designer.RunMode.PageCanvas.Containers.verify_containers_title(['Category Sales', 'Revenue Product Bar', 'Blue', 'Revenue Region Bar'], '03.02')
        Designer.RunMode.PageCanvas.Heading.verify_heading("Page Heading", '03.03')
        Designer.RunMode.PageCanvas.Containers.verify_number_of_containers(5, '03.04')        
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)
        
        STEP_04 = """
            STEP 04 : Click on the second page.
        """
        # Designer._core_utils.switch_to_default_content()        
        link_tile_obj = self.driver.find_element_by_xpath("//div[@data-ibx-type='ibxAccordionPane'][@data-ibxp-single-click-expand='true']/div[3]")
        print(link_tile_obj)
        core_utils.left_click(link_tile_obj)   
       
        # Designer._utils.wait_for_page_loads(180)
        # Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        WFHub._utils.capture_screenshot("04", STEP_04)
        
        STEP_04_EXPECTED = """
            STEP 04 - Expected : Scroll down and verify the contents are visible without error.
        """      
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.wait_for_text("Category Sales", 120)  
        Designer.RunMode.PageCanvas.Containers.verify_containers_title(['Category Sales', 'Revenue Product Bar', 'Blue', 'Revenue Region Bar'], '04.01')
        Designer.RunMode.PageCanvas.Heading.verify_heading("Page Heading", '04.02')
        Designer.RunMode.PageCanvas.Containers.verify_number_of_containers(25, '04.03')
        Designer._javascript.scrollIntoView(Designer.RunMode.PageCanvas.Section._get_section_object(2))
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)
        
        STEP_05 = """
            STEP 05 : Click on the second tab, area and slide in all the containers.
        """        
        # Designer._core_utils.switch_to_default_content()
        # Designer.RunMode.PageCanvas.Containers.Basic("Category Sales").switch_to_frame()
        # Designer.RunMode.PageCanvas.Containers.Basic("Category Sales (Copy)").switch_to_frame()
        #
        # Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 3').select('Regional Sales Trend')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 3').switch_to_frame('Regional Sales Trend')
        
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 3 (Copy)').select('Regional Sales Trend (Copy)')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 3 (Copy)').switch_to_frame('Regional Sales Trend (Copy)')
        
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').click_on_next_slide(2)
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5 (Copy)').click_on_next_slide(2)
        
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 7').expand_area('Silver')
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 7 (Copy)').expand_area('Silver (Copy)')
        
        WFHub._utils.capture_screenshot("05", STEP_05)
        
        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify contents are visible without error.
        """        
        Designer.RunMode.PageCanvas.Containers.verify_containers_title(['Category Sales', 'Revenue Product Bar', 'Blue', 'Revenue Region Bar'], '03.01')
        Designer.RunMode.PageCanvas.Heading.verify_heading("Page Heading", '03.03')
        Designer.RunMode.PageCanvas.Containers.verify_number_of_containers(25, '03.02')
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)
        
        
        