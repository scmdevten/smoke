from common.lib import html_controls
from common.pages.basepage import BasePage
from common.lib.webfocus import ibx_custom_controls
from common.locators.webfocus_hub import dialog as Locators
from selenium.common import exceptions as SeleniumExceptions
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import NoSuchElementException
from profile import _Utils

class Dialog:
    
    @property
    def Base(self): return _Base("Dialog")
    
    @property
    def ChangePassword(self): return _ChangePassword()
    
    @property
    def NewWorkspace(self): return _NewWorkspace()
    
    @property
    def NewFolder(self): return _NewFolder()
    
    @property
    def Delete(self): return _Delete()
    
    @property
    def Warning(self): return _Warning()
    
    @property
    def ShareWithOthers(self): return _ShareWithOthers()
    
    @property
    def NewURL(self): return _NewURL()
    
    @property
    def SampleContent(self): return _SampleContent()
    
    @property
    def NewPortal(self): return _NewPortal()
    
    @property
    def NewBlog(self): return _NewBlog()
    
    @property
    def NewTextResource(self): return _NewTextResource()
    
    @property
    def Alert(self): return _Alert()
    
    @property
    def ExploreData(self): return _ExploreData()
    
    @property
    def AboutWebFOCUS(self): return _ABOUT_WF()
    
   
    
class _Base(BasePage):
    
    def __init__(self, name):
        
        super().__init__()
        self._locators = Locators.Base
        self._name = name
        
    def wait_until_visible(self, time_out=10, pause_time=0, raise_error=True):
        """
        Description: Wait until dialog invisible
        """
        self._webelement.wait_until_element_visible(self._locators.dialog, time_out, pause_time, raise_error)
    
    def wait_for_text(self, text, time_out=10, pause_time=0, case_sensitive=False, raise_error=True):
        """
        Description: Wait until given text is present in dialog
        """
        self._webelement.wait_for_element_text(self._locators.dialog, text, time_out, pause_time, case_sensitive, raise_error)
        
    def wait_for_appear(self, time_out=20):
        """
        Description : Web driver will wait until modal dialog appear on screen
        """
        self._utils.synchronize_until_element_is_visible(self._locators.base_css, time_out)
    
    def wait_for_diappear(self, time_out=10):
        """
        Description : Web driver will wait until modal dialog disappear from screen
        """
        self._utils.synchronize_until_element_disappear(self._locators.base_css, time_out)
    
    def wait_until_invisible(self, time_out=10, pause_time=0, raise_error=True):
        """
        Description: Wait until dialog invisible
        """
        self._webelement.wait_until_element_invisible(self._locators.dialog, time_out, pause_time, raise_error)
    
    def close(self, wait=True):
        """
        Description: Click on close icon to close the dialog
        :arg - wait : True if wait to until dialog not visible
        """
        close = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.close_icon, 'Modal dialog close icon', self._object)
        #self._core_utils.left_click(close)
        close.click()
        wait and self.wait_until_invisible()
        
    def verify_title(self, expected_title, step_num):
        """
        Description: Verify the modal dialog title
        """
        actual_title = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.title, 'Modal dialog title', self._object).text.strip()
        msg = "Step {0}: Verify [{1}] dialog title".format(step_num, self._name)
        self._utils.asequal(expected_title, actual_title, msg)
    
    @property
    def _object(self):
        """
        Description: Return the parent object of modal dialog.
        Raise an error if dialog is not visible
        """
        dialog_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.dialog, self._name)
        if dialog_object.is_displayed():
            return dialog_object 
        else:
            raise SeleniumExceptions.ElementNotVisibleException("[{}] dialog not visible".format(self._name))

class TextBox( html_controls.TextBox,BasePage):
    
    def __init__(self, textbox_label, model_dialog_title, parent_object=None):
        
        BasePage.__init__(self)
        self._dialog_title_ = model_dialog_title
        self._textbox_label_ = textbox_label
        self._parent_object_ = parent_object
        html_controls.TextBox.__init__(self, self._object_, self._textbox_label_)
        
    @property
    def _object_(self):
        
        css = Locators.Base.textbox_css.format(self._textbox_label_)
        textbox_object = self._utils.validate_and_get_webdriver_object(css, "{0} textbox of {1} modal dialog".format(self._textbox_label_, self._dialog_title_), parent_object=self._parent_object_)
        return textbox_object
        
    def verify_disabled(self, step_num):
        """
        Description : Verify whether textbox is disabled or not
        :Usage - verify_disabled("01.02")
        """
        parent_obj = self._javascript_.get_parent_element(self._object_)
        opacity = parent_obj.value_of_css_property('opacity')
        pointer_events = parent_obj.value_of_css_property('pointer-events')
        status = all([opacity=='0.5', pointer_events=='none'])
        msg = "Step {0} : Verify [{1}] textbox disabled in [{2}] model dialog".format(step_num, self._textbox_label_, self._dialog_title_)
        self._utils_.asequal(True, status, msg)
    
    def verify_enabled(self, step_num):
        """
        Description : Verify whether textbox is enabled.
        :Usage - verify_enabled("01.02")
        """
        parent_obj = self._javascript_.get_parent_element(self._object_)
        pointer_events = parent_obj.value_of_css_property('pointer-events')
        msg = "Step {0} : Verify [{1}] textbox enabled in [{2}] model dialog".format(step_num, self._textbox_label_, self._dialog_title_)
        self._utils_.asequal('all', pointer_events, msg)

