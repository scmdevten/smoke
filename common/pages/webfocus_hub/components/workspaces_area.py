import keyboard
from common.lib import html_controls
from common.pages.basepage import BasePage
from common.pages.webfocus_hub.dialog import Dialog
from common.lib.webfocus import ibx_custom_controls
from selenium.common.exceptions import NoSuchElementException
from common.locators.webfocus_hub.components.workspaces_area import Workspaces as Locators


class WorkspacesArea(BasePage):
    
    def __init__(self):
        super().__init__()
        
    def switch_to_frame(self):
        """
        Description : Switch to iframe to work on workspaces area
        """
        self._utils.synchronize_until_element_is_visible(Locators.parent_frame_css, expire_time=120)
        self._core_utils.switch_to_frame(Locators.parent_frame_css)
        self._utils.synchronize_until_element_is_visible(Locators.iframe_css, expire_time=120)
        self._core_utils.switch_to_frame(Locators.iframe_css)
        self._utils.synchronize_until_element_is_visible(Locators.ResourceTree.resources_tree_css, 80)
        self._utils.wait_for_page_loads(40, pause_time=2) 
        
    def switch_to_default_content(self):
        """
        Description : Switch to default content
        """
        self._core_utils.switch_to_default_content()
        
    @property
    def ResourcesTree(self): return _ResourcesTree()
    
    @property
    def NavigationBar(self): return _NavigationBar()
    
    @property
    def ContentArea(self): return _ContentArea()
    

