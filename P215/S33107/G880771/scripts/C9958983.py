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
import pyautogui

class C9958983_TestClass(BaseTestCase):
    
    def test_C9958983(self):
        
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
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Worksapces')
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S33107->G880402")
        WFHub._utils.capture_screenshot("02", STEP_02)
        
        STEP_03 = """
            STEP 03 : Run C9958983 portal
        """
        WFHub.Workspaces.ContentArea.right_click_on_folder("C9958983")
        WFHub.ContextMenu.select("Run")
        core_utils.switch_to_new_window() 
        WFHub._utils.capture_screenshot("03", STEP_03)
        
        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify portal runs successfully and contents are visible without error.
        """        
        utils.verify_current_tab_name("C9958983","Step 03.01 Verify portal runs successfully ") 
        Designer.RunMode.PageCanvas.Containers.Tab('Container 5').verify_tabs_title(['Regional Sales Trend', 'Category Sales'], '03.02a')
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 8').verify_no_of_sliders(2, '03.02b')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 13').verify_areas_title(['Bar - Highest Margin Products', 'Arc - Sales by Region'], '03.02c')
        Designer.RunMode.PageCanvas.Containers.Basic('Container 15')
        Designer.RunMode.PageCanvas.Containers.LinkTile()
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)
        
        STEP_04 = """
            STEP 04 : Click on Category Sales tab, Arc - Sales by Region area and second slide in Container 8.
        """
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 5').select('Category Sales')
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 13').expand_area('Arc - Sales by Region')
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 8').click_on_next_slide(2)
        WFHub._utils.capture_screenshot("04", STEP_04)
        
        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify contents are visible.
        """        
        Designer.RunMode.PageCanvas.Containers.Tab('Container 5').verify_tabs_title(['Regional Sales Trend', 'Category Sales'], '04.01a')
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 8').verify_no_of_sliders(2, '04.01b')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 13').verify_areas_title(['Bar - Highest Margin Products', 'Arc - Sales by Region'], '04.01c')
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)
        
        STEP_05 = """
            STEP 05 : Click on Blue link tile content in the second row.
        """
        Designer._core_utils.switch_to_default_content()
        link_tile_obj = utils.validate_and_get_webdriver_object(".grid-stack-item-content [data-ibx-type='pdContent'][data-ibxp-type='link_tile']", 'link tile widget')
        core_utils.left_click(link_tile_obj)       
        core_utils.switch_to_frame(frame_css="[data-ibx-type='ibxIFrame'] [class='ibx-iframe-frame']")
        WFHub._utils.capture_screenshot("05", STEP_05)
        
        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify contents are visible.
        """
        Designer._utils.wait_for_page_loads(60)
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_total_lables(['1.1B'], '05.01')
        PieChart.verify_riser_color([(1, 'bar_blue')], '05.02')
        PieChart.verify_pie_labels(['Revenue'], '05.03')
        Designer._core_utils.switch_to_default_content()
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)
        
        STEP_06 = """
            STEP 06 : Close the viewer window.
        """
        link_tile_obj = utils.validate_and_get_webdriver_object("div[title='Close']", 'close button')
        core_utils.left_click(link_tile_obj)    
        WFHub._utils.capture_screenshot("06", STEP_06)
        
        STEP_07 = """
            STEP 07 : Mouse hover over blue link tile widget.
        """
        Designer._core_utils.switch_to_default_content()
        pyautogui.moveTo(1400, 800)
        WFHub._utils.capture_screenshot("07", STEP_07)
        
        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify tooltip is visible.
        """        
        tooltip_css = "[data-ibxp-tile-tooltip-text='Link tile background']"
        tooltip_visible = self.driver.find_element_by_css_selector(tooltip_css).is_displayed()
        Designer._utils.asequal(True, tooltip_visible, 'Step 07.01 : Verify tooltip is visible. for LinkTile')
        WFHub._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)
        
        STEP_08 = """
            STEP 08 : Close the portal.
        """        
        core_utils.switch_to_previous_window()
        WFHub.Workspaces.switch_to_default_content()
        WFHub._utils.capture_screenshot("08", STEP_08)
        
        STEP_09 = """
            STEP 09 : Sign out WF.
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("09", STEP_09)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        