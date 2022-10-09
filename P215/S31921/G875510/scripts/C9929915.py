"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 11-November-2021
-------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9929915_TestClass(BaseTestCase):
    
    def test_C9929915(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
            https://machine.ibi.com:port/alias/designer?is508=false&item=IBFS:/WFC/Repository/P215_S31921/G875510&tool=framework&startlocation=IBFS:/WFC/Repository/P215_S31921/G875510&startUpConditions=%7B%27mode%27%3A%27assemble%27%7D
        """
        Designer.API.invoke_assemble_visualizations(credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Blank template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Blank')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Right-click on the default section of the page canvas
            Click on 'Insert section below' option
        """
        Designer.PageCanvas.Section.right_click(1)
        Designer.ContextMenu.select("Insert section below")
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Right-click on the default section of the page canvas
            Click on 'Insert section above' option
        """
        Designer.PageCanvas.Section.right_click(1)
        Designer.ContextMenu.select('Insert section above')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click on container side tab;
            Drag and drop 'Basic' and 'Tab' containers onto the first section of the page canvas.
        """
        Designer.SideBar.Container.click()
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Drag and drop 'Carousel' and 'Accordion' containers onto the second section of the page canvas
        """

        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Drag and drop 'Grid' and 'Link Tile' containers onto the third section of the page canvas
        """

        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click on the 'Content' button from the sidebar > Navigate to the 'Retail Samples' > Reports folder > Drag and drop 'Margin by Product Category' into 'Container 1'
        """

        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify the 'Margin by Product Category' content is into the 'Container 1' and 'Container 1' title has been changed into 'Margin by Product Category'
        """

        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Drag and drop 'Quantity Sold By Stores' into 'Container 2' and Drag and drop 'Sales Metrics YTD' into 'Container 2' > Choose 'Add Content'
        """

        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify that two tabs available are with the contents 'Quantity Sold By Stores' and 'Sales Metrics YTD' into the 'Container 2'
        """

        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Navigate to the 'Retail Samples'  > 'Charts' folder > Drag and drop 'Arc-Sales by Region' into 'Container 3' and Drag and drop 'Bar - Highest Margin Products'  into 'Container 3' > Choose 'Add Content'
        """

        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify that two carousels are available with the contents 'Arc-Sales by Region' and 'Bar - Highest Margin Products' into the 'Container 3'
        """

        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Drag and drop 'Choropleth Map - Sales by State' in to 'Container 4' and Drag and drop 'Heatmap - Average Margin Product By Country (Animation)' into Container 4  > Choose 'Add Content'
        """

        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify that two areas are available with the contents 'Choropleth Map - Sales by State' and 'Heatmap - Average Margin Product By Country (Animation)' into the 'Container 4'
        """

        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Right-click on 'Link tile' Container (i.e., Container 6) > Under Settings Click on the Background Ellipses > Navigate to Workspaces > Retail Samples > Portal > Test widgets> Select 'Blue' > Click 'Select background' button
        """

        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Click on Content Elipses > Navigate to Workspaces > Retail Samples > Portal > Test widgets > Select 'Gray' > Click 'Select Content'
        """

        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify the 'Link Tile' settings as follows:
    
            Background: IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html
            Content: IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Gray.html
            Target: Viewer
        """

        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click on 'Run in new window'
        """

        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the following DF_Page opens successfully with the three sections along with those containers and contents
        """

        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Scroll down to see the third section of the container
        """

        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify that the 'Container 5' and 'Container 6' are available in the third section of the canvas
        """

        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Click on 'Link tile' Container (i.e., Container 6)
        """

        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify it opens 'Gray' content in the same window
        """

        Designer._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Close the two run windows
        """

        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : Click on the 'WebFOCUS DESIGNER' application menu > Select 'Save As..' > Enter the title as 'DF_Page8' > Click 'Save as'.
        """

        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Close the page.
        """

        Designer._utils.capture_screenshot("19", STEP_19)

        STEP_20 = """
            STEP 20 : Logout :
    
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """

        Designer._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : Edit the saved DF_Page using below API URL
    
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875510/df_page_8&startlocation=IBFS:/WFC/Repository
        """

        Designer._utils.capture_screenshot("21", STEP_21)

        STEP_21_EXPECTED = """
            STEP 21 - Expected : Verify the following DF_Page8 opens successfully without any error
        """

        Designer._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)

        STEP_22 = """
            STEP 22 : Scroll down to see the third section of the page canvas
        """

        Designer._utils.capture_screenshot("22", STEP_22)

        STEP_22_EXPECTED = """
            STEP 22 - Expected : Verify that the 'Container 3' and 'Container 4' are available in the third section of the canvas
        """

        Designer._utils.capture_screenshot("22 - Expected", STEP_22_EXPECTED, True)

        STEP_23 = """
            STEP 23 : Logout :
    
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """

        Designer._utils.capture_screenshot("23", STEP_23)