class _ResourcesTree(BasePage):
    
    def __init__(self):
        super().__init__() 
        self._locators = Locators.ResourceTree
        self._name = "Resource Tree"
        
    @property
    def NewWorkspace(self):
        """ Return New Workspace button to perform actions """
        name = self._name + " New Workspace"
        new_workspace_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.new_workspace , "New Workspace Button")
        return ibx_custom_controls.Icon(new_workspace_button, self._locators.new_workspace_icon, "\ebf3", name)
        
    @property
    def NewFolder(self):
        """ Return New Folder button to perform actions """
        name = self._name + " New Folder"
        new_folder_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.new_folder , "New Folder Button")
        return ibx_custom_controls.Icon(new_folder_button, self._locators.new_folder_icon, "\ebf2", name)

    def select_workspaces(self):
        """
        Description : Left click on Workspaces 
        """
        self.select("Workspaces")
            
    def expand_workspaces(self):
        """
        Description : Select the tree by left click
        :Usage1 - expand("P292->S12345->G123456")
        """
        self.expand("Workspaces")
            
    def expand(self, tree_path):
        """
        Description : Expand the tree by clicking expand icon
        :Usage - expand("P292->S12345")
        """
        self._expand_tree_(tree_path.split("->"))
        self._utils.wait_for_page_loads(15, pause_time=1)
        
    def collapse(self, tree_path, collapse_parent=True):
        """
        Description : Collapse the tree by clicking collapse icon
        arg : collapse_parent = if True then collapse parent node otherwise collapse child nodes except parent
        :Usage - collapse("S12345->P292")
        """
        child_note_xpath = "/following-sibling::div//div[normalize-space()='{}']"
        tree_path = tree_path.split("->")[::-1]
        parent_node_xpath = "//div[@class='ibfs-tree']//div[normalize-space()='{}']".format(tree_path[0])
        for index in range(len(tree_path), 0, -1):
            if not collapse_parent and index == 1:
                break
            target_node_xpath = child_note_xpath*(index-1)
            target_node_xpath = parent_node_xpath + target_node_xpath.format(*tree_path[1:index])
            nodes = self._driver.find_elements_by_xpath(target_node_xpath)
            if nodes != []:
                self._javascript.scrollIntoView(nodes[0], wait_time=1)
                collapse_icon = nodes[0].find_elements(*self._locators.collapse_icon)
                (collapse_icon != []) and self._core_utils.left_click(collapse_icon[0])
                self._utils.wait_for_page_loads(15, pause_time=1)
            else:
                msg = "[{0}] folder not exists in home page workspace resources tree".format("->".join(tree_path[:index]))
                raise KeyError(msg)
            
    def collapse_workspaces(self):
        """
        Description : Collapse the Workspaces by clicking collapse icon
        :Usage - collapse_workspaces()
        """
        self.collapse("Workspaces")
            
    def select(self, tree_path):
        """
        Description : Select the tree by left click
        :Usage1 - expand("P292->S12345->G123456")
        """
        tree_object = self._get_tree_object_(tree_path)
        self._core_utils.left_click(tree_object)
        self._utils.wait_for_page_loads(15, pause_time=2)
        self._utils.synchronize_until_element_is_visible(Locators.page_load_completed_css, 120)
        
    def double_click(self, tree_path):
        """
        Description : Select the tree by left click
        :Usage1 - expand("P292->S12345->G123456")
        """
        tree_object = self._get_tree_object_(tree_path)
        self._core_utils.double_click(tree_object)
        self._utils.wait_for_page_loads(15, pause_time=2)
        self._utils.synchronize_until_element_is_visible(Locators.page_load_completed_css, 120)
        
    def right_click(self, tree_path):
        """
        Description : Select the tree by left click
        :Usage1 - expand("P292->S12345->G123456")
        """
        tree_object = self._get_tree_object_(tree_path)
        self._core_utils.right_click(tree_object)
        self._utils.synchronize_until_element_is_visible(Locators.page_load_completed_css, 60)
        
    def verify_items(self, expected_items, step_num, assert_type='asin', parent_folder=None):
        """
        Description : Verify the visible or invisible resource items text in workspaces view
        :arg : parent_folder = If you wants to verify items under the specific folder then pass parent_folder. Exp: parent_folder="P292->S123456"
        :Usage : verify_items(["Workspaces", "1TestV3", "P292_S10660"], "01.02")
        """
        if parent_folder:
            parent_object = self._get_tree_object_(parent_folder)
            item_css = "#{} + div.ibfs-children .ibfs-label".format(parent_object.get_attribute("id"))
            items_object = self._driver.find_elements_by_css_selector(item_css)
        else:
            items_object = self._driver.find_elements(*self._locators.items)
        actual_items = [item.text.strip() for item in items_object if item.is_displayed()]
        msg = "Step {0} : Verify items in workspaces resources tree".format(step_num)
        self._utils.verify_list_values(expected_items, actual_items, msg, assert_type)
        
    def verify_unpublished_items(self, expected_items, step_num, assert_type='asin', parent_folder=None):
        """
        Description : Verify the visible or invisible resource items text in workspaces view
        :arg : parent_folder = If you wants to verify items under the specific folder then pass parent_folder. Exp: parent_folder="P292->S123456"
        :Usage : verify_unpublished_items(["Workspaces", "1TestV3", "P292_S10660"], "01.02")
        """
        if parent_folder:
            parent_object = self._get_tree_object_(parent_folder)
            item_css = "#{} + div.ibfs-children .ibfs-label".format(parent_object.get_attribute("id"))
            items_object = self._driver.find_elements_by_css_selector(item_css)
        else:
            items_object = self._driver.find_elements(*self._locators.items)
        actual_items = [item.text.strip() for item in items_object if item.is_displayed() and item.value_of_css_property('font-style') == 'italic']
        msg = "Step {0} : Verify unpublished items in workspaces resources tree".format(step_num)
        self._utils.verify_list_values(expected_items, actual_items, msg, assert_type)
            
    def verify_selected_item(self, expected_item, step_num):
        """
        Description : Verify the selected resource items text in workspaces view
        :Usage : verify_selected_item(["P292_S10660"], "01.02")
        """
        items_object = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.selected_item, "Workspaces resources selected tree")
        actual_items = [item.text.strip() for item in items_object if item.is_displayed()]
        msg = "Step {0} : Verify {1} item selected in workspaces resources tree".format(step_num, expected_item)
        self._utils.verify_list_values(expected_item, actual_items, msg)
        
    def verify_expanded(self, tree_path, step_num):
        """
        Description : Verify whether resource tree item is expanded or Not
        :Usage : verify_expanded("P292", "01.02")
        """
        tree_object = self._get_tree_object_(tree_path)
        expanded_icon = tree_object.find_elements(*self._locators.collapse_icon)
        if len(expanded_icon) > 0 :
            expected_value = '"\ue993"'
            expanded_icon_value = self._javascript.get_element_before_style_properties(expanded_icon[0], 'content')
            state = True if expected_value == expanded_icon_value else False
        else :
            state = False
        msg = "Step {0} : Verify [{1}] item expanded in workspaces resources tree".format(step_num, tree_path)
        self._utils.asequal(True, state, msg)
            
    def verify_collapsed(self, tree_path, step_num):
        """
        Description : Verify whether resource tree item is collapsed or Not
        :Usage : verify_collapsed("P292", "01.02")
        """
        tree_object = self._get_tree_object_(tree_path)
        collapsed_icon = tree_object.find_elements(*self._locators.expand_icon)
        if len(collapsed_icon) > 0 :
            expected_value = '"\ue98c"'
            expanded_icon_value = self._javascript.get_element_before_style_properties(collapsed_icon[0], 'content')
            state = True if expected_value == expanded_icon_value else False
        else :
            state = False
        msg = "Step {0} : Verify [{1}] item collapsed in workspaces resources tree".format(step_num, tree_path)
        self._utils.asequal(True, state, msg)
            
    def _expand_tree_(self, tree_path_list):
        """
        Description : Expand tree path and return the last tree path xpath value.
        :Usage : _expand_tree_("P292->S1300")
        """
        tree_xpath = "//div[@class='ibfs-tree']//div[normalize-space()='{0}']"
        for tree in tree_path_list:
            tree_xpath = tree_xpath.format(tree)
            tree_objects = self._driver.find_elements_by_xpath(tree_xpath)
            if tree_objects != [] :
                tree_object = tree_objects[0]
                self._javascript.scrollIntoView(tree_object, wait_time=1)
                expand_icon_objs = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.expand_icon, "Expand Icon", parent_object=tree_object)
                if expand_icon_objs != [] :
                    expand_icon_obj = expand_icon_objs[0]
                    self._core_utils.python_left_click(expand_icon_obj)
                    self._utils.wait_for_page_loads(15, pause_time=0.5)
                    self._utils.synchronize_until_element_is_visible(Locators.page_load_completed_css, 120)
            else :
                msg = "[{0}] does not exists in paris home page resource tree".format(tree)
                raise LookupError(msg)
            tree_xpath = tree_xpath + "/following-sibling::div//div[normalize-space()='{0}']"
        return tree_xpath
        
    def _get_tree_object_(self, tree_path):
        """
        Description : Return the tree object
        :Usage - _get_tree_object_("P292->S123456")
        """
        tree_path = tree_path.split("->")
        (tree_path[0] != 'Global Resources') and self.expand_workspaces()
        target_tree = tree_path[-1]
        tree_path = tree_path[:-1]
        tree_xpath = self._expand_tree_(tree_path)
        self._utils.wait_for_page_loads(25, pause_time=3)
        tree_objects = self._driver.find_elements_by_xpath(tree_xpath.format(target_tree))
        if tree_objects == [] :
            msg = "[{0}] does not exists in paris home page resource tree".format(target_tree)
            raise LookupError(msg)
        tree_object = tree_objects[0]
        self._javascript.scrollIntoView(tree_object, wait_time=1)
        return tree_object
    
    
