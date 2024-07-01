# -*- coding:utf-8 -*-
import decimal,os,datetime
import gettext
_ = gettext.gettext
from Chemulator_batch import *
from Chemulator_mw import *
from Chemulator_Solubility import *
from Taowa_wx import *
from Taowa_skin import *


# 皮肤定义全局变量
global_variable = None


def load_global_variable():
    file_path = './Configuration/global_variable.txt'  # 替换为你保存全局变量的文件路径
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            global_variable = eval(file.read())
    except FileNotFoundError:
        # 如果文件不存在，则进行全局变量的初始化
        global_variable = None

load_global_variable()

class Frame(wx.Frame):
    def __init__(self):
        wx_Frame.__init__(self, None, title='化学浓度换算', size=(1014, 635),name='frame',style=541072384)
        icon = wx.Icon(r'.\ICO\volumetric-flask.png')
        self.SetIcon(icon)
        self.Bind(wx.EVT_CLOSE, self.on_close)  # 绑定关闭事件
        self.启动窗口 = wx.Panel(self)
        self.启动窗口.SetOwnBackgroundColour((249, 249, 249, 249))
        self.Centre()

        self.m_menubar4 = wx.MenuBar(0)
        self.m_menubar4.SetFont(
            wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))

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
        self.m_menuItem61.Enable(False)

        self.m_menu11.AppendSeparator()

        self.m_menuItem7 = wx.MenuItem(self.m_menu11, wx.ID_ANY, _(u"批量计算模式") + u"\t" + u"Ctrl+W", _(u"用于多个数据批量计算"),
                                       wx.ITEM_NORMAL)
        self.m_menuItem7.SetBitmap(
            wx.Bitmap(u"./ICO/multiple.png", wx.BITMAP_TYPE_ANY))
        self.m_menu11.Append(self.m_menuItem7)

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

        self.m_menu4 = wx.Menu()
        self.m_menu1 = wx.Menu()
        self.m_menu2 = wx.Menu()
        self.m_menuItem16 = wx.MenuItem(self.m_menu2, wx.ID_ANY, _(u"Black04"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.Append(self.m_menuItem16)

        self.m_menuItem17 = wx.MenuItem(self.m_menu2, wx.ID_ANY, _(u"Adamant"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.Append(self.m_menuItem17)

        self.m_menuItem18 = wx.MenuItem(self.m_menu2, wx.ID_ANY, _(u"photo2"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.Append(self.m_menuItem18)

        self.m_menuItem19 = wx.MenuItem(self.m_menu2, wx.ID_ANY, _(u"Longhorn"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.Append(self.m_menuItem19)

        self.m_menu1.AppendSubMenu(self.m_menu2, _(u"黑色系"))

        self.m_menu41 = wx.Menu()
        self.m_menuItem20 = wx.MenuItem(self.m_menu41, wx.ID_ANY, _(u"粉红主题"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu41.Append(self.m_menuItem20)

        self.m_menuItem21 = wx.MenuItem(self.m_menu41, wx.ID_ANY, _(u"彩虹"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu41.Append(self.m_menuItem21)

        self.m_menu1.AppendSubMenu(self.m_menu41, _(u"粉色系"))

        self.m_menu51 = wx.Menu()
        self.m_menuItem22 = wx.MenuItem(self.m_menu51, wx.ID_ANY, _(u"Vista绿"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu51.Append(self.m_menuItem22)

        self.m_menuItem23 = wx.MenuItem(self.m_menu51, wx.ID_ANY, _(u"Storm"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu51.Append(self.m_menuItem23)

        self.m_menu1.AppendSubMenu(self.m_menu51, _(u"绿色系"))

        self.m_menu61 = wx.Menu()
        self.m_menuItem24 = wx.MenuItem(self.m_menu61, wx.ID_ANY, _(u"编程助手"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu61.Append(self.m_menuItem24)

        self.m_menuItem25 = wx.MenuItem(self.m_menu61, wx.ID_ANY, _(u"彗星小助手"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu61.Append(self.m_menuItem25)

        self.m_menu1.AppendSubMenu(self.m_menu61, _(u"青色系"))

        self.m_menu71 = wx.Menu()
        self.m_menuItem26 = wx.MenuItem(self.m_menu71, wx.ID_ANY, _(u"记忆蓝"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu71.Append(self.m_menuItem26)

        self.m_menuItem28 = wx.MenuItem(self.m_menu71, wx.ID_ANY, _(u"高标栏"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu71.Append(self.m_menuItem28)

        self.m_menuItem29 = wx.MenuItem(self.m_menu71, wx.ID_ANY, _(u"蓝色电脑管家"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu71.Append(self.m_menuItem29)

        self.m_menuItem30 = wx.MenuItem(self.m_menu71, wx.ID_ANY, _(u"QQ2011"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu71.Append(self.m_menuItem30)

        self.m_menuItem31 = wx.MenuItem(self.m_menu71, wx.ID_ANY, _(u"MSN"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu71.Append(self.m_menuItem31)

        self.m_menuItem32 = wx.MenuItem(self.m_menu71, wx.ID_ANY, _(u"Xenes"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu71.Append(self.m_menuItem32)

        self.m_menuItem27 = wx.MenuItem(self.m_menu71, wx.ID_ANY, _(u"ENJOY"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu71.Append(self.m_menuItem27)

        self.m_menuItem33 = wx.MenuItem(self.m_menu71, wx.ID_ANY, _(u"Win7"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu71.Append(self.m_menuItem33)

        self.m_menuItem34 = wx.MenuItem(self.m_menu71, wx.ID_ANY, _(u"ShanMeng窄版"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu71.Append(self.m_menuItem34)

        self.m_menuItem35 = wx.MenuItem(self.m_menu71, wx.ID_ANY, _(u"可爱蓝"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu71.Append(self.m_menuItem35)

        self.m_menu1.AppendSubMenu(self.m_menu71, _(u"蓝色系"))

        self.m_menu81 = wx.Menu()
        self.m_menuItem36 = wx.MenuItem(self.m_menu81, wx.ID_ANY, _(u"MAC"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu81.Append(self.m_menuItem36)

        self.m_menuItem38 = wx.MenuItem(self.m_menu81, wx.ID_ANY, _(u"Itunes"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu81.Append(self.m_menuItem38)

        self.m_menuItem37 = wx.MenuItem(self.m_menu81, wx.ID_ANY, _(u"Dogmax"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu81.Append(self.m_menuItem37)

        self.m_menu1.AppendSubMenu(self.m_menu81, _(u"其他系"))

        self.m_menuItem301 = wx.MenuItem(self.m_menu1, wx.ID_ANY, _(u"恢复默认"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem301)

        self.m_menu4.AppendSubMenu(self.m_menu1, _(u"皮肤"))

        self.m_menubar4.Append(self.m_menu4, _(u"设置"))


        self.m_menu10 = wx.Menu()
        self.m_menuItem9 = wx.MenuItem(self.m_menu10, wx.ID_ANY, _(u"帮助文档") + u"\t" + u"F1", _(u"打开帮助文档"),
                                       wx.ITEM_NORMAL)
        self.m_menuItem9.SetBitmap(
            wx.Bitmap(u"./ICO/help.png", wx.BITMAP_TYPE_ANY))
        self.m_menu10.Append(self.m_menuItem9)

        self.m_menubar4.Append(self.m_menu10, _(u"帮助"))

        # Connect Events
        self.Bind(wx.EVT_MENU, self.Open, id = self.m_menuItem6.GetId())
        self.Bind(wx.EVT_MENU, self.exit, id = self.m_menuItem5.GetId())
        self.Bind(wx.EVT_MENU, self.main, id = self.m_menuItem61.GetId())
        self.Bind(wx.EVT_MENU, self.Batch, id = self.m_menuItem7.GetId())
        self.Bind(wx.EVT_MENU, self.Quality, id = self.m_menuItem8.GetId())
        self.Bind(wx.EVT_MENU, self.solu, id=self.m_menuItem10.GetId())
        self.Bind(wx.EVT_MENU, self.Q1, id = self.m_menuItem16.GetId())
        self.Bind(wx.EVT_MENU, self.Q2, id = self.m_menuItem17.GetId())
        self.Bind(wx.EVT_MENU, self.Q3, id = self.m_menuItem18.GetId())
        self.Bind(wx.EVT_MENU, self.Q4, id = self.m_menuItem19.GetId())
        self.Bind(wx.EVT_MENU, self.Q5, id = self.m_menuItem20.GetId())
        self.Bind(wx.EVT_MENU, self.Q6, id = self.m_menuItem21.GetId())
        self.Bind(wx.EVT_MENU, self.Q7, id = self.m_menuItem22.GetId())
        self.Bind(wx.EVT_MENU, self.Q8, id = self.m_menuItem23.GetId())
        self.Bind(wx.EVT_MENU, self.Q9, id = self.m_menuItem24.GetId())
        self.Bind(wx.EVT_MENU, self.Q10, id = self.m_menuItem25.GetId())
        self.Bind(wx.EVT_MENU, self.Q11, id = self.m_menuItem26.GetId())
        self.Bind(wx.EVT_MENU, self.Q12, id = self.m_menuItem28.GetId())
        self.Bind(wx.EVT_MENU, self.Q13, id = self.m_menuItem29.GetId())
        self.Bind(wx.EVT_MENU, self.Q14, id = self.m_menuItem30.GetId())
        self.Bind(wx.EVT_MENU, self.Q15, id = self.m_menuItem31.GetId())
        self.Bind(wx.EVT_MENU, self.Q16, id = self.m_menuItem32.GetId())
        self.Bind(wx.EVT_MENU, self.Q17, id = self.m_menuItem27.GetId())
        self.Bind(wx.EVT_MENU, self.Q18, id = self.m_menuItem33.GetId())
        self.Bind(wx.EVT_MENU, self.Q19, id = self.m_menuItem34.GetId())
        self.Bind(wx.EVT_MENU, self.Q20, id = self.m_menuItem35.GetId())
        self.Bind(wx.EVT_MENU, self.Q21, id = self.m_menuItem36.GetId())
        self.Bind(wx.EVT_MENU, self.Q22, id = self.m_menuItem38.GetId())
        self.Bind(wx.EVT_MENU, self.Q23, id = self.m_menuItem37.GetId())
        self.Bind(wx.EVT_MENU, self.default, id=self.m_menuItem301.GetId())
        self.Bind(wx.EVT_MENU, self.help, id = self.m_menuItem9.GetId())

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
        self.列表框2 = wx_ListBox(self.启动窗口, size=(649, 218), pos=(337, 353), name='listBox', choices=[], style=1073741984)
        列表框2_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.列表框2.SetFont(列表框2_字体)
        self.列表框2.SetOwnBackgroundColour((249, 249, 249, 249))
        self.列表框2.Bind(wx.EVT_RIGHT_DOWN, self.列表框2_鼠标右键按下)

        图文按钮5_图片 = wx.Image(r'.\ICO\plus.png').ConvertToBitmap()
        self.图文按钮5 = lib_button.ThemedGenBitmapTextButton(self.启动窗口, size=(30, 28), pos=(484, 11), bitmap=图文按钮5_图片,
                                                          label='', name='genbutton')
        self.图文按钮5.SetToolTip("创建项目文件")
        self.图文按钮5.Bind(wx.EVT_BUTTON, self.图文按钮5_按钮被单击)
        self.标签1 = wx_StaticTextL(self.启动窗口, size=(178, 28), pos=(335, 107), label='化合物(Compound)', name='staticText',
                                  style=1)
        标签1_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签1.SetFont(标签1_字体)
        self.编辑框3 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(637, 139), value='', name='text', style=256)
        编辑框3_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框3.SetFont(编辑框3_字体)
        self.编辑框3.SetOwnBackgroundColour((249, 249, 249, 249))
        self.标签2 = wx_StaticTextL(self.启动窗口, size=(120, 28), pos=(637, 107), label='数量(Amount)', name='staticText',
                                  style=1)
        标签2_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签2.SetFont(标签2_字体)

        self.标签3 = wx_StaticTextL(self.启动窗口, size=(92, 27), pos=(740, 88), label='转化自', name='staticText', style=257)
        标签3_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签3.SetFont(标签3_字体)
        self.标签4 = wx_StaticTextL(self.启动窗口, size=(92, 27), pos=(860, 88), label='转化为', name='staticText', style=257)
        标签4_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签4.SetFont(标签4_字体)
        self.标签5 = wx_StaticTextL(self.启动窗口, size=(109, 28), pos=(523, 107), label='分子量(m.w)', name='staticText',
                                  style=1)
        标签5_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签5.SetFont(标签5_字体)
        self.标签8 = wx_StaticTextL(self.启动窗口, size=(131, 28), pos=(754, 107), label='(Convert from)', name='staticText',
                                  style=1)
        标签8_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签8.SetFont(标签8_字体)
        self.标签10 = wx_StaticTextL(self.启动窗口, size=(106, 28), pos=(876, 107), label='(Convert to)', name='staticText',
                                   style=1)
        标签10_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签10.SetFont(标签10_字体)
        self.编辑框4 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(522, 139), value='', name='text', style=256)
        编辑框4_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框4.SetFont(编辑框4_字体)
        self.编辑框4.SetForegroundColour((128, 0, 0, 255))
        self.编辑框4.SetOwnBackgroundColour((249, 249, 249, 249))
        self.组合框3 = wx.ComboBox(self.启动窗口,value='',pos=(758, 139),name='comboBox',choices=['g/L','mg/L','μg/L','ng/L','g/mL', 'mg/mL', 'μg/mL', 'ng/mL', 'pg/mL', 'fg/mL', 'ng/dL', 'mol/L', 'mmol/L', 'μmol/L', 'nmol/L', 'pmol/L'],style=16)
        self.组合框3.SetSize((110, 28))
        组合框3_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.组合框3.SetFont(组合框3_字体)
        self.组合框3.SetOwnBackgroundColour((249, 249, 249, 249))
        self.组合框4 = wx.ComboBox(self.启动窗口,value='',pos=(876, 139),name='comboBox',choices=['g/L','mg/L','μg/L','ng/L','g/mL', 'mg/mL', 'μg/mL', 'ng/mL', 'pg/mL', 'fg/mL', 'ng/dL', 'mol/L', 'mmol/L', 'μmol/L', 'nmol/L', 'pmol/L'],style=16)
        self.组合框4.SetSize((110, 28))
        组合框4_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.组合框4.SetFont(组合框4_字体)
        self.组合框4.SetOwnBackgroundColour((249, 249, 249, 249))
        self.编辑框7 = wx_TextCtrl(self.启动窗口, size=(590, 32), pos=(336, 269), value='', name='text', style=16)
        编辑框7_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框7.SetFont(编辑框7_字体)
        self.编辑框7.SetOwnBackgroundColour((249, 249, 249, 249))
        图文按钮6_图片 = wx.Image(r'.\ICO\down.png').ConvertToBitmap()
        self.图文按钮6 = lib_button_ThemedGenBitmapTextButton(self.启动窗口, size=(35, 32), pos=(925, 269), bitmap=图文按钮6_图片,
                                                          label='', name='genbutton')
        self.图文按钮6.SetToolTip("结果移入历史记录")
        self.图文按钮6.Bind(wx.EVT_BUTTON, self.图文按钮6_按钮被单击)

        self.图文按钮L2 = lib_gb_GradientButton(self.启动窗口, size=(96, 30), pos=(336, 235), bitmap=None, label='计算结果',
                                            name='gradientbutton')
        self.图文按钮L2.Disable()
        图文按钮L2_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.图文按钮L2.SetFont(图文按钮L2_字体)
        self.图文按钮L2.SetForegroundColour((255, 255, 255, 255))

        self.图文按钮L3 = lib_gb_GradientButton(self.启动窗口, size=(96, 30), pos=(336, 320), bitmap=None, label='历史记录',
                                            name='gradientbutton')
        图文按钮L3_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.图文按钮L3.Disable()
        self.图文按钮L3.SetFont(图文按钮L3_字体)
        self.图文按钮L3.SetForegroundColour((255, 255, 255, 255))
        图文按钮7_图片 = wx.Image(r'.\ICO\plus.png').ConvertToBitmap()
        self.图文按钮7 = lib_button_ThemedGenBitmapTextButton(self.启动窗口,size=(30, 28),pos=(306, 140),bitmap=图文按钮7_图片,label='',name='genbutton')
        self.图文按钮7.SetToolTip("新增化合物到项目文件")
        self.图文按钮7.Bind(wx.EVT_BUTTON, self.图文按钮7_按钮被单击)
        self.整数微调框1 = wx_SpinCtrl(self.启动窗口,size=(40, 28),pos=(890, 241),name='wxSpinCtrl',min=1,max=9,initial=2,style=16640)
        self.整数微调框1.SetBase(10)
        整数微调框1_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.整数微调框1.SetFont(整数微调框1_字体)
        self.整数微调框1.Bind(wx.EVT_SPINCTRL,self.整数微调框1_数值被调整)
        self.整数微调框1.SetForegroundColour((128, 0, 0, 255))
        self.标签6 = wx_StaticTextL(self.启动窗口, size=(192, 24), pos=(712, 245), label='设置计算结果的小数位数：', name='staticText',
                                  style=256)
        标签6_字体 = wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" )
        self.标签6.SetFont(标签6_字体)
        self.编辑框6 = wx_TextCtrl(self.启动窗口, size=(178, 28), pos=(336, 139), value='', name='text', style=0)
        编辑框6_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框6.SetFont(编辑框6_字体)
        self.编辑框6.SetForegroundColour((128, 0, 0, 255))
        self.编辑框6.SetOwnBackgroundColour((249, 249, 249, 249))

        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框6)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框4)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框3)
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

    def solu(self, event):
        from Chemulator_Solubility import Frame_solu
        solu_frame = Frame_solu()  # 创建 Frame_solu.py中的窗口实例
        self.Destroy() #直接退出程序
        solu_frame.Show(True)  # 显示窗口
    def help( self, event ):
        # 打开帮助文档
        current_dir = os.getcwd()
        help_file_path = os.path.join(current_dir, "help.chm")
        os.system(f'explorer {help_file_path}')

    def Q1( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.Black04)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.Black04)')

    def Q2( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.Adamant)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.Adamant)')
    def Q3( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.photo2)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.photo2)')

    def Q4( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.Longhorn)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.Longhorn)')

    def Q5( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.粉红主题)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.粉红主题)')

    def Q6( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.彩虹)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.彩虹)')

    def Q7( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.Vista绿)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.Vista绿)')

    def Q8( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.Storm)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.Storm)')

    def Q9( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.精易编程助手)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.精易编程助手)')

    def Q10( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.彗星小助手深蓝色)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.彗星小助手深蓝色)')

    def Q11( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.记忆蓝)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.记忆蓝)')

    def Q12( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.高标栏)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.高标栏)')

    def Q13( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.蓝色电脑管家)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.蓝色电脑管家)')

    def Q14( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.QQ2011)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.QQ2011)')

    def Q15( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.MSN)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.MSN)')

    def Q16( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.Xenes)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.Xenes)')

    def Q17( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.ENJOY)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.ENJOY)')

    def Q18( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.Win7)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.Win7)')

    def Q19( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.ShanMeng窄版)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.ShanMeng窄版)')

    def Q20( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.可爱蓝)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.可爱蓝)')

    def Q21( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.MAC)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.MAC)')

    def Q22( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.Itunes)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.Itunes)')

    def Q23( self, event ):
        # 直接在类定义内部修改全局变量
        global global_variable
        global_variable = 皮肤_加载(皮肤.Dogmax)
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('皮肤_加载(皮肤.Dogmax)')

    def default(self, event):
        file_path = './Configuration/global_variable.txt'  # 替换为你希望保存全局变量的文件路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('None')
        皮肤_卸载()
        self.Destroy() #直接退出程序
        self.frame = Frame()
        self.frame.Show(True)



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
        # Clear the data in 编辑框6, 编辑框4, 编辑框3, 组合框3, and 组合框4
        self.编辑框6.SetValue('')
        self.编辑框4.SetValue('')
        self.组合框3.SetValue('')
        self.组合框4.SetValue('')
        self.编辑框7.Clear()



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

    def 列表框2_鼠标右键按下(self, event):
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


    def 图文按钮6_按钮被单击(self, event):
        self.compound_name = self.编辑框6.GetValue()
        self.conversion_unit = self.组合框4.GetValue()
        self.data_value = self.编辑框3.GetValue()
        self.data_unit = self.组合框3.GetValue()
        self.molecular_weight = self.编辑框4.GetValue()

        variable = self.variable  # 引用self.variable中的variable
        # 获取选中列表项的数值并转换为整数
        selected_value = int(self.整数微调框1.GetValue())

        # 判断是否使用科学计数法表示，并受到小数位数限制
        if (variable != 0) and (variable >= 10 ** 4 or variable <= 10 ** -4) and selected_value != 0:
            variable = "{:.{}e}".format(variable, selected_value)
        elif variable * 1 == 0:
            variable = "0.0"
        else:
            variable = "{:.{}f}".format(variable, selected_value)

        if str(variable) != "0.0":
            result = " ".join([self.compound_name, "：", self.data_value, self.data_unit, "=", variable,
                               self.conversion_unit])
            self.列表框2.Append(result)
        else:
            wx.MessageBox("没有正确计算结果", "提示", wx.OK | wx.ICON_INFORMATION)


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
        self.compound_name = self.编辑框6.GetValue()
        self.data_value = self.编辑框3.GetValue()
        self.data_value4 = self.编辑框4.GetValue()
        self.molecular_weight = self.组合框4.GetValue()
        self.data_unit = self.组合框3.GetValue()
        if self.compound_name and self.data_value and self.data_value4 and self.molecular_weight and self.data_unit:

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

            result = " ".join([self.compound_name, "：", self.data_value, self.data_unit, "=", variable, self.molecular_weight])
            self.编辑框7.SetValue(result)

    def 整数微调框1_数值被调整(self, event):
        self.更新编辑框7内容(event)

    def 单位计算过程(self, event):
        # 获取组合框3和组合框4当前选中的单位
        unit_3 = self.组合框3.GetValue()
        unit_4 = self.组合框4.GetValue()

        concentration_str = self.编辑框3.GetValue()
        if concentration_str == '':
            concentration = decimal.Decimal(0)  # 设置一个默认值
        else:
            concentration = decimal.Decimal(concentration_str)

        mw_str = self.编辑框4.GetValue()
        if mw_str == '':
            mw = decimal.Decimal(1)   # 设置一个默认值
        else:
            mw = decimal.Decimal(mw_str)

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
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()