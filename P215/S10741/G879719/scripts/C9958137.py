"""-------------------------------------------------------------------------------------------
Author Name  : HJEEVANA@TIBCO.COM
Automated On : 21-July-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub 

class C9958137_TestClass(BaseTestCase):
    
    def test_C9958137(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        STEP_01 = """
            STEP 01 : Sign into 'TIBCO WebFOCUS' as Admin User
        """
        WFHub.invoke_with_login("mridadm", "mrpassadm")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_01_EXPECTED = """
            STEP 01 - Expected : Verify the following options are available in the left side navigation bar
        """
        WFHub.LeftSideNavigationBar.Home.click()
        WFHub.Home.wait_for_text("Favorites", time_out=120)
        WFHub.Home.verify_available_view(['Recently worked on', 'Shared with me', 'My workspace', 'Favorites'], "01")
        WFHub._utils.capture_screenshot("01 - Expected", STEP_01_EXPECTED, True)

        STEP_02 = """
            STEP 02 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Sign into 'TIBCO WebFOCUS' as Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify the following options are available in the left side navigation bar
        """
        WFHub.LeftSideNavigationBar.Home.click()
        WFHub.Home.wait_for_text("Favorites", time_out=120)
        WFHub.Home.verify_available_view(['Recently worked on', 'Shared with me', 'My workspace', 'Favorites'], "03")
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on the 'User profile' banner link > Click 'Sign Out'
        """ 
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Sign into 'TIBCO WebFOCUS' as Basic User
        """
        WFHub.invoke_with_login("mridbas", "mrpassbas")
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the following options are available in the left side navigation bar
        """
        WFHub.LeftSideNavigationBar.Home.click()
        WFHub.Home.wait_for_text("Favorites", time_out=120)
        WFHub.Home.verify_available_view(['Recently worked on', 'Shared with me', 'Favorites'], "05")
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Sign into 'TIBCO WebFOCUS' as Advanced User
        """
        WFHub.invoke_with_login("mridadv", "mrpassadv")
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the following options are available in the left side navigation bar
        """
        WFHub.LeftSideNavigationBar.Home.click()
        WFHub.Home.wait_for_text("Favorites", time_out=120)
        WFHub.Home.verify_available_view(['Recently worked on', 'Shared with me', 'My workspace', 'Favorites'], "07")
        WFHub._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Sign into 'TIBCO WebFOCUS' as GroupAdmin User
        """
        WFHub.invoke_with_login("mridgadm", "mrpassgadm")
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the following options are available in the left side navigation bar
        """
        WFHub.LeftSideNavigationBar.Home.click()
        WFHub.Home.wait_for_text("Recently", time_out=120)
        WFHub.Home.verify_available_view(['Recently worked on', 'Shared with me'], "09")
        WFHub._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("10", STEP_10)