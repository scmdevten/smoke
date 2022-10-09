"""-------------------------------------------------------------------------------------------
Author Name  : HJEEVANA@TIBCO.COM
Automated On : 19-August-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub
from common.wftools.designer import Designer as DesignerPage
from selenium.webdriver.common.by import By

class C9953122_TestClass(BaseTestCase):
    
    def test_C9953122(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        
        Element1 = (By.CSS_SELECTOR,"div[data-ibx-name='pageSizeSelect'] input")
        
        STEP_01 = """
            STEP 01 : Launch Designer with car:
            http://machine.ibi.com:port/alias/designer?&master=qawfretail/wf_retail_lite&item=IBFS:/WFC/Repository/P452_S31923/G881097&tool=framework&startlocation=IBFS:/WFC/Repository/P452_S31923/G881097
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='qawfretail/wf_retail_lite')
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Double click on 'Product Category' and 'Cost of Goods'.
        """
        Designer.ResourcesPanel.Fields.Dimensions.expand('Product')
        Designer.ResourcesPanel.Fields.Dimensions.double_click('Product Category')
        Designer.ResourcesPanel.Fields.Measures.double_click('Cost of Goods')
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Select 'Standard Report' from chart picker.
        """
        Designer.ContentPicker.All.select('Standard Report')
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click 'Format' and select 'Output Settings'
            select 'PowerPoint Slide' from Page Size.
        """
        Designer.PropertiesPanel.select('Format')
        Designer.PropertiesPanel.Format.click_general_dropdown()
        Designer.PropertiesPanel.Format.Dropdown.select('Output Settings')
        Designer.PropertiesPanel.Format.click_PageSize_dropdown()
        Designer.PropertiesPanel.Format.Dropdown.select('PowerPoint Slide')
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : ![](index.php?/attachments/get/1916761)
        """
        
        elem_obj = Designer._utils.validate_and_get_webdriver_object_using_locator(Element1, 'Page Size')
        Actual = Designer._utils.get_element_attribute(elem_obj, 'aria-label')
        print(Actual)
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click 'Outline' and right click on Content > select 'view source code...'
        """

        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : ![](index.php?/attachments/get/1916762)
        """

        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Verify source code contains 'PAGESIZE=PPT-SLIDE'.
        """

        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : ![](index.php?/attachments/get/1916763)
        """

        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click Close icon to close view source code...
        """

        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Close Designer and click NO in the save dialog.
        """

        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Logout WebFOCUS
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

        WFHub._utils.capture_screenshot("09", STEP_09)

