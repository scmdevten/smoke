"""-------------------------------------------------------------------------------------------
Author Name  : GRETHINA@TIBCO.COM
Automated On : 14-June-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub
from selenium.webdriver.common.by import By

class C9961043_TestClass(BaseTestCase):
    
    def test_C9961043(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        """
        TEST CASE VAIABLES
        """
        text      = "div.search-help-questions"
        hyperlink = 'div[class^="search-plugin-options"] div[class*=ibx-anchor-link]:not([data-ibx-name="_btnConditionsDlg"])'
        Allitems  = (By.CSS_SELECTOR, "div[data-ibxp-user-value='clientrsrv']")
        Content   = (By.CSS_SELECTOR, "div[data-ibxp-user-value='client']")
        Data      = (By.CSS_SELECTOR, "div[data-ibxp-user-value='rsrv']")
        
        STEP_01 = """
            STEP 01 : Sign into TIBCO WebFOCUS as Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar, click on the 'Search' icon
        """
        WFHub._utils.wait_for_page_loads(10)
        WFHub.LeftSideNavigationBar.SearchWebFocus.click()
        WFHub._utils.wait_for_page_loads(10)
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify the following for the 'Search Content & Data' Explorer pane:
        """
        WFHub._utils.verify_object_visible("[data-ibx-name='_pluginNavFrame']", True, "Step 2: 'Search Content & Data' Explorer pane is Visible")              
        WFHub._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click on the 'Content' tab
        """
        WFHub.SearchWebfocus.Content.ContentButton.click()
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify the following for the 'Search Content & Data' Explorer pane:
    
            1.'All Items', 'Content' (Selected) , and 'Data' displayed
            2.'Search query' text box displayed with the no place holder text as 'Search (use * ? '' + to refine)
            3.By default 'Search by' filter is selected with 'All categories' option
            4.By default 'Type' filter is selected with 'All types' option
            5.By default 'Content in' filter is selected with 'All Workspaces' option
            6.By default 'Data in' filters are selected with the 'All reporting servers' and 'All application directories' options get disabled
            7.'Clear' and 'Search buttons are enabled by default
            8.Bottom of the explorer pane displays with 'Questions?' label and 'Get Search help' hyperlink.
        """
        WFHub.SearchWebfocus.AllItems.AllItemButton.verify_enabled("03.01")
        WFHub.SearchWebfocus.Content.ContentButton.verify_checked("03.02")
        WFHub.SearchWebfocus.Data.DataButton.verify_enabled("03.03")
        WFHub.SearchWebfocus.SearchTextBox.verify_placeholder_search('Search (use * ? "" + to refine)', "03.04")
        WFHub.SearchWebfocus.Content.SearchBy.verify_selected_option("All categories", "03.05")
        WFHub.SearchWebfocus.Content.Type.verify_selected_option("All types", "03.06")
        WFHub.SearchWebfocus.Content.ContentIn.verify_selected_option("All workspaces", "03.07")
        WFHub.SearchWebfocus.Content.ContentIn.verify_disabled_directories("3.20")
        WFHub.SearchWebfocus.Content.ContentIn.verify_disabled_servers("3.21")
        WFHub.SearchWebfocus.Content.DataIn.verify_selected_option_directories("All application directories", "03.09")
        WFHub.SearchWebfocus.Content.Clear.verify_enabled("3.10")
        WFHub.SearchWebfocus.Content.Search.verify_enabled("3.11")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub._utils.verify_element_text(hyperlink, "Get Search help", "3.33 Get Search help hyperlink")
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on the 'Data' tab
        """
        WFHub.SearchWebfocus.Data.DataButton.click()
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify the following for the 'Search Content & Data' Explorer pane:
    
            1.'All Items', 'Content', and 'Data' (Selected) displayed
            2.'Search query' text box displayed with the no place holder text as 'Search (use * ? '' + to refine)
            3.By default 'Search by' filter is selected with 'All Categories' option
            4.By default 'Type' filter is selected with 'All types' option
            5.By default 'Content in' filter with 'All Workspaces' option get disabled
            6.By default 'Data in' filters are selected with: i) 'All reporting servers' option and ii) 'All application directories' option
            7.'Clear' and 'Search buttons are enabled by default
            8.Bottom of the explorer pane displays with 'Questions?' label and 'Get Search help' hyperlink.
        """
        WFHub.SearchWebfocus.Data.AllItemButton.verify_enabled("4.01")
        WFHub.SearchWebfocus.Content.ContentButton.verify_enabled("4.02")
        WFHub.SearchWebfocus.Data.DataButton.verify_checked("4.03")
        WFHub.SearchWebfocus.Data.SearchBy.verify_selected_option("All categories", "4.04")
        WFHub.SearchWebfocus.Data.Type.verify_selected_option("All types", "4.05")
        WFHub.SearchWebfocus.Data.DataIn.verify_disabled_all_workspaces("4.06")
        WFHub.SearchWebfocus.Data.DataIn.verify_selected_option_servers("All reporting servers", "4.07")
        WFHub.SearchWebfocus.Data.DataIn.verify_selected_option_directories("All application directories", "4.08")
        WFHub.SearchWebfocus.Data.Clear.verify_enabled("4.09")
        WFHub.SearchWebfocus.Data.Search.verify_enabled("4.10")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub._utils.verify_element_text(hyperlink, "Get Search help", "4.44 Get Search help hyperlink")
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on 'Get Search help' Hyperlink
        """
        WFHub.SearchWebfocus.click_help()
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : 1.Verify it opens TIBCO WebFOCUS Online Help in a new tab and display WebFOCUS help Document without any error.
            2.Verify the following URL:
            http://na1devfocxbx17.dev.tibco.com:12410/ibi_apps/ibi_help/index.jsp?scope=dash&topic=/com.ibi.help.intro/source/hub_search.htm
        """
        WFHub._core_utils.switch_to_new_window()  
        WFHub._utils.asin("TIBCO WebFOCUS", self.driver.title, "Step 05.01 : Verify TIBCO WebFOCUS Online Help open in a new window without any issue")
        WFHub._utils.asin("Online Help", self.driver.title, "Step 05.02 : Verify TIBCO WebFOCUS Online Help open in a new window without any issue")
        WFHub._utils.verify_current_url("ibi_help/index.jsp?scope=dash&topic=/com.ibi.help.intro/source/hub_search.htm", "Step 5.02")
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on 'Close' 'X' button in new tab.
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : 1.Verify new tab is closed and it is reverted back to TIBCO WebFOCUS Home Page.
        """
        WFHub._utils.verify_current_tab_name("TIBCO WebFOCUS Home Page", "Step 6.01")
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Sign into TIBCO WebFOCUS as an Advanced User
        """
        WFHub.invoke_with_login("mridadv", "mrpassadv")
        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : From the left side navigation bar, click on the 'Search' icon
        """
        WFHub.LeftSideNavigationBar.SearchWebFocus.click()
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the following for the 'Search Content & Data' Explorer pane:
    
            1.verify 'All Items', 'Content', and 'Data' all the three options are not available.
            2.'Search query' text box displayed with the no place holder text as 'Search (use * ? '' + to refine)
            3.By default 'Search by' filter is selected with 'All Categories' option
            4.By default 'Type' filter is selected with 'All types' option
            5.By default 'Content in' filter is selected with 'All Workspaces' option.
            6.Verify 'Data in' filters are not available.
            7.'Clear' and 'Search buttons are enabled by default
            8.Bottom of the explorer pane displays with 'Questions?' label and 'Get Search help' hyperlink.
        """
        #WFHub._utils.verify_object_visible("div.wfshell-plugin-nav-frame [data-ibx-type='ibxButtonGroup']", False, "Step 9.01: 'All Items', 'Content', and 'Data' is not Visible")
        both = self.driver.find_element(*Allitems).text.strip()
        WFHub._utils.as_not_equal(both, "All Items", "Step 9.011 All Items not available")
        client = self.driver.find_element(*Content).text.strip()
        WFHub._utils.as_not_equal(client, "content", "Step 9.012 content not available")
        #WFHub._utils.verify_object_visible("div[data-ibxp-user-value='rsrv']", False, "Step 9.013 Data not available")      
        WFHub.SearchWebfocus.SearchTextBox.verify_placeholder_search('Search (use * ? "" + to refine)', "9.02")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub.SearchWebfocus.AllItems.SearchBy.verify_selected_option('All categories', "9.03")
        WFHub.SearchWebfocus.AllItems.Type.verify_selected_option("All types", "9.04")
        WFHub.SearchWebfocus.AllItems.ContentIn.verify_selected_option("All workspaces", "9.05")  
        WFHub._utils.verify_object_visible("div[data-ibx-name='_selectRptSrvrs'] ", False, "Step 9.051 Datain Filters not available") 
        WFHub._utils.verify_object_visible("div[data-ibx-name='_selectAppDirs'] ", False, "Step 9.052 Datain Filters not available")  
        WFHub.SearchWebfocus.AllItems.Clear.verify_enabled("9.06")
        WFHub.SearchWebfocus.AllItems.Search.verify_enabled("9.07")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub._utils.verify_element_text(hyperlink, "Get Search help", "Step:9.08 Get Search help hyperlink")   
        WFHub._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Sign into TIBCO WebFOCUS as Basic User
        """
        WFHub.invoke_with_login("mridbas", "mrpassbas")
        WFHub._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : From the left side navigation bar, click on the 'Search' icon
        """
        WFHub.LeftSideNavigationBar.SearchWebFocus.click()
        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify the following for the 'Search Content & Data' Explorer pane:
    
            1.verify 'All Items', 'Content', and 'Data' all the three options are not available.
            2.'Search query' text box displayed with the no place holder text as 'Search (use * ? '' + to refine)
            3.By default 'Search by' filter is selected with 'All Categories' option
            4.By default 'Type' filter is selected with 'All types' option
            5.By default 'Content in' filter is selected with 'All Workspaces' option.
            6.Verify 'Data in' filters are not available.
            7.'Clear' and 'Search buttons are enabled by default
            8.Bottom of the explorer pane displays with 'Questions?' label and 'Get Search help' hyperlink.
        """
        both = self.driver.find_element(*Allitems).text.strip()
        WFHub._utils.as_not_equal(both, "All Items", "Step 12.011 All Items not available")
        client = self.driver.find_element(*Content).text.strip()
        WFHub._utils.as_not_equal(client, "content", "Step 12.012 content not available")
        #WFHub._utils.verify_object_visible("div[data-ibxp-user-value='rsrv']", False, "Step 12.013 Data not available")
        WFHub.SearchWebfocus.SearchTextBox.verify_placeholder_search('Search (use * ? "" + to refine)', "12.02")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub.SearchWebfocus.AllItems.SearchBy.verify_selected_option('All categories', "12.03")
        WFHub.SearchWebfocus.AllItems.Type.verify_selected_option("All types", "12.04")
        WFHub.SearchWebfocus.AllItems.ContentIn.verify_selected_option("All workspaces", "12.05")  
        WFHub._utils.verify_object_visible("div[data-ibx-name='_selectRptSrvrs'] ", False, "Step 12.051 Datain Filters not available") 
        WFHub._utils.verify_object_visible("div[data-ibx-name='_selectAppDirs'] ", False, "Step 12.052 Datain Filters not available")           
        WFHub.SearchWebfocus.AllItems.Clear.verify_enabled("12.06")
        WFHub.SearchWebfocus.AllItems.Search.verify_enabled("12.07")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub._utils.verify_element_text(hyperlink, "Get Search help", "Step:12.08 Get Search help hyperlink")          
        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Sign into TIBCO WebFOCUS as Group Admin User
        """
        WFHub.invoke_with_login("mridgadm", "mrpassgadm")
        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : From the left side navigation bar, click on the 'Search' icon
        """
        WFHub.LeftSideNavigationBar.SearchWebFocus.click()
        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify the following for the 'Search Content & Data' Explorer pane:
    
            1.verify 'All Items', 'Content', and 'Data' all the three options are not available.
            2.'Search query' text box displayed with the no place holder text as 'Search (use * ? '' + to refine)
            3.By default 'Search by' filter is selected with 'All Categories' option
            4.By default 'Type' filter is selected with 'All types' option
            5.By default 'Content in' filter is selected with 'All Workspaces' option.
            6.Verify 'Data in' filters are not available.
            7.'Clear' and 'Search buttons are enabled by default
            8.Bottom of the explorer pane displays with 'Questions?' label and 'Get Search help' hyperlink.
        """
        both = self.driver.find_element(*Allitems).text.strip()
        WFHub._utils.as_not_equal(both, "All Items", "Step 15.011 All Items not available")
        client = self.driver.find_element(*Content).text.strip()
        WFHub._utils.as_not_equal(client, "content", "Step 15.012 content not available")
        #WFHub._utils.verify_object_visible("div[data-ibxp-user-value='rsrv']", False, "Step 15.013 Data not available")
        WFHub.SearchWebfocus.SearchTextBox.verify_placeholder_search('Search (use * ? "" + to refine)', "15.02")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub.SearchWebfocus.AllItems.SearchBy.verify_selected_option('All categories', "15.03")
        WFHub.SearchWebfocus.AllItems.Type.verify_selected_option("All types", "15.04")
        WFHub.SearchWebfocus.AllItems.ContentIn.verify_selected_option("All workspaces", "15.05") 
        WFHub._utils.verify_object_visible("div[data-ibx-name='_selectRptSrvrs'] ", False, "Step 15.051 Datain Filters not available") 
        WFHub._utils.verify_object_visible("div[data-ibx-name='_selectAppDirs'] ", False, "Step 15.052 Datain Filters not available")            
        WFHub.SearchWebfocus.AllItems.Clear.verify_enabled("15.06")
        WFHub.SearchWebfocus.AllItems.Search.verify_enabled("15.07")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub._utils.verify_element_text(hyperlink, "Get Search help", "Step:15.08 Get Search help hyperlink") 
        WFHub._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("16", STEP_16)

