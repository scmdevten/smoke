"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh Ravichandran
Automated On : 22-January-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub

class C9953034_TestClass(BaseTestCase):
    
    def test_C9953034(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        """
        TEST CASE VAIABLES
        """
        portal_content = "div.domains-item-div"
        infoassist_menu = "div#splash_options"
        infoassist_options = "div#splash_options div#splash_bar_content div[id*='splash_options']"
        infographics  = "div#easel-container p.login_description"
        
        STEP_01 = """
            STEP 01 : Sign into 'TIBCO WebFOCUS' as Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the Header toolbar > Click on the 'Main Menu' button
        """
        WFHub.Banner.MainMenu.Button.click()
        WFHub.Banner.MainMenu.wait_for_text("Home")
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify the following options,
        """
        WFHub.Banner.MainMenu.verify_menu_options(['Home', 'Workspaces', 'Application Directories', 'Portals', 'Management Center', 'Search'], "02.01")
        WFHub.Banner.MainMenu.verify_quick_access_options(['InfoAssist', 'WebFOCUS Infographics', 'ReportCaster Status', 'ReportCaster Explorer', 'Magnify Search'], "02.02")
        WFHub._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Under 'Menu' section > Click on 'Home'
        """
        WFHub.Banner.MainMenu.select_menu_option("Home")
        WFHub.Banner.MainMenu.wait_for_invisible()
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that 'Home' is selected in the left side navigation bar and its related contents are displayed in the content area
        """
        WFHub.Home.wait_for_text("Recently", time_out=100)
        WFHub.LeftSideNavigationBar.Home.verify_background_color("midnight_express", "03.01")
        WFHub.Home.verify_available_view(['Recently worked on', 'Shared with me', 'My workspace', 'Favorites'], "03.02", assert_type="in")
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on the 'Main Menu' button > Under 'Menu' section > Click on 'Workspaces'
        """
        WFHub.Banner.MainMenu.Button.click()
        WFHub.Banner.MainMenu.wait_for_text("Home")
        WFHub.Banner.MainMenu.select_menu_option("Workspaces")
        WFHub.Banner.MainMenu.wait_for_invisible()
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify that 'Workspaces' is selected in the left side navigation bar and its related contents are displayed in the content area
        """
        WFHub.LeftSideNavigationBar.Workspaces.verify_background_color("midnight_express", "04.01")
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.wait_for_text("Content", time_out=100)
        WFHub.Workspaces.ResourcesTree.verify_items(["Workspaces"], "04.02")
        WFHub.Workspaces.switch_to_default_content()
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on the 'Main Menu' button > Under 'Menu' section > Click on 'Application Directories'
        """
        WFHub.Banner.MainMenu.Button.click()
        WFHub.Banner.MainMenu.wait_for_text("Home")
        WFHub.Banner.MainMenu.select_menu_option("Application Directories")
        WFHub.Banner.MainMenu.wait_for_invisible()
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that 'Application Directories' is selected in the left side navigation bar and its related contents are displayed in the content area
        """
        WFHub.LeftSideNavigationBar.ApplicationDirectories.verify_background_color("midnight_express", "05.01")
        WFHub.ApplicationDirectories.switch_to_frame()
        WFHub.ApplicationDirectories.RibbonBar.wait_for_text("Get", time_out=100)
        WFHub.ApplicationDirectories.RibbonBar.verify_ribbon_bar_options(['Get Data', 'Filter', 'Manage'], "05.01")
        WFHub.ApplicationDirectories.switch_to_default_content()
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on the 'Main Menu' button > Under 'Menu' section > Click on 'Portals'
        """
        WFHub.Banner.MainMenu.Button.click()
        WFHub.Banner.MainMenu.wait_for_text("Home")
        WFHub.Banner.MainMenu.select_menu_option("Portals")
        WFHub.Banner.MainMenu.wait_for_invisible()
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that 'Portals' is selected in the left side navigation bar and its related contents are displayed in the content area
        """
        WFHub.LeftSideNavigationBar.Portals.verify_background_color("midnight_express", "06.01")
        WFHub.Portals.switch_to_frame()
        WFHub._utils.synchronize_until_element_is_visible(portal_content, 120)
        WFHub._utils.verify_element_visiblty(element_css=portal_content, msg="Step 06.02: Verify Portals Content is visible")
        WFHub.Portals.switch_to_default_content()
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on the 'Main Menu' button > Under 'Menu' section > Click on 'Management Center'
        """
        WFHub.Banner.MainMenu.Button.click()
        WFHub.Banner.MainMenu.wait_for_text("Home")
        WFHub.Banner.MainMenu.select_menu_option("Management Center")
        WFHub.Banner.MainMenu.wait_for_invisible()
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify that 'Management Center' is selected in the left side navigation bar and its related contents are displayed in the content area
        """
        WFHub.LeftSideNavigationBar.ManagementCenter.verify_background_color("midnight_express", "07.01")
        WFHub._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : From the Header toolbar > Click on the 'Main Menu' button > Under 'Quick Access' section > Click on 'InfoAssist'
        """
        WFHub.Banner.MainMenu.Button.click()
        WFHub.Banner.MainMenu.wait_for_text("Home")
        WFHub.Banner.MainMenu.select_quick_access_option("InfoAssist")
        WFHub.Banner.MainMenu.wait_for_invisible()
        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify 'TIBCO WebFOCUS InfoAssist' window opens with the splash screen dialog,
        """
        WFHub._core_utils.switch_to_new_window()
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Close the 'TIBCO WebFOCUS InfoAssist' splash screen dialog > Close the 'TIBCO WebFOCUS InfoAssits' window
        """
        WFHub._utils.synchronize_with_visble_text(infoassist_menu, "Build", 60)
        WFHub._webelement.verify_elements_text((WFHub._By.CSS_SELECTOR, infoassist_options), ['Getting Started', 'Build a Report', 'Build a Chart', 'Build a Document', 'Build a Visualization', 'Open Existing Item', 'Change Default Options', 'Close Application'], "09", "Infoassist Options")
        WFHub._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : From the Home Header toolbar > Click on the 'Main Menu' button  > Under 'Quick Access' section > Click on 'WebFOCUS Infographics'
        """
        WFHub.Banner.MainMenu.Button.click()
        WFHub.Banner.MainMenu.wait_for_text("Home")
        WFHub.Banner.MainMenu.select_quick_access_option("WebFOCUS Infographics")
        WFHub.Banner.MainMenu.wait_for_invisible()
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify 'TIBCO WebFOCUS|Infographics' window opens in a new tab,
        """
        WFHub._core_utils.switch_to_new_window()
        current_url = self.driver.current_url
        WFHub._utils.verify_current_tab_name('easel.ly | create and share visual ideas using infographics',"Step 10.01 : Verify webfocus infographics Page URL")
        WFHub._utils.asequal(current_url,'https://webfocus.easel.ly/','Step 10.02 : Verify the infographics URl')
        WFHub._webelement.verify_elements_text((WFHub._By.CSS_SELECTOR, infographics), ['Welcome to WebFOCUS Infographics, powered by Easelly.'], "10.03", "Infographics")
        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Close the 'TIBCO WebFOCUS|Infographics' window
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : From the Home Header toolbar > Click on the 'Main Menu' button > Under 'Quick Access' section > Click on 'ReportCaster Status'
        """
        WFHub.Banner.MainMenu.Button.click()
        WFHub.Banner.MainMenu.wait_for_text("Home")
        WFHub.Banner.MainMenu.select_quick_access_option("ReportCaster Status")
        WFHub.Banner.MainMenu.wait_for_invisible()
        WFHub._core_utils.switch_to_new_window()
        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify that 'TIBCO WebFOCUS ReportCaster Status' window opens in a new tab,
        """
        WFHub._utils.verify_current_url('rcc.rc', "Step 12.01 : Verify Report Caster Status URL")
        WFHub._utils.verify_current_tab_name("TIBCO WebFOCUS Schedule Status",'Step 12.02 : Verify the window displayed with ReportCaster Status')
        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Close the 'TIBCO WebFOCUS ReportCaster Status' window
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : From the Home Header toolbar > Click on the 'Main Menu' button > Under 'Quick Access' section > Click on 'ReportCaster Explorer'
        """
        WFHub.Banner.MainMenu.Button.click()
        WFHub.Banner.MainMenu.wait_for_text("Home")
        WFHub.Banner.MainMenu.select_quick_access_option("ReportCaster Explorer")
        WFHub.Banner.MainMenu.wait_for_invisible()
        WFHub._core_utils.switch_to_new_window()
        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify that 'TIBCO WebFOCUS ReportCaster Explorer' window opens in a new tab,
        """
        WFHub._utils.verify_current_url('rcex.rc',"Step 14.01 : Verify the session viewer URL")
        WFHub._utils.verify_current_tab_name("TIBCO WebFOCUS Schedule Explorer",'Step 14.02 : Verify the window displayed with Report Caster Explorer')
        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Close the 'TIBCO WebFOCUS ReportCaster Explorer' window
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : From the Home Header toolbar > Click on the 'Main Menu' button > Under 'Quick Access' section > Click on 'Magnify Search'
        """
        WFHub.Banner.MainMenu.Button.click()
        WFHub.Banner.MainMenu.wait_for_text("Home")
        WFHub.Banner.MainMenu.select_quick_access_option("Magnify Search")
        WFHub.Banner.MainMenu.wait_for_invisible()
        WFHub._core_utils.switch_to_new_window()
        WFHub._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify that 'Magnify Search' window opens in a new tab without any error,
        """
        WFHub._utils.verify_current_url('search/',"Step 16.01 : Verify magnify Search Page URL")
        WFHub._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Close the 'Magnify Search' window
        """
        WFHub._core_utils.switch_to_previous_window()
        WFHub._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : Click on the 'Main Menu' button > Click 'X' to close the main menu
        """
        WFHub.Banner.MainMenu.Button.click()
        WFHub.Banner.MainMenu.wait_for_text("Home")
        WFHub.Banner.MainMenu.click_on_close_button()
        WFHub.Banner.MainMenu.wait_for_invisible()
        WFHub._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify that the 'Main Menu' box closed
        """
        WFHub.Banner.MainMenu.verify_main_menu_closed("18")
        WFHub._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("19", STEP_19)

