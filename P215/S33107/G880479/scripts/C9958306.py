"""-------------------------------------------------------------------------------------------
Author Name  : HJEEVANA@TIBCO.COM
Automated On : 07-July-2022
-------------------------------------------------------------------------------------------"""

import keyboard
from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub

class C9958306_TestClass(BaseTestCase):
    
    def test_C9958306(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        """
        TEST CASE VAIABLES
        
        """
        STEP_01 = """
            STEP 01 : Sign into 'TIBCO WebFOCUS Hub' as a Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar > Click on the 'Workspaces' icon > Expand 'Workspaces' > Click on 'P215_S31921' workspaces from the resource tree
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        WFHub.Workspaces.ResourcesTree.expand("Workspaces")
        WFHub.Workspaces.ResourcesTree.select("P215_S31921")
        WFHub.Workspaces.ContentArea.delete_folder_if_exists('C9958306_Folder')
        WFHub._utils.capture_screenshot("02", STEP_02)
        
        STEP_03 = """
            STEP 03 : Click on the '+ Content' button > Hover over the mouse on the 'Other' option > Click on the 'Folder'
        """
        WFHub.Workspaces.NavigationBar.ContentButton.click()
        WFHub.ContextMenu.hover_over_content_options("Other")
        WFHub.ContextMenu.select("Other->Folder")
        WFHub._utils.capture_screenshot("03", STEP_03)
        
        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify New folder dialogue opens
        """
        WFHub.Dialog.NewFolder.verify_title("New Folder", 03.01)
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)
        
        STEP_04 = """
            STEP 04 : Enter title as 'C9958306_Folder' > Click on 'OK'
        """
        WFHub.Dialog.NewFolder.Title.enter_text('C9958306_Folder')
        WFHub.Dialog.NewFolder.Ok.click()
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("04", STEP_04)
        
        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify 'C9958306_Folder' folder has been created and it is unpublished
        """
        WFHub.Workspaces.ContentArea.verify_unpublished_folders(['C9958306_Folder'], 04.01)
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)
        
        STEP_05 = """
            STEP 05 : Right click on 'C9958306_Folder' > Click on 'Publish'
        """
        WFHub.Workspaces.ContentArea.right_click_on_folder('C9958306_Folder')
        WFHub.ContextMenu.select("Publish")
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("05", STEP_05)
        
        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify 'C9958306_Folder' has been Published
        """
        WFHub.Workspaces.ContentArea.verify_published_folders(['C9958306_Folder'], 05.01)
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)
        
        STEP_06 = """
            STEP 06 : Expand 'Retail Samples' > 'Portal' > 'Test Widgets' from resource tree
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        WFHub._utils.capture_screenshot("06", STEP_06)
        
        STEP_07 = """
            STEP 07 : Right click 'Test Widgets' folder > Select 'Copy'
        """
        WFHub.Workspaces.ResourcesTree.right_click('Workspaces->Retail Samples->Portal->Test Widgets')
        WFHub.ContextMenu.select('Copy')
        WFHub._utils.capture_screenshot("07", STEP_07)
        
        STEP_08 = """
            STEP 08 : Right-click 'C9958306_Folder' folder from resource tree > Select 'Paste'
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        WFHub.Workspaces.ResourcesTree.right_click('Workspaces->P215_S31921->C9958306_Folder')
        WFHub.ContextMenu.select('Paste')
        WFHub._utils.capture_screenshot("08", STEP_08)
        
        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify 'Test Widgets' is copied and placed under 'C9958306_Folder' from resource tree.
        """
        WFHub.Workspaces.ResourcesTree.expand('C9958306_Folder')
        WFHub.Workspaces.ResourcesTree.verify_items(['Test Widgets'], 08.01)
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)
        
        STEP_09 = """
            STEP 09 : Click on 'Retail Samples' workspace from the resourec tree > Double-click on 'Reports' folder in Content area > Right-click on **Margin by Product Category** > Select 'Copy'
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        WFHub.Workspaces.ResourcesTree.select('Workspaces->Retail Samples')
        WFHub.Workspaces.ContentArea.double_click_on_folder('Reports')
        WFHub.Workspaces.ContentArea.right_click_on_file('Margin by Product Category')
        WFHub.ContextMenu.select('Copy')
        WFHub._utils.capture_screenshot("09", STEP_09)
        
        STEP_10 = """
            STEP 10 : Click on 'P215_S31921' workspaces from the resource tree > Right-click on 'C9958306_Folder' from the Content area > Select 'Paste'.
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921')
        WFHub.Workspaces.ContentArea.right_click_on_folder('C9958306_Folder')
        WFHub.ContextMenu.select('Paste')
        WFHub._utils.capture_screenshot("10", STEP_10)
        
        STEP_10_EXPECTED = """
            STEP 10 - Expected : Click on 'C9958306_Folder' from resource tree > Verify **Margin by Product Category** report is copied under 'C9958306_Folder'.
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921->C9958306_Folder')
        WFHub.Workspaces.ContentArea.verify_files(['Margin by Product Category'], 10.01)
        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)
        
        STEP_11 = """
            STEP 11 : Double click on copied 'Reports' folder > Run **Margin by Product Category**
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->Retail Samples->Reports')
        WFHub.Workspaces.ContentArea.right_click_on_file('Margin by Product Category')
        WFHub.ContextMenu.select('Run')
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("11", STEP_11)
        
        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify output is displayed without any errors,
        """
        
        WFHub.RunWindow.verify_title('Margin by Product Category', 11.01)
        WFHub._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)
        
        STEP_12 = """
            STEP 12 : Close the 'Run' window
        """
        WFHub.RunWindow.close()
        WFHub._utils.capture_screenshot("12", STEP_12)
        
        STEP_13 = """
            STEP 13 : Right-click on **Margin by Product Category** from content area > Select 'Cut'
        """
        WFHub.Workspaces.ContentArea.right_click_on_file('Margin by Product Category')
        WFHub.ContextMenu.select('Cut')
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("13", STEP_13)
        
        STEP_13_EXPECTED = """
            STEP 13 - Expected : Observe the report thumbnail fades while performing 'Cut' operation,
        """
        WFHub._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)
        
        STEP_14 = """
            STEP 14 : Expand 'P215_S31921' workspace > Right-click on 'My Content' folder from resource tree > Select 'Paste'
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.right_click('Workspaces->P215_S31921->My Content')
        WFHub.ContextMenu.select('Paste')
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("14", STEP_14)
        
        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify **Margin by Product Category** is moved under P215_S31921 > My Content folder.
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921->My Content')
        WFHub.Workspaces.ContentArea.verify_files(['Margin by Product Category'], 14.01)
        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)
        
        STEP_15 = """
            STEP 15 : Run fex **Margin by Product Category** in My Content folder
        """
        WFHub.Workspaces.ContentArea.right_click_on_file('Margin by Product Category')
        WFHub.ContextMenu.select('Run')
        WFHub._utils.wait_for_page_loads(5)
        WFHub._utils.capture_screenshot("15", STEP_15)
        
        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify output is displayed without any errors,
        """
        WFHub.RunWindow.verify_title('Margin by Product Category', 15.01)
        WFHub._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)
        
        STEP_16 = """
            STEP 16 : Close the 'Run' Window
        """
        WFHub.RunWindow.close()
        WFHub._utils.capture_screenshot("16", STEP_16)
        
        STEP_17 = """
             STEP 17 : Under 'P215_S31921' workspace > Click on 'My Content' folder > Select **Margin by Product Category** > using keyboard shortcut press **Ctrl+X** to Cut.
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921->My Content')
        WFHub.Workspaces.ContentArea.select_file('Margin by Product Category')
        keyboard.press_and_release('ctrl+x')
        WFHub._utils.capture_screenshot("17", STEP_17)
        

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Observe the report thumbnail fades while performing 'Cut' operation,
        """
        
        WFHub._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)
        
        STEP_18 = """
            STEP 18 : Click on 'P215_S31921' workspace > Click on empty space in the content area > Using keyboard shortcut press **Ctrl+V** to Paste.
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921')
        WFHub.Workspaces.ContentArea.select_folder('C9958306_Folder')
        keyboard.press_and_release('ctrl+v')
        WFHub._utils.wait_for_page_loads(10)
        WFHub._utils.capture_screenshot("18", STEP_18)
        
        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify **Margin by Product Category** is pasted under 'P215_S31921' workspace.
        """
        WFHub.Workspaces.ContentArea.verify_files(['Margin by Product Category'], 18.01)
        WFHub._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)
        
        STEP_19 = """
            STEP 19 : Click on 'P215_S31921' workspace > Select report **Margin by Product Category** from content area > Using keyboard press **Ctrl+C** to Copy.
        """
        WFHub.Workspaces.ContentArea.select_file('Margin by Product Category')
        keyboard.press_and_release('ctrl+c')
        WFHub._utils.capture_screenshot("19", STEP_19)
        
        STEP_19_EXPECTED = """
            STEP 19 - Expected : Observe the report thumbnail does not fade while performing 'Copy' operation,
        """
        
        WFHub._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)
        
        STEP_20 = """
            STEP 20 : Under 'P215_S31921' workspace > Click on 'My Content' folder from the resource tree> Click on empty space in the content area > Using keyboard press **Ctrl+V** to Paste.
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921->My Content')
        keyboard.press_and_release('ctrl+v')
        WFHub._utils.wait_for_page_loads(10)
        WFHub._utils.capture_screenshot("20", STEP_20)
        
        STEP_20_EXPECTED = """
            STEP 20 - Expected : Verify **Margin by Product Category** is pasted under P215_S31921 > My Content folder.
        """
        WFHub.Workspaces.ContentArea.verify_files(['Margin by Product Category'],20.01)
        WFHub._utils.capture_screenshot("20 - Expected", STEP_20_EXPECTED, True)
        
        STEP_21 = """
            STEP 21 : Right-click on copied **Margin by Product Category** > Select 'Delete'
        """
        WFHub.Workspaces.ContentArea.right_click_on_file('Margin by Product Category')
        WFHub.ContextMenu.select('Delete')
        WFHub._utils.capture_screenshot("21", STEP_21)
        
        STEP_21_EXPECTED = """
            STEP 21 - Expected : Verify the following dialogue appears
        """
        WFHub.Dialog.Delete.verify_title('Delete', 21.01)
        WFHub._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)
        
        STEP_22 = """
            STEP 22 : Click 'OK'
        """
        WFHub.Dialog.Delete.Ok.click()
        WFHub._utils.wait_for_page_loads(10)
        WFHub._utils.capture_screenshot("22", STEP_22)
    
        STEP_22_EXPECTED = """
            STEP 22 - Expected : Verify report is deleted under 'My Content' folder.
        """
        WFHub.Workspaces.ContentArea.verify_files(['Margin by Product Category'], 22.01, assert_type= 'asnotin')
        WFHub._utils.capture_screenshot("22 - Expected", STEP_22_EXPECTED, True)

        STEP_23 = """
            STEP 23 : Under 'P215_S31921' workspace > Right-click on **Margin by Product Category** from the content area > Select 'Delete'
        """
        WFHub.Workspaces.NavigationBar.select_breadcrumb('Workspaces')
        WFHub.Workspaces.ResourcesTree.select('Workspaces->P215_S31921')
        WFHub.Workspaces.ContentArea.right_click_on_file('Margin by Product Category')
        WFHub.ContextMenu.select('Delete')
        WFHub._utils.wait_for_page_loads(10)
        WFHub.Dialog.Delete.Ok.click()
        WFHub._utils.wait_for_page_loads(10)
        WFHub._utils.capture_screenshot("23", STEP_23)

        STEP_23_EXPECTED = """
            STEP 23 - Expected : Verify report is deleted under 'P215_S31921' workspace.
        """
        WFHub.Workspaces.ContentArea.verify_files(['Margin by Product Category'], 23.01, assert_type='asnotin')
        WFHub._utils.capture_screenshot("23 - Expected", STEP_23_EXPECTED, True)

        STEP_24 = """
            STEP 24 : Under 'P215_S31921' workspace > Right click on 'C9958306_Folder' from the resource tree > Select 'Delete'
        """
        WFHub.Workspaces.ContentArea.right_click_on_folder('C9958306_Folder')
        WFHub.ContextMenu.select('Delete')
        WFHub._utils.wait_for_page_loads(10)
        WFHub.Dialog.Delete.Ok.click()
        WFHub._utils.wait_for_page_loads(10,pause_time=5)
        WFHub._utils.capture_screenshot("24", STEP_24)

        STEP_24_EXPECTED = """
            STEP 24 - Expected : Verify sub-folder is deleted under the 'P215_S31921' workspace.
        """
        WFHub.Workspaces.ContentArea.verify_folders(['C9958306_Folder'], 24.01, assert_type='asnotin')
        WFHub._utils.capture_screenshot("24 - Expected", STEP_24_EXPECTED, True)

        STEP_25 = """
            STEP 25 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Workspaces.switch_to_default_content()
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select('Sign Out')
        WFHub._utils.capture_screenshot("25", STEP_25)

