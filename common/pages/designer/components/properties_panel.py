from common.pages.basepage import BasePage
from common.lib.html_controls import TextBox, CheckBox, Button
from common.locators.ibx_custom_controls import bucket as bucket_locators
from common.locators.designer.components import properties_panel as Locators
from common.lib.webfocus.ibx_custom_controls import ibxSpinner, ibxRadioButton, ibxSelectItemList, bucket
from pandas._libs.index import self

class PropertiesPanel(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locators = Locators.PropertiesPanel

    @property
    def Settings(self): return _Settings()
    
    @property
    def Format(self): return _Format()
        
    def select(self, property_name):
        """
        Description: Select Property panel tab
        Usage: select('Format')
        """
        property_tab_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.property_panel_tab, 'Property Panel Tab')
        actual_property_tab_objects = [tab_objects for tab_objects in property_tab_objects if tab_objects.is_displayed()]
        property_tab_object = self._javascript.find_elements_by_text(actual_property_tab_objects, property_name)
        if property_tab_object != None:
            self._core_utils.left_click(property_tab_object[0])
        else:
            msg = '[{}] property panel is not available'.format(property_name)
            raise TypeError(msg)
        
class _Settings(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators.Settings
        
    @property
    def GeneralSettings(self): return _GeneralSettings()
    
    @property
    def DataSettings(self): return _DataSettings()
    
    @property
    def Parameters(self): return _Parameters()
    
    @property
    def ControlSettings(self): return _ControlSettings()
    
    @property
    def ContainerSettings(self): return _ContainerSettings()
    
    @property
    def ContainerCustomization(self): return _ContainerCustomization()
    
    @property
    def ContentSettings(self): return _ContentSettings()
    
    @property
    def Display(self): return _Display()
    
    @property
    def Filters(self): return _Filters()
    
    
class _GeneralSettings(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators.Settings
    
    @property
    def Type(self): 
        textbox_name = "Type"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.type, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def ID(self): 
        textbox_name = "ID"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.id, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def Classes(self): 
        textbox_name = "Classes"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.classes, textbox_name)
        return TextBox(textbox_object, textbox_name)

    @property
    def Tooltip(self): 
        textbox_name = "Tooltip"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.tooltip, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def GlobalName(self): 
        textbox_name = "GlobalName"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.global_name, textbox_name)
        return TextBox(textbox_object, textbox_name)

class _ControlSettings(BasePage):
    
    @property
    def Optional(self):
        checkbox_name = "Optional"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.optional, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
    
    @property
    def PlaceholderText(self): 
        textbox_name = "PlaceholderText"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.placeholder, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def Search(self):
        checkbox_name = "Search"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.search, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)

    @property
    def SelectionControls(self):
        checkbox_name = "SelectionControls"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.selection_controls, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
    
    @property
    def AllowReordering(self):
        checkbox_name = "AllowReordering"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.allow_reordering, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
    
    
class _DataSettings(BasePage):
    
    @property
    def DisplayText(self): 
        textbox_name = "DisplayText"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.display_text, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def DefaultValue(self): 
        textbox_name = "DefaultValue"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.default_value, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def DefaultValue2(self): 
        textbox_name = "DefaultValue2"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.default_value2, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def ShowAllOption(self):
        checkbox_name = "ShowAllOption"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.show_all_option, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
    
class _Parameters(BasePage):
    
    @property
    def Parameters(self): 
        textbox_name = "Parameters"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.parameter_value, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def Parameters2(self): 
        textbox_name = "Parameters2"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.parameter_value2, textbox_name)
        return TextBox(textbox_object, textbox_name)
 
 
class _ContainerSettings(BasePage):
    
    @property
    def ID(self): 
        textbox_name = "ID"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.id, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def Classes(self): 
        textbox_name = "Classes"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.classes, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def ShowAllOption(self):
        checkbox_name = "ShowAllOption"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.show_all_option, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
    
    @property
    def ShowTitle(self):
        checkbox_name = "ShowTitle"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.show_title, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
    
    @property
    def ShowToolbar(self):
        checkbox_name = "ShowToolbar"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.show_toolbar, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
    
    @property
    def ShowOnDesktop(self):
        button_name = "Desktop"
        pass
        
 
    @property
    def ShowOnTablet(self):
        button_name = "Tablet"
        pass
    
    @property
    def ShowOnMobile(self):
        button_name = "Mobile"
        pass
    
    @property
    def AutoplayInterval(self): return ibxSpinner(name="Autoplay Interval", index=0)
        
    @property
    def RerunContent(self):
        checkbox_name = "Reruncontent"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.show_toolbar, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
 
 
