"""-------------------------------------------------------------------------------------------
Author Name  : RAJESH RAVICHANDRAN
Automated On : 23-November-2021
-------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub 

class C9958304_TestClass(BaseTestCase):
    
    def test_C9958304(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        """
        TEST CASE VAIABLES
        """
        
        STEP_01 = """
            STEP 01 : Sign into 'TIBCO WebFOCUS' as Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar > Click on 'Workspaces' button > Expand 'Workspaces' node > Click on 'Retail Samples' workspaces from the resource tree
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify by default the view is set to tile view,
        """
        WFHub.Banner.PlusMenu.Button.click()
        WFHub.Banner.PlusMenu.wait_for_text("Get Data")
        WFHub._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Hover on toggle ![](index.php?/attachments/get/1891526) icon on the top right banner below search bar.
        """

        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify it displays tooltip 'Switch to list view'
        """

        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click  on toggle ![](index.php?/attachments/get/1891526) icon on the top right banner below search bar.
        """

        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify view changes from 'Tile View' to 'List View'
        """

        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Hover on toggle ![](index.php?/attachments/get/1891534) icon on the top right banner below search bar.
        """

        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify it displays tooltip 'Switch to grid view'
        """

        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on 'Choose columns' button next to the last column heading.
        """

        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify 'Title', 'Name', 'Summary', 'Last Modified', 'Created on', 'Size', 'Owner', 'Published' and 'Shown' are listed in drop down box
        """

        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Un-check 'Summary' from the drop down list.
        """

        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify 'Summary' heading does not appear and drop down list remains open.
        """

        WFHub._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Check 'Summary' from the drop down list.
        """

        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify 'Summary' heading appears and drop down list remains open.
        """

        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click anywhere outside drop down list.
        """

        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify drop down list disappears.
        """

        WFHub._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click on toggle ![](index.php?/attachments/get/1891534) icon on the top right banner below search bar.
        """

        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify display changes from 'List View' to 'Tile View'.
        """

        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : From the left side navigation bar > Click on 'Workspaces' view > Expand 'Workspaces' > 'Retail Samples' workspaces > Click on 'Reports' folder from the resource tree
        """

        WFHub._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify the following:
    
            * Folder appear first, followed by 4 reports aligned in alphabetical order in Grid view.
            * 'Default Sort' with upward arrow grayed out is displayed at the right corner of the content area.
        """

        WFHub._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click on 'Default sort' button.
        """

        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify drop down list,
        """

        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Select 'Title' from the drop down list
        """

        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify the following:
    
            * Sort arrow appears next to 'Title' pointing upward direction.
            * Folder is displayed first and followed by 4 reports which are aligned alphabetically in ascending order.
        """

        WFHub._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Select upward arrow button besides 'Title'.
        """

        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the following:
    
            * Sort arrow appears next to 'Title' pointing downward direction.
            * Folder is displayed first and followed by 4 reports which are aligned alphabetically in descending order.
        """

        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click on 'Title' button >> Select 'Default Sort' from the drop down list.
        """

        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify the following:
    
            * Folder appear first, followed by 4 reports aligned in alphabetical order in Tile view.
            * 'Default Sort' with upward arrow grayed out is displayed at the right corner of the content area.
        """

        WFHub._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Click on toggle ![](index.php?/attachments/get/1891526) icon on the top right banner below search bar.
        """

        WFHub._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify the following:
    
            * Display changes from 'Tile View' to 'List View'.
            * No sort arrow appears next to any heading. 
            * Folder appear first, followed by 4 reports in alphabetical order.
        """

        WFHub._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Click on **Title** heading
        """

        WFHub._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify the following:
    
            * Sort arrow appears next to 'Title' pointing downward direction.
            * Folder is displayed first and followed by 4 reports which are sorted alphabetically in descending order.
        """

        WFHub._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Click on **Title** heading (twice).
        """

        WFHub._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify the following:
    
            * Sort arrow appears next to 'Title' pointing upward direction.
            * Folder is displayed first and followed by 4 reports which are sorted alphabetically in ascending order.
        """

        WFHub._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Click on **Title** heading (thrice).
        """

        WFHub._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify the following:
            * No sorting arrow appears next to 'Title'.
            * Folder is displayed first and followed by 4 reports which are sorted alphabetically in ascending order.
        """

        WFHub._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Click on the 'User profile' banner link > Click 'Sign Out'
        """

        WFHub._utils.capture_screenshot("20", STEP_20)