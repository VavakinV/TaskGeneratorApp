import wx
import MainFrame

# Создание приложения и главного окна
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame.View(None, title="Генерация заданий по Теории вероятностей и математической статистике")
    frame.Show()
    app.MainLoop()