class _Button(BasePage):
    
    def __init__(self, button_name, dialog_title, dialog_object):
        
        super().__init__()
        self._dialog_object = dialog_object
        self._dialog_title = dialog_title
        self._button_name = button_name
        self._button_locator = Locators.Base.buttons
    
    @property
    def _object(self):
        
        buttons_object = self._utils.validate_and_get_webdriver_objects_using_locator(
            self._button_locator, "{0} Dialog Buttons".format(self._button_name), parent_object=self._dialog_object)
        button_index = self._javascript.find_element_index_by_text(buttons_object, self._button_name)
        if button_index is None:
            msg = "[{0}] button not displayed in [{1}] dialog".format(self._button_name, self._dialog_title)
            raise LookupError(msg)
        else:
            return buttons_object[button_index]
    
    def click(self):
        """
        Description : Left click on button
        """
        self._core_utils.python_left_click(self._object)
        #self._object.click()
        
    def verify_enabled(self, step_num):
        """
        Description : Verify whether button is enabled
        :Usage - verify_disabled("02.01")
        """
        opacity = self._object.value_of_css_property('opacity').strip()
        pointer_events = self._object.value_of_css_property('pointer-events').strip()
        state = True if (opacity == '1' and pointer_events == 'all') else False
        msg = "Step {0} : Verify [{1}] button is enabled in [{2}] dialog".format(step_num, self._button_name, self._dialog_title)
        self._utils.asequal(True, state, msg)
    
    def verify_disabled(self, step_num):
        """
        Description : Verify whether button is disabled
        :Usage - verify_disabled("02.01")
        """
        opacity = self._object.value_of_css_property('opacity').strip()
        pointer_events = self._object.value_of_css_property('pointer-events').strip()
        state = True if (opacity == '0.5' and pointer_events == 'none') else False
        msg = "Step {0} : Verify [{1}] button is disabled in [{2}] dialog".format(step_num, self._button_name, self._dialog_title)
        self._utils.asequal(True, state, msg)

class _ChangePassword(_Base):
    
    def __init__(self):
        super().__init__("Change Password")
        self._locator = Locators.ChangePassword
        self._name = 'Change Password'
        
    @property
    def UserName(self):
        new_workspace_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.Username, self._name + ' User name Input', parent_object=self._object)
        return html_controls.TextBox(new_workspace_textbox_obj, self._name + ' User name Input Text Box')         
    
    @property
    def OldPassword(self):
        new_workspace_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.OldPassword, self._name + ' Old Password Input', parent_object=self._object)
        return html_controls.TextBox(new_workspace_textbox_obj, self._name + ' Old Password Input Text Box')
    
    @property
    def NewPassword(self):
        new_workspace_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.NewPassword, self._name + ' New Password Input', parent_object=self._object)
        return html_controls.TextBox(new_workspace_textbox_obj, self._name + ' New Password Input Text Box')
    
    @property
    def ConfirmNewPasswword(self):
        new_workspace_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.ConfirmNewPassword, self._name + ' Confirm New Password Input', parent_object=self._object)
        return html_controls.TextBox(new_workspace_textbox_obj, self._name + ' New Password Input Text Box')
    
    @property
    def OldPasswordRgb(self):
        new_workspace_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.OldPasswordRgb, self._name + 'Old Password Border', parent_object=self._object)
        return html_controls.TextBox(new_workspace_textbox_obj, self._name + 'Old Password Border Text Box')
    
    @property
    def NewPasswordRgb(self):
        new_workspace_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.NewPasswordRgb, self._name + 'New Password Border', parent_object=self._object)
        return html_controls.TextBox(new_workspace_textbox_obj, self._name + 'New Password Border Text Box')
    
    @property
    def ConfirmNewPasswwordRgb(self):
        new_workspace_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.ConfirmNewPasswordRgb, self._name + ' Confirm New Password Border', parent_object=self._object)
        return html_controls.TextBox(new_workspace_textbox_obj, self._name + ' New Password Border Text Box')

    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        return button
    
    @property
    def ChangePassword(self):
        button = _Button("Change Password", self._name, self._object)
        return button
    
    @property
    def ErrorMessage(self): 
        error_msg_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.warning_msg, "Change Password Error Message Label")
        return html_controls.Label(error_msg_obj, 'Change Password Error Message')

