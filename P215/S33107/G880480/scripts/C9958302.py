"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh Ravichandran
Automated On : 24-January-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub

class C9958302_TestClass(BaseTestCase):
    
    def test_C9958302(self):
        
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
            STEP 02 : From the left side navigation bar > Click on 'Management Center'
        """
        WFHub.LeftSideNavigationBar.ManagementCenter.click()
        WFHub.ManagementCenter.wait_for_text("Security Center", time_out=120)
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify the following options displayed under Management Center,
        """
        WFHub.ManagementCenter.verify_available_menu_options(['Administration Console', 'Security Center', 'Private Resources', 'Import Packages', 'Export Packages', 'Magnify Console', 'Server Preferences', 'Access Control', 'Server Workspaces', 'Resource Management', 'Scalability'], "02")
        WFHub._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Sign into 'TIBCO WebFOCUS' as Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub.LeftSideNavigationBar.ManagementCenter.click()
        WFHub.ManagementCenter.wait_for_text("Server", time_out=120)
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify the following options displayed under Management Center,
        """
        WFHub.ManagementCenter.verify_available_menu_options(['Server Preferences', 'Server Workspaces'], "04")
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Sign into 'TIBCO WebFOCUS' as Basic User
        """
        WFHub.invoke_with_login("mridbas", "mrpassbas")
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that 'Management Center' option is not available
        """
        try:
            WFHub.LeftSideNavigationBar.ManagementCenter.click()
            value = False
        except AttributeError:
            value = True
        WFHub._utils.asequal(True, value, "Step 06: Verify that 'Management Center' option is not available")
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Sign into 'TIBCO WebFOCUS' as Advanced User
        """
        WFHub.invoke_with_login("mridadv", "mrpassadv")
        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that 'Management Center' option is not available
        """
        try:
            WFHub.LeftSideNavigationBar.ManagementCenter.click()
            value = False
        except AttributeError:
            value = True
        WFHub._utils.asequal(True, value, "Step 08: Verify that 'Management Center' option is not available")
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Sign into 'TIBCO WebFOCUS' as Group Admin User
        """
        WFHub.invoke_with_login("mridgadm", "mrpassgadm")
        WFHub.LeftSideNavigationBar.ManagementCenter.click()
        WFHub.ManagementCenter.wait_for_text("Security Center", time_out=120)
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify the following options displayed under Management Center,
        """
        WFHub.ManagementCenter.verify_available_menu_options(['Security Center', 'Private Resources'], "10")
        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("11", STEP_11)
