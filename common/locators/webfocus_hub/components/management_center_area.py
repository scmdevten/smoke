from selenium.webdriver.common.by import By

class ManagementCenter:
    
    management_center = (By.CSS_SELECTOR, "div[data-ibx-name='_pluginBox'] ")
    left_side_menu = (By.CSS_SELECTOR, management_center[1] + "div[data-ibx-name='_pluginNavFrame']")
    left_side_menu_options = (By.CSS_SELECTOR, left_side_menu[1] + " div[data-ibx-type='ibxRadioButton']")