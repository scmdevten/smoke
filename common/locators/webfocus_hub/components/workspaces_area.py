from selenium.webdriver.common.by import By

class Workspaces:
    
    parent_frame_css        =  "div.wfshell-plugin-content-frame iframe[class*='legacy-workspaces-plugin-content']"
    iframe_css              =  "div.home-old-workspaces iframe"
    page_load_completed_css =  "body.ibx-visible"
    
    
    class ResourceTree:
        
        resources_tree_css  =  "div.left-pane .ibfs-tree "  
        expand_icon         =  (By.CSS_SELECTOR, "div.home-tree-node-btn")
        collapse_icon       =  (By.CSS_SELECTOR, "div[class='home-tree-node-btn fld-open']")
        selected_item       =  (By.CSS_SELECTOR, resources_tree_css + ".ibfs-item-selected")
        collapse            =  (By.CSS_SELECTOR, "div.left-pane div.tree-collapse-button")
        expand              =  (By.CSS_SELECTOR, "div.tree-showcollapse-button:not([style*='none'])")
        items               =  (By.CSS_SELECTOR, resources_tree_css + " .ibfs-label")
        new_workspace       =  (By.CSS_SELECTOR, "div[title='New workspace']")
        new_folder          =  (By.CSS_SELECTOR, "div[title='New folder']")
        new_workspace_icon  =  (By.CSS_SELECTOR, new_workspace[1] + " div.ds-icon-workspace-add")
        new_folder_icon     =  (By.CSS_SELECTOR, new_folder[1] + " div.ds-icon-folder-add")
        
        
    class NavigationBar:
        
        navigation_bar_css        =  "div.toolbar "
        breadcrumb_css            =  "div.toolbar div[data-ibx-type='breadCrumbTrail'] div[title='{0}'] "
        breadcrumb_arrow_css      =  breadcrumb_css + "+ div.sd-right-carat .fa-chevron-right"
        breadcrumbs               =  (By.CSS_SELECTOR, "div.toolbar div[data-ibx-type='breadCrumbTrail'] div[title]")
        list_view                 =  (By.CSS_SELECTOR, navigation_bar_css + ".btn-how-view-grid:not([style*='none'])")
        grid_view                 =  (By.CSS_SELECTOR, navigation_bar_css + ".btn-how-view:not([style*='none'])")
        refresh                   =  (By.CSS_SELECTOR, navigation_bar_css + "div.btn-refresh")
        content                   =  (By.CSS_SELECTOR, navigation_bar_css + "div.user-action-menu-btn")
        tile_view                 =  (By.CSS_SELECTOR, navigation_bar_css + "div[data-ibxp-glyph-classes*='ds-icon-grid']")
        list_view_                =  (By.CSS_SELECTOR, navigation_bar_css + "div[data-ibxp-glyph-classes*='ds-icon-list']")
        reverse_sort_order        =  (By.CSS_SELECTOR, navigation_bar_css + "div[data-ibxp-glyph-classes='ds-icon-arrow-up']")
        select_display_column     =  (By.CSS_SELECTOR, navigation_bar_css + "div[data-ibxp-glyph-classes='ds-icon-configure']")
        tile_view_icon            =  (By.CSS_SELECTOR, tile_view[1] + " div[class*='ds-icon-grid']")
        list_view_icon            =  (By.CSS_SELECTOR, list_view_[1] + " div[class*='ds-icon-list']")
        refresh_icon              =  (By.CSS_SELECTOR, refresh[1] + " div[class*='ds-icon-refresh']")
        select_display_column_icon=  (By.CSS_SELECTOR, select_display_column[1] + " div[class*='ds-icon-configure']")
        reverse_sort_order_icon   =  (By.CSS_SELECTOR, reverse_sort_order[1] + " div[class*='ds-icon-arrow-up']")
        
        
        
        
        class SortBy:
            
            navigation_bar_css   =  "div.toolbar "
            sort_by   =  (By.CSS_SELECTOR, navigation_bar_css + "div.sort-field-list")
            sort_by_input =  (By.CSS_SELECTOR, sort_by[1] + " input")
        
            
    class ContentArea:
        
        content_area_css        =  "div.files-box"
        gridview_xpth           =  "//div[@id='files-box-area'][not(contains(@style, 'none'))]"
        gridview_file_xpath     =  gridview_xpth + "//img[contains(@src, '{1}')]//parent::div//following-sibling::div[normalize-space() = '{0}'][contains(@class, 'file-item-hbox')]/parent::div" 
        listview_file_xpath     =  "//div[@id='files-listing-area'][not(contains(@style, 'none'))]//div[normalize-space()='{0}'][@title]//div[not(contains(@class, 'fa-folder'))][contains(@class,'ibx-glyph-{1}')]//parent::div[@title]"
        grid_view               =  (By.CSS_SELECTOR, "div.files-box-files:not([style*='none']) ")
        grid_view_files         =  (By.CSS_SELECTOR, grid_view[1] + ".file-item")
        grid_view_folders       =  (By.CSS_SELECTOR, grid_view[1] + ".folder-item .folder-div")
        list_view               =  (By.CSS_SELECTOR, "div.files-listing:not([style*='none']) ")
        list_view_files         =  (By.CSS_SELECTOR, list_view[1] + "div[data-ibx-type='ibxLabel']:not([class*='files-box-files-'])")
        list_view_folders       =  (By.CSS_SELECTOR, list_view[1] + "[class*='files-box-files-'].grid-cell-data")
        list_view_folder_icon   =  (By.CSS_SELECTOR, ".ibx-label-icon")
        grid_view_summary       =  (By.CSS_SELECTOR, ".file-item-text-box")
        listview_columns_heading=  (By.CSS_SELECTOR, list_view[1] + ".grid-cell-title")
        shared_item_icon        =  (By.CSS_SELECTOR, ".fa-share-alt")
        shared_user_icon        =  (By.CSS_SELECTOR, ".fa-user")
        shortcut_icon           =  (By.CSS_SELECTOR, ".ds-icon-shortcut")
        listview_choose_columns =  (By.CSS_SELECTOR, list_view[1] + "div[title='Choose columns'] div.fa-cog")
        grid_view_sorting       =  (By.CSS_SELECTOR, grid_view[1] + ".content-title-btn-name")
        grid_view_sorted_arrow  =  (By.CSS_SELECTOR, grid_view[1] + ".content-title-buttons .material-icons")
        coloumn_titles          =  (By.CSS_SELECTOR, ".files-box-files-title [role='button']:not([style*='none']) ") 
        
        