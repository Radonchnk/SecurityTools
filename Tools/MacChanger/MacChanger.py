import wx

def Quit_all(self):
    exit()

class MacChanger(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(None, title='MAC Changer',*args, **kwargs)
        self.Show()

        self.Bind(wx.EVT_CLOSE, Quit_all, self)

        wx.App().MainLoop()
