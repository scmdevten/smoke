from common.wftools.login import Login
from common.pages.basepage import BasePage
from common.pages.webfocus_hub import dialog
from common.pages.webfocus_hub import components
from common.lib.webfocus import ibx_custom_controls
from common.pages import paris_home_page
from common.lib.webfocus import get_data_frame
from common.pages import vfour_miscelaneous, vfour_portal_ribbon, rc_advance
from common.wftools import text_editor

class WebFocusHub(BasePage):
    
    def __init__(self):
        super().__init__()
        
    def invoke_with_login(self, mrid, mrpass):
        
        Login(self._driver).invoke_paris_home_page(mrid, mrpass)
    
    @property
    def Banner(self): return components.Banner()
    
    @property
    def LeftSideNavigationBar(self): return components.LeftSideNavigationBar()
    
    @property
    def Home(self): return components.HomeArea()
    
    @property
    def Workspaces(self): return components.WorkspacesArea()
    
    @property
    def ManagementCenter(self): return components.ManagementCenter()
    
    @property
    def ApplicationDirectories(self): return components.ApplicationDirectories()
    
    @property
    def Portals(self): return components.Portals()
    
    @property
    def SearchWebfocus(self): return components.SearchWebfocus()

    @property
    def Dialog(self): return dialog.Dialog()
        
    @property
    def ContextMenu(self): return ibx_custom_controls.ContextMenu()
    
    @property
    def GetDataFrame(self): return get_data_frame.GetDataFrame(self._driver)
    
    @property
    def Vfour_Miscelaneous(self): return vfour_miscelaneous.Vfour_Miscelaneous(self._driver)
    
    @property
    def Vfour_Portal_Ribbon(self): return vfour_portal_ribbon.Vfour_Portal_Ribbon(self._driver)
    
    @property
    def RC_Advance(self): return rc_advance.RC_Advance(self._driver)
    
    @property
    def Wf_Mainpage(self): return text_editor.Wf_Mainpage(self._driver)
    
    @property
    def NotifyPopup(self):return paris_home_page.NotifyPopup(self._driver)
    
    @property
    def RunWindow(self): return paris_home_page.RunWindow(self._driver)
    
    @property
    def Wf_Texteditor(self): return text_editor.wf_texteditor(self._driver)
    
    
    
    
    
    