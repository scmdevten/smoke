"""-------------------------------------------------------------------------------------------
Author Name  : GRETHINA@TIBCO.COM
Automated On : 15-July-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub
from selenium.webdriver.common.by import By

class C9958305_TestClass(BaseTestCase):
    
    def test_C9958305(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        """
        TEST CASE VAIABLES
        """
        content             = (By.CSS_SELECTOR, ".toolbar-button-divset div[data-ibxp-glyph-classes='ds-icon-plus']")
        
        IA_REPORT_MENU= ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                               'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        IA_CHART_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                               'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        IA_VISUAL_MENU = ['Run', 'Run...', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                               'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        IA_DOCUMENT_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                               'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        IA_ALERT_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                               'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        
        DF_CHART_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                              'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        DF_REPORT_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                              'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        ASSEMBLE_PAGE_MENU = ['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut',
                             'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        EMBEDDED_PAGE_MENU = ['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut',
                             'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        
        V4_PORTAL_MENU = ['Run', 'Edit', 'Customizations' , 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties'] 
        
        PORTAL_PAGE_MENU = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Unlink Page', 'Unpublish', 'Hide', 'Security', 'Properties']
        
        V5_PORTAL_MENU = ['Open', 'Run', 'Edit', 'Customizations' , 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties'] 
        
        REPORTING_OBJECT_MENU = ['Run', 'Run...', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                                'Delete DEL', 'open_in_new New', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        
        SCHEDULE_MENU = ['Edit', 'Run', 'View log', 'Disable' , 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties'] 
        
        ACCESSLIST_MENU = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']   
        
        DISTRIBUTIONLIST_MENU = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']   
        
        IMAGE_MENU = ['View', 'View in new window',  'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                              'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        
        URL_MENU = ['View', 'View in new window', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                            'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        BLOG_MENU = ['Edit', 'Comments', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                             'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        TEXTEDITOR_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                                   'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        
        STEP_01 = """
            STEP 01 : Sign into 'TIBCO WebFOCUS' as Developer User
        """
        WFHub.invoke_with_login("mriddev", "mrpassdev")        
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar > Click on 'Workspaces' view > Expand 'Workspaces' > 'P215_S31921' workspaces > Click on 'G875466' folder from the resource tree
        """
        WFHub.LeftSideNavigationBar.Workspaces.click()
        WFHub.Workspaces.switch_to_frame()
        WFHub.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        WFHub.Workspaces.ResourcesTree.select("Workspaces->P215_S31921->G875466")
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Right click on 'IA_Report' in the content area
        """
        WFHub.Workspaces.ContentArea.right_click_on_file("IA_Report")
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify the context menu:
    
            - Run.
            - Run (Run in new window/Run deferred/Run with SQL trace).
            - Schedule (Email/FTP/Printer/Report Library/Repository).
            - Edit.
            - Edit with text editor.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(IA_REPORT_MENU, "03.01")
        WFHub.ContextMenu.select("Run...")
        WFHub.ContextMenu.verify_options(['Run in new window', 'Run deferred', 'Run with SQL trace'], "03.02",menu_path="Run...")
        WFHub.ContextMenu.select("Schedule")
        WFHub.ContextMenu.verify_options(['Email','FTP','Printer','Report Library','Repository'], "03.03",menu_path="Schedule")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "03.04",menu_path="Security")
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Right click on 'IA_Chart' in the content area
        """
        WFHub.Workspaces.ContentArea.right_click_on_file("IA_Chart")
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify the context menu:
    
            - Run.
            - Run (Run in new window/Run deferred/Run with SQL trace).
            - Schedule (Email/FTP/Printer/Report Library/Repository).
            - Edit.
            - Edit with text editor.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(IA_CHART_MENU, "04.01")
        WFHub.ContextMenu.select("Run...")
        WFHub.ContextMenu.verify_options(['Run in new window', 'Run deferred', 'Run with SQL trace'], "04.02",menu_path="Run...")
        WFHub.ContextMenu.select("Schedule")
        WFHub.ContextMenu.verify_options(['Email','FTP','Printer','Report Library','Repository'], "04.03",menu_path="Schedule")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "04.04",menu_path="Security")
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Right click on 'IA_Visual' in the content area.
        """
        WFHub.Workspaces.ContentArea.right_click_on_file("IA_Visual")
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the context menu:
    
            - Run.
            - Run (Run in new window).
            - Edit.
            - Edit with text editor.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(IA_VISUAL_MENU, "05.01")
        WFHub.ContextMenu.select("Run...")
        WFHub.ContextMenu.verify_options(['Run in new window'], "05.02",menu_path="Run...")       
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "05.03",menu_path="Security")
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right click on 'IA_Document' in the content area.
        """
        WFHub.Workspaces.ContentArea.right_click_on_file("IA_Document")
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify the context menu:
    
            - Run.
            - Run (Run in new window/Run deferred/Run with SQL trace).
            - Schedule (Email/FTP/Printer/Report Library/Repository).
            - Edit.
            - Edit with text editor.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(IA_DOCUMENT_MENU, "06.01")
        WFHub.ContextMenu.select("Run...")
        WFHub.ContextMenu.verify_options(['Run in new window', 'Run deferred', 'Run with SQL trace'], "06.02",menu_path="Run...")
        WFHub.ContextMenu.select("Schedule")
        WFHub.ContextMenu.verify_options(['Email','FTP','Printer','Report Library','Repository'], "06.03",menu_path="Schedule")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "06.04",menu_path="Security")
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right click on 'IA_Alert' in the content area.
        """
        WFHub.Workspaces.ContentArea.right_click_on_file("IA_Alert")
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the context menu:
    
            - Run.
            - Run (Run in new window/Run deferred).
            - Schedule (Email/FTP/Printer/Report Library/Repository).
            - Edit.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(IA_ALERT_MENU, "07.01")
        WFHub.ContextMenu.select("Run...")
        WFHub.ContextMenu.verify_options(['Run in new window', 'Run deferred'], "07.02",menu_path="Run...")
        WFHub.ContextMenu.select("Schedule")
        WFHub.ContextMenu.verify_options(['Email','FTP','Printer','Report Library','Repository'], "07.03",menu_path="Schedule")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "07.04",menu_path="Security")
        WFHub._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Right click on 'DF_Chart' in the content area.
        """
        outside = WFHub._utils.validate_and_get_webdriver_object_using_locator(content,"content for outside click")
        WFHub._core_utils.python_right_click(outside)
        WFHub.Workspaces.ContentArea.right_click_on_file("DF_Chart")
        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify the context menu:
    
            - Run.
            - Run (Run in new window/Run deferred/Run with SQL trace).
            - Schedule (Email/FTP/Printer/Report Library/Repository).
            - Edit.
            - Edit with text editor.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(DF_CHART_MENU, "08.01")
        WFHub.ContextMenu.select("Run...")
        WFHub.ContextMenu.verify_options(['Run in new window', 'Run deferred', 'Run with SQL trace'], "08.02",menu_path="Run...")
        WFHub.ContextMenu.select("Schedule")
        WFHub.ContextMenu.verify_options(['Email','FTP','Printer','Report Library','Repository'], "08.03",menu_path="Schedule")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "08.04",menu_path="Security")        
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Right click on chart 'DF_Report' in the content area.
        """
        outside = WFHub._utils.validate_and_get_webdriver_object_using_locator(content,"content for outside click")
        WFHub._core_utils.python_right_click(outside)
        WFHub.Workspaces.ContentArea.right_click_on_file("DF_Report")
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the context menu:
    
            - Run.
            - Run (Run in new window/Run deferred/Run with SQL trace).
            - Schedule (Email/FTP/Printer/Report Library/Repository).
            - Edit.
            - Edit with text editor.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(DF_REPORT_MENU, "09.01")
        WFHub.ContextMenu.select("Run...")
        WFHub.ContextMenu.verify_options(['Run in new window', 'Run deferred', 'Run with SQL trace'], "09.02",menu_path="Run...")
        WFHub.ContextMenu.select("Schedule")
        WFHub.ContextMenu.verify_options(['Email','FTP','Printer','Report Library','Repository'], "09.03",menu_path="Schedule")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "09.04",menu_path="Security")
        WFHub._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Right click on 'Assemble_Page' in the content area.
        """
        WFHub.Workspaces.ContentArea.right_click_on_file("Assemble_Page")
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify the context menu:
    
            - Run.
            - Run in new window.
            - Edit.
            - Download translations.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(ASSEMBLE_PAGE_MENU, "10.01")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "10.02",menu_path="Security")
        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Right click on 'Embedded_Page' in the content area.
        """
        outside = WFHub._utils.validate_and_get_webdriver_object_using_locator(content,"content for outside click")
        WFHub._core_utils.python_right_click(outside)
        WFHub.Workspaces.ContentArea.right_click_on_file("Embedded_Page")
        WFHub._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify the context menu:
    
            - Run.
            - Run in new window.
            - Edit.
            - Download translations.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(EMBEDDED_PAGE_MENU, "11.01")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "11.02",menu_path="Security")        
        WFHub._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Right click on 'V4_Portal' in the content area.
        """
        WFHub.Workspaces.ContentArea.right_click_on_file("V4_Portal")
        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify the context menu:
    
            - Run.
            - Edit.
            - Customizations (Remove my customizations/Remove customizations for all users).
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(V4_PORTAL_MENU, "12.01")           
        WFHub.ContextMenu.select("Customizations")
        WFHub.ContextMenu.verify_options(['Remove my customizations','Remove customizations for all users'], "12.02",menu_path="Customizations")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "12.03",menu_path="Security")
        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Right click on 'Portal_Page' in the content area.
        """
        outside = WFHub._utils.validate_and_get_webdriver_object_using_locator(content,"content for outside click")
        WFHub._core_utils.python_right_click(outside)
        WFHub.Workspaces.ContentArea.right_click_on_file("Portal_Page")
        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify the context menu:
    
            - Edit.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Delete DEL.
            - Unlink page.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(PORTAL_PAGE_MENU, "13.01")  
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "13.02",menu_path="Security")
        WFHub._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Right click on 'V5_Portal' in the content area.
        """
        WFHub.Workspaces.ContentArea.right_click_on_folder("V5_Portal")
        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the context menu:
    
            - Open
            - Run
            - Edit
            - Customizations (Remove my customizations/Remove customizations for all users)
            - Paste Ctrl+V (greyed out by default)
            - Delete DEL
            - Add to Favorites
            - Unpublish
            - Hide
            - Security (Rules on this resource.../Effective policy.../Owner...)
            - Properties
        """
        WFHub.ContextMenu.verify_options(V5_PORTAL_MENU, "14.01") 
        WFHub.ContextMenu.select("Customizations")
        WFHub.ContextMenu.verify_options(['Remove my customizations','Remove customizations for all users'], "14.02",menu_path="Customizations")        
        WFHub.ContextMenu.verify_disabled_options(['Paste Ctrl+V'], '14.03') 
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "14.04",menu_path="Security") 
        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Right click on 'Reporting_Object' in the content area.
        """
        WFHub.Workspaces.ContentArea.right_click_on_file("Reporting_Object")
        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify the context menu:
    
            - Run.
            - Run... (Run in new window/Run deferred).
            - Edit.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - New (InfoAssist[Report/Chart/Document]).
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(REPORTING_OBJECT_MENU, "15.01")
        WFHub.ContextMenu.select("Run...")
        WFHub.ContextMenu.verify_options(['Run in new window', 'Run deferred'], "15.02",menu_path="Run...")
        WFHub.ContextMenu.select("New")
        WFHub.ContextMenu.verify_options(['InfoAssist'], "15.03",menu_path="New")
        WFHub.ContextMenu.select("New->InfoAssist")
        WFHub.ContextMenu.verify_options(['Report', 'Chart', 'Document'], "15.04",menu_path="New->InfoAssist")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "15.05",menu_path="Security")
        WFHub._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Right click on 'Schedule' in the content area.
        """
        outside = WFHub._utils.validate_and_get_webdriver_object_using_locator(content,"content for outside click")
        WFHub._core_utils.python_right_click(outside)
        WFHub.Workspaces.ContentArea.right_click_on_file("Schedule")
        WFHub._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify the context menu:
    
            - Edit.
            - Run.
            - View log.
            - Disable.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(SCHEDULE_MENU, "16.01")   
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "16.02",menu_path="Security")
        WFHub._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Right click on 'Access_List' in the content area.
        """
        
        WFHub.Workspaces.ContentArea.right_click_on_file("Access_List")
        WFHub._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify the context menu:
    
            - Edit.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(ACCESSLIST_MENU, "17.01")   
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "17.02",menu_path="Security")
        WFHub._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Right click on 'Distribution_List' in the content area.
        """
        outside = WFHub._utils.validate_and_get_webdriver_object_using_locator(content,"content for outside click")
        WFHub._core_utils.python_right_click(outside)
        WFHub.Workspaces.ContentArea.right_click_on_file("Distribution_List")
        WFHub._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify the context menu:
    
            - Edit.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(DISTRIBUTIONLIST_MENU, "18.01")   
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "18.02",menu_path="Security") 
        WFHub._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Right click on 'Image' in the content area.
        """
        WFHub.Workspaces.ContentArea.right_click_on_file("Image")
        WFHub._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify the context menu:
    
            - View.
            - View in new window.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(IMAGE_MENU, "19.01")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "19.02",menu_path="Security")
        WFHub._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Right click on 'URL' in the content area.
        """
        outside = WFHub._utils.validate_and_get_webdriver_object_using_locator(content,"content for outside click")
        WFHub._core_utils.python_right_click(outside)
        WFHub.Workspaces.ContentArea.right_click_on_file("URL")
        WFHub._utils.capture_screenshot("20", STEP_20)

        STEP_20_EXPECTED = """
            STEP 20 - Expected : Verify the context menu:
    
            - View.
            - View in new window.
            - Edit.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(URL_MENU, "20.01")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "20.02",menu_path="Security")
        WFHub._utils.capture_screenshot("20 - Expected", STEP_20_EXPECTED, True)

        STEP_21 = """
            STEP 21 : Right click on 'Blog' in the content area.
        """
        WFHub.Workspaces.ContentArea.right_click_on_file("Blog")
        WFHub._utils.capture_screenshot("21", STEP_21)

        STEP_21_EXPECTED = """
            STEP 21 - Expected : Verify the context menu:
    
            - Edit.
            - Comments (View comments/Remove all comments).
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create shortcut.
            - Delete DEL.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(BLOG_MENU, "21.01")
        WFHub.ContextMenu.select("Comments")
        WFHub.ContextMenu.verify_options(['View comments', 'Remove all comments'], "21.02",menu_path="Comments")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "21.03",menu_path="Security")
        WFHub._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)

        STEP_22 = """
            STEP 22 : Right click on 'Text_Editor' in the content area.
        """
        outside = WFHub._utils.validate_and_get_webdriver_object_using_locator(content,"content for outside click")
        WFHub._core_utils.python_right_click(outside)
        WFHub.Workspaces.ContentArea.right_click_on_file("Text_Editor")
        WFHub._utils.capture_screenshot("22", STEP_22)

        STEP_22_EXPECTED = """
            STEP 22 - Expected : Verify the context menu:
    
            - Run.
            - Run (Run in new window/Run deferred/Run with SQL trace).
            - Schedule (Email/FTP/Printer/Report Library/Repository).
            - Edit.
            - Duplicate.
            - Cut Ctrl+X.
            - Copy Ctrl+C.
            - Create Shortcut.
            - Delete DEL.
            - Add to Favorites.
            - Unpublish.
            - Hide.
            - Security (Rules on this resource.../Effective Policy.../Owner...).
            - Properties.
        """
        WFHub.ContextMenu.verify_options(TEXTEDITOR_MENU, "22.01")
        WFHub.ContextMenu.select("Run...")
        WFHub.ContextMenu.verify_options(['Run in new window', 'Run deferred', 'Run with SQL trace'], "22.02",menu_path="Run...")
        WFHub.ContextMenu.select("Schedule")
        WFHub.ContextMenu.verify_options(['Email','FTP','Printer','Report Library','Repository'], "22.03",menu_path="Schedule")
        WFHub.ContextMenu.select("Security")
        WFHub.ContextMenu.verify_options(['Rules on this resource...', 'Effective policy...', 'Owner...'], "22.04",menu_path="Security")
        WFHub._utils.capture_screenshot("22 - Expected", STEP_22_EXPECTED, True)

        STEP_23 = """
            STEP 23 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Workspaces.switch_to_default_content()
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")       
        WFHub._utils.capture_screenshot("23", STEP_23)

