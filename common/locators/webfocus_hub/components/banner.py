from selenium.webdriver.common.by import By

class Banner:
    
    parent = (By.CSS_SELECTOR, "div[data-ibx-type='wfShellHeader'] ")
    tools = (By.CSS_SELECTOR, parent[1] + "div[title='Tools']")
    help = (By.CSS_SELECTOR, parent[1] + "div[title='Help']")
    user_profile = (By.CSS_SELECTOR, parent[1] + "div[title*='User profile']")
    plus_button = (By.CSS_SELECTOR, "div[title='Start Something New']")
    normal_view = (By.CSS_SELECTOR, "div[title='Switch to Normal View']")
    admin_view = (By.CSS_SELECTOR, "div[title='Switch to Admin View']")
    area_name = (By.CSS_SELECTOR, "div[data-ibx-name='_pluginName']")
    tools_icon = (By.CSS_SELECTOR, tools[1] + " div[class*='ds-icon-tools']")
    help_icon = (By.CSS_SELECTOR, help[1], " div[class*='ds-icon-help']")
    user_profile_icon = (By.CSS_SELECTOR, user_profile[1] + " div[class*='ds-icon-user-male']")
    plus_icon = (By.CSS_SELECTOR, plus_button[1] + " div[class*='ds-icon-plus']")
    session_log_text_verify = (By.CSS_SELECTOR, "div.wfshell-errors-title")
    kill_selected_agents_button = (By.CSS_SELECTOR, "div[title='Kill all selected agents']")
    checkbox_manage_my_agents = (By.CSS_SELECTOR, "div.wcx-grid-body-row-cell.c0")
    checkbox_manage_my_agents_icon = (By.CSS_SELECTOR, "div[class^='ibx-check-box-simple-marker']")
    verify_state_manage_my_agent = (By.CSS_SELECTOR, "div.wcx-grid-body-row-cell.c3")
    tracing_level = (By.CSS_SELECTOR, "option[value='OFF']")
    Stop_request_message = (By.CSS_SELECTOR, "div[class='errorTitle']")
    
    class MainMenu:
        
        parent = (By.CSS_SELECTOR, "div[data-ibx-type='wfShellHeader'] ")
        main_menu = (By.CSS_SELECTOR, parent[1] + "div[data-ibx-name='_mainMenuBtn']")
        main_menu_icon = (By.CSS_SELECTOR, main_menu[1] + " div[class*='ds-icon-menu']")
        main_menu_shelf = (By.CSS_SELECTOR, "div[data-ibx-name='_mainMenuShelf']")    
        close = (By.CSS_SELECTOR, main_menu_shelf[1] + " div[data-ibx-name='_btnClose']")
        menu = (By.CSS_SELECTOR, main_menu_shelf[1] + " div[data-ibx-name='_navPanel']")
        menu_options = (By.CSS_SELECTOR, menu[1] + " div[data-ibx-type='ibxRadioButton']")
        quick_access = (By.CSS_SELECTOR, main_menu_shelf[1] + " div[data-ibx-name='_newPanel']")
        quick_access_options = (By.CSS_SELECTOR, quick_access[1] + " div[data-ibx-type='ibxButtonSimple']")
        
        
    class PlusButton:
        
        plus_button = (By.CSS_SELECTOR, "div[title='Start Something New']")
        plus_icon = (By.CSS_SELECTOR, plus_button[1] + " div[class*='ds-icon-plus']")
        plus_button_menu = (By.CSS_SELECTOR, "div[data-ibx-name='_popupNew'] [data-ibx-type='wfShellNavPanel']")
        plus_menu_options = (By.CSS_SELECTOR, plus_button_menu[1] + " div[data-ibx-type='ibxButtonSimple']")
        
        