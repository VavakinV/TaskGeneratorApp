import wx
import CheckBoxPanel
import docx_generation
import InfoFrame

class MainPanel(wx.Panel):
    
    def __init__(self, parent):
        super(MainPanel, self).__init__(parent)
        
        #Main titles
        self.mainTitle = wx.StaticText(self, label="Задания формируются согласно варианту №3 типовых расчетов"
                                       , pos=(50, 20))
        
        #CheckBoxes
        self.checkBoxPanel = CheckBoxPanel.CheckBoxPanel(self)

        self.checkBoxPanel.SetPosition((10, 100))
        self.checkBoxPanel.SetSize((500, 320))
        
        #Setting active all checkboxes
        for i in range(18):
            self.checkBoxPanel.checkboxes[i].SetValue(True)
        
        #Count of variants
        self.countVariantsTextBox = wx.TextCtrl(self, pos=(325, 60), size=(30, -1))
        self.countVariantsTextBox.Bind(wx.EVT_TEXT, self.onTextChange)
        
        self.variantsLabel = wx.StaticText(self, label="Введите количество вариантов: ", pos=(120, 62))
        
        self.generateButton = wx.Button(self, label="Сгенерировать варианты и ответы", pos=(100, 420), size=(300, 25))
        self.generateButton.Bind(wx.EVT_BUTTON, self.onClickGenerateButton)

        self.generateButton = wx.Button(self, label="О программе", pos=(100, 470), size=(300, 25))
        self.generateButton.Bind(wx.EVT_BUTTON, self.showInfo)

        
    def onTextChange(self, event):
        content = self.countVariantsTextBox.GetValue()
        
        if len(content) > 2:
            self.countVariantsTextBox.SetValue(content[:2])
            self.countVariantsTextBox.SetInsertionPointEnd()
        event.Skip() 

    def onClickGenerateButton(self, event):
        # Создание диалогового окна для выбора папки
        dialog = wx.DirDialog(None, "Выберите папку для сохранения файлов", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        
        if dialog.ShowModal() == wx.ID_OK:
            # Получение выбранного пути
            folder_path = dialog.GetPath()
            
            tasks = []
            for i in range(18):
                if self.checkBoxPanel.checkboxes[i].GetValue():
                    tasks.append(i + 1)
            
            # Формирование путей для сохранения файлов
            taskOutputFile = f"{folder_path}/tasks.docx"
            answerOutputFile = f"{folder_path}/answers.docx"

            print(taskOutputFile)
            print(answerOutputFile)
            
            # Вызов функции для генерации документов
            docx_generation.generateDocument(taskOutputFile=taskOutputFile, answerOutputFile=answerOutputFile, variants=int(self.countVariantsTextBox.GetValue()), tasks=tasks)
        
        dialog.Destroy()    

    def showInfo(self, event):
        infoFrame = InfoFrame.View(None, title="О программе")
        infoFrame.Show()
    
        