class _NewWorkspace(_Base):
    
    def __init__(self):
        super().__init__("New Workspace")
        self._locator = Locators.NewWorkspace
        self._name = 'New Workspace'
        
    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        return button
    
    @property
    def Ok(self):
        button = _Button("OK", self._name, self._object)
        return button 
    
    @property
    def DropdownSelection(self): return ibx_custom_controls.ibxSelectItemList()
            
    def click_type_dropdown(self):
        type_dropdown_button_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.type_dropdown, self._name + ' Type Dropdown')
        self._core_utils.python_left_click(type_dropdown_button_obj)
            
    @property
    def Title(self):
        new_workspace_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.title_input, self._name + ' Title Input', parent_object=self._object)
        return html_controls.TextBox(new_workspace_textbox_obj, self._name + ' Title Input Text Box')
    
    @property
    def Name(self):
        name_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.name_input, self._name + ' Name Input', parent_object=self._object)
        return html_controls.TextBox(name_textbox_obj, self._name + ' Name Input Text Box')
    
    @property
    def ReportingSeverCheckbox(self):
        checkbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.reporting_server_checkbox, self._name + ' Reporting server checkbox', parent_object=self._object)
        return html_controls.CheckBox(checkbox_obj, self._name + " Reporting Server Checkbox")
 
class _ABOUT_WF(_Base):
        
        def __init__(self):    
            super().__init__("About WebFOCUS")      
            self._locator = Locators.AboutWebFOCUS               
            self._name = "About WebFOCUS"        
            
        
        def close(self, wait_for_close=True):
            """
            Description : Close the modal dialog by click on close icon
            """
            close_icon_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.close_icon, self._name + " dialog close icon")
            self._core_utils.left_click(close_icon_obj)
            wait_for_close and self._utils.synchronize_until_element_disappear(self._locator.base_css, 20)
            
        def verify_selected_tab_in_about_wf_dialog(self, tab_name, msg):
            '''
            This function will verify selected tab label in About WebFocus  dialog.
            :Usage verify_selected_tab_in_about_wf_dialog('General', "Step 9: verify")
            '''
            properties_selected_tab_css="{0}.checked .ibx-label-text".format(self._locator.about_wf_tab_css)
            selected_tab_value=self._driver.find_element_by_css_selector(properties_selected_tab_css).text.strip()
            self._utils.asequal(tab_name, selected_tab_value, msg)
    
        def verify_about_wf_dialog_tab_list(self, expected_list, msg):
            '''
            This function will check the list of About WebFocus dialog tab label.
            :Usage verify_about_wf_dialog_tab_list(['General', 'Web Client Detail'], "Step 9: verify")
            '''            
            properties_tab_label_css="{0} .ibx-label-text".format(self._locator.about_wf_tab_css)
            elem_obj=self._driver.find_elements_by_css_selector(properties_tab_label_css)  
            tabs_list=[tab.text.strip() for tab in elem_obj if tab.is_displayed()]
            self._utils.verify_list_values(expected_list, tabs_list, msg)
        
        def select_about_wf_tab_value(self, property_value):
            '''
            This function will select  tab values.
            @param property_value: 'General' 
            :usage select_about_wf_tab_value('General')            
            '''           
            elem_obj=self._driver.find_elements_by_css_selector("{0}  .ibx-label-text".format(self._locator.about_wf_tab_css))
            tabs_list =elem_obj[[tab.text.strip() for tab in elem_obj if tab.is_displayed()].index(property_value)]
            self._core_utils.python_left_click(tabs_list)
        
class _NewFolder(_Base):
    
    def __init__(self):
        super().__init__("New Folder")
        self._locator = Locators.NewFolder
        self._name = 'New Folder'
        
    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        return button
    
    @property
    def Ok(self):
        button = _Button("OK", self._name, self._object)
        return button

    @property
    def Title(self):
        new_workspace_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.title_input, self._name + ' Title Input', parent_object=self._object)
        return html_controls.TextBox(new_workspace_textbox_obj, self._name + ' Title Input Text Box')
    
    @property
    def Name(self):
        name_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.name_input, self._name + ' Name Input', parent_object=self._object)
        return html_controls.TextBox(name_textbox_obj, self._name + ' Name Input Text Box')
    
    
