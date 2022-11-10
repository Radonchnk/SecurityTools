import wx
import sys


def Quit_all():
    exit()


class MyPanel(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(MyPanel, self).__init__(*args, **kwargs)
        self.basicGUI()

    def basicGUI(self):
        # Main panel
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Choose tool

        dataFile = open("Tools/ToolsManager/data.txt", "r")
        ToolsList = dataFile.readline()
        dataFile.close()

        chooseOneBox = wx.SingleChoiceDialog(None, "Choose tool for work with",
                                             "Tools", ToolsList.split(','))
        if chooseOneBox.ShowModal() == wx.ID_OK:
            self.bilder(chooseOneBox.GetStringSelection())
        else:
            exit()

        self.Bind(wx.EVT_CLOSE, Quit_all, self)
        self.Show()

    def bilder(self, ToolName):
        Tool = "".join(ToolName.split())
        sys.path.insert(0, "Tools\\" + Tool)
        command = "import " + Tool + "\n" + Tool + "." + Tool + "()"
        exec(command)

class MyFrame(wx.Frame):
    app = wx.App()

    MyPanel(None)
    # app.MainLoop()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MyFrame()
    app.MainLoop()