class _ContainerCustomization(BasePage):
    
    @property
    def LockContainer(self):
        checkbox_name = "LockContainer"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.lock_container, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
    
    @property
    def LockPath(self):
        checkbox_name = "LockPath"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.lock_path, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
    
    @property
    def FlattenList(self):
        checkbox_name = "FlattenList"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.flatten_list, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
    
    @property
    def HideTags(self):
        checkbox_name = "HideTags"
        checkbox_object = self._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.hide_tags, checkbox_name)
        return CheckBox(checkbox_object, checkbox_name)
    
    @property
    def Grid(self):
        button_name = "Grid"
        pass
    
    @property
    def List(self):
        button_name = "List"
        pass


class _ContentSettings(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators.Settings
        self._name = 'Content Settings'
            
    @property
    def ID(self): 
        textbox_name = "ID"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.content_id, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def Classes(self): 
        textbox_name = "Classes"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.content_classes, textbox_name)
        return TextBox(textbox_object, textbox_name)  
    
    @property   
    def EnableHeading(self):
        self.__scroll_into_view__()
        checkbox_name = "Enable Heading"
        enable_heading_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.enable_heading, self._name + " -Enable Heading")
        return CheckBox(enable_heading_object, checkbox_name)
    
    @property   
    def EnableFooting(self):
        self.__scroll_into_view__()
        checkbox_name = "Enable Footing"
        enable_footing_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.enable_footing, self._name + " -Enable Footing")
        return CheckBox(enable_footing_object, checkbox_name)
    
    @property   
    def EnableAutoRefresh(self):
        self.__scroll_into_view__()
        checkbox_name = "Enable Auto Refresh"
        enable_footing_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.enable_auto_refresh, self._name + " -Enable Auto Refresh")
        return CheckBox(enable_footing_object, checkbox_name)
    
    @property
    def RunWithInsight(self):
        self.__scroll_into_view__()
        checkbox_name = "Run with Insight"
        run_with_insight_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.run_with_insight, self._name + " -Run with Insight")
        return CheckBox(run_with_insight_object, checkbox_name)
    
    @property
    def DrillAnywhere(self):
        self.__scroll_into_view__()
        checkbox_name = "Drill Anywhere"
        drill_anywhere_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.drill_anywhere, self._name + " -Drill Anywhere")
        return CheckBox(drill_anywhere_object, checkbox_name)
    
    @property
    def AutoDrill(self):
        self.__scroll_into_view__()
        checkbox_name = "Auto Drill"
        auto_drill_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.autodrill, self._name + " -Auto Drill")
        return CheckBox(auto_drill_object, checkbox_name)
    
    @property
    def AutoLink(self):
        self.__scroll_into_view__()
        checkbox_name = "Auto Link"
        auto_link_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.autolink, self._name + " -Auto Link")
        return CheckBox(auto_link_object, checkbox_name)
    
    @property
    def AutoLinkTarget(self):
        self.__scroll_into_view__()
        checkbox_name = "AutoLink Target"
        run_with_insight_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.autolinktarget, self._name + " -AutoLink Target")
        return CheckBox(run_with_insight_object, checkbox_name)
    
    def ScrollIntoView(self): return self.__scroll_into_view__()
    
    def __scroll_into_view__(self):
        content_settings = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.content_settings, self._name)
        self._javascript.scrollIntoView(content_settings)


class _Display(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators.Settings.Display
    
    @property
    def Vertical(self): return bucket(bucket_name="Vertical")
    
    @property
    def Horizontal(self): return bucket(bucket_name="Horizontal")
    
    @property
    def Size(self): return bucket(bucket_name="Size")
    
    @property
    def Color(self): return bucket(bucket_name="Color")
    
    @property
    def Tooltip(self): return bucket(bucket_name="Tooltip")
    
    @property
    def Animate(self): return bucket(bucket_name="Animate")
    
    @property
    def MultiPage(self): return bucket(bucket_name="MultiPage")
    
    @property
    def Rows(self): return bucket(bucket_name="Rows")
    
    @property
    def ColumnGroups(self): return bucket(bucket_name="Column Groups")
    
    @property
    def Summaries(self): return bucket(bucket_name="Summaries")
    
    def clear_bucket_contents(self):
        """
        Description: verify selected theme
        Usage: clear_bucket_contents()
        """
        clear_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.clear_buckets_content, "Clear buckets content")
        clear_button.click()
    
    def change_chart_orientation(self):
        """
        Description: verify selected theme
        Usage: change_chart_orientation()
        """
        change_chart_orientation_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.change_chart_orientation, "Change chart orientation")
        change_chart_orientation_button.click()
    
    def click_layout_button(self):
        """
        Description: verify selected theme
        Usage: click_layout_button()
        """
        layout_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.layout_button, "Layout button")
        layout_button.click()
    
    def click_type_button(self):
        """
        Description: verify selected theme
        :Usage: click_type_button()
        """
        type_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.type_button, "Type button")
        type_button.click()
    
    def verify_available_buckets(self, expected_buckets, step_num, assert_type='equal'):
        """
        Description: verify available buckets in display accordion
        :Usage - verify_available_buckets()
        """
        self._webelement.verify_elements_text(bucket_locators.bucket_label, expected_buckets, step_num, "Buckets", assert_type)
        
    