class _Delete(_Base):
    
    def __init__(self):
        super().__init__("Delete")
        self._locators = Locators.Base
        self._name = "Delete"
        
    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        return button
    
    @property
    def Ok(self):
        button = _Button("OK", self._name, self._object)
        return button
    
class _Warning(_Base):
    
    def __init__(self):
        super().__init__("Warning")
        self._locator = Locators.Base
        self._name = "Warning"
    
    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        return button
    
    def ok(self):
        is_warning = self._webelement.wait_for_element_text(Locators.Base.dialog, "Warning", 3, raise_error=False)
        if is_warning:
            button = _Button("OK", self._name, self._object)
            self._core_utils.left_click(button)
    
    @property            
    def Yes(self):
        button = _Button("Yes", self._name, self._object)
        return button
                
class _ShareWithOthers(_Base):
    
    def __init__(self):
        super().__init__("Share With others")
        self._locators = Locators.Base
        self._name = "Share With Others"
        
    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        return button
    
    @property
    def Ok(self):
        button = _Button("OK", self._name, self._object)
        return button
    
    @property
    def ShareWitheveryoneCheckbox(self):
        checkbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(Locators.ShareWithOthers.share_with_everyone_checkbox, self._name + 'Share with everyone Checkbox', parent_object=self._object)
        return html_controls.CheckBox(checkbox_obj, self._name + " Share with everyone Checkbox")
     
    
    @property
    def SearchTextBox(self): return self._search_textbox_()
    
    @property
    def UserGroupResults(self): return self._user_group_results_()
    
    @property
    def SharedWith(self): return self._shared_with_()
        
    class _search_textbox_(TextBox):
        
        def __init__(self):
            
            super(_ShareWithOthers._search_textbox_, self).__init__("Search Input", "Share With Others")
        
        @property
        def _object_(self):
            textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.ShareWithOthers.search_textbox, "{0} textbox of {1} modal dialog".format(self._textbox_label_, self._dialog_title_))
            return textbox_object
        
        def click_dropdown_button(self):
            """
            Description : Left click on drop down button
            """
            drop_down = self._utils.validate_and_get_webdriver_object_using_locator(Locators.ShareWithOthers.search_dropdown, "Share With Other Dialog Search Textbox drop down")
            self._core_utils.left_click(drop_down)
        
        def verify_dropdown_displayed(self, step_num):
            """
            Description : Verify whether User and Groups search text box dropdown button is dsiplayed
            """
            dropdown = self._utils.validate_and_get_webdriver_object_using_locator(Locators.ShareWithOthers.search_dropdown, "Share With Other Dialog Search Textbox drop down")
            state = True if(dropdown.is_displayed()) else False
            msg = "Step {0} : Verify 'Users and groups' search textbox drop down displayed in Share with Others model dialog".format(step_num)
            self._utils.asequal(True, state, msg)
        
        
    class _user_group_results_(BasePage):
        
        def __init__(self):
             
            super(_ShareWithOthers._user_group_results_, self).__init__()
            self.locators = Locators.ShareWithOthers.UserGroupResults
        
        def verify_name_contains_searched_text(self, searched_text, step_num):
            """
            Description : Verify all results name contains searched Users/Groups
            :Usage - verify_name_contains_searched_text("Autodev", "05.02")
            """
            status = False
            for name in self._get_names_object_():
                if name.is_displayed():
                    if searched_text.lower() in name.text.lower():
                        status = True
                    else :
                        status = False
                        break
            msg = "Step {0} : Verify User/Group results name contains [{1}] in Share with others dialog".format(step_num, searched_text)
            self._utils.asequal(True, status, msg)
            
        def verify_description_contains_searched_text(self, searched_text, step_num):
            """
            Description : Verify all results description contains searched Users/Groups
            :Usage - verify_description_contains_searched_text("Autodev", "05.02")
            """
            status = False
            for description in self._get_descriptions_object_():
                if description.is_displayed():
                    if searched_text.lower() in description.text.lower():
                        status = True
                    else :
                        status = False
                        break
            msg = "Step {0} : Verify User/Group results description contains [{1}] in Share with others dialog".format(step_num, searched_text)
            self._utils.asequal(True, status, msg)
            
        def verify_descriptions_in_bold(self, step_num):
            """
            Description : Verify all results descriptions in bold style
            :Usage - verify_descriptions_in_bold("05.02")
            """
            status = False
            for description in self._get_descriptions_object_():
                if description.is_displayed() and ('bold' in description.get_attribute('style')):
                    status = True
                else :
                    status = False
                    break
            msg = "Step {0} : Verify User/Group results descriptions displayed in bold in Share with others dialog".format(step_num)
            self._utils.asequal(True, status, msg)
        
        def wait_for_visible(self, time_out=30):
            """
            Description : Web driver will wait until User/Group results dialog visible on screen
            """
            self._utils.wait_for_page_loads(15, pause_time=0.5)
            self._utils.synchronize_until_element_is_visible(self.locators.base_css, time_out)
        
        def select(self, description):
            """
            Description : Left click on User/Group description to select.
            :Usage - select("autodevuser40")
            """
            error_msg = "[{0}] User/Group does not exist in Share with others results".format(description)
            description_obj = self._core_utils.get_element_object_by_text_using_javascript(self._get_descriptions_object_(), description, error_msg)
            self._core_utils.python_left_click(description_obj, yoffset=10)
            self._utils.wait_for_page_loads(10, pause_time=2)
            
        def verify_disabled_results(self, expected_results, step_num, assert_type='asin'):
            """
            Description : Verify the disabled results(Gray out users/groups)
            :Usage - 
            """
            results = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.results, "Share with other search results")
            actual_results = [result.text.strip().replace("\n", " ") for result in results if result.value_of_css_property("opacity")=='0.4']
            msg = "Step {0} : Verify {1} Users/Groups disabled in Share with others result dialog".format(step_num, expected_results)
            self._utils.verify_list_values(expected_results, actual_results, msg, assert_type)   
            
        def _get_descriptions_object_(self):
            """
            Descriptions : Return the all descriptions object as list
            """
            descriptions_object = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.descriptions, "Share with other search results description")
            return descriptions_object
        
        def _get_names_object_(self):
            """
            Descriptions : Return the all names object as list
            """
            names_object = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.names, "Share with other search results names")
            return names_object
        
    class _shared_with_(BasePage):
        
        def __init__(self):
             
            super(_ShareWithOthers._shared_with_, self).__init__()
            self.locators = Locators.ShareWithOthers.SharedWith
        
        def verify_users_and_groups(self, expected_values, step_num, assert_type='asin'):
            """
            Description : Verify the selected Users/Groups in Share with other 
            :Usage - verify_users_and_groups(["G458325:autodevuser203 autodevuser203(auto@devmail.com)"], "05.05")
            """
            actual_values = [item.text.strip().replace("\n", " ") for item in self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.users_groups, "Selected User/Group ")]
            msg = "Step {0} : Verify {1} Users/Groups selected in Share with others dialog".format(step_num, expected_values)
            self._utils.verify_list_values(expected_values, actual_values, msg, assert_type)   
            
        def verify_users(self, expected_users, step_num, assert_type='asin'):
            """
            Description : Verify the selected Users by checking users icon
            :Usage - verify_users(["autoadvuser01autoadvuser01(auto@devmail.com)"], "05.04")
            """
            actual_users = list()
            users_object = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.users_groups, "Selected User/Group icon")
            for user in users_object:
                user_icon = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.usergroup_icon, "Selected User/Group icon", parent_object=user)
                user_icon_value = self._javascript.get_element_after_style_properties(user_icon, 'content')
                if user_icon_value == '"\uf007"':
                    actual_users.append(user.text.strip().replace("\n", " "))
            msg = "Step {0} : Verify {1} Users selected in Share with others dialog".format(step_num, expected_users)
            self._utils.verify_list_values(expected_users, actual_users, msg, assert_type)
            
        def verify_groups(self, expected_groups, step_num, assert_type='asin'):
            """
            Description : Verify the selected Users by checking users icon
            :Usage - verify_groups(["P406_S31920 Advanced Users P406_S31920/AdvancedUsers"], "05.04")
            """
            actual_groups = list()
            users_object = self._utils.validate_and_get_webdriver_objects_using_locator(self.locator.users_groups)
            for user in users_object:
                user_icon = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.usergroup_icon, "Selected User/Group icon", parent_object=user)
                user_icon_value = self._javascript.get_element_after_style_properties(user_icon, 'content')
                if user_icon_value == '"\uf0c0"':
                    actual_groups.append(user.text.strip().replace("\n", " "))
            msg = "Step {0} : Verify {1} Users selected in Share with others dialog".format(step_num, expected_groups)
            self._utils.verify_list_values(expected_groups, actual_groups, msg, assert_type)
        
        def verify_names_in_normal_text(self, step_num):
            """
            Description : Verify all selected Users/Groups descriptions in normal text 
            :Usage - verify_names_in_normal_text("05.01")
            """
            status = False
            for names in self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.names, "names"):
                if names.is_displayed() and ('bold' not in names.get_attribute('style')):
                    status = True
                else :
                    status = False
                    break
            msg = "Step {0} : Verify selected Users/Groups names displayed in normal text in Share with others dialog".format(step_num)
            self._utils.asequal(True, status, msg)
            
        def verify_descriptions_in_bold(self, step_num):
            """
            Description : Verify all selected Users/Groups descriptions in bold style
            :Usage - verify_descriptions_in_bold("05.02")
            """
            status = False
            for description in self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.descriptions,"description"):
                if description.is_displayed() and ('bold' in description.get_attribute('style')):
                    status = True
                else :
                    status = False
                    break
            msg = "Step {0} : Verify selected Users/Groups descriptions displayed in bold in Share with others dialog".format(step_num)
            self._utils.asequal(True, status, msg)
        
        def verify_remove_icon(self, step_num):
            """
            Description : Verify Remove icon(x) displayed in all selected Users/Groups
            :Usage - verify_remove_icon("05.02")
            """
            status = False
            for users_groups in self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.users_groups, "Selected User/Group remove icon"):
                remove_btn_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.remove_icon, "Selected User/Group remove icon", parent_object=users_groups)
                icon_value = self._javascript.get_element_before_style_properties(remove_btn_obj, 'content')
                if remove_btn_obj.is_displayed() and ('"\uf00d"' == icon_value):
                    status = True
                else :
                    status = False
                    break
            msg = "Step {0} : Verify remove icon(x) displayed in all selected Users/Groups".format(step_num)
            self._utils.asequal(True, status, msg)
        
        def remove(self, description):
            """
            Description : Left click on remove icon to remove the selected Users/Group
            :Usage - remove("autodevuser40")
            """
            error_msg = "[{0}] User/Group does not exist in selected Users/Groups".format(description)
            descriptions_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.descriptions, "Selected Users/Groups")
            description_index = self._javascript.find_element_index_by_text(descriptions_objects, description)
            if description_index is not None:
                users = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.users_groups, "Selected User/Group")
                remove_btn_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.remove_icon, "Selected User/Group remove icon", parent_object=users[description_index])
                self._core_utils.left_click(remove_btn_obj)
                self._utils.wait_for_page_loads(5)
            else:
                raise LookupError(error_msg)
        
