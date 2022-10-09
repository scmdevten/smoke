"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh Ravichandran
Automated On : 05-January-2022
-------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub

class C9958303_TestClass(BaseTestCase):
    
    def test_C9958303(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        STEP_01 = """
            STEP 01 : Sign into 'TIBCO WebFOCUS' as Admin User
        """
        WFHub.invoke_with_login("mridadm", "mrpassadm")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar > Click on 'Workspaces' button > From the resource tree, Click on the 'Workspaces' node
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.ResourcesTree.select_workspaces()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify the following:
            * There are no action tiles displayed in the content area and in the navigation bar '+ content' button gets disabled.
            * From the resource tree, the 'Workspaces' and 'Folders' buttons are available the same as below:
        """
        WFHub.Workspaces.NavigationBar.ContentButton.verify_disabled("02.01")
        WFHub.Workspaces.ResourcesTree.NewWorkspace.verify_enabled("02.02")
        WFHub.Workspaces.ResourcesTree.NewFolder.verify_enabled("02.03")
        WFHub._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : **Create an 'Enterprise Workspace'**
            Click on the 'Workspaces' action tile > Enter 'Title' as 'EW' > Click OK
        """
        WFHub.Workspaces.ResourcesTree.NewWorkspace.click()
        WFHub.Dialog.NewWorkspace.wait_for_text("New")
        WFHub.Dialog.NewWorkspace.Title.enter_text("EW")
        WFHub.Dialog.NewWorkspace.ReportingSeverCheckbox.uncheck()
        WFHub.Dialog.NewWorkspace.Ok.click()
        WFHub.Dialog.NewWorkspace.wait_until_invisible()
        WFHub.Workspaces.ContentArea.wait_for_text("EW", 120)
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify 'EW' workspace is created and displayed in the content area. By default, it is in a published state
        """
        WFHub.Workspaces.ContentArea.verify_folders(["EW"], "03.01")
        WFHub.Workspaces.ContentArea.verify_published_folders(["EW"], "03.02")
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : **Create a 'Tenant Workspace'**
            Click on the 'Workspaces' action tile > Change the 'Type' to 'Tenant Workspace' > Enter 'Title' as 'TW' > Click OK
        """
        WFHub.Workspaces.ResourcesTree.NewWorkspace.click()
        WFHub.Dialog.NewWorkspace.wait_for_text("New")
        WFHub.Dialog.NewWorkspace.click_type_dropdown()
        WFHub.Dialog.NewWorkspace.DropdownSelection.select("Tenant workspace")
        WFHub.Dialog.NewWorkspace.Title.enter_text("TW")
        WFHub.Dialog.NewWorkspace.ReportingSeverCheckbox.uncheck()
        WFHub.Dialog.NewWorkspace.Ok.click()
        WFHub.Dialog.NewWorkspace.wait_until_invisible()
        WFHub.Workspaces.ContentArea.wait_for_text("TW", 120)
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify 'TW' workspace is created and displayed in the content area. By default, it is in a published state
        """
        WFHub.Workspaces.ContentArea.verify_folders(["TW"], "04.01")
        WFHub.Workspaces.ContentArea.verify_published_folders(["TW"], "04.02")
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : **Create a 'Folder'**
            Click on the 'Folder' action tile > Enter 'Title' as 'Test_Folder' > Click OK
        """
        WFHub.Workspaces.ContentArea.delete_folder_if_exists("Test_Folder")
        WFHub.Workspaces.ContentArea.wait_for_text("EW")
        WFHub.Workspaces.ResourcesTree.NewFolder.click()
        WFHub.Dialog.NewFolder.wait_for_text("New")
        WFHub.Dialog.NewFolder.Title.enter_text("Test_Folder")
        WFHub.Dialog.NewFolder.Ok.click()
        WFHub.Dialog.NewFolder.wait_until_invisible()
        WFHub.Workspaces.ContentArea.wait_for_text("Test_Folder", 120)
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify 'Test_Folder' is created and displayed in the content area. By default, it is in a unpublished state and it is displayed with an unpublished condition icon
        """
        WFHub.Workspaces.ContentArea.verify_folders(["Test_Folder"], "05.01")
        WFHub.Workspaces.ContentArea.verify_unpublished_folders(["Test_Folder"], "05.02")
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Expand 'Workspaces' > Click on  'Retail Samples' workspaces from the resource tree > Click on '+ Content' button
        """
        WFHub.Workspaces.ResourcesTree.collapse_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Retail Samples")
        WFHub.Workspaces.NavigationBar.wait_for_text("Content")
        WFHub.Workspaces.NavigationBar.ContentButton.click()
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify 5 action menus (Data, Application, InfoAssist, Schedule, and Other) are displayed under the '+Content' button.
        """
        WFHub.ContextMenu.verify_options(['Data', 'Application', 'InfoAssist', 'Schedule', 'Other'], "06")
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Hover over 'Data' action menu
        """
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify 'Reporting Object' option is displayed under the '+Content' button.
        """
        WFHub.ContextMenu.verify_options(["Reporting Object"], "07", menu_path="Data")
        WFHub._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Hover over 'Application' action menu
        """
        WFHub._utils.capture_screenshot("08", STEP_08)
        
        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify 'Portal' option is displayed under the '+Content' button.
        """
        WFHub.ContextMenu.verify_options(['Portal'], "08", menu_path="Application")
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Hover over 'InfoAssist' action menu
        """
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify 6 options ( Chart, Visualization, Report, Document, Sample content, Alert) are displayed under the '+Content' button.
        """
        WFHub.ContextMenu.verify_options(['Chart', 'Visualization', 'Report', 'Document', 'Sample Content', 'Alert'], "09", menu_path="InfoAssist")
        WFHub._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Hover over 'Schedule' action menu
        """
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify 3 options ( Access List, Distribution List, Schedule) are displayed under the '+Content' button.
        """
        WFHub.ContextMenu.verify_options(['Access List', 'Distribution List', 'Schedule'], "10", menu_path="Schedule")
        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Hover over 'Other' action menu
        """
        WFHub._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify the following: 
    
            * 7 options (Upload File, URL, Shortcut, Text Editor, Blog, Portal Page, Collaborative Portal) are displayed under the '+Content' button.
            * The 'Folder' button is displayed under the resource tree.
            * The 'Workspaces' button gets disabled under the resource tree.
        """
        WFHub.ContextMenu.verify_options(['Folder', 'Upload File', 'URL', 'Shortcut', 'Text Editor', 'Blog', 'Portal Page', 'Collaborative Portal'], "11.01", menu_path="Other")
        WFHub.Workspaces.ResourcesTree.NewWorkspace.verify_disabled("11.02")
        WFHub.Workspaces.ResourcesTree.NewFolder.verify_enabled("11.03")
        WFHub.Workspaces.switch_to_default_content()
        WFHub._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Sign into 'TIBCO WebFOCUS' as Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : From the left side navigation bar > Click on 'Workspaces' view > From the resource tree, Click on the 'Workspaces' node
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.ResourcesTree.select_workspaces()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the following:
    
            * There are no action tiles displayed in the content area and in the navigation bar '+ content' button gets disabled.
            * From the resource tree, the 'Workspaces' button gets disabled and the 'Folders' button enabled same as below:
        """
        WFHub.Workspaces.NavigationBar.ContentButton.verify_disabled("14.01")
        WFHub.Workspaces.ResourcesTree.NewWorkspace.verify_disabled("14.02")
        WFHub.Workspaces.ResourcesTree.NewFolder.verify_disabled("14.03")
        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Expand 'Workspaces' > Click on  'Retail Samples' workspaces from the resource tree
        """
        WFHub.Workspaces.ResourcesTree.select("Workspaces->Retail Samples")
        WFHub.Workspaces.NavigationBar.wait_for_text("Content")
        WFHub.Workspaces.NavigationBar.ContentButton.click()
        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify 5 action menus (Data, Application, InfoAssist, Schedule, and Other) are displayed under the '+Content' button.
        """
        WFHub.ContextMenu.verify_options(['Data', 'Application', 'InfoAssist', 'Schedule', 'Other'], "15")
        WFHub._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Hover over 'Application' action menu
        """
        WFHub._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify 'Portal' option is displayed under the '+Content' button.
        """
        WFHub.ContextMenu.verify_options(["Reporting Object"], "16.01", menu_path="Data")
        WFHub.ContextMenu.verify_options(['Portal'], "16.02", menu_path="Application")
        WFHub._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Hover over 'InfoAssist' action menu
        """
        WFHub._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify 6 options ( Chart, Visualization, Report, Document, Sample content, Alert) are displayed under the '+Content' button.
        """
        WFHub.ContextMenu.verify_options(['Chart', 'Visualization', 'Report', 'Document', 'Sample Content', 'Alert'], "17", menu_path="InfoAssist")
        WFHub._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Hover over 'Schedule' action menu
        """
        WFHub._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify 3 options ( Access List, Distribution List, Schedule) are displayed under the '+Content' button.
        """
        WFHub.ContextMenu.verify_options(['Access List', 'Distribution List', 'Schedule'], "18", menu_path="Schedule")
        WFHub._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Hover over 'Other' action menu
        """
        WFHub._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify the following: 
    
            * 7 options (Upload File, URL, Shortcut, Text Editor, Blog, Portal Page, Collaborative Portal) are displayed under the '+Content' button.
            * The 'Folder' button is displayed under the resource tree.
            * The 'Workspaces' button gets disabled under the resource tree.
        """
        WFHub.ContextMenu.verify_options(['Folder', 'Upload File', 'URL', 'Shortcut', 'Text Editor', 'Blog', 'Portal Page', 'Collaborative Portal'], "19.01", menu_path="Other")
        WFHub.Workspaces.ResourcesTree.NewWorkspace.verify_disabled("19.02")
        WFHub.Workspaces.ResourcesTree.NewFolder.verify_enabled("19.03")
        WFHub.Workspaces.switch_to_default_content()
        WFHub._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("20", STEP_20)