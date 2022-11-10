import wx
import requests
import subprocess
import re
import multiprocessing


def Quit_all(self):
    exit()


class CloudflayerCheck(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Cloudflayer Check')
        self.GuiCloudCheck()

    def GuiCloudCheck(self):
        # menu bar
        menuBar = wx.MenuBar()
        HelpButton = wx.Menu()

        HelpButton.Append(wx.ID_EXIT, "Help", "status mag...")
        menuBar.Append(HelpButton, "Help")

        # Main panel
        # todo коли користувач натискає на "help" повинне вилазити вікно, яке каже як і що робити
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Reading Host
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        HostnameTextLine = wx.StaticText(panel, -1, "Write your hostname")
        hbox1.Add(HostnameTextLine, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.TextInputHostname = wx.TextCtrl(panel, value="google.com", style=wx.TE_CENTER)
        hbox1.Add(self.TextInputHostname, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        vbox.Add(hbox1)

        # todo додати мождивість оновлювати словник

        # Ip reange read
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        RangeText = wx.StaticText(panel, -1, "Write range of IPs")
        hbox2.Add(RangeText, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.IpRangeTextLine = wx.TextCtrl(panel)
        hbox2.Add(self.IpRangeTextLine, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        vbox.Add(hbox2)

        # Start button
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        StartText = wx.StaticText(panel, -1, "Start Script")
        hbox3.Add(StartText, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.btn = wx.Button(panel, -1, "Start!")
        self.Bind(wx.EVT_BUTTON, self.ScriptStart, self.btn)
        hbox3.Add(self.btn, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        vbox.Add(hbox3)

        # Setup Panel
        panel.SetSizer(vbox)
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_CLOSE, Quit_all, self)

        self.Show()
        wx.App().MainLoop()

    def ScriptStart(self, *args):
        data = str(self.TextInputHostname.GetLineText(0))
        self.CloudCheck(data)

    def CloudCheck(self, data):
        print("sdfgh")
        try:

            domain = data
            print(data)
        except KeyboardInterrupt:
            print('\n[-] Cloud Killer is closed !! ')
            quit()

        def checker(domain):
            try:
                link = requests.get('http://' + domain)
                print(link)
                if link.status_code == 200 or link.status_code == 403:
                    print("ans 200")
                    ping_command = subprocess.check_output('ping -c 1 ' + domain, shell=True)
                    print("1")
                    filtered_re = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ping_command.decode('utf-8'))

                    print("asdfghjkl" + str(filtered_re[0]) + "sdfghj")
                    print('\x1b[1;32;40m' + '[+] the domain : ' + domain + ' has Ip address by : ' + filtered_re[
                        0] + '\033[0m')

                else:
                    print("2")
                    print('\x1b[0;31;40m' + '[-] the domain : ' + domain + ' has Ip address by : N/A ' + '\033[0m')
            except Exception:
                print('\x1b[0;31;40m' + '[-] the domain : ' + domain + ' has Ip address by : N/A ' + '\033[0m')
                pass

        try:

            with open('subl.txt', 'r') as wordlist:
                for word in wordlist:
                    word = word.strip()

                    try:

                        subwdom = word + '.' + domain
                        checker(subwdom)
                        p = multiprocessing.Process(target=checker, args=(subwdom,))
                        p.start()
                        p.join()
                    except Exception:
                        quit()
        except KeyboardInterrupt:

            print('[-] Cloud Killer is closed !! ')
            quit()
        print('[-] Cloud Killer is closed !! ')
