import wx
import InfoPanel

class View(wx.Frame):
    def __init__(self, parent, title):
        super(View, self).__init__(parent, title=title, size=(600, 450))
        self.SetSizeHints(minW=600, minH=450, maxW=600, maxH=450)
        panel = InfoPanel.InfoPanel(self)
   