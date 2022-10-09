"""-------------------------------------------------------------------------------------------
Author Name  : GRETHINA@TIBCO.COM
Automated On : 16-May-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub

class C9960407_TestClass(BaseTestCase):
    
    def test_C9960407(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        """
        TEST CASE VAIABLES
        """
        defaultServer = ["All reporting servers"]
        defaultDirectories = ['All application directories']
        Servers = ["EDASERVE"]
        Directories = ['baseapp','baseapp/dimensions','baseapp/facts','baseapp/test','baseapp/vr','ibisamp','jsonmaps','map_temp']
        
        STEP_01 = """
            STEP 01 : Sign into TIBCO WebFOCUS as Admin User
        """
        WFHub.invoke_with_login("mridadm", "mrpassadm")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar, click on the 'Search WebFOCUS' icon
        """
        WFHub._utils.wait_for_page_loads(10)
        WFHub.LeftSideNavigationBar.SearchWebFocus.click()
        WFHub._utils.wait_for_page_loads(10)
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : From the 'Data in' filter > Click on the 'All reporting servers' option in the dropdown control
        """
        WFHub.SearchWebfocus.AllItems.DataIn.click_servers()
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify the following options displayed:
    
            All reporting servers (By default gets check-off)
            **Note: No servers are shown by default because that is not indexing**
        """
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_checked(defaultServer, "3.01")
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on the 'All reporting servers' option to close the lists of options displayed
        """
        WFHub.SearchWebfocus.Data.DataIn.click_dropdown_icon_servers()
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : From the 'Data in' filter > Click on the 'All application directories' option in the dropdown control
        """
        WFHub.SearchWebfocus.Data.DataIn.click_directories()
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the following options displayed:
    
            All application directories (By default gets check-off)
    
            **Note: No application directories are shown by default because that is not indexing.**
        """
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_checked(defaultDirectories, "5.01")        
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on the 'All application directories' option to close the lists of options displayed
        """
        WFHub.SearchWebfocus.Data.DataIn.click_dropdown_icon_directories()
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : From the left side navigation bar, click on the 'Application Directories' icon
        """
        WFHub.LeftSideNavigationBar.ApplicationDirectories.click()
        WFHub.ApplicationDirectories.switch_to_frame()
        #WFHub._utils.wait_for_page_loads(time_out =3 , pause_time=3)
        
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Right-click on the 'Applications' node > Select 'Properties' > Select the options same as mentioned in the screenshot:
        """
        WFHub.ApplicationDirectories.Applications.edit_directories("Applications")
        WFHub._utils.wait_for_page_loads(time_out=1, pause_time=3)
        WFHub.ContextMenu.select("Properties")
        WFHub._utils.wait_for_page_loads(time_out=1, pause_time=3)
        WFHub.ApplicationDirectories.SearchIndexOptions.allAppPath.click()
        
        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click 'Save'
        """
        WFHub.ApplicationDirectories.SearchIndexOptions.Save.click()
        WFHub._core_utils.switch_to_frame(".wcx-mfc-properties iframe.ibx-iframe-frame")
        
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the following message:
             Index Create Initiated
            (ICM18533) Request Submitted: _edahome/catalog/solrindx
            (ICM18762) Job ID: 20220511023609_30c18f72.
    
            **Note: Job ID, Request Submitted number are changed each and every time while adding index**
        """
        WFHub._utils.verify_object_visible_by_xpath( "/html/body/pre[contains(text(),'Index Create Initiated')][contains(text(),'(ICM18533) Request Submitted: _edahome/catalog/solrindx')][contains(text(),'(ICM18762) Job ID:')]",True,"Step 9:Index Message")
        WFHub.ApplicationDirectories.switch_to_default_content()
        WFHub._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click on the 'User profile' banner link > Click 'Reset View'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Reset View")
        WFHub._utils.wait_for_page_loads(time_out = 8,pause_time=3)
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : From the left side navigation bar, click on the 'Search WebFOCUS' icon
        """
        WFHub.LeftSideNavigationBar.SearchWebFocus.click()
        WFHub._utils.wait_for_page_loads(time_out = 10,pause_time=20)
        self.driver.refresh()
        WFHub._utils.wait_for_page_loads(time_out = 4 ,pause_time=4)
        WFHub._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : From the 'Data in' filter > Click on the 'All reporting servers' option in the dropdown control
        """
        WFHub.SearchWebfocus.Data.DataIn.click_servers()
        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify the following options displayed:
    
            1. All reporting servers (By default gets check-off)
    
            **Note: The below server is unchecked by default**
    
            1. EDASERVE
        """
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_checked(defaultServer, "12.01")
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_unchecked(Servers, "12.02")
        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click on the 'All reporting servers' option to close the lists of options displayed
        """
        WFHub.SearchWebfocus.Data.DataIn.click_dropdown_icon_servers()
        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : From the 'Data in' filter > Click on the 'All application directories' option in the dropdown control
        """
        WFHub.SearchWebfocus.Data.DataIn.click_directories()
        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the following options displayed:
    
            1. All application directories (By default gets check-off)
    
            **Note: The following application folders under EDASERVE section are unchecked by default and based on the available server total No. of application folders will be varied.**
    
            1. baseapp
            2. baseapp/dimensions
            3. baseapp/facts
            4. baseapp/test
            5. baseapp/vr
            6. ibisamp
            7. jsonmaps
            8. map_temp
    
            **Important Note: As per https://jira.tibco.com/browse/IBIUX-1039, JIRA retail samples, wf retail application folders fail to index. Once JIRA has been resolved need to update the test case Until verify this expected result.**
    
            2. 'citibike' application folder is not available in the 'All application directories' list
        """
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_checked(defaultDirectories, "14.01")
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_unchecked(Directories, "14.02")
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_options_notin(["citibike"], "14.03","notin")
        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click on the 'All application directories' option to close the lists of options displayed
        """
        WFHub.SearchWebfocus.Data.DataIn.click_dropdown_icon_directories()
        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : From the left side navigation bar, click on the 'Application Directories' icon
        """
        WFHub.LeftSideNavigationBar.ApplicationDirectories.click()
        WFHub.ApplicationDirectories.switch_to_frame()
        WFHub._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Right-click on 'citibike' application folder > Select 'Create Index'
        """
        WFHub.ApplicationDirectories.Applications.edit_directories("citibike")
        WFHub._utils.wait_for_page_loads(time_out=1, pause_time=3)
        WFHub.ContextMenu.select("Create Index")
        WFHub._utils.wait_for_page_loads(time_out=1, pause_time=3)
        WFHub._core_utils.switch_to_frame("div[frame_id='MFOFrame'] iframe.ibx-iframe-frame")
        
        WFHub._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify the following message:
             Index Create Initiated
            (ICM18533) Request Submitted: _edahome/catalog/solrindx
            (ICM18762) Job ID: 20220511025353_6147ef42
    
            **Note: Job ID, Request Submitted number are changed each and every time while adding index**
        """
        WFHub._utils.verify_object_visible_by_xpath( "/html/body/pre[contains(text(),'Index Create Initiated')][contains(text(),'(ICM18533) Request Submitted: _edahome/catalog/solrindx')][contains(text(),'(ICM18762) Job ID:')]",True,"Step 17:Index Message")
        WFHub.ApplicationDirectories.switch_to_default_content()
        WFHub._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : From the left side navigation bar, click on the 'Search WebFOCUS' icon
        """
        WFHub.LeftSideNavigationBar.SearchWebFocus.click()
        WFHub._utils.wait_for_page_loads(time_out = 3)
        WFHub._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : From the 'Data in' filter > Click on the 'All application directories' option in the dropdown control
        """
        WFHub.SearchWebfocus.Data.DataIn.click_directories()
        WFHub._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify the following options displayed:
    
            1. All application directories (By default gets check-off)
    
            2.'citibike' application folder is available in the 'All application directories' list
        """
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_checked(defaultDirectories, "19.01")
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_options(["citibike"], "19.02", "in")
        WFHub._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Click on the 'All application directories' option to close the lists of options displayed
        """
        WFHub.SearchWebfocus.Data.DataIn.click_dropdown_icon_directories()
        WFHub._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : From the left side navigation bar, click on the 'Application Directories' icon
        """
        WFHub.LeftSideNavigationBar.ApplicationDirectories.click()
        WFHub.ApplicationDirectories.switch_to_frame()
        WFHub._utils.capture_screenshot("21", STEP_21)

        STEP_22 = """
            STEP 22 : Right-click on 'citibike' application folder > Select 'Delete Index'
        """
        WFHub.ApplicationDirectories.Applications.edit_directories("citibike")
        WFHub._utils.wait_for_page_loads(time_out=1, pause_time=3)
        WFHub.ContextMenu.select("Delete Index")
        WFHub._utils.wait_for_page_loads(time_out=1, pause_time=3)
        WFHub._core_utils.switch_to_frame(".wcx-multiframes-content-view .ibx-iframe-frame")
        WFHub._utils.capture_screenshot("22", STEP_22)

        STEP_22_EXPECTED = """
            STEP 22 - Expected : Verify the following message:
    
             Index Delete Initiated
            (ICM18533) Request Submitted: _edahome/catalog/solrindx
            (ICM18762) Job ID: 20220511025750_d769cc32
        """
        WFHub._utils.verify_object_visible_by_xpath( "/html/body/pre[contains(text(),'Index Delete Initiated')][contains(text(),'(ICM18533) Request Submitted: _edahome/catalog/solrindx')][contains(text(),'(ICM18762) Job ID:')]",True,"Step 22:Index Message")
        WFHub.ApplicationDirectories.switch_to_default_content()
        WFHub._utils.capture_screenshot("22 - Expected", STEP_22_EXPECTED, True)

        STEP_23 = """
            STEP 23 : From the left side navigation bar, click on the 'Search WebFOCUS' icon
        """
        WFHub.LeftSideNavigationBar.SearchWebFocus.click()
        WFHub._utils.wait_for_page_loads(time_out = 3)
        WFHub._utils.capture_screenshot("23", STEP_23)

        STEP_24 = """
            STEP 24 : From the 'Data in' filter > Click on the 'All application directories' option in the dropdown control
        """
        WFHub.SearchWebfocus.Data.DataIn.click_directories()
        WFHub._utils.capture_screenshot("24", STEP_24)

        STEP_24_EXPECTED = """
            STEP 24 - Expected : Verify the following options displayed:
    
            1. All application directories (By default gets check-off)
    
            2.'citibike' application folder is not available in the 'All application directories' list
        """
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_checked(defaultDirectories, "24.01")
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_options_notin(["citibike"], "24.02","notin")
        WFHub._utils.capture_screenshot("24 - Expected", STEP_24_EXPECTED, True)

        STEP_25 = """
            STEP 25 : Click on the 'All application directories' option to close the lists of options displayed
        """
        WFHub.SearchWebfocus.Data.DataIn.click_dropdown_icon_directories()
        WFHub._utils.capture_screenshot("25", STEP_25)

        STEP_26 = """
            STEP 26 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("26", STEP_26)

