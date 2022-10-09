"""-------------------------------------------------------------------------------------------
Author Name  : GRETHINA@TIBCO.COM
Automated On : 04-July-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub
from selenium.webdriver.common.by import By

class C9958304_TestClass(BaseTestCase):
    
    def test_C9958304(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        
        """
        TEST CASE VAIABLES
        """
        DisplayColoumns     = ['Title', 'Name', 'Summary', 'Tags', 'Last modified', 'Created on', 'Size', 'Owner', 'Not Published', 'Hidden','Run with Insight']
        content             = (By.CSS_SELECTOR, ".toolbar-button-divset div[data-ibxp-glyph-classes='ds-icon-plus']")
        Items               = ["Quantity Sold By Stores", "Sales Metrics YTD", "Yearly Product Metrics"]
        FolderFirst         = (By.CSS_SELECTOR, ".files-box .files-box-files .sd-content-title-label-folders")
        navigation_bar_css  = "div.toolbar "
        SortByOptions       = ["Default sort", "Title", "Summary", "Last modified", "Size", "Not Published", "Hidden", "Run with Insight"]
        arrowup             = (By.CSS_SELECTOR, ".ds-icon-arrow-up")
        arrowdown           = (By.CSS_SELECTOR, ".ds-icon-arrow-down")
        list_view           = (By.CSS_SELECTOR, navigation_bar_css + ".btn-how-view:not([style*='none'])")
        grid_view           = (By.CSS_SELECTOR, navigation_bar_css + ".btn-how-view-grid:not([style*='none'])")
        
        
        STEP_01 = """
            STEP 01 : Sign into 'TIBCO WebFOCUS' as Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar > Click on 'Workspaces' button > Expand 'Workspaces' node > Click on 'Retail Samples' workspaces from the resource tree
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        WFHub.Workspaces.ResourcesTree.select("Workspaces->Retail Samples")
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify by default the view is set to tile view,
        """
        WFHub.Workspaces.ContentArea.verify_grid_view_displayed("2.01")
        WFHub._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Hover on toggle ![](index.php?/attachments/get/1924678) icon on the top right corner of the navigation bar.
        """
        WFHub.Workspaces.NavigationBar.TileView.hover_over()
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify it displays tooltip 'Tile view'
        """
        tile_tooltip = WFHub._utils.validate_and_get_webdriver_object_using_locator(grid_view,"Tile view").get_attribute("title").strip()
        WFHub._utils.asequal(tile_tooltip, 'Tile view', 'Step 03.01: Verify the tooltip as "Tile view"')
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click  on toggle ![](index.php?/attachments/get/1924679) icon on the top right corner of the navigation bar.
        """
        WFHub.Workspaces.NavigationBar.ListView.click()
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify view changes from 'Tile View' to 'List View'
        """
        WFHub.Workspaces.ContentArea.verify_list_view_displayed("4.01")
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Hover on toggle ![](index.php?/attachments/get/1924681) icon on the top right corner of the navigation bar.
        """
        WFHub.Workspaces.NavigationBar.ListView.hover_over()
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify it displays tooltip 'List view'
        """
        list_tooltip = WFHub._utils.validate_and_get_webdriver_object_using_locator(list_view,"List view").get_attribute("title").strip()
        WFHub._utils.asequal(list_tooltip, 'List view', 'Step 05.01: Verify the tooltip as "list view"')
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on 'Select Display columns' icon on the top right corner of the navigation bar.
        """
        WFHub.Workspaces.NavigationBar.SelectDisplayColumn.click()
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify 'Title', 'Name', 'Summary', 'Last Modified', 'Created on', 'Size', 'Owner', 'Not Published', 'Hidden', and 'Run with Insight' are listed in drop down box
        """
        WFHub.ContextMenu.verify_options(DisplayColoumns, "6.01")
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Un-check 'Summary' from the drop down list.
        """
        WFHub.ContextMenu.select("Summary")
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify 'Summary' column does not appear and drop down list remains open.
        """
        WFHub.Workspaces.ContentArea.verify_Display_coloumns(["Summary"], "07.01",assert_type= "asnotin")
        WFHub.ContextMenu.verify_context_menu_visible("07.02")
        WFHub._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Check 'Summary' from the drop down list.
        """
        WFHub.ContextMenu.select("Summary")
        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify 'Summary' column appears and drop down list remains open.
        """
        WFHub.Workspaces.ContentArea.verify_Display_coloumns(["Summary"], "08.01",assert_type= "asin")
        WFHub.ContextMenu.verify_context_menu_visible("07.02")
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click anywhere outside drop down list.
        """
        outside = WFHub._utils.validate_and_get_webdriver_object_using_locator(content,"content for outside click")
        WFHub._core_utils.python_right_click(outside)
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify drop down list disappears.
        """
        WFHub.ContextMenu.verify_context_menu_not_visible("9.01")
        WFHub._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click  on toggle ![](index.php?/attachments/get/1924678)  icon on the top right corner of the navigation bar.
        """
        WFHub.Workspaces.NavigationBar.TileView.click()
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify view changes from 'List View' to 'Tile View'
        """
        WFHub.Workspaces.ContentArea.verify_grid_view_displayed("10.01")
        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : From the resource tree, Under 'Retail Samples' workspaces > Click on 'Reports' folder
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        WFHub.Workspaces.ResourcesTree.select("Workspaces->Retail Samples->Reports")
        WFHub._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify the following:
    
            * Sort by: 'Default Sort' button with dropdown control appears and upward arrow icon gets grayed out at the right corner of the navigation bar.
            * Folder appear first, followed by 4 reports aligned in alphabetical order in Tile view.
        """
        WFHub.Workspaces.NavigationBar.SortBy.verify_displayed("11.01")
        WFHub.Workspaces.NavigationBar.SortBy.verify_selected_option("Default sort", "11.02")
        WFHub.Workspaces.NavigationBar.ReverseSortOrder.verify_disabled("11.03")
        folder = WFHub._utils.validate_and_get_webdriver_object_using_locator(FolderFirst, "folder alignment first").text.strip()
        WFHub._utils.asequal(folder,"Folders","Step 09.02: Verify folder aligned first")
        WFHub.Workspaces.ContentArea.verify_files(Items, "11.04")
        WFHub._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click on Sort by: 'Default sort' button
        """
        WFHub.Workspaces.NavigationBar.SortBy.Click()
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify drop down list,
        """
        WFHub.Workspaces.NavigationBar.SortBy.Dropdown.verify_options(SortByOptions, "12.01")
        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Select 'Title' from the drop down list
        """
        WFHub.Workspaces.NavigationBar.SortBy.Dropdown.select("Title")
        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify the following:
    
            * Sort by: 'Title' button with dropdown control appears and 'Reverse sort order' icon pointing to the upward direction.
            * Folder is displayed first and followed by 4 reports which are aligned alphabetically in ascending order.
        """
        WFHub.Workspaces.NavigationBar.SortBy.verify_selected_option("Title", "13.01")
        upwards = WFHub._utils.validate_and_get_webdriver_object_using_locator(arrowup, "Reverse sort order").get_attribute("class")
        WFHub._utils.asin("ds-icon-arrow-up",upwards,"Step 13.02: Verify pointing up arrow button is displayed")  
        WFHub._utils.asequal(folder,"Folders","Step 13.03: Verify folder aligned first")
        WFHub.Workspaces.ContentArea.verify_files(Items, "13.04")      
        WFHub._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click on 'Reverse sort order' icon to change the arrow from upward to downward
        """
        WFHub.Workspaces.NavigationBar.ReverseSortOrder.click()
        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the following:
    
            * Sort by: 'Title' button with dropdown control appears and 'Reverse sort order' icon pointing to the downward direction.
            * Folder is displayed first and followed by 4 reports which are aligned alphabetically in descending order.
        """
        WFHub.Workspaces.NavigationBar.SortBy.verify_selected_option("Title", "14.01")
        downwards = WFHub._utils.validate_and_get_webdriver_object_using_locator(arrowdown, "Reverse sort order").get_attribute("class")
        WFHub._utils.asin("ds-icon-arrow-down",downwards,"Step 14.02: Verify pointing up arrow button is displayed")
        folder = WFHub._utils.validate_and_get_webdriver_object_using_locator(FolderFirst, "folder alignment first").text.strip()
        WFHub._utils.asequal(folder,"Folders","Step 14.03: Verify folder aligned first")
        WFHub.Workspaces.ContentArea.verify_files(Items[::-1], "14.04")
        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click on Sort by: 'Title' button >> Select 'Default Sort' from the drop down list.
        """
        WFHub.Workspaces.NavigationBar.SortBy.Click()
        WFHub.Workspaces.NavigationBar.SortBy.Dropdown.select("Default sort")
        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify the following:
    
            * Sort by: 'Default Sort' button with dropdown control appears and upward arrow icon gets grayed out at the right corner of the navigation bar.
            * Folder appear first, followed by 4 reports aligned in alphabetical order in Tile view.
        """
        WFHub.Workspaces.NavigationBar.SortBy.verify_displayed("15.01")
        WFHub.Workspaces.NavigationBar.SortBy.verify_selected_option("Default sort", "15.02")
        WFHub.Workspaces.NavigationBar.ReverseSortOrder.verify_disabled("15.03")
        folder = WFHub._utils.validate_and_get_webdriver_object_using_locator(FolderFirst, "folder alignment first").text.strip()
        WFHub._utils.asequal(folder,"Folders","Step 15.03: Verify folder aligned first")
        WFHub.Workspaces.ContentArea.verify_files(Items, "15.04")
        WFHub._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Click  on toggle ![](index.php?/attachments/get/1924679) icon on the top right corner of the navigation bar.
        """
        WFHub.Workspaces.NavigationBar.ListView.click()
        WFHub._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify the following:
    
            * View changes from 'Tile View' to 'List View'.
            * No sort arrow appears next to any column. 
            * Folder appear first, followed by 4 reports in alphabetical order.
        """
        WFHub.Workspaces.ContentArea.verify_list_view_displayed("16.01")
        WFHub._utils.verify_object_visible(arrowup, False, "Step 16.02: Verify pointing up arrow button is not displayed")
        WFHub._utils.verify_object_visible(arrowdown, False, "Step 16.02: Verify pointing down arrow button is not displayed")
        WFHub._utils.verify_object_visible(".grid_row0 .ds-icon-folder", True, "Step 16.03: Verify folder aligned first")
        WFHub.Workspaces.ContentArea.verify_files(Items, "16.04")
        WFHub._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Click on **Title** column
        """
        WFHub.Workspaces.ContentArea.click_listView_coloumn_Title("Title")
        WFHub._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify the following:
    
            * Sort arrow appears next to 'Title' column pointing downward direction.
            * Folder is displayed first and followed by 4 reports which are sorted alphabetically in descending order.
        """
        WFHub._utils.verify_object_visible("div[data-ibxp-text='Title'] .ds-icon-arrow-down", True, "Step 17.01: Verify pointing down arrow button near title is displayed")
        WFHub._utils.verify_object_visible(".grid_row0 .ds-icon-folder", True, "Step 17.02: Verify folder aligned first")
        WFHub.Workspaces.ContentArea.verify_files(Items[::-1], "17.03")
        WFHub._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Click on **Title** column (twice).
        """
        WFHub.Workspaces.ContentArea.click_listView_coloumn_Title("Title")
        WFHub._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify the following:
    
            * Sort arrow appears next to 'Title' column pointing upward direction.
            * Folder is displayed first and followed by 4 reports which are sorted alphabetically in ascending order.
        """
        WFHub._utils.verify_object_visible("div[data-ibxp-text='Title'] .ds-icon-arrow-up", True, "Step 18.01: Verify pointing up arrow button near title is displayed")
        WFHub._utils.verify_object_visible(".grid_row0 .ds-icon-folder", True, "Step 18.02: Verify folder aligned first")
        WFHub.Workspaces.ContentArea.verify_files(Items, "18.03")
        WFHub._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Click on **Title** column (thrice).
        """
        WFHub.Workspaces.ContentArea.click_listView_coloumn_Title("Title")
        WFHub._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify the following:
    
            * No sorting arrow appears next to 'Title' column.
            * Folder is displayed first and followed by 4 reports which are sorted alphabetically in ascending order.
        """
        WFHub._utils.verify_object_visible(arrowup, False, "Step 19.01: Verify pointing up arrow button is not displayed")
        WFHub._utils.verify_object_visible(arrowdown, False, "Step 19.02: Verify pointing down arrow button is not displayed")
        WFHub._utils.verify_object_visible(".grid_row0 .ds-icon-folder", True, "Step 19.03: Verify folder aligned first")
        WFHub.Workspaces.ContentArea.verify_files(Items, "19.04")
        WFHub.Workspaces.switch_to_default_content()
        WFHub._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Click on the 'User profile' banner link > Click 'Reset View'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Reset View")
        WFHub._utils.wait_for_page_loads(time_out=5, pause_time=5)
        WFHub._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")        
        WFHub._utils.capture_screenshot("21", STEP_21)

