# -*- coding:utf-8 -*-
import decimal,os,datetime
import gettext
_ = gettext.gettext
from Taowa_wx import *
from Taowa_skin import *
from Chemulator import *
from Chemulator_mw import *
from Chemulator_Solubility import *


class Frame_batch(wx.Frame):
    def __init__(self):
        wx_Frame.__init__(self, None, title='化学浓度换算', size=(1014, 635),name='frame',style=541072384)
        icon = wx.Icon(r'.\ICO\volumetric-flask.png')
        self.SetIcon(icon)
        self.Bind(wx.EVT_CLOSE, self.on_close)  # 绑定关闭事件
        self.启动窗口 = wx.Panel(self)
        self.启动窗口.SetOwnBackgroundColour((249, 249, 249, 249))
        self.Centre()

        self.m_menubar4 = wx.MenuBar(0)
        self.m_menu8 = wx.Menu()
        self.m_menuItem6 = wx.MenuItem(self.m_menu8, wx.ID_ANY, _(u"打开根目录") + u"\t" + u"Ctrl+O", _(u"打开项目根目录"),
                                       wx.ITEM_NORMAL)
        self.m_menuItem6.SetBitmap(
            wx.Bitmap(u"./ICO/open.png", wx.BITMAP_TYPE_ANY))
        self.m_menu8.Append(self.m_menuItem6)

        self.m_menu8.AppendSeparator()

        self.m_menuItem5 = wx.MenuItem(self.m_menu8, wx.ID_ANY, _(u"退出程序") + u"\t" + u"Esc", _(u"退出应用程序"),
                                       wx.ITEM_NORMAL)
        self.m_menuItem5.SetBitmap(
            wx.Bitmap(u"./ICO/exit.png", wx.BITMAP_TYPE_ANY))
        self.m_menu8.Append(self.m_menuItem5)

        self.m_menubar4.Append(self.m_menu8, _(u"文件"))

        self.m_menu11 = wx.Menu()
        self.m_menuItem61 = wx.MenuItem(self.m_menu11, wx.ID_ANY, _(u"返回主界面") + u"\t" + u"Ctrl+Q", _(u"返回主界面"),
                                        wx.ITEM_NORMAL)
        self.m_menuItem61.SetBitmap(
            wx.Bitmap(u"./ICO/windows.png", wx.BITMAP_TYPE_ANY))
        self.m_menu11.Append(self.m_menuItem61)


        self.m_menu11.AppendSeparator()

        self.m_menuItem7 = wx.MenuItem(self.m_menu11, wx.ID_ANY, _(u"批量计算模式") + u"\t" + u"Ctrl+W", _(u"用于多个数据批量计算"),
                                       wx.ITEM_NORMAL)
        self.m_menuItem7.SetBitmap(
            wx.Bitmap(u"./ICO/multiple.png", wx.BITMAP_TYPE_ANY))
        self.m_menu11.Append(self.m_menuItem7)
        self.m_menuItem7.Enable(False)

        self.m_menuItem8 = wx.MenuItem(self.m_menu11, wx.ID_ANY, _(u"其他换算") + u"\t" + u"Ctrl+E",
                                       _(u"用于常见的摩尔分数与质量分数间的转化"), wx.ITEM_NORMAL)
        self.m_menuItem8.SetBitmap(
            wx.Bitmap(u"./ICO/weight.png", wx.BITMAP_TYPE_ANY))
        self.m_menu11.Append(self.m_menuItem8)

        self.m_menuItem10 = wx.MenuItem(self.m_menu11, wx.ID_ANY, _(u"溶解度计算") + u"\t" + u"Ctrl+R", _(u"用于化学溶解度计算"),
                                        wx.ITEM_NORMAL)
        self.m_menuItem10.SetBitmap(
            wx.Bitmap(u"./ICO/solution.png", wx.BITMAP_TYPE_ANY))
        self.m_menu11.Append(self.m_menuItem10)

        self.m_menubar4.Append(self.m_menu11, _(u"计算"))

        self.m_menu10 = wx.Menu()
        self.m_menuItem9 = wx.MenuItem(self.m_menu10, wx.ID_ANY, _(u"帮助文档") + u"\t" + u"F1", _(u"打开帮助文档"),
                                       wx.ITEM_NORMAL)
        self.m_menuItem9.SetBitmap(
            wx.Bitmap(u"./ICO/help.png", wx.BITMAP_TYPE_ANY))
        self.m_menu10.Append(self.m_menuItem9)

        self.m_menubar4.Append(self.m_menu10, _(u"帮助"))

        # Connect Events
        self.Bind(wx.EVT_MENU, self.Open, id=self.m_menuItem6.GetId())
        self.Bind(wx.EVT_MENU, self.exit, id=self.m_menuItem5.GetId())
        self.Bind(wx.EVT_MENU, self.main, id=self.m_menuItem61.GetId())
        self.Bind(wx.EVT_MENU, self.Batch, id=self.m_menuItem7.GetId())
        self.Bind(wx.EVT_MENU, self.Quality, id=self.m_menuItem8.GetId())
        self.Bind(wx.EVT_MENU, self.help, id=self.m_menuItem9.GetId())
        self.Bind(wx.EVT_MENU, self.solu, id=self.m_menuItem10.GetId())

        self.SetMenuBar(self.m_menubar4)

        ##  更新关键词匹配功能
        self.search_ctrl = wx.SearchCtrl(self.启动窗口, pos=(0, 51), size=(286, 30))
        self.search_ctrl.ShowSearchButton(True)
        self.search_ctrl.ShowCancelButton(True)
        self.all_data()
        self.Bind(wx.EVT_TEXT, self.on_search, self.search_ctrl)


        self.variable = decimal.Decimal(0)
        图文按钮3_图片 = wx.Image(r'.\ICO\left arrow.png').ConvertToBitmap()
        self.图文按钮3 = lib_button_ThemedGenBitmapTextButton(self.启动窗口,size=(35, 30),pos=(291, 343),bitmap=图文按钮3_图片,label='',name='genbutton')
        self.图文按钮3.SetToolTip("清除化合物、分子量")
        self.图文按钮3.Bind(wx.EVT_BUTTON, self.图文按钮3_按钮被单击)
        project_dir = "./Project"  # 将此处修改为 "Project" 目录的路径
        folder_names = os.listdir(project_dir)
        self.组合框2 = wx.ComboBox(self.启动窗口, value='', pos=(311, 11), name='comboBox', choices=folder_names, style=16)
        self.组合框2.SetSize((172, 28))
        # 刷新Combobox的选项
        self.refresh_folder_names()
        组合框2_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.组合框2.SetFont(组合框2_字体)
        self.组合框2.SetOwnBackgroundColour((249, 249, 249, 249))
        self.组合框2.Bind(wx.EVT_COMBOBOX, self.组合框2_选中列表项)
        self.组合框2.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.组合框2_弹出列表项)
        self.超级列表框1 = wx_ListCtrl(self.启动窗口,size=(285, 490),pos=(1, 79),name='listCtrl',style=32)
        self.超级列表框1.AppendColumn('名称', 0, 118)
        self.超级列表框1.AppendColumn('化学式', 0, 85)
        self.超级列表框1.AppendColumn('分子量', 0, 85)
        self.超级列表框1.Append(['', '', ''])
        超级列表框1_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.超级列表框1.SetFont(超级列表框1_字体)
        # 创建字典来存储选中的化合物和分子量数据
        self.selected_data = {}
        self.超级列表框1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.超级列表框1_选中表项)
        self.超级列表框1.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.超级列表框1_取消选中表项)
        self.超级列表框1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.超级列表框1_右键单击表项)
        self.超级列表框1.Bind(wx.EVT_LEFT_DCLICK, self.超级列表框1_鼠标左键双击)
        self.超级列表框1.SetOwnBackgroundColour((249, 249, 249, 249))
        图片框3_图片 = wx.Image(r'.\ICO\folder.png').ConvertToBitmap()
        self.图片框3 = wx_StaticBitmap(self.启动窗口, bitmap=图片框3_图片,size=(32, 30),pos=(283, 12),name='staticBitmap',style=0)
        self.图片框3.Bind(wx.EVT_LEFT_DOWN,self.图片框3_鼠标左键按下)
        self.图片框3.SetToolTip("打开项目根目录")
        图文按钮2_图片 = wx.Image(r'.\ICO\right-arrow.png').ConvertToBitmap()
        self.图文按钮2 = lib_button_ThemedGenBitmapTextButton(self.启动窗口,size=(35, 30),pos=(291, 235),bitmap=图文按钮2_图片,label='',name='genbutton')
        self.图文按钮2.SetToolTip("填入选中化合物、分子量")
        self.图文按钮2.Bind(wx.EVT_BUTTON, self.图文按钮2_按钮被单击)

        图文按钮5_图片 = wx.Image(r'.\ICO\plus.png').ConvertToBitmap()
        self.图文按钮5 = lib_button.ThemedGenBitmapTextButton(self.启动窗口, size=(30, 28), pos=(484, 11), bitmap=图文按钮5_图片,
                                                          label='', name='genbutton')
        self.图文按钮5.SetToolTip("创建项目文件")
        self.图文按钮5.Bind(wx.EVT_BUTTON, self.图文按钮5_按钮被单击)
        self.标签1 = wx_StaticTextL(self.启动窗口, size=(178, 28), pos=(335, 80), label='化合物(Compound)', name='staticText',
                                  style=1)
        标签1_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签1.SetFont(标签1_字体)
        self.标签2 = wx_StaticTextL(self.启动窗口, size=(120, 28), pos=(336, 164), label='数量(Amount)', name='staticText',
                                  style=1)
        self.标签2.SetFont(wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ))

        self.标签3 = wx_StaticTextL(self.启动窗口, size=(92, 27), pos=(724, 60), label='转化自', name='staticText', style=257)
        标签3_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签3.SetFont(标签3_字体)
        self.标签4 = wx_StaticTextL(self.启动窗口, size=(92, 27), pos=(850, 60), label='转化为', name='staticText', style=257)
        标签4_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签4.SetFont(标签4_字体)
        self.标签5 = wx_StaticTextL(self.启动窗口, size=(109, 28), pos=(610, 80), label='分子量(m.w)', name='staticText',
                                  style=1)
        标签5_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签5.SetFont(标签5_字体)
        self.标签8 = wx_StaticTextL(self.启动窗口, size=(131, 28), pos=(740, 80), label='(Convert from)', name='staticText',
                                  style=1)
        标签8_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签8.SetFont(标签8_字体)
        self.标签10 = wx_StaticTextL(self.启动窗口, size=(106, 28), pos=(870, 80), label='(Convert to)', name='staticText',
                                   style=1)
        标签10_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签10.SetFont(标签10_字体)
        self.编辑框4 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(610, 112), value='', name='text', style=256)
        编辑框4_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框4.SetFont(编辑框4_字体)
        self.编辑框4.SetForegroundColour((128, 0, 0, 255))
        self.组合框3 = wx.ComboBox(self.启动窗口,value='',pos=(740, 112),name='comboBox',choices=['g/L','mg/L','μg/L','ng/L','g/mL', 'mg/mL', 'μg/mL', 'ng/mL', 'pg/mL', 'fg/mL', 'ng/dL', 'mol/L', 'mmol/L', 'μmol/L', 'nmol/L', 'pmol/L'],style=16)
        self.组合框3.SetSize((110, 28))
        组合框3_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.组合框3.SetFont(组合框3_字体)
        self.组合框3.SetOwnBackgroundColour((249, 249, 249, 249))
        self.组合框4 = wx.ComboBox(self.启动窗口,value='',pos=(870, 112),name='comboBox',choices=['g/L','mg/L','μg/L','ng/L','g/mL', 'mg/mL', 'μg/mL', 'ng/mL', 'pg/mL', 'fg/mL', 'ng/dL', 'mol/L', 'mmol/L', 'μmol/L', 'nmol/L', 'pmol/L'],style=16)
        self.组合框4.SetSize((110, 28))
        组合框4_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.组合框4.SetFont(组合框4_字体)
        self.组合框4.SetOwnBackgroundColour((249, 249, 249, 249))


        图文按钮7_图片 = wx.Image(r'.\ICO\plus.png').ConvertToBitmap()
        self.图文按钮7 = lib_button_ThemedGenBitmapTextButton(self.启动窗口,size=(30, 28),pos=(306, 113),bitmap=图文按钮7_图片,label='',name='genbutton')
        self.图文按钮7.SetToolTip("新增化合物到项目文件")
        self.图文按钮7.Bind(wx.EVT_BUTTON, self.图文按钮7_按钮被单击)
        self.整数微调框1 = wx_SpinCtrl(self.启动窗口,size=(36, 28),pos=(944, 160),name='wxSpinCtrl',min=1,max=9,initial=2,style=16640)
        self.整数微调框1.SetBase(12)
        整数微调框1_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.整数微调框1.SetFont(整数微调框1_字体)
        self.整数微调框1.SetForegroundColour((128, 0, 0, 255))
        self.整数微调框1.SetOwnBackgroundColour((249, 249, 249, 249))
        self.整数微调框1.Bind(wx.EVT_SPINCTRL,self.整数微调框1_数值被调整)
        self.标签6 = wx_StaticTextL(self.启动窗口, size=(151, 24), pos=(766, 164), label='设置计算结果的小数位数：', name='staticText',
                                  style=256)
        标签6_字体 = wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" )
        self.标签6.SetFont(标签6_字体)
        self.编辑框6 = wx_TextCtrl(self.启动窗口, size=(260, 28), pos=(336, 112), value='', name='text', style=0)
        编辑框6_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框6.SetFont(编辑框6_字体)
        self.编辑框6.SetOwnBackgroundColour((249, 249, 249, 249))
        self.编辑框6.SetForegroundColour((128, 0, 0, 255))

        self.编辑框8 = wx_TextCtrl(self.启动窗口, size=(140, 375), pos=(334, 195), value='', name='text', style=1073741856)
        编辑框8_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框8.SetFont(编辑框8_字体)
        self.编辑框8.Bind(wx.EVT_TEXT, self.编辑框8_内容被改变)
        self.编辑框8.SetOwnBackgroundColour((249, 249, 249, 249))

        self.标签11 = wx_StaticTextL(self.启动窗口, size=(140, 28), pos=(490, 164), label='计算结果(Result)', name='staticText',
                                   style=1)
        self.标签11.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑"))

        self.列表框2 = wx_ListBox(self.启动窗口, size=(490, 375), pos=(490, 195), name='listBox', choices=[], style=1073741984)
        列表框2_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.列表框2.SetFont(列表框2_字体)
        self.列表框2.SetOwnBackgroundColour((249, 249, 249, 249))
        self.列表框2.Bind(wx.EVT_RIGHT_DOWN, self.列表框2_鼠标右键按下)



        # 在初始化方法中添加事件绑定
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框6)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框4)
        self.Bind(wx.EVT_COMBOBOX, self.更新编辑框7内容, self.组合框3)
        self.Bind(wx.EVT_COMBOBOX, self.更新编辑框7内容, self.组合框4)



    # Virtual event handlers, overide them in your derived class
    def Open( self, event ):
        directory_path = "./Project"
        os.system(f'explorer {os.path.abspath(directory_path)}')

    def exit( self, event ):
        dlg = wx.MessageDialog(self, "是否退出程序？", "摩尔浓度换算", wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()

        if result == wx.ID_YES:
            self.Destroy()

    def main(self, event):
        from Chemulator import Frame
        main_frame = Frame()
        self.Destroy() #直接退出程序
        main_frame.Show(True)

    def Batch(self, event):
        from Chemulator_batch import Frame_batch
        batch_frame = Frame_batch()  # 创建 Chemulator_batch.py中的窗口实例
        self.Destroy() #直接退出程序
        batch_frame.Show(True)  # 显示窗口

    def Quality(self, event):
        from Chemulator_mw import Frame_mw
        quality_frame = Frame_mw()  # 创建 Chemulator_batch.py中的窗口实例
        self.Destroy() #直接退出程序
        quality_frame.Show(True)  # 显示窗口

    def help( self, event ):
        # 打开帮助文档
        current_dir = os.getcwd()
        help_file_path = os.path.join(current_dir, "help.chm")
        os.system(f'explorer {help_file_path}')

    def solu(self, event):
        from Chemulator_Solubility import Frame_solu
        solu_frame = Frame_solu()  # 创建 Frame_solu.py中的窗口实例
        self.Destroy() #直接退出程序
        solu_frame.Show(True)  # 显示窗口

    def all_data(self):
        project_dir = "./Project"
        folder_names = os.listdir(project_dir)
        self.data_list = []
        for folder_name in folder_names:
            folder_path = os.path.join(project_dir, folder_name)
            file_path = os.path.join(folder_path, "化合物.txt")
            with open(file_path, 'r', encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split("\t")
                    if len(data) >= 3:
                        self.data_list.append(data)
        # self.data_list2 = [data[0] for data in self.data_list]
        # print(self.data_list2)

    def on_search(self, event):
        keyword = self.search_ctrl.GetValue()
        self.超级列表框1.ClearAll()  # 清空超级列表框中的所有列
        self.超级列表框1.AppendColumn('名称', 0, 118)
        self.超级列表框1.AppendColumn('化学式', 0, 85)
        self.超级列表框1.AppendColumn('分子量', 0, 85)
        for i, choice in enumerate(self.data_list):
            if keyword.lower() in choice[0].lower():
                self.超级列表框1.Append([choice[0], choice[1], choice[2]])

    def 图文按钮3_按钮被单击(self, event):
        # Clear the data in 编辑框6, 编辑框4, 组合框3, and 组合框4
        self.编辑框6.SetValue('')
        self.编辑框4.SetValue('')
        self.组合框3.SetValue('')
        self.组合框4.SetValue('')
        self.列表框2.Clear()




    def 组合框2_选中列表项(self, event):
        selected_folder = self.组合框2.GetValue()
        project_dir = "./Project"  # 替换为实际的 "Project" 目录路径

        folder_path = os.path.join(project_dir, selected_folder)
        file_path = os.path.join(folder_path, "化合物.txt")

        self.超级列表框1.ClearAll()  # 清空超级列表框中的所有列
        self.超级列表框1.AppendColumn('名称', 0, 118)
        self.超级列表框1.AppendColumn('化学式', 0, 85)
        self.超级列表框1.AppendColumn('分子量', 0, 85)

        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.strip().split('\t')  # 使用制表符作为分隔符
                self.超级列表框1.Append([data[0], data[1], data[2]])

    def 组合框2_弹出列表项(self, event):
        self.refresh_folder_names()


    def refresh_folder_names(self):
        project_dir = "./Project"  # 替换为实际的 "Project" 目录路径
        folder_names = os.listdir(project_dir)
        self.组合框2.Set(folder_names)

    def 超级列表框1_选中表项(self, event):
        selected_index = self.超级列表框1.GetFirstSelected()  # 获取选中的第一个表项的索引

        while selected_index != -1:
            compound_name = self.超级列表框1.GetItemText(selected_index)
            molecular_weight = self.超级列表框1.GetItemText(selected_index, 2)  # 使用列索引2获取"分子量"列的数据

            # 将选中的化合物和分子量数据添加到字典中
            self.selected_data[compound_name] = molecular_weight

            selected_index = self.超级列表框1.GetNextSelected(selected_index)


    def 超级列表框1_取消选中表项(self, event):
        selected_index = self.超级列表框1.GetFirstSelected()  # 获取取消选中的第一个表项的索引

        while selected_index != -1:
            compound_name = self.超级列表框1.GetItemText(selected_index)

            # 从字典中删除取消选中的化合物和分子量数据
            if compound_name in self.selected_data:
                del self.selected_data[compound_name]

            selected_index = self.超级列表框1.GetNextSelected(selected_index)

    def 超级列表框1_右键单击表项(self, event):
        selected_index = self.超级列表框1.GetFirstSelected()

        if selected_index != -1:
            # 创建一个删除的菜单项
            menu = wx.Menu()
            delete_item = menu.Append(wx.ID_ANY, "删除")

            # 绑定菜单项的单击事件
            self.Bind(wx.EVT_MENU, self.删除选中行, delete_item)

            # 显示菜单
            self.PopupMenu(menu)

            # 销毁菜单
            menu.Destroy()

    def 超级列表框1_鼠标左键双击(self, event):
        # 从中获取所选化合物的名称和分子量 超级列表框1
        selected_index = self.超级列表框1.GetFirstSelected()
        if selected_index != -1:
            compound_name = self.超级列表框1.GetItemText(selected_index)
            chemical_formula = self.超级列表框1.GetItemText(selected_index, 1)
            molecular_weight = self.超级列表框1.GetItemText(selected_index, 2)

            # 设置化合物名称和分子量 编辑框6 and 编辑框4
            self.编辑框6.SetValue(compound_name + "  " + chemical_formula)
            self.编辑框4.SetValue(molecular_weight)



    def 删除选中行(self, event):
        selected_index = self.超级列表框1.GetFirstSelected()

        if selected_index != -1:
            self.超级列表框1.DeleteItem(selected_index)
            selected_folder = self.组合框2.GetValue()
            project_dir = "./Project"  # 替换为实际的 "Project" 目录路径

            folder_path = os.path.join(project_dir, selected_folder)
            file_path = os.path.join(folder_path, "化合物.txt")

            # 保存删除后的数据到文件（使用 utf-8 编码）
            with open(file_path, "w", encoding="utf-8") as file:
                # 获取超级列表框中的数据
                for row in range(self.超级列表框1.GetItemCount()):
                    compound_name = self.超级列表框1.GetItemText(row)
                    chemical_formula = self.超级列表框1.GetItemText(row, 1)
                    molecular_weight = self.超级列表框1.GetItemText(row, 2)
                    # 将数据写入文件
                    file.write(f"{compound_name}\t{chemical_formula}\t{molecular_weight}\n")

        self.组合框2_选中列表项(event)


    def 图片框3_鼠标左键按下(self, event):
        directory_path = "./Project"
        os.system(f'explorer {os.path.abspath(directory_path)}')


    def 图文按钮2_按钮被单击(self, event):
        # 从中获取所选化合物的名称和分子量 超级列表框1
        selected_index = self.超级列表框1.GetFirstSelected()
        if selected_index != -1:
            compound_name = self.超级列表框1.GetItemText(selected_index)
            chemical_formula = self.超级列表框1.GetItemText(selected_index, 1)
            molecular_weight = self.超级列表框1.GetItemText(selected_index, 2)

            # 设置化合物名称和分子量 编辑框6 and 编辑框4
            self.编辑框6.SetValue(compound_name + "  " + chemical_formula)
            self.编辑框4.SetValue(molecular_weight)


    def 图文按钮5_按钮被单击(self, event):
        dialog = wx.TextEntryDialog(self, "请输入文件夹名称：", "创建文件夹")
        if dialog.ShowModal() == wx.ID_OK:
            folder_name = dialog.GetValue()
            project_dir = "./Project"  # 替换为实际的 "Project" 目录路径

            folder_path = os.path.join(project_dir, folder_name)

            if os.path.exists(folder_path):
                wx.MessageBox("相同项目名称", "错误", wx.OK | wx.ICON_ERROR)
            else:
                os.makedirs(folder_path)

                file_path = os.path.join(folder_path, "化合物.txt")
                with open(file_path, 'w') as f:
                    f.write("")

                wx.MessageBox("文件夹和文件已成功创建！", "成功", wx.OK | wx.ICON_INFORMATION)

                # 刷新Combobox的选项
                self.refresh_folder_names()

                self.组合框2.SetValue(folder_name)  # 设置组合框的值为新创建的文件夹名称
                self.组合框2_选中列表项(event)  # 调用组合框2_选中列表项方法，选中新创建的文件夹

        dialog.Destroy()

    def 图文按钮7_按钮被单击(self, event):
        compound_name = self.编辑框6.GetValue()
        data_value = self.编辑框4.GetValue()
        if not compound_name or not data_value:
            # 提示未输入完整数据
            dlg = wx.MessageDialog(None, "未输入完整数据，请查看帮助文档！", "提示", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            return
        else:

            # 分析compound_name内容并分组
            compound_name_list = compound_name.split("  ")
            compound_name_1 = compound_name_list[0]
            compound_name_2 = compound_name_list[1] if len(compound_name_list) > 1 else ""

            # 拼接要写入文件的内容
            content = compound_name_1 + "\t" + compound_name_2 + "\t" + data_value

            # 检查是否存在完全相同的数据
            folder_name = self.组合框2.GetValue()

            # 检查folder_name是否为空
            if not folder_name:
                # 提示未选择项目文件
                dialog = wx.MessageDialog(None, "未选择项目文件，取消数据添加！", "提示")
                dialog.ShowModal()
                dialog.Destroy()
                return

            file_path = f"./Project/{folder_name}/化合物.txt"

            duplicate = False

            try:
                # 读取文件内容
                with open(file_path, "r", encoding="utf-8") as file:
                    lines = file.readlines()

                    # 检查每一行是否与要添加的数据完全相同
                    for line in lines:
                        if line.strip() == content:
                            duplicate = True
                            break

            except FileNotFoundError:
                # 文件不存在，不会存在重复数据，继续添加数据
                pass

            if duplicate:
                # 提示重复数据
                dlg = wx.MessageDialog(None, "该数据已存在，无需再次添加！", "重复", wx.OK)

            else:
                # 弹出确认对话框
                dlg = wx.MessageDialog(None, "是否确认添加数据?", "确认添加", wx.YES_NO | wx.ICON_QUESTION)

                if dlg:
                    try:
                        # 打开文件并以追加模式写入内容
                        with open(file_path, "a", encoding="utf-8") as file:
                            file.write(content + "\n")

                        # 提示添加成功
                        dlg = wx.MessageDialog(None, "数据添加成功！", "成功", wx.OK)
                        dlg.ShowModal()
                        dlg.Destroy()


                    except Exception as e:
                        # 提示添加失败
                        dlg = wx.MessageDialog(None, "数据添加失败！", "失败", wx.OK | wx.ICON_ERROR)
                        dlg.ShowModal()
                        dlg.Destroy()
                else:
                    # 提示取消添加
                    dlg = wx.MessageDialog(None, "已取消添加数据！", "提示", wx.OK)
                    dlg.ShowModal()
                    dlg.Destroy()

            self.组合框2_选中列表项(event)

    def 更新编辑框7内容(self, event):
        self.列表框2.Clear()
        self.data_lines = self.编辑框8.GetValue()
        self.compound_name = self.编辑框6.GetValue()
        self.mw_str = self.编辑框4.GetValue()
        self.molecular_weight = self.组合框4.GetValue()
        self.data_unit = self.组合框3.GetValue()
        self.lines = self.data_lines.splitlines()
        # print(self.lines)
        # 初始化 result
        result = ""
        # print(self.lines) ##遍历每行数据
        if self.data_lines and self.compound_name and self.mw_str and self.molecular_weight and self.data_unit:
            # 如果文本框中有数据，执行后续操作
            for data in self.lines:
                if data != "":
                    self.concentration_str1 = data
                    # print(self.concentration_str)


                    # 获取选中列表项的数值
                    selected_value = int(self.整数微调框1.GetValue())

                    # 调用单位计算过程函数来计算variable变量的值
                    self.单位计算过程(event)
                    # 添加变量的声明和初始化
                    variable = self.variable
                    # print(variable)

                    # 判断是否使用科学计数法表示，并受到小数位数限制
                    if (variable != 0) and (variable >= 10 ** 4 or variable <= 10 ** -4) and selected_value != 0:
                        variable = "{:.{}e}".format(variable, selected_value)
                    elif variable * 1 == 0:
                        variable = "0.0"
                    else:
                        variable = "{:.{}f}".format(variable, selected_value)

                    result = " ".join([self.compound_name, "：", self.concentration_str1, self.data_unit, "=", variable, self.molecular_weight])
                    self.列表框2.Append(result)

    def 整数微调框1_数值被调整(self, event):
        self.更新编辑框7内容(event)

    def 编辑框8_内容被改变(self,event):
        self.更新编辑框7内容(event)


    def 列表框2_鼠标右键按下(self,event):
        selected_index = self.列表框2.GetSelections()

        if selected_index != -1:
            # 创建一个菜单
            menu = wx.Menu()
            delete_item = menu.Append(wx.ID_ANY, "删除选中行")
            copy_item = menu.Append(wx.ID_ANY, "复制选中行")
            allcopy_item = menu.Append(wx.ID_ANY, "全选复制")
            Export_excel = menu.Append(wx.ID_ANY, "全选导出到txt")

            # 绑定菜单项的单击事件
            self.Bind(wx.EVT_MENU, self.删除列表框2选中行, delete_item)
            self.Bind(wx.EVT_MENU, self.复制列表框2选中行, copy_item)
            self.Bind(wx.EVT_MENU, self.全选复制列表框2选中行, allcopy_item)
            self.Bind(wx.EVT_MENU, self.save_data_to_txt, Export_excel)
            # 显示菜单
            self.PopupMenu(menu)

            # 销毁菜单
            menu.Destroy()
    def 删除列表框2选中行(self, event):
        selected_indices = self.列表框2.GetSelections()
        # 从列表框中删除选定的项
        for index in reversed(selected_indices):
            self.列表框2.Delete(index)

    def 复制列表框2选中行(self, event):
        selected_indices = self.列表框2.GetSelections()

        if selected_indices:
            item_data = []
            for index in selected_indices:
                item_data.append(self.列表框2.GetString(index))

            # 复制选中行的数据到剪贴板
            data = '\n'.join(item_data)
            clipboard = wx.TextDataObject()
            clipboard.SetText(data)
            if wx.TheClipboard.Open():
                wx.TheClipboard.SetData(clipboard)
                wx.TheClipboard.Close()

    def 全选复制列表框2选中行(self, event):
        clipboard = wx.Clipboard.Get()
        selected_items = []
        for row in range(self.列表框2.GetCount()):
            item_data = []
            item_data.append(self.列表框2.GetString(row))
            selected_items.append(item_data)
        # 将数据转换为文本格式
        data_text = '\n'.join(['\t'.join(row) for row in selected_items])

        # 将数据设置到剪贴板
        clipboard.Open()
        clipboard.SetData(wx.TextDataObject(data_text))
        clipboard.Flush()
        clipboard.Close()

        # 显示成功提示
        wx.MessageBox("数据已复制到剪贴板！", "成功", wx.OK | wx.ICON_INFORMATION)

    def save_data_to_txt(self, data):
        # 获取选中行数据
        selected_items = []
        for row in range(self.列表框2.GetCount()):
            item_data = []
            item_data.append(self.列表框2.GetString(row))
            selected_items.append(item_data)

        # 将数据保存到txt文件
        desktop_path = os.path.expanduser("~/Desktop")  # 获取桌面路径
        current_time = datetime.datetime.now().strftime("%Y%m%d")  # 获取当前时间
        file_path = os.path.join(desktop_path, current_time + "_all_data.txt")  # 拼接文件路径

        with open(file_path, 'w') as file:
            for row in selected_items:
                file.write('\t'.join(row) + '\n')

        # 打开txt文件
        os.startfile(file_path)

        wx.MessageBox("数据已保存至桌面上的txt文件！", "成功", wx.OK | wx.ICON_INFORMATION)


    def 单位计算过程(self, event):
        # 获取组合框3和组合框4当前选中的单位
        unit_3 = self.组合框3.GetValue()
        unit_4 = self.组合框4.GetValue()
        if self.concentration_str1 == '':
            concentration = decimal.Decimal(0)  # 设置一个默认值
        else:
            concentration = decimal.Decimal(self.concentration_str1)

        self.mw_str = self.编辑框4.GetValue()
        if self.mw_str == '':
            mw = decimal.Decimal(1)   # 设置一个默认值
        else:
            mw = decimal.Decimal(self.mw_str)

        # 判断组合框3为"g/mL"和组合框4的单位并执行相应的计算
        if unit_3 == "g/mL" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "g/mL" and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "g/mL" and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif unit_3 == "g/mL" and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)
        elif unit_3 == "g/mL" and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 12)
        elif unit_3 == "g/mL" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 15)
        elif unit_3 == "g/mL" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 2)
        elif unit_3 == "g/mL" and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3) / decimal.Decimal(mw)
        elif unit_3 == "g/mL" and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6) / decimal.Decimal(mw)
        elif unit_3 == "g/mL" and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9) / decimal.Decimal(mw)
        elif unit_3 == "g/mL" and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 12) / decimal.Decimal(mw)
        elif unit_3 == "g/mL" and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 15) / decimal.Decimal(mw)
        elif unit_3 == "g/mL" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 11)

        # 判断组合框3为"mg/mL"和组合框4的单位并执行相应的计算
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 3)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 12)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 1)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(mw)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3) / decimal.Decimal(mw)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6) / decimal.Decimal(mw)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9) / decimal.Decimal(mw)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 12) / decimal.Decimal(mw)
        elif (unit_3 == "mg/mL" or unit_3 == "g/L") and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 8)

        # 判断组合框3为"μg/mL"和组合框4的单位并执行相应的计算
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 6)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 3)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 4)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3) / decimal.Decimal(mw)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(mw)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3) / decimal.Decimal(mw)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6) / decimal.Decimal(mw)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9) / decimal.Decimal(mw)
        elif (unit_3 == "μg/mL" or unit_3 == "mg/L") and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 5)

        # 判断组合框3为"ng/mL"和组合框4的单位并执行相应的计算
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 9)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 6)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 3)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 7)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6) / decimal.Decimal(mw)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3) / decimal.Decimal(mw)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration)  / decimal.Decimal(mw)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3) / decimal.Decimal(mw)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6) / decimal.Decimal(mw)
        elif (unit_3 == "ng/mL" or unit_3 == "μg/L") and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 2)

        # 判断组合框3为"pg/mL"和组合框4的单位并执行相应的计算
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 12)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 9)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 6)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 3)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 10)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -9) / decimal.Decimal(mw)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6) / decimal.Decimal(mw)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3) / decimal.Decimal(mw)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(mw)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3) / decimal.Decimal(mw)
        elif (unit_3 == "pg/mL" or unit_3 == "ng/L") and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -1)

        # 判断组合框3为"fg/mL"和组合框4的单位并执行相应的计算
        elif unit_3 == "fg/mL" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 15)
        elif unit_3 == "fg/mL" and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 12)
        elif unit_3 == "fg/mL" and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 9)
        elif unit_3 == "fg/mL" and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 6)
        elif unit_3 == "fg/mL" and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 3)
        elif unit_3 == "fg/mL" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "fg/mL" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 13)
        elif unit_3 == "fg/mL" and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -12) / decimal.Decimal(mw)
        elif unit_3 == "fg/mL" and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -9) / decimal.Decimal(mw)
        elif unit_3 == "fg/mL" and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6) / decimal.Decimal(mw)
        elif unit_3 == "fg/mL" and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3) / decimal.Decimal(mw)
        elif unit_3 == "fg/mL" and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(mw)
        elif unit_3 == "fg/mL" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -4)

        # 判断组合框3为"%"和组合框4的单位并执行相应的计算
        elif unit_3 == "%" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -2)
        elif unit_3 == "%" and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 1)
        elif unit_3 == "%" and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 4)
        elif unit_3 == "%" and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 7)
        elif unit_3 == "%" and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 10)
        elif unit_3 == "%" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 13)
        elif unit_3 == "%" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "%" and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 1) / decimal.Decimal(mw)
        elif unit_3 == "%" and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 4) / decimal.Decimal(mw)
        elif unit_3 == "%" and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 7) / decimal.Decimal(mw)
        elif unit_3 == "%" and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 10) / decimal.Decimal(mw)
        elif unit_3 == "%" and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 13) / decimal.Decimal(mw)
        elif unit_3 == "%" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)

        # 判断组合框3为"mol/L"和组合框4的单位并执行相应的计算
        elif unit_3 == "mol/L" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 3)
        elif unit_3 == "mol/L" and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw)
        elif unit_3 == "mol/L" and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -3)
        elif unit_3 == "mol/L" and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -6)
        elif unit_3 == "mol/L" and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -9)
        elif unit_3 == "mol/L" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -12)
        elif unit_3 == "mol/L" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 1)
        elif unit_3 == "mol/L" and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "mol/L" and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "mol/L" and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif unit_3 == "mol/L" and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)
        elif unit_3 == "mol/L" and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 12)
        elif unit_3 == "mol/L" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -8)

        # 判断组合框3为"mmol/L"和组合框4的单位并执行相应的计算
        elif unit_3 == "mmol/L" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 6)
        elif unit_3 == "mmol/L" and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 3)
        elif unit_3 == "mmol/L" and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw)
        elif unit_3 == "mmol/L" and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -3)
        elif unit_3 == "mmol/L" and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -6)
        elif unit_3 == "mmol/L" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -9)
        elif unit_3 == "mmol/L" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 4)
        elif unit_3 == "mmol/L" and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3)
        elif unit_3 == "mmol/L" and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "mmol/L" and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "mmol/L" and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif unit_3 == "mmol/L" and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)
        elif unit_3 == "mmol/L" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -5)

        # 判断组合框3为"μmol/L"和组合框4的单位并执行相应的计算
        elif unit_3 == "μmol/L" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 9)
        elif unit_3 == "μmol/L" and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 6)
        elif unit_3 == "μmol/L" and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 3)
        elif unit_3 == "μmol/L" and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw)
        elif unit_3 == "μmol/L" and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -3)
        elif unit_3 == "μmol/L" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -6)
        elif unit_3 == "μmol/L" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 7)
        elif unit_3 == "μmol/L" and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6)
        elif unit_3 == "μmol/L" and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3)
        elif unit_3 == "μmol/L" and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "μmol/L" and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "μmol/L" and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif unit_3 == "μmol/L" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -2)

        # 判断组合框3为"nmol/L"和组合框4的单位并执行相应的计算
        elif unit_3 == "nmol/L" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 12)
        elif unit_3 == "nmol/L" and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 9)
        elif unit_3 == "nmol/L" and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 6)
        elif unit_3 == "nmol/L" and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 3)
        elif unit_3 == "nmol/L" and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw)
        elif unit_3 == "nmol/L" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -3)
        elif unit_3 == "nmol/L" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 10)
        elif unit_3 == "nmol/L" and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -9)
        elif unit_3 == "nmol/L" and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6)
        elif unit_3 == "nmol/L" and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3)
        elif unit_3 == "nmol/L" and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "nmol/L" and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "nmol/L" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 1)

        # 判断组合框3为"pmol/L"和组合框4的单位并执行相应的计算
        elif unit_3 == "pmol/L" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 15)
        elif unit_3 == "pmol/L" and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 12)
        elif unit_3 == "pmol/L" and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 9)
        elif unit_3 == "pmol/L" and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 6)
        elif unit_3 == "pmol/L" and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 3)
        elif unit_3 == "pmol/L" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw)
        elif unit_3 == "pmol/L" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 13)
        elif unit_3 == "pmol/L" and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -12)
        elif unit_3 == "pmol/L" and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -9)
        elif unit_3 == "pmol/L" and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6)
        elif unit_3 == "pmol/L" and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3)
        elif unit_3 == "pmol/L" and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "pmol/L" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 4)

        # 判断组合框3为"ng/dL"和组合框4的单位并执行相应的计算
        elif unit_3 == "ng/dL" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -11)
        elif unit_3 == "ng/dL" and (unit_4 == "mg/mL" or unit_4 == "g/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -8)
        elif unit_3 == "ng/dL" and (unit_4 == "μg/mL" or unit_4 == "mg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -5)
        elif unit_3 == "ng/dL" and (unit_4 == "ng/mL" or unit_4 == "μg/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -2)
        elif unit_3 == "ng/dL" and (unit_4 == "pg/mL" or unit_4 == "ng/L"):
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 1)
        elif unit_3 == "ng/dL" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 4)
        elif unit_3 == "ng/dL" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -9)
        elif unit_3 == "ng/dL" and unit_4 == "mol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -8) / decimal.Decimal(mw)
        elif unit_3 == "ng/dL" and unit_4 == "mmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -5) / decimal.Decimal(mw)
        elif unit_3 == "ng/dL" and unit_4 == "μmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -2) / decimal.Decimal(mw)
        elif unit_3 == "ng/dL" and unit_4 == "nmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 1) / decimal.Decimal(mw)
        elif unit_3 == "ng/dL" and unit_4 == "pmol/L":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 4) / decimal.Decimal(mw)
        elif unit_3 == "ng/dL" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration)

        else:
            # 如果组合框3和组合框4的单位不匹配，可以定义一个默认值或提示错误信息
            self.variable = decimal.Decimal(0)

    def on_close(self, event):
        dlg = wx.MessageDialog(self, "是否退出程序？", "摩尔浓度换算", wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()

        if result == wx.ID_YES:
            self.Destroy()


class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame_batch()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()