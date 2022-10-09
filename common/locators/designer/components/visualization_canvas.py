from selenium.webdriver.common.by import By


class VisualizationCanvas:
    
    chart_preview = (By.CSS_SELECTOR, "div[id*='chartpreview'] ")
    
    
    class FormattingToolbar:
        
        font_name = (By.CSS_SELECTOR, "div[title='Font Name']")
        font_size = (By.CSS_SELECTOR, "div[title='Font Size']")
        bold = (By.CSS_SELECTOR, "div[title*='bold']")
        italic = (By.CSS_SELECTOR, "div[title*='italic']")
        underline = (By.CSS_SELECTOR, "div[title*='underline']")
        left_align = (By.CSS_SELECTOR, "div[title*='Left']")
        centered = (By.CSS_SELECTOR, "div[title*='Centered']")
        right_align = (By.CSS_SELECTOR, "div[title*='Right']")
        text_color = (By.CSS_SELECTOR, "div.tb-colorSwatch-fore")
        background_color = (By.CSS_SELECTOR, "div.tb-colorSwatch-back")
        close = (By.CSS_SELECTOR, "div[title='Close']")
        color_palette = (By.CSS_SELECTOR, "div[data-ibx-type='colorSwatchPopup']")
        color = "div[data-ibx-type='colorSwatchPopup'] div[title='{}']"
        
    
    class Heading:
        
        heading = (By.CSS_SELECTOR, "div[data-ibx-type='wfcHeading'] div[role='region']")
        iframe = (By.CSS_SELECTOR, heading[1] + " iframe.ibx-iframe-frame")
        text = (By.CSS_SELECTOR, "body font textnode")
        parent = (By.CSS_SELECTOR, "body")
        title = (By.CSS_SELECTOR, parent[1] + " span[style*='font-size']")
    
    
        class RunMode:
            
            parent = (By.CSS_SELECTOR, "foreignObject[class='title']")
        
        
    class Footing:
        
        footing = (By.CSS_SELECTOR, "div[data-ibx-type='wfcFooting'] div[role='region']")
        iframe = (By.CSS_SELECTOR, footing[1] + " iframe.ibx-iframe-frame")
        
        
        class RunMode:
            
            parent = (By.CSS_SELECTOR, "foreignObject[class='footnote']")
            
            
    class RunMode:
        
        class AutoDrill:
            
            auto_drill_parent = (By.CSS_SELECTOR, "[id*='tdgchart-tooltip'][style*='visible']")
            menu_options = (By.CSS_SELECTOR, auto_drill_parent[1] + " ul li[class*='tdgchart-tooltip-pointer']")
            parent_menu_options = (By.CSS_SELECTOR, auto_drill_parent[1] + ">div>ul>li:nth-child(3)")
            sub_menu_parent = (By.CSS_SELECTOR, parent_menu_options[1] + " div[class*='tdgchart-submenu'][style*='visible']")
            sub_menu_options = (By.CSS_SELECTOR, sub_menu_parent[1] + " ul li[class*='tdgchart-tooltip-pointer']")
            tooltip_values = (By.CSS_SELECTOR, auto_drill_parent[1] + " li.tdgchart-tooltip-pad table tr td")
            
            
        class BreadCrumbTrail:
            
            bread_crumb_trail = (By.CSS_SELECTOR, "foreignObject[class='title'] span")
             
    
    class ConditionalStyling:  
        
        condtional_styling_panel = (By.CSS_SELECTOR, "div[data-ibx-type='conditionalStylingPanel'] ")      
        title_box = (By.CSS_SELECTOR, condtional_styling_panel[1] + "div[data-ibx-name='titleBox']")
        main_box = (By.CSS_SELECTOR, condtional_styling_panel[1] + "div[data-ibx-name='condStylingMain']")
        condition_title = (By.CSS_SELECTOR, condtional_styling_panel[1] + "div[data-ibx-name='conditionTitle']")
        condition_styling_elements = (By.CSS_SELECTOR, condtional_styling_panel[1] + "div[data-ibx-type='conditionalStylingElement']")
        add_condition = (By.CSS_SELECTOR, condtional_styling_panel[1] + " div[data-ibx-name='addCondition']")
        
        
        class Conditions:
            
            condtional_styling_panel = (By.CSS_SELECTOR, "div[data-ibx-type='conditionalStylingPanel'] ")
            styling_control_pane = (By.CSS_SELECTOR, condtional_styling_panel[1] + " div[data-ibx-name='stylingCtrlPane']")
            condition_heading = (By.CSS_SELECTOR, styling_control_pane[1] + " div[data-ibx-name='condHeader']")
            condition_sub_heading = (By.CSS_SELECTOR, styling_control_pane[1] + " div[data-ibx-name='condSubHeader']")
            conditional_statement = (By.CSS_SELECTOR, styling_control_pane[1] + " div[data-ibx-name='leftField']")
            condition_dropdown = (By.CSS_SELECTOR, styling_control_pane[1] + " div[data-ibx-name='operator']")
            field_or_value = (By.CSS_SELECTOR, styling_control_pane[1] + " div[data-ibx-name='fieldOrValue']")
            right_field = (By.CSS_SELECTOR, styling_control_pane[1] + " div[data-ibx-name='rightField']")
            value_inputbox = (By.CSS_SELECTOR, styling_control_pane[1] + " div[data-ibx-type='ibxTextField'] input")
        
        
        class Buttons:
            
            condtional_styling_panel = (By.CSS_SELECTOR, "div[data-ibx-type='conditionalStylingPanel'] ")
            cancel_button = (By.CSS_SELECTOR, condtional_styling_panel[1] + "div[data-ibxp-text='Cancel']")
            apply_button = (By.CSS_SELECTOR, condtional_styling_panel[1] + "div[data-ibxp-text='Apply']")
                    
            
    class PaginatedCanvas:
        
        paginated_canvas = (By.CSS_SELECTOR, "div[data-ibx-type='paginatedCanvas'] ")  
        canvas_pages = (By.CSS_SELECTOR, paginated_canvas[1] + "div[data-ibx-type='canvasPage']")
        canvas_report_data = (By.CSS_SELECTOR, "div[style*='position:absolute']")
        
    class Insights:
        
        base_css            =   "div[data-ibx-type='insightsWrapper'] "
        Activechart         =   (By.CSS_SELECTOR, "div[class^='insights-accordion-page']:not([class*='acc-pg-closed'])")
        Actionsbutton       =   (By.CSS_SELECTOR, base_css + "div[class^='insights-accordion-page']:not([class*='acc-pg-closed']) div[title='Actions']")
        Insight_trend_xaxis =   (By.CSS_SELECTOR, base_css + "div[class^='insights-accordion-page']:not([class*='acc-pg-closed']) div[class^='pd-canvas-widget'] [class^='xaxis'][class$='title']")
        Insight_trend_xaxis_labels = (By.CSS_SELECTOR, base_css + "div[class^='insights-accordion-page']:not([class*='acc-pg-closed']) div[class^='pd-canvas-widget'] [class^='xaxisOrdinal-labels']")
        Insight_trend_zaxis_labels = (By.CSS_SELECTOR, base_css + "div[class^='insights-accordion-page']:not([class*='acc-pg-closed']) div[class^='pd-canvas-widget'] [class^='zaxisOrdinal-labels']")
        Riser_locator       =   (By.CSS_SELECTOR, base_css + "div[class^='insights-accordion-page']:not([class*='acc-pg-closed']) div[class^='pd-canvas-widget'] rect[tdgtitle='placeholder']")
        