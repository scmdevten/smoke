from selenium.webdriver.common.by import By

class Base:
    
    base_css            =  ".pop-top[role*='dialog'] "
    textbox_css         =  str(base_css + "div[data-ibxp-text='{0}'] ~ div [role='textbox']")
    dialog = (By.CSS_SELECTOR, "div.pop-modal[role*='dialog'][aria-hidden='false']")
    title = (By.CSS_SELECTOR, "div.ibx-title-bar-caption")
    close_icon = (By.CSS_SELECTOR, "div.ibx-title-bar-close-button")
    buttons = (By.CSS_SELECTOR, ".ibx-dialog-button-box .ibx-dialog-button:not([style*='none'])")
    

class ChangePassword:
    
    base_css               =  "div.pop-modal[role*='dialog'][aria-hidden='false'] "
    warning_msg            =  (By.CSS_SELECTOR, base_css + "div[class*='ds-messaging-ui']")
    Username               =  (By.CSS_SELECTOR, base_css + "div[class*='hp-reboot-user-name'] input")
    OldPassword            =  (By.CSS_SELECTOR, base_css + "div[class*='hp-reboot-old-password'] input")
    NewPassword            =  (By.CSS_SELECTOR, base_css + "div[class*='hp-reboot-new-password'] input")
    ConfirmNewPassword     =  (By.CSS_SELECTOR, base_css + "div[class*='hp-reboot-confirm-password'] input")
    OldPasswordRgb         =  (By.CSS_SELECTOR, base_css + "div[class*='hp-reboot-old-password']")
    NewPasswordRgb         =  (By.CSS_SELECTOR, base_css + "div[class*='hp-reboot-new-password']")
    ConfirmNewPasswordRgb  =  (By.CSS_SELECTOR, base_css + "div[class*='hp-reboot-confirm-password']")
        
class NewWorkspace:
    
    type_dropdown = (By.CSS_SELECTOR, "div#sdtxtTypeEnterpriseTenant input")
    title_input = (By.CSS_SELECTOR, "div#sdtxtFileTitle input")
    name_input = (By.CSS_SELECTOR, "div#sdtxtFileName input")
    reporting_server_checkbox = (By.CSS_SELECTOR, "div.CheckBoxSimpleOrder div.ibx-check-box-simple-marker")
    
class  AboutWebFOCUS:
        
    base_css            =  ".pop-top[role*='dialog'] "
    close_icon = (By.CSS_SELECTOR, "div[title='Close']")     
    about_wf_tab_css="div[data-ibx-type='wfShellAbout'] [data-ibx-type$='TabGroup'] [data-ibx-type$='Button'][role='tab']"
    

class NewFolder:
    
    title_input = (By.CSS_SELECTOR, "div#sdtxtFileTitle input")
    name_input = (By.CSS_SELECTOR, "div#sdtxtFileName input ")

class ShareWithOthers:

    
    base_css            =  "div.pop-modal[role*='dialog'][aria-hidden='false'] "
    search_textbox      =  (By.CSS_SELECTOR, base_css + ".share-with-txt-search input")
    search_dropdown     =  (By.CSS_SELECTOR, base_css + ".Share-with-menu-btn .ds-icon-caret-down")
    share_with_everyone_checkbox = (By.CSS_SELECTOR, base_css + ".ibx-check-box-simple-marker")
    
    class UserGroupResults:
        
        base_css        =  "#shareWithDropdown "
        results         =  (By.CSS_SELECTOR, base_css + ".item-user-group ")
        descriptions    =  (By.CSS_SELECTOR, results[1] + ".sw-item-desc")
        names           =  (By.CSS_SELECTOR, results[1] + ".sw-item-name")
    
    class SharedWith:
        
        base_css        =  ".ibx-dialog-content .share-with-hbox "
        users_groups    =  (By.CSS_SELECTOR, base_css + ".share-with-item ")
        descriptions    =  (By.CSS_SELECTOR, users_groups[1] + ".sw-item-desc")
        names           =  (By.CSS_SELECTOR, users_groups[1] + ".sw-item-name")
        usergroup_icon  =  (By.CSS_SELECTOR, ".sw-item-icon")
        remove_icon     =  (By.CSS_SELECTOR, ".item-close-icon")