class _NewURL(_Base):
    
    def __init__(self):
        super().__init__("New URL")
        self._locator = Locators.NewURL
        self._name = "New URL"
        
    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        return button
    
    @property
    def Ok(self):
        button = _Button("OK", self._name, self._object)
        return button
    
    @property
    def Update(self):
        button = _Button("Update", self._name, self._object)
        return button

    @property
    def Title(self):
        newURL_title_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.title_input, self._name + ' Title Input', parent_object=self._object)
        return html_controls.TextBox(newURL_title_textbox_obj, self._name + ' Title Input Text Box')
    
    @property
    def Name(self):
        newURL_name_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.name_input, self._name + ' Name Input', parent_object=self._object)
        return html_controls.TextBox(newURL_name_textbox_obj, self._name + ' Name Input Text Box')

    @property
    def Summary(self):
        newURL_summary_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.summary_input, self._name + ' Summary Input', parent_object=self._object)
        return html_controls.TextBox(newURL_summary_textbox_obj, self._name + ' Summary Input Text Box')
    
    @property
    def URL(self):
        URL_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.URL_input, self._name + ' URL Input', parent_object=self._object)
        return html_controls.TextBox(URL_textbox_obj, self._name + 'URL Input')
    
class _SampleContent(_Base):
    
    def __init__(self):
        super().__init__("Sample Content")
        self._locator = Locators.SampleContent
        self._name = "Sample Content"
        
    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        return button
    
    @property
    def select(self):
        button = _Button("Select", self._name, self._object)
        return button
    
    @property
    def Title(self):
        title_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.title_input, self._name + ' Title Input', parent_object=self._object)
        return html_controls.TextBox(title_textbox_obj, self._name + ' Title Input Text Box')
    
    @property
    def Name(self):
        newURL_name_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.name_input, self._name + ' Name Input', parent_object=self._object)
        return html_controls.TextBox(newURL_name_textbox_obj, self._name + ' Name Input Text Box')
    
