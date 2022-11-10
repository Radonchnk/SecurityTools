import wx

def Quit_all(self):
    exit()

class ToolsManager(wx.Frame):
    def __init__(self, *args):
        super().__init__(None, title='Tools Manager')
        self.ToolsManager()

    def ToolsManager(self):
        wx.Panel(self)

        # Choose tool
        dataFile = open("Tools/ToolsManager/data.txt", "r")
        ToolsList = dataFile.readline()
        dataFile.close()

        chooseOneBox = wx.SingleChoiceDialog(None, "Choose tool", "Tools Manager", ToolsList.split(','))




        if chooseOneBox.ShowModal() == wx.ID_OK:
            exit()

        self.Bind(wx.EVT_CLOSE, Quit_all, self)
        self.Show()

        '''
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        ToolsList = wx.StaticText(panel, -1, "Tools")
        hbox2.Add(ToolsList, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.ToolsListBox = wx.TextCtrl(panel, size=(300, 100), style=wx.TE_MULTILINE | wx.TE_READONLY, value=Tools)
        hbox2.Add(self.ToolsListBox, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        vbox.Add(hbox2)

        # Start button
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        StartText = wx.StaticText(panel, -1, "Start Script")
        hbox3.Add(StartText, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.btn = wx.Button(panel, -1, "Start!")
        hbox3.Add(self.btn, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        vbox.Add(hbox3)

        # Setup Panel
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CLOSE, Quit_all, self)
        '''