class NewURL:
    
    base_css            =  "div.pop-modal[role*='dialog'][aria-hidden='false'] "
    title_input         = (By.CSS_SELECTOR, "div#sdtxtFileTitle input") 
    name_input          = (By.CSS_SELECTOR, "div#sdtxtFileName input")
    summary_input       = (By.CSS_SELECTOR, "div#sdtxtFileSummary textarea")
    URL_input           = (By.CSS_SELECTOR, "div#sdtxtFileURL input")
    
class SampleContent:
    
    base_css            = "div.pop-modal[role*='dialog'][aria-hidden='false'] "
    title_input         = (By.CSS_SELECTOR, "div.sd-form-field-text-title input")
    name_input          = (By.CSS_SELECTOR, "div.sd-form-field-text-name input")
    
class NewPortal:
    
    base_css            = "div.pop-modal[role*='dialog'][aria-hidden='false'] "
    title_input         = (By.CSS_SELECTOR, "div#sdtxtFileTitle input")
    name_input          = (By.CSS_SELECTOR, "div#sdtxtFileName input")
    path_input          = (By.CSS_SELECTOR, "div#sdtxtFilePath input")
    URL_input           = (By.CSS_SELECTOR, "div#sdtxtFileURL input")
    
class NewBlog:
    
    title_input         = (By.CSS_SELECTOR, "div#sdtxtFileTitle input")
    summary_input       = (By.CSS_SELECTOR, "div#FormFieldSummaryID textarea")
    
class NewTextResource:
    
    text_Editor_title   =    (By.CSS_SELECTOR, "div.ibx-title-bar-caption")
    root_css            =   ".text-editor-startup" + Base.base_css
    file_type_tabs      =   (By.CSS_SELECTOR, root_css + ".ibx-tab-button")
    file_types          =   (By.CSS_SELECTOR, root_css + ".tpg-selected .text-editor-file-type")
    
class Alert:
    
    base_css            = "div.pop-modal[role*='dialog'][aria-hidden='false'] "
    message             =  (By.CSS_SELECTOR, base_css + ".ibx-dialog-content")
        
class ExploreData:
    
    base_css            = "div.pop-modal[role*='dialog'][aria-hidden='false'] "
    activechart         =   (By.CSS_SELECTOR, "div[class^='insights-accordion-page']:not([class*='acc-pg-closed'])")
    Actionsbutton       =   (By.CSS_SELECTOR, base_css + "div[class^='insights-accordion-page']:not([class*='acc-pg-closed']) div[title='Actions']")
    Insight_trend_xaxis =   (By.CSS_SELECTOR, base_css + "div[class^='insights-accordion-page']:not([class*='acc-pg-closed']) div[class^='pd-canvas-widget'] [class^='xaxis'][class$='title']")
    Insight_trend_xaxis_labels = (By.CSS_SELECTOR, base_css + "div[class^='insights-accordion-page']:not([class*='acc-pg-closed']) div[class^='pd-canvas-widget'] [class^='xaxisOrdinal-labels']")
    Insight_trend_zaxis_labels = (By.CSS_SELECTOR, base_css + "div[class^='insights-accordion-page']:not([class*='acc-pg-closed']) div[class^='pd-canvas-widget'] [class^='zaxisOrdinal-labels']")
    Riser_locator       =   (By.CSS_SELECTOR, base_css + "div[class^='insights-accordion-page']:not([class*='acc-pg-closed']) div[class^='pd-canvas-widget'] rect[tdgtitle='placeholder']")