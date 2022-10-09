"""-------------------------------------------------------------------------------------------
Author Name  : GRETHINA@TIBCO.COM
Automated On : 04-May-2022
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.webfocus_hub import WebFocusHub

class C9959854_TestClass(BaseTestCase):
    
    def test_C9959854(self):
        
        """
        TEST CASE OBJECTS
        """
        WFHub = WebFocusHub()
        
        """
        TEST CASE VAIABLESF
        """
        
        FileTypes = ['Access List','Datasource','Distribution List','Document','HTML File','Image','Library Report','Link','Page','Portal','PowerPoint','Procedure','Programming Language','Schedule','Spreadsheet','Stylesheet','Text File','URL','Other']
        Categories = ['Title','Summary','Tags','File Name'] 
        default = ['All categories']
        TypesDefault = ['All types']
        defaultWorkspace = ['All workspaces']
        workspaces = ["My Workspace","GlobalSearch_Folder","GlobalSearch_Misc","GlobalSearch_MyContent","GlobalSearch_Part1","GlobalSearch_Part2","Retail Samples"]
        defaultServer = ["All reporting servers"]
        Servers = ["EDASERVE"]
        defaultDirectories = ['All application directories']
        Directories = ['baseapp/dimensions','baseapp/facts','baseapp/test','baseapp/vr','ibisamp','jsonmaps','map_temp']
        
        text = "div.search-help-questions"
        hyperlink = 'div[class^="search-plugin-options"] div[class*=ibx-anchor-link]:not([data-ibx-name="_btnConditionsDlg"])'
        
        
        STEP_01 = """
            STEP 01 : Sign into TIBCO WebFOCUS as Admin User
        """
        WFHub.invoke_with_login("mridadm", "mrpassadm")
        WFHub._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : From the left side navigation bar, click on the 'Search WebFOCUS' icon
        """
        WFHub.LeftSideNavigationBar.SearchWebFocus.click()
        WFHub._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify the following for the 'Search Content & Data' Explorer pane:
    
            1. 'All Items' (By default selected), 'Content', and 'Data' displayed
            2. 'Search query' text box displayed with the no place holder text as 'Search (use * ? '' + to refine)
            3. By default 'Search by' filter selected with the 'All categories' option
            4. By default 'Type' filter is selected with the 'All types' option
            5. By default 'Content in' filter is selected with the 'All Workspaces' option
            6. By default 'Data in' filters are selected with:
            i) 'All reporting servers' option and 
            ii) 'All application  directories' option
            7. 'Clear' and 'Search buttons are enabled by default
            8. Bottom of the explorer pane displays with 'Questions?' label and 'Get Search help' hyperlink
        """
        WFHub.SearchWebfocus.AllItems.AllItemButton.verify_checked("2.01")
        WFHub.SearchWebfocus.Content.ContentButton.verify_unchecked("2.02")
        WFHub.SearchWebfocus.Data.DataButton.verify_unchecked("2.03")
        
        WFHub.SearchWebfocus.SearchTextBox.verify_placeholder_search('Search (use * ? "" + to refine)', "2.04")
        WFHub.SearchWebfocus.AllItems.SearchBy.verify_selected_option('All categories', "2.05")
        WFHub.SearchWebfocus.AllItems.Type.verify_selected_option("All types", "2.06")
        WFHub.SearchWebfocus.AllItems.ContentIn.verify_selected_option("All workspaces", "2.07")
        WFHub.SearchWebfocus.AllItems.DataIn.verify_selected_option_servers("All reporting servers", "2.08")
        WFHub.SearchWebfocus.AllItems.DataIn.verify_selected_option_directories("All application directories", "2.09")
        WFHub.SearchWebfocus.AllItems.Clear.verify_enabled("2.10")
        WFHub.SearchWebfocus.AllItems.Search.verify_enabled("2.11")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub._utils.verify_element_text(hyperlink, "Get Search help", "2.22 Get Search help hyperlink")
        
        
        WFHub._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)
        

        STEP_03 = """
            STEP 03 : Click on the 'Content' tab
        """
        WFHub.SearchWebfocus.Content.ContentButton.click()
        WFHub._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify the following for the 'Search Content & Data' Explorer pane:
    
            1. 'All Items', 'Content' (Selected) , and 'Data' displayed
            2. 'Search query' text box displayed with the no place holder text as 'Search (use * ? '' + to refine)
            3. By default 'Search by' filter is selected with  'All Categories' option
            4. By default 'Type' filter is selected with 'All types' option
            5. By default 'Content in' filter is selected with 'All Workspaces' option
            6. By default 'Data in' filters  are selected with the 'All reporting servers' and 'All application  directories' options get disabled
            7. 'Clear' and 'Search buttons are enabled by default
            8. Bottom of the explorer pane displays with 'Questions?' label and 'Get Search help' hyperlink
        """
        WFHub.SearchWebfocus.AllItems.AllItemButton.verify_enabled("03.01")
        WFHub.SearchWebfocus.Content.ContentButton.verify_checked("03.02")
        WFHub.SearchWebfocus.Data.DataButton.verify_enabled("03.03")
        WFHub.SearchWebfocus.SearchTextBox.verify_placeholder_search('Search (use * ? "" + to refine)', "03.04")
        WFHub.SearchWebfocus.Content.SearchBy.verify_selected_option("All categories", "03.05")
        WFHub.SearchWebfocus.Content.Type.verify_selected_option("All types", "03.06")
        WFHub.SearchWebfocus.Content.ContentIn.verify_selected_option("All workspaces", "03.07")
        WFHub.SearchWebfocus.Content.ContentIn.verify_disabled_directories("3.20")
        WFHub.SearchWebfocus.Content.ContentIn.verify_disabled_servers("3.21")
        WFHub.SearchWebfocus.Content.DataIn.verify_selected_option_directories("All application directories", "03.09")
        WFHub.SearchWebfocus.Content.Clear.verify_enabled("3.10")
        WFHub.SearchWebfocus.Content.Search.verify_enabled("3.11")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub._utils.verify_element_text(hyperlink, "Get Search help", "3.33 Get Search help hyperlink")
        
        WFHub._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on the 'Data' tab
        """
        WFHub.SearchWebfocus.Data.DataButton.click()
        WFHub._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify the following for the 'Search Content & Data' Explorer pane:
    
            1. 'All Items', 'Content', and 'Data' (Selected) displayed
            2. 'Search query' text box displayed with the no place holder text as 'Search (use * ? '' + to refine)
            3. By default 'Search by' filter is selected with  'All Categories' option
            4. By default 'Type' filter is selected with 'All types' option
            5. By default 'Content in' filter with 'All Workspaces' option get disabled
            6. By default 'Data in' filters are selected with:
            i) 'All reporting servers' option and 
            ii) 'All application  directories' option
            7. 'Clear' and 'Search buttons are enabled by default
            8. Bottom of the explorer pane displays with 'Questions?' label and 'Get Search help' hyperlink
        """
        WFHub.SearchWebfocus.Data.AllItemButton.verify_enabled("4.01")
        WFHub.SearchWebfocus.Content.ContentButton.verify_enabled("4.02")
        WFHub.SearchWebfocus.Data.DataButton.verify_checked("4.03")
        WFHub.SearchWebfocus.Data.SearchBy.verify_selected_option("All categories", "4.04")
        WFHub.SearchWebfocus.Data.Type.verify_selected_option("All types", "4.05")
        WFHub.SearchWebfocus.Data.DataIn.verify_disabled_all_workspaces("4.06")
        WFHub.SearchWebfocus.Data.DataIn.verify_selected_option_servers("All reporting servers", "4.07")
        WFHub.SearchWebfocus.Data.DataIn.verify_selected_option_directories("All application directories", "4.08")
        WFHub.SearchWebfocus.Data.Clear.verify_enabled("4.09")
        WFHub.SearchWebfocus.Data.Search.verify_enabled("4.10")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub._utils.verify_element_text(hyperlink, "Get Search help", "4.44 Get Search help hyperlink")
        WFHub._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on the 'All Items' tab
        """
        WFHub.SearchWebfocus.AllItems.AllItemButton.click()
        WFHub._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the following for the 'Search Content & Data' Explorer pane:
    
            1. 'All Items' (By default selected), 'Content', and 'Data' displayed
            2. 'Search query' text box displayed with the no place holder text as 'Search (use * ? '' + to refine)
            3. By default 'Search by' filter selected with the 'All Categories' option
            4. By default 'Type' filter is selected with the 'All types' option
            5. By default 'Content in' filter is selected with the 'All Workspaces' option
            6. By default 'Data in' filters are selected with:
            i) 'All reporting servers' option and 
            ii) 'All application  directories' option
            7. 'Clear' and 'Search buttons are enabled by default
            8. Bottom of the explorer pane displays with 'Questions?' label and 'Get Search help' hyperlink
        """
        WFHub.SearchWebfocus.AllItems.AllItemButton.verify_checked("5.01")
        WFHub.SearchWebfocus.Content.ContentButton.verify_unchecked("5.02")
        WFHub.SearchWebfocus.Data.DataButton.verify_unchecked("5.03")
        
        WFHub.SearchWebfocus.SearchTextBox.verify_placeholder_search('Search (use * ? "" + to refine)', "5.04")
        WFHub.SearchWebfocus.AllItems.SearchBy.verify_selected_option('All categories', "5.05")
        WFHub.SearchWebfocus.AllItems.Type.verify_selected_option("All types", "6.06")
        WFHub.SearchWebfocus.AllItems.ContentIn.verify_selected_option("All workspaces", "6.07")
        WFHub.SearchWebfocus.AllItems.DataIn.verify_selected_option_servers("All reporting servers", "6.08")
        WFHub.SearchWebfocus.AllItems.DataIn.verify_selected_option_directories("All application directories", "6.09")
        WFHub.SearchWebfocus.AllItems.Clear.verify_enabled("6.10")
        WFHub.SearchWebfocus.AllItems.Search.verify_enabled("6.11")
        WFHub._utils.verify_element_text(text, "Questions?", "Questions? text displayed ")
        WFHub._utils.verify_element_text(hyperlink, "Get Search help", "5.55 Get Search help hyperlink")
        WFHub._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : From the 'Search by' filter > Click on the 'All categories' option dropdown control
        """
        WFHub.SearchWebfocus.AllItems.SearchBy.Click()
        WFHub._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify the following options displayed:
    
            1. 'All Categories' (By default gets check-off),
            2. 'Title' (Uncheck)
            3. 'Summary' (Uncheck)
            4. 'Tags' (Uncheck)
            5. 'File Name' (Uncheck)
        """
        WFHub.SearchWebfocus.AllItems.SearchBy.Dropdown.verify_multiple_checked(default, "6.12")
        WFHub.SearchWebfocus.AllItems.SearchBy.Dropdown.verify_multiple_unchecked(Categories, "6.13")
        WFHub._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on the 'All categories' option in the dropdown control to close the lists of options displayed
        """
        WFHub.SearchWebfocus.AllItems.SearchBy.click_dropdown_icon()
        WFHub._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : From the 'Type' filter > Click on the 'All types' option in the dropdown control
        """
        WFHub.SearchWebfocus.AllItems.Type.Click()
        WFHub._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify the following options displayed:
    
            1. All types (By default gets check-off)
    
            **Note: The following options are unchecked by default**
    
            1. Access File (acx)
            2. Access List (acl)
            3. Adobe Acrobat Document (pdf)
            4. Blog comment file (blog)
            5. Cascading Style Sheet (css)
            6. Comma Separated Text File (csv)
            7. Configuration File (cfg)
            8. DIF File (dif)
            9. Deferred Report output file (orw)
            10. Distribution List (adr)
            11. E97 File (e97)
            12. Error (err)
            13. Excel Workbook file (wk1)
            14. FOR File (for)
            15. FTM File (ftm)
            16.File ()
            17. Flash file (swf)
            18. Focus Database (foc)
            19. Folder (null)
            20. HEX File (hex)
            21. HTML Document (htm)
            22. HTML Document (html)
            23. HTS File (hts)
            24. Icon (ico)
            25. Image (BMP) (bmp)
            26. Image (GIF) (gif)
            27. Image (JPEG) (jpg)
            28. Image (JPEG) (jpe)
            29. Image (JPEG) (jpeg)
            30. Image (PNG) (png)
            31. Image (SVG) (svg)
            32. JAR File (jar)
            33. JSON file (json)
            34. Java Class File (class)
            35. Java Source File (java)
            36. JavaScript File (js)
            37. Maintain (mnt)
            38. Manifest file (man)
            39. Master File (mas)
            40. Micorosft Excel Macro-Enabled Template (xltm)
            41. Micorosft Excel Macro-Enabled Workbook (xlsm)
            42. Micorosft Excel Template (xltx)
            43.Microsoft Excel 97-2003 Workbook (xht)
            44. Microsoft Excel 97-2003 Workbook (xmh)
            45. Microsoft Excel 97-2003 Worksheet (xls)
            46. Microsoft Excel Worksheet (xlsx)
            47. Microsoft Office 97-2003 Template (mht)
            48. Microsoft PowerPoint 97-2003 Presentation (ppt)
            49. Microsoft PowerPoint Macro-Enabled Presentation (pptm)
            50. Microsoft PowerPoint Macro-Enabled Template (potm)
            51. Microsoft PowerPoint Presentation (pptx)
            52. Microsoft PowerPoint Template (potx)
            53. Microsoft Word 97-2003 Document (doc)
            54. Microsoft Word Document (docx)
            55. Microsoft Write Document (wri)
            56. PRN File (prn)
            57. Parameter file (parm)
            58. PostScript (ps)
            59. Profile (prf)
            60. Project File (gfa)
            61. Property file (prop)
            62. R script (r)
            63. Report (fex)
            64. SQL File (sql)
            65. SQLOUT File (sqlout)
            66. Schedule (sch)
            67. TAB Delimitted File (tab)
            68. Temporary File (tmp)
            69. Text File (txt)
            70. Text File (wp)
            71. Text File (text)
            72. URL (url)
            73. V4 portal (prtl)
            74. VBScript File (vbs)
            75. WKL File (wkl)
            76. WebFOCUS Script File (wfs)
            77. WebFOCUS Stylesheet (sty)
            78. What-if file (wif)
            79. WinForms (wfm)
            80. XML File (xml)
            81. ZIP file (zip)
            82. easel.ly template (ely)
            83. python procedure (py)
        """
        WFHub.SearchWebfocus.AllItems.Type.Dropdown.verify_multiple_checked(TypesDefault, "8.01")
        WFHub.SearchWebfocus.AllItems.Type.Dropdown.verify_multiple_unchecked(FileTypes,"8.02")
        WFHub._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click on the 'All types' option in the dropdown control to close the lists of options displayed
        """
        WFHub.SearchWebfocus.AllItems.Type.click_dropdown_icon()
        WFHub._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : From the 'Content in' filter > Click on the 'All workspaces' option in the dropdown control
        """
        WFHub.SearchWebfocus.AllItems.ContentIn.Click()
        WFHub._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify the following options displayed:
    
            1. 'All workspaces' (By default gets check-off)
    
            **Note: The following workspaces are unchecked by default and based on the available workspaces in the repository tree total No. of workspaces will be varied.**
        """
        WFHub.SearchWebfocus.AllItems.ContentIn.Dropdown.verify_multiple_checked(defaultWorkspace, "10.01")
        WFHub.SearchWebfocus.AllItems.ContentIn.Dropdown.verify_multiple_unchecked(workspaces, "10.02")
        WFHub._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click on the 'All workspaces' option in the dropdown control to close the lists of options displayed
        """
        WFHub.SearchWebfocus.AllItems.ContentIn.click_dropdown_icon()
        WFHub._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : From the 'Data in' filter > Click on the 'All reporting servers' option in the dropdown control
        """
        WFHub.SearchWebfocus.AllItems.DataIn.click_servers()
        WFHub._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify the following options displayed:
    
            1. All reporting servers (By default gets check-off)
    
            **Note: The below server is unchecked by default)
    
            1. EDASERVE
        """
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_checked(defaultServer, "12.01")
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_unchecked(Servers, "12.02")
        WFHub._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click on the 'All reporting servers' option to close the lists of options displayed
        """
        WFHub.SearchWebfocus.Data.DataIn.click_dropdown_icon_servers()
        WFHub._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : From the 'Data in' filter > Click on the 'All application directories' option in the dropdown control
        """
        WFHub.SearchWebfocus.Data.DataIn.click_directories()
        WFHub._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the following options displayed:
    
            1. All application directories (By default gets check-off)
    
            **Note: The following application folders under EDASERVE section are unchecked by default and based on the available server total No. of application folders will be varied.**
    
            1. 181206130
            2. active_valid
            3. bank
            4. bank/app01
            5. baseapp
            6. baseapp/bike_share_nyc
            7. baseapp/dimens
            8. baseapp/fact
            9. baseapp/test
            10. baseapp/vr
            11. baseapp/wf_retail
            12. baseapp/wf_retail/bv_inheritance_exampl
            13. baseapp/wf_retail/dimens
            14. baseapp/wf_retail/dm
            15. baseapp/wf_retail/fact
            16. baseapp/wf_retail/test
            17. baseapp/wf_retail/test/geomap
            18. baseapp/wf_retail/test/util
            19. baseapp/wf_retail/test/xcmp
            20. baseapp/wf_retail/upload
            21. baseapp_2
            21. bostonscientif
            22. caster
            23. caster/active_layout
            24. caster/baselin
            25. caster/breakpag
            26. caster/cast
            27. caster/caster/active_layout
            28. caster/caster/baselin
            29. caster/caster/breakpag
            30. caster/caster/dynamic_distribution_list
            31. cast31. er/caster/fex
            32. caster/caster/subroutin
            33. caster/dynamic_distribution_list
            34. caster/fex
            35. caster/subroutin
            36. caster_old
            37. caster_old/active_layout
            38. caster_old/baselin
            39. caster_old/breakpag
            40. caster_old/dynamic_distribution_list
            41. caster_old/fex
            42. caster_old/subroutin
            43. cmpd
            44. county_data
            45. dcreal
            46. dcreal/dcreal
            47. fff
            48. hp_focusrelatedfil
            49. ibinccen
            50. ibisamp
            51. ibisamp/se/fact
            52. ibisamp_unicod
            53. ibisamp_unicode/mc
            54. intlgeorol
            55. it
            56. jsonmap
            57. map_temp
            58. natural_disast
            59. place
            60. projected_lay
            61. richmondretail
            62. s1427/156508
            63. s1427/61972527
            64. s1427/rpt_style
            65. seattlemap
            66. servic
            67. servicing/base_t
            68. servicing/blended_servicing_base_t
            69. servicing/dba
            70. servicing/dial
            71. servicing/excel_fil
            72. servicing/hold_fil
            73. servicing/ivr_ev
            74. servicing/me_base_t
            75. servicing/ocwen_base_t
            76. servicing/odssrv
            77. servicing/roundpoint_base_t
            78. servicing/sch_hold_fil
            79. servicing/snowflake_tempo
            80. servicing/sql_seg
            81. servicing/tempo
            82. servicing/tempo_stag
            83. servicing/trans_histori
            84. skoretail
            85. smoke_retailsamples_alphaformat
            86. smoke_retailsamples_alphaformat/bv_namespace_off
            87. smoke_retailsamples_alphaformat/bv_namespace_off/advanc
            88. smoke_retailsamples_alphaformat/bv_namespace_on
            89. smoke_retailsamples_alphaformat/bv_namespace_on/advanc
            90. smoke_retailsamples_alphaformat/dimens
            91. smoke_retailsamples_alphaformat/fact
            92. smoke_retailsamples_alphaformat/test
            93. smoke_retailsamples_alphaformat/test/geomap
            94. smoke_retailsamples_alphaformat/test/util
            95. smoke_retailsamples_alphaformat/upload
            96. soprano
            97. ta_autom
            98. unicod
            99. usgeorol
            100. vashti_backup_donottouch
            101. vashti_backup_donottouch/dimens
            102. vashti_backup_donottouch/fact
            103. vashti_backup_donottouch/test
            104. win_focusrelatedfil
            105. world
            106. world/bv_namespace_off
            107. world/bv_namespace_off/advanc
            108. world/bv_namespace_off/test
            109. world/bv_namespace_on
            110. world/bv_namespace_on/advanc
            120. world/dimens
            121. world/fact
            122. world/test
            123. world/test/util
            124. world/upload
            125. worldciti
            126. worldgeorol
            127. zipcod
        """
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_checked(defaultDirectories, "14.01")
        WFHub.SearchWebfocus.Data.DataIn.Dropdown.verify_multiple_unchecked(Directories, "14.02")
        WFHub._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click on the 'All application directories' option to close the lists of options displayed
        """
        WFHub.SearchWebfocus.Data.DataIn.click_dropdown_icon_directories()
        WFHub._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Click on the 'User profile' banner link > Click 'Sign Out'
        """
        WFHub.Banner.UserMenu.click()
        WFHub.ContextMenu.select("Sign Out")
        WFHub._utils.capture_screenshot("16", STEP_16)

