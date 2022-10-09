from selenium.webdriver.common.by import By

class LeftSideNavigationBar:
    
    parent = (By.CSS_SELECTOR, "div.wfshell-nav-bar-plugins ")
    home = (By.CSS_SELECTOR, parent[1] + "div[title='Home']")
    workspaces = (By.CSS_SELECTOR, parent[1] + "div[title='Workspaces']")
    application_directories = (By.CSS_SELECTOR, parent[1] + "div[title='Application Directories']")
    portals = (By.CSS_SELECTOR, parent[1] + "div[title='Portals']")
    management_center = (By.CSS_SELECTOR, parent[1] + "div[title='Management Center']")
    search_webfocus = (By.CSS_SELECTOR, parent[1] + "div[title='Search']")
    home_icon = (By.CSS_SELECTOR, parent[1] + "div.ds-icon-home")
    workspaces_icon = (By.CSS_SELECTOR, parent[1] + "div.ds-icon-workspaces")
    application_directories_icon = (By.CSS_SELECTOR, parent[1] + "div.ds-icon-application-directory-alt")
    portals_icon = (By.CSS_SELECTOR, parent[1] + "div.ds-icon-dashboard")
    management_center_icon = (By.CSS_SELECTOR, parent[1] + "div.ds-icon-role")
    search_webfocus_icon = (By.CSS_SELECTOR, parent[1] + "div.ds-icon-search")