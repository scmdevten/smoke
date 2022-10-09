"""-------------------------------------------------------------------------------------------
Author Name  : HJEEVANA@TIBCO.COM
Automated On : 13-July-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub

class C9958308_TestClass(BaseTestCase):
    
    def test_C9958308(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        """
        TEST CASE VAIABLES
        """
        
        Small_Widgets_contents = ['Category Sales', 'Regional Sales Trend', 'Discount by Region', 'Regional Profit by Category', 'Average Cost v Sales', 'Average Cost vs Revenue Scatter', 'Product Profit Line By Month', 'Revenue Product Bar', 'Revenue Region Bar']
        
        STEP_01 = """
            STEP 01 : Sign into 'TIBCO WebFOCUS' as Developer User
        """
        WFHub.invoke_with_login('mriddev', 'mrpassdev')
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar > Click on 'Workspaces' view > Expand 'Workspaces' > Click on 'P215_S31921' workspaces from the resource tree
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921')
        WFHub.Workspaces.ContentArea.delete_file_if_exists('Category Sales_1')
        WFHub.Workspaces.ContentArea.delete_folder_if_exists('Test_drag')
        WFHub._utils.wait_for_page_loads(30)
        WFHub._utils.capture_screenshot("02", STEP_02)
        
        STEP_03 = """
            STEP 03 : Click on the '+ Content' button > Hover over the mouse on the 'Other' option > Click on the 'Folder'
        """
        WFHub.Workspaces.NavigationBar.ContentButton.click()
        WFHub.ContextMenu.select("Other->Folder")
        WFHub._utils.capture_screenshot("03", STEP_03)
        
        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify New folder dialogue opens
        """
        WFHub.Dialog.NewFolder.verify_title('New Folder', 03.01)
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)
        
        STEP_04 = """
            STEP 04 : Enter Title as 'Test_drag' > Click 'OK'
        """
        WFHub.Dialog.NewFolder.Title.enter_text('Test_drag')
        WFHub.Dialog.NewFolder.Ok.click()
        WFHub._utils.wait_for_page_loads(10)
        WFHub._utils.capture_screenshot("04", STEP_04)
        
        STEP_04_EXPECTED = """
            STEP 04 - Expected : 'Test_drag' unpublished folder is created under 'P215_S31921'.
        """
        WFHub.Workspaces.ContentArea.verify_unpublished_folders(['Test_drag'], 04.01)
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Expand Retail Samples > Portal > Select 'Small Widgets' folder from the resource tree.
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->Retail Samples->Portal->Small Widgets')
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify all the contents underneath 'Small Widgets' folder are displayed in content area.
        """
        WFHub.Workspaces.ContentArea.verify_files(Small_Widgets_contents, 05.01)
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right-click on **Category Sales** > Select 'Duplicate' from context menu
        """
        WFHub.Workspaces.ContentArea.right_click_on_file('Category Sales')
        WFHub.ContextMenu.select('Duplicate')
        WFHub._utils.wait_for_page_loads(10)
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify 'Category Sales_1' duplicated item is created.
        """
        WFHub.Workspaces.ContentArea.verify_files(['Category Sales_1'], 06.01)
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : **Case I: Drag & Drop contents from Content area to Resource tree.**
    
            Drag 'Category Sales_1' from content area and drop it on 'P215_S31921' workspace under resource tree.
        """
        WFHub.Workspaces.ContentArea.drag_and_drop_files_into_worksapces('Category Sales_1', 'P215_S31921')
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : A warning message is popped on the screen,
        """
        WFHub.Dialog.Warning.verify_title('Warning', 07.01)
        WFHub._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click 'Yes' in warning message.
        """
        WFHub.Dialog.Warning.Yes.click()
        WFHub._utils.wait_for_page_loads(15)
        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify 'Category Sales_1' is not present under Retail Samples >> Portal >> 'Small Widgets'.
        """
        WFHub.Workspaces.ContentArea.verify_files(['Category Sales_1'], 08.01, assert_type='asnotin')
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Select 'P215_S31921' workspace from resource tree.
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921')
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify 'Category Sales_1' is present underneath,
        """
        WFHub.Workspaces.ContentArea.verify_files(['Category Sales_1'], 09.01)
        WFHub._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Right-Click on 'Category Sales_1' > Select 'Publish' from context menu.
        """
        WFHub.Workspaces.ContentArea.right_click_on_file('Category Sales_1')
        WFHub.ContextMenu.select('Publish')
        WFHub._utils.wait_for_page_loads(15)
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify 'Category Sales_1' is in published state.
        """
        WFHub.Workspaces.ContentArea.verify_published_files(['Category Sales_1'], 10.01)
        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : **Case II: Drag & Drop contents from Content area to Content area.**
    
            Drag 'Category Sales_1' from content area of 'P215_S31921' workspace & drop it on un-published 'Test_drag' folder in content area.
        """
        WFHub.Workspaces.ContentArea.drag_and_drop_files_into_contentarea('Category Sales_1', 'Test_drag')
        WFHub._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : A warning message is popped on the screen,
        """
        WFHub.Dialog.Warning.verify_title('Warning', 11.01)   
        WFHub._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click 'Yes' in warning message.
        """
        WFHub.Dialog.Warning.Yes.click()
        WFHub._utils.wait_for_page_loads(15)
        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify 'Category Sales_1' is moved underneath P215_S31921 > 'Test_drag' folder & reverted back to un-published state.
        """
        WFHub.Workspaces.ContentArea.double_click_on_folder('Test_drag')
        WFHub.Workspaces.ContentArea.verify_files(['Category Sales_1'], 12.01)
        WFHub.Workspaces.ContentArea.verify_unpublished_files(['Category Sales_1'], 12.02)
        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Select 'P215_S31921' workspace from Resource tree & expand it.
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921')
        WFHub.Workspaces.ResourcesTree.expand('P215_S31921')
        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : **Case III: Drag & Drop contents from Resource tree to Content area.**
    
            Drag 'Test_drag' from resource tree underneath P215_S319121 workspace & drop it on 'My Content' folder in content area.
        """
        WFHub.Workspaces.ContentArea.drag_and_drop_files_tree_into_contentarea('Test_drag', 'My Content')
        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : A warning message is popped on the screen,
        """
        WFHub.Dialog.Warning.verify_title('Warning', 14.01)  
        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click 'Yes' in warning message.
        """
        WFHub.Dialog.Warning.Yes.click()
        WFHub._utils.wait_for_page_loads(15)
        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify 'Test_drag' folder is moved underneath P215_S319121 > 'My Content' folder in published state.
        """
        WFHub.Workspaces.ContentArea.verify_folders(['Test_drag'], 15.01)
        WFHub.Workspaces.ContentArea.verify_published_folders(['Test_drag'], 15.02)
        WFHub._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Double click on 'Test_drag' folder.
        """
        WFHub.Workspaces.ContentArea.double_click_on_folder('Test_drag')
        WFHub._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify 'Category Sales_1' is published.
        """
        WFHub.Workspaces.ContentArea.verify_files(['Category Sales_1'], 16.01)
        WFHub.Workspaces.ContentArea.verify_published_files(['Category Sales_1'], 16.02)
        WFHub._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Right-click on 'Test_drag' under My Content folder > Select 'Delete' from context menu.
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('My Content')
        WFHub.Workspaces.ContentArea.right_click_on_folder('Test_drag')
        WFHub.ContextMenu.select('Delete')
        WFHub._utils.wait_for_page_loads(15)
        WFHub._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify the following dialogue appears
        """
        WFHub.Dialog.Delete.verify_title('Delete', 17.01)
        WFHub._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Click 'OK'
        """
        WFHub.Dialog.Delete.Ok.click()
        WFHub._utils.wait_for_page_loads(30)
        WFHub._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify 'Test_drag' folder is deleted.
        """
        WFHub.Workspaces.ContentArea.verify_folders(['Test_drag'], 18.01, assert_type='asnotin')
        WFHub._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Workspaces.switch_to_default_content()
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select('Sign Out')
        WFHub._utils.capture_screenshot("19", STEP_19)

