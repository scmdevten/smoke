from selenium.webdriver.common.by import By

class ApplicationDirectories:
    
    parent_css = "div[data-ibx-name='_pluginBox']"
    frame = parent_css + " iframe.wfrslegacyexplorer-content"
    all_app_directory = "[role='treeitem']"
    
    class SearchIndexOptions:
        
        cancel = (By.CSS_SELECTOR, "[qa='Cancel']")
        save = (By.CSS_SELECTOR, "[qa='Save']")
    
    
    class RibbonBar:
        
        parent = (By.CSS_SELECTOR, "div.wcx-mainribbon-bar ")
        menu_buttons = (By.CSS_SELECTOR, parent[1] + "div[class$='wcx-ribbon-left'] div[role='button']")
        
    class Application_Directory:
        
        filter_text_box =  (By.CSS_SELECTOR, "div.wcx-grid-toolbar-searchbox")
        
               

        
        
        