class _NewPortal(_Base):
    
    def __init__(self):
        super().__init__("New Portal")
        self._locator = Locators.NewPortal
        self._name = "New Portal"
    
    @property
    def AddPage(self): return self._AddPage()
        
    @property
    def Title(self):
        title_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.title_input, self._name + ' Title Input', parent_object=self._object)
        return html_controls.TextBox(title_textbox_obj, self._name + ' Title Input Text Box')
    
    @property
    def Name(self):
        name_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.name_input, self._name + ' Name Input', parent_object=self._object)
        return html_controls.TextBox(name_textbox_obj, self._name + ' Name Input Text Box')
    
    @property
    def Path(self):
        path_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.path_input, self._name + ' Title Input', parent_object=self._object)
        return html_controls.TextBox(path_textbox_obj, self._name + ' Path Input Text Box')
    
    @property
    def URL(self):
        URL_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.URL_input, self._name + ' URL Input', parent_object=self._object)
        return html_controls.TextBox(URL_textbox_obj, self._name + 'URL Input')
    
    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        return button
    
    @property
    def Create(self):
        button = _Button("Create", self._name, self._object)
        return button
    
        
class _NewBlog(_Base):
    
    def __init__(self):
        super().__init__("New Blog")
        self._locator = Locators.NewBlog
        self._name = "New Blog"
    
    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        return button
    
    @property
    def Ok(self):
        button = _Button("OK", self._name, self._object)
        return button
       
    @property
    def Title(self):
        title_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.title_input, self._name + ' Title Input', parent_object=self._object)
        return html_controls.TextBox(title_textbox_obj, self._name + ' Title Input Text Box')
    
    @property
    def Summary(self):
        newblog_summary_textbox_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.summary_input, self._name + ' Summary Input', parent_object=self._object)
        return html_controls.TextBox(newblog_summary_textbox_obj, self._name + ' Summary Input Text Box')
    
