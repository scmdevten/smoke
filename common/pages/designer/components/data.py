from common.pages.basepage import BasePage
from common.lib import html_controls
from common.lib.webfocus import ibx_custom_controls
from selenium.webdriver.support.ui import WebDriverWait
from common.lib.global_variables import Global_variables
from common.locators.designer.components import data as locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Data(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = locator.Data
        self._name = "Data"
    
    @property
    def Source(self): return _Source()
    
    @property
    def Canvas(self): return _Canvas()
    
    @property
    def SampleData(self): return _SampleData()
    
    @property
    def DataToolbar(self): return _DataToolbar()
    
    @property
    def SelectEditorFrame(self): return _SelectEditorFrame()
    
    def switch_to_frame(self, timeout=90):
        """
        Description: Switch inside Data Tab Frame
        """
        frame = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.FRAME, "Data Frame")
        frame_location = self._core_utils.get_web_element_coordinate(frame, element_location='top_left')
        WebDriverWait(self._driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(frame))
        Global_variables.current_working_area_browser_x=frame_location['x']
        Global_variables.current_working_area_browser_y=frame_location['y']
        
        
class _Source(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = locator.Data.Source
        self._name = "Data Source"
        
    def drag_to_original_data(self, data_source, original_data, item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0):
        """
        Description: drag source item to original data in canvas to create a join
        """
        item_object = self._get_content_tree_row_object(data_source)
        self._core_utils.python_left_click(item_object)
        source_loc = self._core_utils.get_web_element_coordinate(item_object, item_loc, sx, sy)
        original_data_obj = _Canvas()._get_original_data_object(original_data)
        target_loc = self._core_utils.get_web_element_coordinate(original_data_obj, target_obj_loc, tx, ty)
        self._core_utils.drag_and_drop_without_using_click(source_loc['x'], source_loc['y'], target_loc['x'], target_loc['y'])
        _Canvas()._wait_for_text(original_data)
        
    def _get_content_tree_row_object(self, data_source):
        """
        Description : This method will return content view tree items element object as list
        """
        content_tree_items_object = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.row_css, 'Data content view items')
        required_obj = self._javascript.find_elements_by_text(content_tree_items_object, data_source)
        self._javascript.scrollIntoView(required_obj[0])
        return required_obj[0]
    
    @property
    def SearchTextBox(self):
        search_text_box = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Search_box, 'Search Text Box')
        return html_controls.TextBox(search_text_box,' Search Text Box')
    
    
class _Canvas(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = locator.Data.Canvas
        self._name = "Canvas"
        
    def verify_join_created(self, expected_join, step_num):
        """
        Description: Verifying created in join labels in canvas
        :Usage - verify_join_created(['Join 1', 'empdata (T01)', 'training (T02)'])
        """
        join_title_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.join_label_css, self._name + ' Join Label')
        self._webelement.verify_elements_text(join_title_objects, expected_join, step_num, self._name + ' Join Label')
        
    def _get_original_data_object(self, data_name):
        """
        Description: returns original data field object in canvas
        """
        original_data_object_css = self._locators.original_data_css.format(data_name)
        original_data_objects = self._utils.validate_and_get_webdriver_objects(original_data_object_css, 'Original Data')
        required_object = self._javascript.find_elements_by_text(original_data_objects, data_name)
        return required_object[0]
    
    def _wait_for_text(self, text, timeout=60):
        """
        Description: wait for text in the data canvas
        """
        self._webelement.wait_for_element_text(self._locators.canvas_css, text, timeout)

    
    def click(self, data_name):
        """
        Descriptions : This method will left click on canvas node.
        example      : click([wf_retail_sales'])
        """
        try:
            node_object = self._get_original_data_object(data_name)
            self._core_utils.python_left_click(node_object)
        except Exception as e:
            raise Exception(e)
        
    def Right_click(self,data_name):
        """
        Descriptions : This method will right click on canvas node.
        example      : click([wf_retail_sales'])
        """
        Node = (By.CSS_SELECTOR, "div[class*='ds-flow-node'][qa='{}']".format(data_name))
        node_obj = self._utils.validate_and_get_webdriver_object_using_locator(Node,'node_name')
        self._core_utils.right_click(node_obj)

    
class _SampleData(BasePage):
    
    def __init__(self):
        super().__init__()
    
    
class _DataToolbar():
        
    def __init(self):
        super().__init()
        
class _SelectEditorFrame(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = locator.Data.SelectEditor
        self._name = "Select Editor"
        
        
    @property
    def LeftSourcePane(self): return self._LeftSourcePane()
    
    @property
    def MiddlePane(self): return self._MiddlePane()
    
    @property
    def RightPane(self): return self._RightPane()
    
    def CancelButton(self):
        Button_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Cancel_Button, 'Cancel Button')
        self._core_utils.python_left_click(Button_obj)

    def OKButton(self):
        Button_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.OK_Button, 'OK Button')
        self._core_utils.python_left_click(Button_obj)    
    
    class _LeftSourcePane(BasePage):
        
    
        def __init__(self):
            super().__init__()
            self._locators = locator.Data.SelectEditor.LeftSourcePane
            self._name = "Select Editor Source pane"
          
        def SelectData(self,Data_name):
            """
            Descriptions : This method will double click Data_name ( BODY(T01) or SPECS(T01) )
            example      : SelectData('BODY(T01)')
            """
            Data_object = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Data_name.format(Data_name),'Data name')
            self._core_utils.double_click(Data_object)
            
        def SelectDataField(self,field_name):
            """
            Descriptions : This method will double click Field_name ('COUNTRY')
            example      : SelectDataField('COUNTRY')
            """            
            Field_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.Field_name,'Field name')
            Field_object = Field_objects[[field.text.strip() for field in Field_objects ].index(field_name)]
            self._core_utils.python_doubble_click(Field_object)
        
        
        
    class _MiddlePane(BasePage):
    

        def __init__(self):
            super().__init__()
            self._locators = locator.Data.SelectEditor.MiddlePane
            self._name = "Select Editor Middle pane"     
        
        
        @property
        def DeleteQuery(self):
            
            """
            Description : It returns delete query button object to perform actions
            """
            name = self._name + "Delete Query Button"
            delete_query_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.Delete_Query_Icon, name)
            return ibx_custom_controls.Icon(delete_query_obj, self._locators.Delete_Query_Icon, "", name)
        
        def VerifyBucketField(self,field_name,step_num):
            
            """
            Description : verifies field available in the bucket
            usage : VerifyBucketField('COUNTRY','01.01')
            """            
            
            Field_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.BucketField_name,'Field name')
            Field_object = Field_objects[[field.text.strip() for field in Field_objects ].index(field_name)]
            Bucket_Field_name  = Field_object.text.strip()
            msg = "Step {} : {} available in bucket".format(step_num,field_name)
            self._utils.asequal(Bucket_Field_name,field_name,msg)
    
    class _RightPane(BasePage):
    

        def __init__(self):
            super().__init__()
            self._locators = locator.Data.SelectEditor.RightPane
            self._name = "Select Editor Right pane"  
            
            
            
            
            
            
    