class _NavigationBar(BasePage):
    
    def __init__(self):
        super().__init__() 
        self._locators = Locators.NavigationBar
        self._name = "Navigation Bar "
        
    @property
    def ContentButton(self):
        """Return content button class object to perform actions"""
        content_button = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.content, "Content Button")
        return html_controls.Button(content_button, "Content Button")
    
    @property
    def SelectDisplayColumn(self):
        """ 
        Return Select Display Column Icon class object to perform actions
        """
        name = self._name + "Select Display Column"
        select_display_column_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.select_display_column, name)
        return ibx_custom_controls.Icon(select_display_column_obj, self._locators.select_display_column_icon, "\ea5a", name)
    
    @property
    def ReverseSortOrder(self):
        """ 
        Return Reverse Sort Order Icon class object to perform actions
        """
        name = self._name + "Reverse Sort Order"
        reverse_sort_order_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.reverse_sort_order, name)
        return ibx_custom_controls.Icon(reverse_sort_order_obj, self._locators.reverse_sort_order_icon, "\ea70", name)
    
    @property
    def TileView(self):
        """ 
        Return Tile View Icon class object to perform actions
        """
        name = self._name + "Tile View"
        tile_view_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.tile_view, name)
        return ibx_custom_controls.Icon(tile_view_obj, self._locators.tile_view_icon, "\e9e6", name)
    
    @property
    def ListView(self):
        """ 
        Return List View Icon class object to perform actions
        """
        name = self._name + "List View"
        list_view_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.list_view_, name)
        return ibx_custom_controls.Icon(list_view_obj, self._locators.list_view_icon, "\e9e7", name)
    
    @property
    def Refresh(self):
        """ 
        Return Refresh Icon class object to perform actions
        """
        name = self._name + "Refresh"
        refresh_obj = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.refresh, name)
        return ibx_custom_controls.Icon(refresh_obj, self._locators.refresh_icon, "\e9ea", name)
    
    @property 
    def SortBy(self): return _SortBy()
        
    def select_workspaces(self):
        """
        Description : Left click on Workspaces in breadcrumb
        """
        self.select_breadcrumb("Workspaces")
        
    def select_breadcrumb(self, name):
        """
        Description : Left click on given breadcrumb option
        :Usage - select_breadcrumb("My Content") 
        """
        breadcrumb_object =  self._utils.validate_and_get_webdriver_object(self._locators.breadcrumb_css.format(name), "Workspaces breadcrumb")
        self._core_utils.left_click(breadcrumb_object)
        self._utils.wait_for_page_loads(80, pause_time=1)
        self._utils.synchronize_until_element_is_visible(Locators.page_load_completed_css, 120)
            
    def click_breadcrumb_arrow(self, name):
        """
        Description : Left click on given breadcrumb arrow icon
        :Usage - select_breadcrumb("My Content") 
        """
        arrow_object =  self._utils.validate_and_get_webdriver_object(self._locators.breadcrumb_arrow_css.format(name), "Workspaces breadcrumb arrow")
        self._core_utils.left_click(arrow_object)
        # self._utils.synchronize_until_element_is_visible(paris_home_page_locators.Banner.popup_css, 20)
        
    def verify_breadcrumbs(self, expected_breadcrumbs, step_num):
        """
        Description : Verify the breadcrumbs text
        :Usage - verify_breadcrumbs("Workspaces>P292_S28313>G671781", "02.01")
        """
        actual_breadcrumbs = ""
        breadcrumbs_object = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.breadcrumbs, "Workspaces breadcrumbs")
        for breadcrumb in breadcrumbs_object :
            breadcrumb_text = breadcrumb.text.strip()
            actual_breadcrumbs += breadcrumb_text
            breadcrumb_arrow_obj = self._driver.find_elements_by_css_selector(self._locators.breadcrumb_arrow_css.format(breadcrumb_text))
            if breadcrumb_arrow_obj != []:
                arrow_text = self._javascript.get_element_before_style_properties(breadcrumb_arrow_obj[0], "content").replace('"\uf054"', ">")
                actual_breadcrumbs += arrow_text
        msg = "Step {0} : Verify [{1}] breadcrumbs displayed in workspaces navigation bar".format(step_num, expected_breadcrumbs)
        self._utils.asequal(expected_breadcrumbs, actual_breadcrumbs, msg)
        
    def wait_for_text(self, text, time_out=60):
        self._utils.synchronize_with_visble_text(self._locators.navigation_bar_css, text, time_out)
        
        