class _NewTextResource(_Base):
     
    def __init__(self):
        super().__init__("New Text Resource")
        self._locator = Locators.NewTextResource
        self._name = "New Text Resource"   
        
    def select_tab(self, tab_name):
        """
        Description : Left click on file type tab to select
        :Usage - select_tab("WEB")
        """
        tabs_obj = self._utils.validate_and_get_webdriver_objects_using_locator(self._locator.file_type_tabs, self._name + " File type tabs")
        error_msg = "[{0}] file type tab does not exists in [{1}] dialog".format(tab_name, self._name)
        tab_object = self._core_utils.get_element_object_by_text(tabs_obj, tab_name, error_msg=error_msg, scroll_into_view=False)
        self._core_utils.left_click(tab_object)
        
    def select_file_type(self, file_type, tab_name=None):
        """
        Description : Description : Left click on file type to select
        :Usage - select_file_type("FOCEXEC (fex)")
        """
        (tab_name != None) and self.select_tab(tab_name)
        file_types_obj = self._utils.validate_and_get_webdriver_objects_using_locator(self._locator.file_types, self._name+ " File types")
        error_msg = "[{0}] file type does not exists in [{1}] dialog".format(file_type, self._name)
        file_type_obj = self._core_utils.get_element_object_by_text(file_types_obj, file_type, error_msg=error_msg, scroll_into_view=False)
        self._core_utils.left_click(file_type_obj)
            
    def verify_tabs(self, expected_tabs, step_num, assert_type='asequal'):
        """
        Description : Verify the file type tabs
        :Usage - verify_tabs(['CONTENT', 'WEB', 'DATA SCIENCE'], "05.01")
        """
        msg = "Step {0} : Verify {1} file type tabs displayed in {2} dialog".format(step_num, expected_tabs, self._name)
        actual_tabs = [tab.text.strip() for tab in self._utils.validate_and_get_webdriver_object_using_locator(self._locator.file_type_tabs)]
        self._utils.verify_list_values(expected_tabs, actual_tabs, msg, assert_type)
        
    def verify_file_types(self, expected_files, step_num, assert_type='asequal'):
        """
        Description : Verify the file types
        :Usage - verify_file_types(['FOCEXEC (fex)', 'WebFOCUS Style Sheet (sty)', 'Plain Text (txt)', 'SQL Script (sql)'], "05.01")
        """
        msg = "Step {0} : Verify {1} file types displayed in {2} dialog".format(step_num, expected_files, self._name)
        actual_files = [tab.text.strip() for tab in self._utils.validate_and_get_webdriver_object_using_locator(self._locator.file_types)]
        self._utils.verify_list_values(expected_files, actual_files, msg, assert_type)
        
    def verify_selected_tab(self, expected_tabs, step_num):
        """
        Description : Verify the selected tab in text editor
        :Usage - verify_selected_tab(['CONTENT'], "05.01")
        """
        tabs_obj = self._utils.validate_and_get_webdriver_objects_using_locator(self._locator.file_type_tabs, self._name + " File type tabs")
        actual_tabs = []
        for tab in tabs_obj:
            color = Color.from_string(tab.value_of_css_property('color')).rgba
            bg_img = self._javascript.get_element_after_style_properties(tab, 'background-image')
            status = all([color=='rgba(52, 81, 94, 1)', bg_img=='radial-gradient(circle at 0px 0px, rgb(52, 85, 219), rgb(145, 44, 167))'])
            status and actual_tabs.append(tab.text.strip())
        msg = "Step {0} : Verify {1} tab selected in {2} dialog".format(step_num, expected_tabs, self._name)
        self._utils.asequal(expected_tabs, actual_tabs, msg)


