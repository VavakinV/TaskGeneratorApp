import wx
import MainPanel

class View(wx.Frame):
    def __init__(self, parent, title):
        super(View, self).__init__(parent, title=title, size=(500, 550))
        self.SetSizeHints(minW=500, minH=550, maxW=500, maxH=550)
        panel = MainPanel.MainPanel(self)
   