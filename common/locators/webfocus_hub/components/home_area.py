from selenium.webdriver.common.by import By

class HomeArea:
    
    views = (By.CSS_SELECTOR, "div[data-ibxp-state-name='legacylaunchpad_selection'] ")
    views_menus = (By.CSS_SELECTOR, views[1] + "div[data-ibx-type='ibxRadioButton']")