class _Alert(_Base):

    def __init__(self):
        super().__init__("Alert Message")
        self._locator = Locators.Alert
        self._name = "Alert Message" 
        
    def verify_message(self, expected_msg, step_num):
        """
        Description : Verify the Alert dialog message
        :Usage - verify_message("Are you sure you want to delete  'Test' ?", "04.02")
        """
        actual_msg = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.message, self._name + " dialog message").text.strip()
        msg = "Step {0} : Verify [{1}] displayed in ['{2}'] dialog".format(step_num, expected_msg, self._name)
        self._utils.asequal(expected_msg, actual_msg, msg)
        
    @property
    def Ok(self):
        button = _Button("OK", self._name, self._object)
        return button
    
    @property
    def Cancel(self):
        button = _Button("Cancel", self._name, self._object)
        return button
    
    @property
    def Yes(self):
        button = _Button("Yes", self._name, self._object)
        return button
    
class _ExploreData(_Base):
    
    def __init__(self):
        super().__init__("Explore Data")
        self._locator = Locators.ExploreData
        self._name = "Explore Data"
            
    def Actions_icon(self):
        """
        Description : It returns Actions icon object to perform actions
        """
        Actions_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.Actionsbutton,self._name)
        self._core_utils.left_click(Actions_obj)
        
    def wait_for_appear(self, time_out=20):
        """
        Description : Web driver will wait until modal dialog appear on screen
        """
        self._utils.synchronize_until_element_is_visible(self._locator.Insight_trend_xaxis, expire_time = time_out)

    def verify_number_of_risers(self, expected_count, step_num):
        """
        Description : verify number of visible risers in chart
        Parameters :
            expected_count:int = Number of visible risers count
            step_num:str = example "04.01"
        Usage:
            verify_number_of_risers(10, "04.01")
        """
        msg = "Step {0} : Verify {1} risers displayed in {2}".format(step_num, expected_count, self._name)
        self._webelement.verify_number_of_visible_elements(self._locator.Riser_locator, expected_count, msg)
        
    
    def verify_xaxis_title(self, expected_title, step_num, value_len=None):
        """
        Description : verify chart x axis title 
        Parameters :
            expected_title = ['CAR','COUNTRY']
            step_num = example "04.01"
        Usage:
            verify_xaxis_title(['COUNTRY'], "04.01")
        """
        self._webelement.verify_elements_text(self._locator.Insight_trend_xaxis, expected_title, step_num, self._name + " X-Axis title", value_len=value_len)
    
    def verify_xaxis_labels(self, expected_labels, step_num, assert_type="equal", label_len=None, slicing=(None, None)):
        """
        Description : verify chart x axis labels 
        Parameters :
            expected_labels = ['CAR','COUNTRY']
            step_num = example "04.01"
        Usage:
            verify_xaxis_labels(['CAR','COUNTRY'], "04.01")
        """
        name = self._name + " X-Axis Labels"
        self._webelement.verify_elements_text(self._locator.Insight_trend_xaxis_labels, expected_labels, step_num, name, assert_type, label_len, slicing)    
        

    def verify_Zaxis_labels(self, expected_labels, step_num, assert_type="equal", label_len=None, slicing=(None, None)):
        """
        Description : verify chart y axis labels 
        Parameters :
            expected_labels = ['0','10','12']
            step_num = example "04.01"
        Usage:
            verify_yaxis_labels(['CAR','COUNTRY'], "04.01")
        """
        name = self._name + " Z-Axis Labels"
        self._webelement.verify_elements_text(self._locator.Insight_trend_zaxis_labels, expected_labels, step_num, name, assert_type, label_len, slicing)
                       
    @property
    def Close(self):
        button = _Button("Close", self._name, self._object)
        return button
        
    
        
    
    