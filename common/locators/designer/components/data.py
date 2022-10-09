from selenium.webdriver.common.by import By


class Data:
    
    DATA = (By.CSS_SELECTOR, "div.tool-container-data ")
    FRAME = (By.CSS_SELECTOR, "iframe.ibx-shell-tool-host")
    
    
    class Source:
        
        source_css = (By.CSS_SELECTOR, "div[qa='MFDataContent']")
        row_css = (By.CSS_SELECTOR, "div.wcx-grid-body-tree-row")
        Search_box = (By.CSS_SELECTOR, "div[class$='underneathsearchbox'] input")
        
        
    class Canvas:
        
        canvas_css = (By.CSS_SELECTOR, "div[qa='MFGraphContent'] ")
        original_data_css = (By.CSS_SELECTOR, "div[class*='ds-flow-node'][qa='{}']")
        join_label_css = (By.CSS_SELECTOR, canvas_css[1] + "div[class*='ds-flow-node'] div.ds-node-label")

    
    class SelectEditor:
        
        Select_Editor_Frame = (By.CSS_SELECTOR, "div[class*='tool-container-data'] iframe")
        Cancel_Button   = (By.CSS_SELECTOR, "div[class$='wcx-wcform-buttonbar'] div[class*='btn-ghost']")
        OK_Button       = (By.CSS_SELECTOR, "div[class$='wcx-wcform-buttonbar'] div[class*='btn-solid']")
        
        class LeftSourcePane:
            
            Data_source_pane= (By.CSS_SELECTOR, "div[class$='wcx-wctable-cgintm_Source_table'] ")
            Data_name = (By.CSS_SELECTOR, Data_source_pane[1] +  "div[aria-label='{}']")
            Field_name = (By.CSS_SELECTOR, Data_source_pane[1] + "div[class$='wcx-image']")
        
        class MiddlePane:
            
            Middel_pane     = (By.CSS_SELECTOR, "div[content_id='MFRightContent'] ")
            Delete_Query_Icon   = (By.CSS_SELECTOR, Middel_pane[1] + "div[title='Delete Query']")
            BucketField_name = (By.CSS_SELECTOR, Middel_pane[1] + "div[class$='wcx-image'] div[class='ibx-label-text']")
        
        class RightPane:
            
            Right_pane      = (By.CSS_SELECTOR, "div[class$='wcx-wctable-startResult']")
            Canvas_value    = (By.CSS_SELECTOR, Right_pane[1] + "div[id='WcMultiframesContentView-7'] div[qa='row-0-column-0']")
        
        
    
    class SampleData:
        
        sample_data_css = (By.CSS_SELECTOR, "div[qa='MFOutputContent']")
    
    
    class Toolbar:
        pass 
        