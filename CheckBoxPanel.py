import wx

class CheckBoxPanel(wx.Panel):
    
    def __init__(self, parent):
        super(CheckBoxPanel, self).__init__(parent)
        
        self.checkboxes = []
        self.countAssignmentsLabel = wx.StaticText(self, label=f"Количество выбранных заданий: 18", pos=(120,260))
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        vbox1 = wx.BoxSizer(wx.VERTICAL) #9 заданий
        vbox2 = wx.BoxSizer(wx.VERTICAL) #9 заданий
        
        for i in range(18):
            
            cb = wx.CheckBox(self)    
            cb.Bind(wx.EVT_CHECKBOX, self.checkBoxValueChange)
            self.checkboxes.append(cb)    
            if (i < 9):
                vbox1.Add(cb, 0, wx.ALL|wx.EXPAND, 5)
            else: vbox2.Add(cb, 0, wx.ALL|wx.EXPAND, 5)
        
        #Лэйблы описания заданий
        self.checkboxes[0].SetLabel("1. Комбинаторика")
        self.checkboxes[1].SetLabel("2. Гипергеометрическое распределение")
        self.checkboxes[2].SetLabel("3. Алгебра событий")
        self.checkboxes[3].SetLabel("4. Случайные события")
        self.checkboxes[4].SetLabel("5. Случайные события")
        self.checkboxes[5].SetLabel("6. Независимые события")
        self.checkboxes[6].SetLabel("7. Формула полной вероятности")
        self.checkboxes[7].SetLabel("8. Формула Байеса")
        self.checkboxes[8].SetLabel("9. Схема Бернулли")
        
        self.checkboxes[9].SetLabel("10. Теорема Лапласа")
        self.checkboxes[10].SetLabel("11. Теорема Лапласа")
        self.checkboxes[11].SetLabel("12. Дискретная СВ")
        self.checkboxes[12].SetLabel("13. Дискретная СВ")
        self.checkboxes[13].SetLabel("14. Дискретная СВ")
        self.checkboxes[14].SetLabel("15. 2 разные СВ")
        self.checkboxes[15].SetLabel("16. Равномерное распределение")
        self.checkboxes[16].SetLabel("17. Показательное распределение")
        self.checkboxes[17].SetLabel("18. Нормальное распределение")
        
        hbox.Add(vbox1, 1, wx.EXPAND)
        hbox.Add(vbox2, 1, wx.EXPAND)

        self.SetSizer(hbox)
        
    def checkBoxValueChange(self, event):
        
        count = 0
        for cb in self.checkboxes:
            if cb.IsChecked(): count += 1
        self.countAssignmentsLabel.Destroy()    
        self.countAssignmentsLabel = wx.StaticText(self, label=f"Количество выбранных заданий: {count}", pos=(120,260))
        