class _Format(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators.Format
    
    @property
    def ContainerFormat(self): return _ContainerFormat() 
    
    @property
    def PageFormat(self): return _PageFormat()
    
    @property
    def GridStyle(self): return _GridStyle()
    
    @property
    def SectionFormat(self): return _SectionFormat()
    
    @property
    def General(self): return _General()
    
    @property
    def MapSettings(self): return _MapSettings()
    
    @property
    def PDFPage(self): return _PDFPage()
    
    @property
    def Dropdown(self): return ibxSelectItemList()
    
    def click_general_dropdown(self):
        """
        Description: CLick on the general drop down button 
        """
        general = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.General.general_dropdown, 'General Dropdown')
        self._core_utils.python_left_click(general)
        
    def click_PageSize_dropdown(self):
        """
        Description: CLick on the Page Size drop down button 
        """
        PageSize = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.Output_Settings.PageSize_dropdown, 'Page Size Dropdown')
        self._core_utils.python_left_click(PageSize)
        
    def verify_selected_format_option(self, Expected_value, step_num):
        
        elem_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.page_size_dropdown, 'Page Size')
        Actual_value = self._utils.get_element_attribute(elem_obj, 'aria-label')
        msg = "Step {} : Format option verified".format(step_num)
        self._utils.asequal(Actual_value,Expected_value,msg)
        

class _ContainerFormat(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators.Format
        
    @property
    def Style(self): 
        container_format_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.container_format, "Container Format")
        return ibxRadioButton(parent_object=container_format_object)

class _PageFormat(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators.Format
        
    def click_theme_dropdown(self):
        """
        Description: Click on the theme dropdown
        """
        self._webelement.wait_for_element_text(self._locator.format, 'Page Format', 60)
        theme_dropdown_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.theme_dropdown, 'Theme Dropdown')
        self._core_utils.left_click(theme_dropdown_object)
        
    def verify_selected_theme(self, theme_name, step_num):
        """
        Description: verify selected theme
        Usage: verify_selected_theme('Midnight', '10')
        """
        theme_dropdown_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.theme_dropdown, 'Theme')
        actual_theme = theme_dropdown_object.get_attribute('aria-label')
        state = True if theme_name == actual_theme else False
        msg = "Step {0}: Verify [{1}] theme is selected".format(step_num, theme_name)
        self._utils.asequal(True, state, msg)
    
    @property
    def Margin(self):
        textbox_name = "Margin"
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.margin_textbox, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def MaximumWidth(self):
        textbox_name = 'Maximum Width'
        textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.maximum_width_textbox, textbox_name)
        return TextBox(textbox_object, textbox_name)
    
    @property
    def ThemeDropdown(self): return ibxSelectItemList()
        
        
class _GridStyle(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators.Format
        self._name = "Grid Style"

    @property
    def Style(self): 
        grid_style_objects = self._utils.validate_and_get_webdriver_object_using_locator(self._locator.grid_style, self._name)
        return ibxRadioButton(parent_object=grid_style_objects)
    
    
class _SectionFormat(BasePage):
    
    def __init__(self):
        
        super().__init__()
        self._locator = Locators.Format
        self._name = 'Section Format'
    
    @property
    def Style(self): 
        option_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locator.options, self._name + 'options')
        option_label_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locator.lables, self._name + 'options label')
        index = self._javascript.find_element_index_by_text(option_label_objects, 'Style')
        return ibxRadioButton(name='Section Style Radio Button', parent_object=option_objects[index])
    

class _General(BasePage):
    
    def __init__(self):
        super().__init__()
        
    @property
    def FrameAndBackground(self): return _FrameAndBackground()
    
    @property
    def Other(self): return _Other()
    
    
class _FrameAndBackground(BasePage):
        
    def __init__(self):
        super().__init__()
        self._locators = Locators.Format.General
        self._name = "Frame and Background"
        
    @property
    def ColorPalette(self): return _ColorPalette()
        
    def click_frame(self):
        """
        Description: Click on the frame button inside frame and background section
        """
        frame = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.frame, self._name + ' Frame Button')
        self._core_utils.python_left_click(frame)
        self._webelement.wait_until_element_visible(self._locators.ColorPalette.color_palette, 30)


