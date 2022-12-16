import wx
import scapy.all as scapy
import netifaces
def Quit_all(self):
    exit()

class NetworkScaner(wx.Frame):
    def __init__(self, *args):
        super().__init__(None, title='Network Scan')
        self.GuiNetworkScan()

    def GuiNetworkScan(self):

        # Main panel
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        gateway = self.get_gateway()

        # Ip reange read
        #todo зробити так, щоб в панель писався айпі пристрою в мережі
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        RangeText = wx.StaticText(panel, -1, "Write range of IPs")
        hbox1.Add(RangeText, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.IpRangeTextLine = wx.TextCtrl(panel, value = str(gateway + "/24") )
        hbox1.Add(self.IpRangeTextLine, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        vbox.Add(hbox1)

        #todo додати поле з типом сканування

        #todo одати поле з періодичністью сканування

        # Scan output
        self.ips = "IP \t\t MAC \n ----------------------------------------------------"
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        OutputText = wx.StaticText(panel, -1, "Output")
        hbox2.Add(OutputText, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.OutputTextBox = wx.TextCtrl(panel, size = (300,100), style = wx.TE_MULTILINE | wx.TE_READONLY, value = self.ips)
        hbox2.Add(self.OutputTextBox, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        vbox.Add(hbox2)

        # Start button
        #todo кнопка повинна змінювати назу на "stop" і навпаки
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        StartText = wx.StaticText(panel, -1, "Start Script")
        hbox3.Add(StartText, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.btn = wx.Button(panel, -1, "Start!")
        self.Bind(wx.EVT_BUTTON, self.ScriptStart, self.btn, lambda evt:self.OutputTextBox.SetLabel(self.ips.pop(0)) or self.ips.append(self.OutputTextBox.GetLabel()))
        hbox3.Add(self.btn, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        vbox.Add(hbox3)

        # Setup Panel
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_CLOSE, Quit_all, self)

        self.Show()
        wx.App().MainLoop()

    def ScriptStart(self, *args):
        #todo скріпт повиннен сканувати кожні n секунд, допоки користувач не натисне кнопку "Stop"
        data = str(self.IpRangeTextLine.GetLineText(0))
        str_scan_result = self.NetworkScan(data)
        self.OutputTextBox.SetValue(str_scan_result)

    def NetworkScan(self, data):

        def scan(ip):
            arp_request = scapy.ARP(pdst=ip)
            brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_brodcast = brodcast / arp_request
            answered_list = scapy.srp(arp_request_brodcast, timeout=3, verbose=False)[0]

            clients_list = []
            for element in answered_list:
                client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
                clients_list.append(client_dict)
            return (clients_list)

        def parser(results_list):
            str_result = "IP \t\t MAC \n ----------------------------------------------------"
            for client in results_list:
                str_result = str_result + "\n" + str(client["IP"]) + "\t " + str(client["MAC"]) + "\t\t"
            return str_result

        scan_results = scan(data)
        return(parser(scan_results))
    def get_gateway(self):
        gws = netifaces.gateways()
        gateway = gws['default'][netifaces.AF_INET][0]
        return gateway
