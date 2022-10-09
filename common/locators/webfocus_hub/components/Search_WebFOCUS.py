from selenium.webdriver.common.by import By

class SearchWebfocus:
    

    search_text_box = (By.CSS_SELECTOR, "div[data-ibx-name='_searchInput'] ") 
    search_help     = (By.CSS_SELECTOR, 'div[class^="search-plugin-options"] div[class*=ibx-anchor-link]:not([data-ibx-name="_btnConditionsDlg"])')
       
    
    class AllItems:
        
        all_items_button = (By.CSS_SELECTOR, "div[data-ibxp-user-value='clientrsrv']:not([style*='none']) ")
        clear_button = (By.CSS_SELECTOR, "div[title='Clear Search Options'] ") 
        search_button = (By.CSS_SELECTOR, "div[title='Do search'] ")
        
        
        class Searchby:
            
            search_by = (By.CSS_SELECTOR, "div[title='Search categories'] ") 
            search_by_input =  (By.CSS_SELECTOR, search_by[1] + " input")
            search_by_dropdown = (By.CSS_SELECTOR, search_by[1] + " [data-ibx-type='ibxButton']")
            
        class Type:
            
            type = (By.CSS_SELECTOR, "div[title='Search file types'] ") 
            type_input =  (By.CSS_SELECTOR, type[1] + " input")
            type_dropdown = (By.CSS_SELECTOR, type[1] + " [data-ibx-type='ibxButton']")
            
        class ContentIn:
            
            all_workspaces = (By.CSS_SELECTOR, "div[title='Search workspaces'] ") 
            all_workspaces_input =  (By.CSS_SELECTOR, all_workspaces[1] + " input")
            all_workspaces_dropdown = (By.CSS_SELECTOR, all_workspaces[1] + " [data-ibx-type='ibxButton']")
            all_reporting_servers  = (By.CSS_SELECTOR, "div[data-ibx-name='_selectRptSrvrs'] ")
            all_directories = (By.CSS_SELECTOR, "div[data-ibx-name='_selectAppDirs'] ")
            
        class DataIn:
            
            all_reporting_servers  = (By.CSS_SELECTOR, "div[data-ibx-name='_selectRptSrvrs'] ")
            all_reporting_servers_input =  (By.CSS_SELECTOR, all_reporting_servers[1] + " input")
            all_reporting_servers_dropdown = (By.CSS_SELECTOR, all_reporting_servers[1] + " [data-ibx-type='ibxButton']")
            all_directories = (By.CSS_SELECTOR, "div[data-ibx-name='_selectAppDirs'] ")
            all_directories_input = (By.CSS_SELECTOR, all_directories[1] + " input")
            all_directories_dropdown = (By.CSS_SELECTOR, all_directories[1] + " [data-ibx-type='ibxButton']")
            all_workspaces = (By.CSS_SELECTOR, "div[title='Search workspaces'] ")
                              
    class Content:
        content_Button = (By.CSS_SELECTOR, "div[data-ibxp-user-value='client']:not([style*='none']) ")
        clear_button = (By.CSS_SELECTOR, "div[title='Clear Search Options'] ")
        search_button = (By.CSS_SELECTOR, "div[title='Do search'] ") 
        
        
    class Data:
        data_button = (By.CSS_SELECTOR, "div[data-ibxp-user-value='rsrv']:not([style*='none']) ")
        all_items_button = (By.CSS_SELECTOR, "div[data-ibxp-user-value='clientrsrv']:not([style*='none']) ")        
        content_Button = (By.CSS_SELECTOR, "div[data-ibxp-user-value='client']:not([style*='none']) ")
        clear_button = (By.CSS_SELECTOR, "div[title='Clear Search Options'] ") 
        search_button = (By.CSS_SELECTOR, "div[title='Do search'] ")
        