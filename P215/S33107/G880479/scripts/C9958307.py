"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh Ravichandran
Automated On : 02-February-2022
-------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub

class C9958307_TestClass(BaseTestCase):
    
    def test_C9958307(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        
        STEP_01 = """
            STEP 01 : Sign into 'TIBCO WebFOCUS' as Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar > Click on 'Workspaces' view > Expand 'Workspaces' > Click on 'Retail Samples' workspaces from the resource tree
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_workspaces()
        WFHub.Workspaces.ResourcesTree.select("Workspaces->Retail Samples")
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Observe breadcrumb trail,
        """
        WFHub.Workspaces.NavigationBar.verify_breadcrumbs("Workspaces>Retail Samples", "02")
        WFHub._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Under Retail_Samples >> Select 'Documents' sub-folder.
        """
        WFHub.Workspaces.ResourcesTree.select("Workspaces->Documents")
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Observe breadcrumb trail,
        """
        WFHub.Workspaces.NavigationBar.verify_breadcrumbs("Workspaces>Retail Samples>Documents", "03")
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Under Retail_Samples >> Charts >> Select 'Auto Link Targets' sub-folder.
        """
        WFHub.Workspaces.ResourcesTree.select("Workspaces->Charts->Auto Link Targets")
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Observe breadcrumb trail,
        """
        WFHub.Workspaces.NavigationBar.verify_breadcrumbs("Workspaces>Retail Samples>Charts>Auto Link Targets", "04")
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Select '>' before 'Charts' under breadcrumb trail.
        """
        WFHub.Workspaces.NavigationBar.click_breadcrumb_arrow("Retail Samples")
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the following,
        """
        WFHub.ContextMenu.verify_options(['My Content', 'Charts', 'Documents', 'InfoApps', 'Mobile', 'Portal', 'Reports', 'Search', 'Visualizations', 'Hidden Content'], "05")
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Select '>' before 'Charts' under breadcrumb trail >> Select 'Portal'
        """
        WFHub.ContextMenu.select("Portal")
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify breadcrumb is modified & displays contents underneath 'Portals' section.
        """
        WFHub.Workspaces.NavigationBar.verify_breadcrumbs("Workspaces>Retail Samples>Portal", "06.01")
        WFHub.Workspaces.ContentArea.verify_files(['Retail Samples'], "06.02")
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on the 'User' banner link > Click 'Sign Out'
        """
        WFHub.Workspaces.switch_to_default_content()
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("07", STEP_07)