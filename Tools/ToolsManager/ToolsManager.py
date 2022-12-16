import wx
import sys
import shutil
def Quit_all(self):
    exit()

class ToolsManager(wx.Frame):
    def __init__(self, *args):
        super().__init__(None, title='Tools Manager')
        self.ToolsManager()

    def ToolsManager(self):
        # Main panel
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        #Chose tool
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        ChooseText = wx.StaticText(panel, -1, "Chose tool:")
        hbox1.Add(ChooseText, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        dataFile = open("Tools/ToolsManager/data.txt", "r")
        ToolsList = dataFile.readline()
        dataFile.close()

        self.choice = wx.Choice(panel, choices=ToolsList.split(','))
        hbox1.Add(self.choice, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        vbox.Add(hbox1)

        # Add and delete buttons
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.AddFilebtn = wx.Button(panel, -1, "Add File")
        self.AddFilebtn.Bind(wx.EVT_BUTTON, self.OnFileAdd) # bind
        hbox2.Add(self.AddFilebtn, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.DeleteToolbtn = wx.Button(panel, -1, "DeliteTool")
        hbox2.Add(self.DeleteToolbtn, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.DeleteToolbtn.Bind(wx.EVT_BUTTON, self.OnDeleteTool)  # bind
        vbox.Add(hbox2)

        # Horisontal line
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.sl = wx.StaticLine(panel, 2, pos=(50, 0), size=(400, 5),style = wx.LI_HORIZONTAL)
        hbox3.Add(self.sl, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        vbox.Add(hbox3)

        # Add tool
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        AddToolText = wx.StaticText(panel, -1, "Add tool:")
        hbox4.Add(AddToolText, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        self.AddToolbtn = wx.Button(panel, -1, "Add")
        self.AddToolbtn.Bind(wx.EVT_BUTTON, self.OnAddTool)  # bind
        hbox4.Add(self.AddToolbtn, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        vbox.Add(hbox4)

        # Setup Panel
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CLOSE, Quit_all, self)

        self.Show()
        wx.App().MainLoop()

    def ErrorMassege(self, message):
        wx.MessageBox(message, "Error", wx.OK | wx.ICON_INFORMATION)

    def OnFileAdd(self, event):
        try:
            ChosenTool = "".join(self.choice.GetString(self.choice.GetSelection()).split())
            sys.path.insert(0, "Tools/" + ChosenTool)

            openFileDialog = wx.FileDialog(None, "Open", "", "",
                                           "Any files (*.*)|*.*",
                                           wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

            openFileDialog.ShowModal()
            FilePath = openFileDialog.GetPath()
            openFileDialog.Destroy()

            shutil.copy(FilePath, "Tools/" + ChosenTool)
        except:
            self.ErrorMassege("Choose tool")

    def OnDeleteTool(self, event):
        try:
            ChosenTool = self.choice.GetString(self.choice.GetSelection())
            print(str(ChosenTool) + "2")
        except:
            self.ErrorMassege("Choose tool")

    def OnAddTool(self, event):
        ChosenTool = self.choice.GetString(self.choice.GetSelection())
        print(str(ChosenTool) + "3")