class _ContentArea(BasePage):

    def __init__(self):
        super().__init__() 
        self._locators = Locators.ContentArea
        self._name = "Content Area "

    def verify_grid_view_displayed(self, step_num):
        """
        Description : Verify whether grid view is active in content area
        :Usage - verify_grid_view_displayed("02.01")
        """
        msg = "Step {0} : Verify Grid view is displayed in workspaces content area".format(step_num)
        self._utils.asequal(True, self._is_grid_view_displayed_(), msg)

    def verify_list_view_displayed(self, step_num):
        """
        Description : Verify whether list view is active in content area
        :Usage - verify_list_view_displayed("02.01")
        """
        msg = "Step {0} : Verify List view is displayed in workspaces content area".format(step_num)
        self._utils.asequal(True, self._is_list_view_displayed_(), msg)

    def select_file(self, file_name, file_type=None):
        """
        Description : Left click on file to select
        :Usage - select_file("C123456")
        """
        file_object = self._get_file_object_(file_name, file_type)
        self._core_utils.left_click(file_object)
        self._utils.wait_for_page_loads(5, pause_time=0.5)

    def select_multiple_file(self, file_name_list):
        """
        Description : Select the multiple file using ctrl
        :Usage - select_multiple_file(["C123456", "C123455", "Chart"])
        """
        keyboard.press('ctrl')
        for file in file_name_list:
            file_object = self._get_file_object_(file)
            self._core_utils.python_left_click(file_object)
            self._utils.wait_for_page_loads(5, pause_time=0.5)
        keyboard.release('ctrl')

    def right_click_on_file(self, file_name, file_type=None):
        """
        Description : Right click on file
        :Usage - right_click_on_file("C123456")
        """
        file_object = self._get_file_object_(file_name, file_type)
        self._core_utils.right_click(file_object)
        self._utils.wait_for_page_loads(5, pause_time=0.5)

    def double_click_on_file(self, file_name, file_type=None):
        """
        Description : Double click on file
        :Usage - double_click_on_file("C123456")
        """
        file_object = self._get_file_object_(file_name, file_type)
        self._core_utils.double_click(file_object)
        self._utils.wait_for_page_loads(5, pause_time=0.5)

    def select_folder(self, folder_name):
        """
        Description : Left click on file to folder
        :Usage - select_folder("G123456")
        """
        folder_object = self._get_folder_object_(folder_name)
        self._core_utils.left_click(folder_object)
        self._utils.wait_for_page_loads(5, pause_time=0.5)

    def right_click_on_folder(self, folder_name):
        """
        Description : Right click on folder
        :Usage - right_click_on_folder("G123456")
        """
        folder_object = self._get_folder_object_(folder_name)
        self._core_utils.right_click(folder_object)
        self._utils.wait_for_page_loads(5, pause_time=0.5)

    def double_click_on_folder(self, folder_name):
        """
        Description : Double click on folder
        :Usage - double_click_on_folder("C123456")
        """
        folder_object = self._get_folder_object_(folder_name)
        self._core_utils.double_click(folder_object)
        self._utils.wait_for_page_loads(5, pause_time=0.5)

    def verify_folders(self, expected_folder, step_num, assert_type='asin'):
        """
        Description : Verify the visible or invisible folders
        :Usage : verify_folders(["G130043"], "01.02")
        """
        folders_locator = self._locators.grid_view_folders if self._is_grid_view_displayed_() else self._locators.list_view_folders
        folders_object = self._driver.find_elements(*folders_locator)
        actual_folders = [folder.text.strip() for folder in folders_object if folder.is_displayed()]
        msg = "Step {0} : Verify folders in workspaces content view".format(step_num)
        self._utils.verify_list_values(expected_folder, actual_folders, msg, assert_type)

    def verify_shared_folders(self, expected_folder, step_num, assert_type='asin'):
        pass

    def verify_shared_files(self, expected_file, step_num, assert_type='asin'):
        pass

    def verify_shortcut_folders(self, expected_folder, step_num, assert_type='asin'):
        pass

    def verify_shortcut_files(self, expected_file, step_num, assert_type='asin'):
        pass

    def verify_published_folders(self, expected_folder, step_num, assert_type='asin'):
        """
        Description : Verify the published folders
        :Usage : verify_published_folders(["G130043"], "01.02")
        """
        if self._is_grid_view_displayed_():
            folders_object = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.grid_view_folders, self._name + " Grid View Folders")
            actual_folders = []
            for folder in folders_object:
                try:
                    folder.find_element_by_css_selector("div[class*='state-div'] div[class*='ds-icon-unpublished']")
                except NoSuchElementException:
                    actual_folders.append(folder.text.strip())
        else:
            pass
        msg = "Step {0} : Verify published folders in workspaces content view".format(step_num)
        self._utils.verify_list_values(expected_folder, actual_folders, msg, assert_type)

    def verify_published_files(self, expected_file, step_num, assert_type='asin'):
        """
        Description : Verify the published files
        :Usage : verify_published_files(["Category Sales"], "01.02")
        """
        if self._is_grid_view_displayed_():
            files_object = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.grid_view_files, self._name + " Grid View Files")
            actual_folders = []
            for file in files_object:
                try:
                    file.find_element_by_css_selector("div[class^='file-item'] div[class*='ds-icon-unpublished']")
                except NoSuchElementException:
                    actual_folders.append(file.text.strip())
        else:
            pass
        msg = "Step {0} : Verify published files in workspaces content view".format(step_num)
        self._utils.verify_list_values(expected_file, actual_folders, msg, assert_type)

    
    def verify_unpublished_folders(self, expected_folder, step_num, assert_type='asin'):
        """
        Description : Verify the unpublished folders
        :Usage : verify_unpublished_folders(["G130043"], "01.02")
        """
        if self._is_grid_view_displayed_():
            folders_object = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.grid_view_folders, self._name + " Grid View Folders")
            actual_folders = []
            for folder in folders_object:
                try:
                    value = folder.find_element_by_css_selector("div[class*='state-div'] div[class*='ds-icon-unpublished']")
                    if value:
                        actual_folders.append(folder.text.strip())
                except NoSuchElementException:
                    pass
        else:
            pass
        msg = "Step {0} : Verify unpublished folders in workspaces content view".format(step_num)
        self._utils.verify_list_values(expected_folder, actual_folders, msg, assert_type)

    def verify_unpublished_files(self, expected_file, step_num, assert_type='asin'):
        """
        Description : Verify the unpublished filess
        :Usage : verify_unpublished_folders(["Category Sales"], "01.02")
        """
        if self._is_grid_view_displayed_():
            files_object = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.grid_view_files, self._name + " Grid View Files")
            actual_files = []
            for file in files_object:
                try:
                    value = file.find_element_by_css_selector("div[class^='file-item'] div[class*='ds-icon-unpublished']")
                    if value:
                        actual_files.append(file.text.strip())
                except NoSuchElementException:
                    pass
        else:
            pass
        msg = "Step {0} : Verify unpublished files in workspaces content view".format(step_num)
        self._utils.verify_list_values(expected_file, actual_files, msg, assert_type)
    
    def verify_folder_border_color(self, folder_name, step_num, expected_color='curious_blue1'):
        """
        Description : Verify the folder border color
        :Usage : verify_folder_border_color("G130043", "01.02")
        """
        folder_obj = self._get_folder_object_(folder_name)
        if self._is_list_view_displayed_():
            parent_xpath = "//div[@id='{0}']/parent::div".format(folder_obj.get_attribute('id'))
            folder_obj = self.driver.find_element_by_xpath(parent_xpath)
        msg = "Step {0} : Verify [{1}] folder border color".format(step_num, folder_name)
        self._utils.verify_element_color_using_css_property(None, expected_color, msg, 'border-top-color', folder_obj)

    def verify_files(self, expected_files, step_num, assert_type='asin'):
        """
        Description : Verify the visible or invisible files
        :Usage : verify_files(["C123456"], "01.02")
        """
        file_locator = self._locators.grid_view_files if self._is_grid_view_displayed_() else self._locators.list_view_files
        file_object = self._driver.find_elements(*file_locator)
        actual_files = [file.text.strip() for file in file_object if file.is_displayed()]
        msg = "Step {0} : Verify files in workspaces content view".format(step_num)
        self._utils.verify_list_values(expected_files, actual_files, msg, assert_type)

    def verify_file_summary(self, file_name, expected_summary, step_num, file_type=None):
        """
        Description : Verify the file summary
        :Usage : verify_file_summary("C123456", "This is chart file", "01.02")
        """
        file_object = self._get_file_object_(file_name, file_type)
        if self._is_grid_view_displayed_():
            self._core_utils.move_to_element(file_object)
            summary_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.grid_view_summary, "File summary", parent_object=file_object)
            actual_summary = summary_obj.text.strip()
        else:
            pass
        msg = "Step {0} : Verify [{1}] summary  displayed for [{2}] file".format(step_num, expected_summary, file_name)
        self._utils.asequal(expected_summary, actual_summary, msg)

    def delete_folder(self, folder_name):
        """
        Description : Delete the folder in content area.
        """
        self.right_click_on_folder(folder_name)
        modal = Dialog()
        ibx_custom_controls.ContextMenu().select("Delete")
        modal.Delete.wait_for_text("Delete")
        modal.Delete.Ok.click()
        modal.Delete.wait_until_invisible()
        self._utils.wait_for_page_loads(30)
        self._utils.synchronize_until_element_is_visible(Locators.page_load_completed_css, 120)

    def delete_file(self, file_name):
        """
        Description : Delete the file in content area.
        """
        self.right_click_on_file(file_name)
        modal = Dialog()
        ibx_custom_controls.ContextMenu().select("Delete")
        modal.Delete.wait_for_text("Delete")
        modal.Delete.Ok.click()
        modal.Delete.wait_until_invisible()
        self._utils.wait_for_page_loads(30)
        self._utils.synchronize_until_element_is_visible(Locators.page_load_completed_css, 120)

    def delete_folder_if_exists(self, folder_name):
        """
        Description : Delete the folder if exists in content area.
        """
        try :
            self.delete_folder(folder_name)
        except:
            pass

    def delete_file_if_exists(self, file_name):
        """
        Description : Delete the file if exists in content area.
        """
        try :
            self.delete_file(file_name)
        except:
            pass

    def _is_grid_view_displayed_(self):
        """
        Description : Return True if grid view is displayed in content area
        """
        grid_view = self._driver.find_elements(*self._locators.grid_view)
        status = True if grid_view != []  else False
        return status

    def _is_list_view_displayed_(self):
        """
        Description : Return True if list view is displayed in content area
        """
        list_view = self._driver.find_elements(*self._locators.list_view)
        status = True if list_view != []  else False
        return status

    def _get_list_view_cell_object_(self, file_name, column_name, file=True, file_type=None):
        """
        Description : Return the list view cell object based on file name column name
        for example, if you want to get summary cell object of any file then you can call this funtion
        :Usage - _get_list_view_cell_object("C1234567", 'Summary')
        """
        if self._is_list_view_displayed_():
            columns_obj = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.list_view_columns, "List view columns")
            column_index = self._javascript.find_element_index_by_text(columns_obj, column_name)
            if column_index is not None:
                file_object = self._get_file_object_(file_name, file_type) if file else self._get_folder_object_()
                row_object = self._javascript.get_parent_element(file_object)
                cell_object = self._javascript.get_child_elements(row_object)[column_index]
                return cell_object
            else:
                msg = "[{0}] column does not displayed in content area list view".format(column_name)
                raise LookupError(msg)
        else:
            msg = "List view does not displayed in content area"
            raise TabError(msg)

    def _get_file_object_(self, file_name, file_type=None):
        """
        Description : Return the file object. If grid view is active then file object return from grid view else return from list view.
        :param - file_type - file type to filter the file object. 
        :file_type : ['fex', 'url', 'folder']
        """
        file_type_value = ''
        if self._is_grid_view_displayed_():
            grid_view_file_types = {'fex' : 'fex', 'url' : 'url'}
            file_xpath = self._locators.gridview_file_xpath
            if file_type is not None :
                file_type = file_type.lower()
                file_type_value = grid_view_file_types.get(file_type)
        else:
            file_xpath = self._locators.listview_file_xpath
            list_view_file_types = {'fex' : 'fex', 'url' : 'url'}
            if file_type is not None :
                file_type = file_type.lower()
                file_type_value = list_view_file_types.get(file_type)
        if file_type_value is None :
            msg = "Currently we are not implemented [{0}] file type to filter the file object.".format(file_type)
            raise NotImplementedError(msg)
        file_xpath = file_xpath.format(file_name, file_type_value)
        file_objects = self._driver.find_elements_by_xpath(file_xpath)
        if file_objects == [] :
            msg = "[{0}] file does not exist in content area.".format(file_name)
            raise FileNotFoundError(msg)
        self._javascript.scrollIntoView(file_objects[0], wait_time=1)
        return file_objects[0]

    def _get_folder_object_(self, folder_name):
        """
        Description : Return the folder object. If grid view is active then file object return from grid view else return from list view.
        """
        if self._is_grid_view_displayed_():
            folders_locator = self._locators.grid_view_folders
        else :
            folders_locator = self._locators.list_view_folders
        folder_objects = self._utils.validate_and_get_webdriver_objects_using_locator(folders_locator, "Content grid view folder")
        folder_index = self._javascript.find_element_index_by_text(folder_objects, folder_name)
        if folder_index is None:
            msg = "[{0}] folder does not exist in content area.".format(folder_name)
            raise FileNotFoundError(msg)
        folder_object = folder_objects[folder_index]
        self._javascript.scrollIntoView(folder_object, wait_time=1)
        return folder_object
    
    def wait_for_text(self, text, time_out=60):
        self._utils.synchronize_with_visble_text(self._locators.content_area_css, text, time_out)
        

    def drag_and_drop_files_into_worksapces(self,file_name,target_tree, file_type=None, item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0):
        """
        Description : This function is to drag and drop file from content area to the workspaces in the resource tree
        
        """        
        file_object = self._get_file_object_(file_name, file_type)
        self._core_utils.python_left_click(file_object)
        tree_xpath = "//div[@class='ibfs-tree']//div[normalize-space()='{0}']"
        target_objects = self._driver.find_elements_by_xpath(tree_xpath.format(target_tree))
        target_obj = target_objects[0]
        self._javascript.scrollIntoView(target_obj, wait_time=1)
        source_loc = self._core_utils.get_web_element_coordinate(file_object, item_loc, sx, sy)
        target_loc = self._core_utils.get_web_element_coordinate(target_obj, target_obj_loc, tx, ty)
        self._core_utils.drag_and_drop_without_using_click(source_loc['x'], source_loc['y'], target_loc['x'], target_loc['y'])
        
    def drag_and_drop_files_into_contentarea(self,source_file_name,target_file_name, file_type=None, item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0):
        """
        Description : This function is to drag and drop file from content area to content area 
         
        """        
        source_file_object = self._get_file_object_(source_file_name,file_type)
        self._core_utils.python_left_click(source_file_object)
        target_file_object = self._get_folder_object_(target_file_name)
        self._javascript.scrollIntoView(target_file_object, wait_time=1)
        source_loc = self._core_utils.get_web_element_coordinate(source_file_object, item_loc, sx, sy)
        target_loc = self._core_utils.get_web_element_coordinate(target_file_object, target_obj_loc, tx, ty)
        self._core_utils.drag_and_drop_without_using_click(source_loc['x'], source_loc['y'], target_loc['x'], target_loc['y'])
        
    def drag_and_drop_files_tree_into_contentarea(self,source_tree,target_file_name, item_loc="middle", sx=0, sy=0, target_obj_loc="middle", tx=0, ty=0):
        """
        Description : This function is to drag and drop folder from resources tree to content area
         
        """        
        tree_xpath = "//div[@class='ibfs-tree']//div[normalize-space()='{0}']"
        source_objects = self._driver.find_elements_by_xpath(tree_xpath.format(source_tree))
        source_obj = source_objects[0]
        target_obj = self._get_folder_object_(target_file_name)
        self._javascript.scrollIntoView(target_obj, wait_time=1)
        source_loc = self._core_utils.get_web_element_coordinate(source_obj, item_loc, sx, sy)
        target_loc = self._core_utils.get_web_element_coordinate(target_obj, target_obj_loc, tx, ty)
        self._core_utils.drag_and_drop_without_using_click(source_loc['x'], source_loc['y'], target_loc['x'], target_loc['y'])
        
    def verify_Display_coloumns(self,expected_option,step_num, assert_type='asequal'):
        if self._is_list_view_displayed_():
            coloumns_object = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.coloumn_titles, "Select Display Coloumns")
            actual_coloumns = [coloumns.text.strip() for coloumns in coloumns_object if coloumns.is_displayed()]
            msg = "Step {0} : Verify display coloumns in workspaces content view".format(step_num)
            self._utils.verify_list_values(expected_option, actual_coloumns, msg, assert_type)
                
        else:
            msg = "List view does not displayed in content area"
            raise TabError(msg)
    
    def click_listView_coloumn_Title(self,option):
        
        if self._is_list_view_displayed_():
            coloumns_object = self._utils.validate_and_get_webdriver_objects_using_locator(self._locators.coloumn_titles, "Select Display Coloumns")
            template_object = coloumns_object[[el.text.strip() for el in coloumns_object].index(option)]
            self._core_utils.python_left_click(template_object)
        
    
class _SortBy(BasePage):
    
    def __init__(self):
        super().__init__()
        self._locators = Locators.NavigationBar.SortBy
        self._name = "Sort By "
        
    @property
    def Dropdown(self): return ibx_custom_controls.ibxSelectItemList()
        
    def Click(self):
        
        sort_by = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.sort_by, self._name)
        self._core_utils.python_left_click(sort_by)
        
    def verify_selected_option(self, expected_option, step_num):
        """
        Description: Function will verify selected option in the sort by dropdown
        :Usage- verify_selected_option("Title", "02")
        """
        sort_by_input = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.sort_by_input, self._name + " Input")
        actual_option = sort_by_input.get_attribute("aria-label")
        msg = "Step {0}: Verify Selected Option".format(step_num)
        self._utils.asequal(expected_option, actual_option, msg)
        
    def verify_displayed(self,step_num):
        """
        Description : Verify whether Dropdown displayed 
        :Usage - verify_displayed("03.04")
        """
        msg = "Step {0} : Verify [{1}] Dropdown is displayed".format(step_num, self._name)
        sort_by = self._utils.validate_and_get_webdriver_object_using_locator(self._locators.sort_by,self._name)
        self._utils.asequal(True, sort_by.is_displayed(), msg) 
        
        
        
        