class _Other():
        pass
    
    
class _ColorPalette(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.Format.General.ColorPalette
        self._name = "Color Palette"
        
    def select_color(self, color):
        """
        Description: Select color in color palette
        :Usage - select_color('#ed1c24')
        """
        color = self._driver.find_element_by_css_selector(self._locators.color.format(color))
        color.click()
        self._webelement.wait_until_element_invisible(self._locators.color_palette, 30)
        
        
class _MapSettings(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.Format
        self._name = "Map Settings"
        
    def click_basemap_dropdown(self):
        """
        Description: Click on basemap dropdown in Map 
        """
        base_map = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.base_map, 'Base Map')
        self._core_utils.python_left_click(base_map)
        
    def click_demographic_layer_dropdown(self):
        """
        Description: Click on demographic layer dropdown in Map 
        """
        demographic_layer = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.demographic_layer, 'Demographic Layer')
        self._core_utils.python_left_click(demographic_layer)
        
    def click_reference_layer_dropdown(self):
        """
        Description: Click on reference layer dropdown in Map 
        """
        reference_layer = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.reference_layer, 'Reference Layer')
        self._core_utils.python_left_click(reference_layer)

class _Filters(BasePage):
    
    def __init__(self, bucket_name="Filters", name="bucket component", bucket_locator=Locators.Settings.Filters.filter_bucket,
                        field_pill=Locators.Settings.Filters.filter_field_list_field_pill, parent_object=None):
        super().__init__()
        self._bucket_name = bucket_name
        self._name = name
        self._parent_obj = parent_object
        self._field_pill = field_pill
        self._bucket_locator = bucket_locator
        self._locators = Locators.Settings.Filters
        self._name = "Filters" 
        
    @property
    def Filters(self): return bucket(bucket_name="Filters", bucket_locator=self._locators.filter_bucket)
    
    def verify_available_filter_fields(self, field_names, step_num, assert_type='equal'):
        """
        Description : To verify all available fields in bucket.
        :Usage - verify_available_fields(["Product Category", "Revenue", "Cost of Goods"], "10.11")
        """
        self._webelement.verify_elements_text(self._field_pill, field_names, step_num, self._name, assert_type, parent_instance=self._get_filter_bucket_object())
    
    def _get_filter_bucket_object(self):
        """
        Description : Returns filter bucket object
        """
        bucket_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._bucket_locator, self._name, self._parent_obj)
        bucket_obj = [bucket for bucket in bucket_objects if self._bucket_name in bucket.text.strip()][0]
        if bucket_obj != None:
            return bucket_obj
        else:
            msg = "[{}] bucket not found".format(self._bucket_name)
            raise LookupError(msg)
        
    def _get_filter_field_object(self, field_name):
        """
        Description : Returns filter field object
        """
        field_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._field_pill, self._name, self._get_bucket_object())
        field_obj = [field for field in field_objects if field_name == field.text.strip()]
        if field_obj != None:
            return field_obj[0]
        else:
            msg = "[{0}] field not found in the [{1}] bucket".format(field_name, self._bucket_name)
            raise LookupError(msg)  
    @property
    def AddParameterFieldList(self): 
        """
        Description: This function will return add parameter field list to perform actions
        """
        add_parameter_field_list_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.add_parameter_field_list, 'Add Parameter Field List')
        return Button(add_parameter_field_list_obj, "Add Parameter Field List Button")
    
    def AddParameterFieldListBuckets(self, Bucket_name):
        """
        Description: This function will return add parameter field list bucket to perform actions
        """
        return bucket(bucket_name=Bucket_name, bucket_locator=self._locators.add_parameter_field_list_bucket, 
                      field_pill=self._locators.add_parameter_field_list_field_pill, bucket_ellipses=self._locators.add_parameter_field_list_bucket_ellipses)
    
    def verify_parameter_field_buckets(self, expected_buckets, step_num, assert_type='equal'):
        """
        Description: Verify available parameter field buckets
        :Usage - verify_parameter_field_buckets(['Bucket 1', '01'])
        """
        self._webelement.verify_elements_text(self._locators.add_parameter_field_list_bucket_label, expected_buckets, step_num, self._name + " Buckets", assert_type)
    
    
class _PDFPage(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.Format
        self._name = "PDF Page" 
        
    def click_page_size_dropdown(self):
        """
        Description: This function will click on the page size dropdown
        """
        page_size_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.page_size_dropdown, self._name + " Page Size Dropdown")
        self._core_utils.python_left_click(page_size_obj)
    
        