# -*- coding:utf-8 -*-
import decimal,os,datetime
import gettext
_ = gettext.gettext
from Taowa_wx import *
from Taowa_skin import *
from Chemulator import *
from Chemulator_batch import *
from Chemulator_mw import *



class Frame_solu(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='化学浓度换算', size=(1014, 635),name='frame',style=541072384)
        icon = wx.Icon(r'.\ICO\volumetric-flask.png')

        self.SetIcon(icon)
        self.Bind(wx.EVT_CLOSE, self.on_close)  # 绑定关闭事件
        self.启动窗口 = wx.Panel(self)
        self.Centre()
        self.启动窗口.Bind(wx.EVT_PAINT, self.OnPaint)
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
        self.m_menuItem10.Enable(False)

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
        组合框2_字体 = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑")
        self.组合框2.SetFont(组合框2_字体)
        self.组合框2.SetOwnBackgroundColour((249, 249, 249, 249))
        self.组合框2.Bind(wx.EVT_COMBOBOX, self.组合框2_选中列表项)
        self.组合框2.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.组合框2_弹出列表项)
        self.超级列表框1 = wx_ListCtrl(self.启动窗口,size=(285, 490),pos=(1, 79),name='listCtrl',style=32)
        self.超级列表框1.AppendColumn('名称', 0, 118)
        self.超级列表框1.AppendColumn('化学式', 0, 85)
        self.超级列表框1.AppendColumn('分子量', 0, 85)
        self.超级列表框1.Append(['', '', ''])
        超级列表框1_字体 = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑")
        self.超级列表框1.SetFont(超级列表框1_字体)
        self.超级列表框1.SetOwnBackgroundColour((249, 249, 249, 249))
        # 创建字典来存储选中的化合物和分子量数据
        self.selected_data = {}
        self.超级列表框1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.超级列表框1_选中表项)
        self.超级列表框1.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.超级列表框1_取消选中表项)
        self.超级列表框1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.超级列表框1_右键单击表项)
        self.超级列表框1.Bind(wx.EVT_LEFT_DCLICK, self.超级列表框1_鼠标左键双击)
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
        self.标签1 = wx_StaticTextL(self.启动窗口, size=(178, 28), pos=(335, 108), label='化合物(Compound)', name='staticText',
                                  style=1)
        标签1_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签1.SetFont(标签1_字体)
        self.编辑框3 = wx_TextCtrl(self.启动窗口, size=(180, 28), pos=(336, 243), value='', name='text', style=256)
        编辑框3_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框3.SetFont(编辑框3_字体)
        self.编辑框3.SetForegroundColour((128, 0, 0, 255))
        self.编辑框3.SetOwnBackgroundColour((249, 249, 249, 249))

        # self.标签2 = wx_StaticTextL(self.启动窗口, size=(130, 28), pos=(335, 209), label='单位选择', name='staticText',
        #                           style=1)
        # 标签2_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        # self.标签2.SetFont(标签2_字体)

        self.组合框3 = wx_ComboBox(self.启动窗口,value='',pos=(335, 209),name='comboBox',choices=['溶质(g)','摩尔溶解度(mol/mol)'],style=32)
        self.组合框3.SetHint('请选择...')
        self.组合框3.SetSize((180, 28))
        组合框3_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.组合框3.SetFont(组合框3_字体)
        self.组合框3.SetForegroundColour((255, 255, 255, 255))
        self.组合框3.SetOwnBackgroundColour((31, 128, 186, 255))



        self.标签5 = wx_StaticTextL(self.启动窗口, size=(151, 28), pos=(335, 287), label='溶质分子量(m.w)', name='staticText',
                                  style=1)
        标签5_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签5.SetFont(标签5_字体)

        self.标签10 = wx_StaticTextL(self.启动窗口, size=(106, 28), pos=(547, 209), label='溶剂密度(ρ）', name='staticText',
                                   style=1)
        标签10_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签10.SetFont(标签10_字体)
        self.编辑框4 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(335, 320), value='', name='text', style=256)
        编辑框4_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框4.SetFont(编辑框4_字体)
        self.编辑框4.SetForegroundColour((128, 0, 0, 255))
        self.编辑框4.SetOwnBackgroundColour((249, 249, 249, 249))


        self.编辑框14 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(547, 243), value='', name='text', style=256)
        编辑框11_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框14.SetFont(编辑框11_字体)
        self.编辑框14.SetOwnBackgroundColour((249, 249, 249, 249))

        self.编辑框7 = wx_TextCtrl(self.启动窗口, size=(590, 32), pos=(336, 473), value='', name='text', style=16)
        编辑框7_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框7.SetFont(编辑框7_字体)
        self.编辑框7.Bind(wx.EVT_RIGHT_DOWN,self.OnRightMouseDown)
        self.编辑框7.SetOwnBackgroundColour((249, 249, 249, 249))
        图文按钮6_图片 = wx.Image(r'.\ICO\down.png').ConvertToBitmap()

        self.图文按钮L2 = lib_gb_GradientButton(self.启动窗口, size=(96, 30), pos=(336, 442), bitmap=None, label='计算结果',
                                            name='gradientbutton')
        图文按钮L2_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.图文按钮L2.SetFont(图文按钮L2_字体)
        self.图文按钮L2.SetForegroundColour((255, 255, 255, 255))
        self.图文按钮L2.Disable()

        图文按钮7_图片 = wx.Image(r'.\ICO\plus.png').ConvertToBitmap()
        self.图文按钮7 = lib_button_ThemedGenBitmapTextButton(self.启动窗口,size=(30, 28),pos=(306, 140),bitmap=图文按钮7_图片,label='',name='genbutton')
        self.图文按钮7.SetToolTip("新增化合物到项目文件")
        self.图文按钮7.Bind(wx.EVT_BUTTON, self.图文按钮7_按钮被单击)
        self.整数微调框1 = wx_SpinCtrl(self.启动窗口,size=(40, 28),pos=(890, 445),name='wxSpinCtrl',min=1,max=9,initial=2,style=16640)
        self.整数微调框1.SetBase(10)
        整数微调框1_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.整数微调框1.SetFont(整数微调框1_字体)
        self.整数微调框1.SetForegroundColour((128, 0, 0, 255))
        self.整数微调框1.SetOwnBackgroundColour((249, 249, 249, 249))
        self.整数微调框1.Bind(wx.EVT_SPINCTRL,self.整数微调框1_数值被调整)

        self.标签6 = wx_StaticTextL(self.启动窗口, size=(192, 24), pos=(708, 449), label='设置计算结果的小数位数：', name='staticText',
                                  style=256)
        标签6_字体 = wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" )
        self.标签6.SetFont(标签6_字体)
        self.编辑框6 = wx_TextCtrl(self.启动窗口, size=(178, 28), pos=(336, 139), value='', name='text', style=0)
        编辑框6_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框6.SetFont(编辑框6_字体)
        self.编辑框6.SetForegroundColour((128, 0, 0, 255))
        self.编辑框6.SetOwnBackgroundColour((249, 249, 249, 249))


        self.标签11 = wx_StaticTextL(self.启动窗口, size=(151, 21), pos=(547, 287), label='溶剂1分子量', name='staticText',
                                   style=1)
        标签11_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签11.SetFont(标签11_字体)
        self.标签11.SetForegroundColour((30, 69, 151, 255))

        self.标签12 = wx_StaticTextL(self.启动窗口, size=(107, 21), pos=(688, 287), label='溶剂2分子量', name='staticText',
                                   style=1)
        标签12_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签12.SetFont(标签12_字体)
        self.标签12.SetForegroundColour((255, 116, 49, 255))
        self.标签13 = wx_StaticTextL(self.启动窗口, size=(109, 21), pos=(819, 287), label='溶剂3分子量', name='staticText',
                                   style=1)
        标签13_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签13.SetFont(标签13_字体)
        self.标签13.SetForegroundColour((58, 118, 118, 255))
        self.标签14 = wx_StaticTextL(self.启动窗口, size=(105, 24), pos=(546, 354), label='溶剂1质量(g)', name='staticText', style=1)
        标签14_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签14.SetFont(标签14_字体)
        self.标签14.SetForegroundColour((30, 69, 151, 255))
        self.标签15 = wx_StaticTextL(self.启动窗口, size=(105, 24), pos=(687, 354), label='溶剂2质量(g)', name='staticText', style=1)
        标签15_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签15.SetFont(标签15_字体)
        self.标签15.SetForegroundColour((255, 116, 49, 255))
        self.标签16 = wx_StaticTextL(self.启动窗口, size=(105, 24), pos=(819, 354), label='溶剂3质量(g)', name='staticText', style=1)
        标签16_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.标签16.SetFont(标签16_字体)
        self.标签16.SetForegroundColour((58, 118, 118, 255))

        self.编辑框9 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(687, 321), value='', name='text', style=256)
        self.编辑框10 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(819, 321), value='', name='text', style=256)
        self.编辑框11 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(546, 388), value='', name='text', style=256)
        self.编辑框12 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(687, 388), value='', name='text', style=256)
        self.编辑框13 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(819, 388), value='', name='text', style=256)
        self.编辑框8 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(547, 320), value='', name='text', style=256)
        编辑框8_字体 = wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" )
        self.编辑框8.SetFont(编辑框8_字体)
        self.编辑框9.SetFont(编辑框8_字体)
        self.编辑框10.SetFont(编辑框8_字体)
        self.编辑框11.SetFont(编辑框8_字体)
        self.编辑框12.SetFont(编辑框8_字体)
        self.编辑框13.SetFont(编辑框8_字体)
        self.编辑框8.SetOwnBackgroundColour((249, 249, 249, 249))
        self.编辑框9.SetOwnBackgroundColour((249, 249, 249, 249))
        self.编辑框10.SetOwnBackgroundColour((249, 249, 249, 249))
        self.编辑框11.SetOwnBackgroundColour((249, 249, 249, 249))
        self.编辑框12.SetOwnBackgroundColour((249, 249, 249, 249))
        self.编辑框13.SetOwnBackgroundColour((249, 249, 249, 249))

        图片框6_图片 = wx.Image(r'.\ICO\arrow.png').ConvertToBitmap()
        self.图片框6 = wx_StaticBitmap(self.启动窗口, bitmap=图片框6_图片, size=(35, 32), pos=(487, 289), name='staticBitmap',
                                    style=0)
        ## 设置分隔竖线条
        # self.m_staticline5 = wx.StaticLine(self.启动窗口, wx.ID_ANY, wx.DefaultPosition, wx.Size(2, 200), wx.LI_HORIZONTAL)
        # self.m_staticline5.SetPosition(wx.Point(600, 50))




        # 在初始化方法中添加事件绑定
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框6)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框4)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框3)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框8)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框9)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框10)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框11)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框12)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框13)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框14)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.组合框3)

    def OnPaint(self, event):
        dc = wx.PaintDC(self.启动窗口)  # 绘制在 self.启动窗口中
        brush = wx.Brush(wx.Colour(249, 249, 249))  # 设置背景颜色为 (249, 249, 249)
        dc.SetBackground(brush)
        dc.Clear()
        color = wx.Colour(255, 0, 0)
        b = wx.Brush(color)
        dc.SetBrush(b)
        dc.SetBrush(wx.Brush(wx.Colour(255, 255, 255)))
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        dc.SetFont(font)
        dc.DrawText("m1/M1", 800, 30)
        pen = wx.Pen(wx.Colour(0, 0, 0))
        dc.SetPen(pen)
        dc.DrawLine(746, 63, 960, 63)
        dc.DrawText("m1/M1+m2/M2+m3/M3", 746, 70)
        font = wx.Font(18, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "华文中宋")
        dc.SetFont(font)
        dc.DrawText("溶解度(x1) =", 600, 50)

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
        # # 关闭当前窗口
        # self.Close()
        self.Destroy() #直接退出程序
        quality_frame.Show(True)  # 显示窗口

    def help( self, event ):
        # 打开帮助文档
        current_dir = os.getcwd()
        help_file_path = os.path.join(current_dir, "help.chm")
        os.system(f'explorer {help_file_path}')

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
        # Clear the data in 编辑框6, 编辑框4, 编辑框3, and 组合框4
        self.编辑框6.SetValue('')
        self.编辑框4.SetValue('')
        self.编辑框3.SetValue('')



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


    def 超级列表框2_选中表项(self, event):
        selected_items = []
        selected_indexes = []

        index = self.超级列表框2.GetFirstSelected()
        while index != -1:
            item_data = []
            for col in range(self.超级列表框2.GetColumnCount()):
                item_data.append(self.超级列表框2.GetItemText(index, col))
            selected_items.append(item_data)
            selected_indexes.append(index)
            index = self.超级列表框2.GetNextSelected(index)

    def 超级列表框2_右键单击表项(self, event):
        selected_index = self.超级列表框2.GetFirstSelected()

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
        selected_index = self.超级列表框2.GetFirstSelected()

        if selected_index != -1:
            self.超级列表框2.DeleteItem(selected_index)

    def 复制列表框2选中行(self, event):
        selected_index = self.超级列表框2.GetFirstSelected()

        if selected_index != -1:
            item_data = []
            for col in range(self.超级列表框2.GetColumnCount()):
                item_data.append(self.超级列表框2.GetItemText(selected_index, col))

            # 复制选中行的数据到剪贴板
            data = '\t'.join(item_data)
            clipboard = wx.TextDataObject()
            clipboard.SetText(data)
            if wx.TheClipboard.Open():
                wx.TheClipboard.SetData(clipboard)
                wx.TheClipboard.Close()

    def 全选复制列表框2选中行(self, event):
        clipboard = wx.Clipboard.Get()
        selected_items = []

        header_data = []
        for col in range(self.超级列表框2.GetColumnCount()):
            header_data.append(self.超级列表框2.GetColumn(col).GetText())
        selected_items.insert(0, header_data)

        for row in range(self.超级列表框2.GetItemCount()):
            item_data = []
            for col in range(self.超级列表框2.GetColumnCount()):
                item_data.append(self.超级列表框2.GetItemText(row, col))
            selected_items.append(item_data)

        data_text = '\n'.join(['\t'.join(row) for row in selected_items])

        clipboard.Open()
        clipboard.SetData(wx.TextDataObject(data_text))
        clipboard.Flush()
        clipboard.Close()

        wx.MessageBox("数据已复制到剪贴板！", "成功", wx.OK | wx.ICON_INFORMATION)

    def save_data_to_txt(self, data):
        # 获取选中行数据
        selected_items = []

        header_data = []
        for col in range(self.超级列表框2.GetColumnCount()):
            header_data.append(self.超级列表框2.GetColumn(col).GetText())
        selected_items.append(header_data)

        for row in range(self.超级列表框2.GetItemCount()):
            item_data = []
            for col in range(self.超级列表框2.GetColumnCount()):
                item_data.append(self.超级列表框2.GetItemText(row, col))
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

        wx.MessageBox("数据已复制到剪贴板并保存至桌面上的txt文件！", "成功", wx.OK | wx.ICON_INFORMATION)

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

    def OnRightMouseDown(self, event):
        menu = wx.Menu()
        copy_item = menu.Append(wx.ID_COPY, "复制")
        self.Bind(wx.EVT_MENU, self.OnCopy, copy_item)

        self.PopupMenu(menu)
        menu.Destroy()

    def OnCopy(self, event):
        data = self.编辑框7.GetLineText(0)  # 获取第一行数据
        clipboard = wx.Clipboard.Get()
        clipboard.SetData(wx.TextDataObject(data))
        clipboard.Close()

        wx.MessageBox("复制成功！", "提示", wx.OK | wx.ICON_INFORMATION)
    def 更新编辑框7内容(self, event):
        compound_name = self.编辑框6.GetValue()
        data_value = self.编辑框3.GetValue()
        data_value_2 = self.编辑框8.GetValue()
        data_value_3 = self.编辑框9.GetValue()
        data_value_4 = self.编辑框10.GetValue()
        data_value_5 = self.编辑框11.GetValue()
        data_value_6 = self.编辑框12.GetValue()
        data_value_7 = self.编辑框13.GetValue()
        data_value_8 = self.编辑框14.GetValue()

        if compound_name and data_value and (data_value_2 or data_value_3 or data_value_4 or data_value_5 or data_value_6 or data_value_7):
            # 获取选中列表项的数值
            selected_value = int(self.整数微调框1.GetValue())

            # 调用单位计算过程函数来计算variable变量的值
            self.单位计算过程(event)
            # 添加变量的声明和初始化
            variable = self.variable  ## variable 是指摩尔溶解度 mol/mol
            # print(variable)
            variable_1 = self.variable_1  ## variable_1 是指质量溶解度 g/100g
            variable_2 = self.variable_2  ## variable_1 是指样本溶解度 g/100mL
            # print(variable)

            # 判断是否使用科学计数法表示，并受到小数位数限制
            if (variable != 0) and (variable >= 10 ** 4 or variable <= 10 ** -4) and selected_value != 0:
                variable = "{:.{}e}".format(variable, selected_value)
            elif variable * 1 == 0:
                variable = "0.0"
            else:
                variable = "{:.{}f}".format(variable, selected_value)

            # 判断 variable_1 是否使用科学计数法表示，并且限制小数位数
            if (variable_1 != 0) and (variable_1 >= 10 ** 4 or variable_1 <= 10 ** -4) and selected_value != 0:
                variable_1 = "{:.{}e}".format(variable_1, selected_value)
            elif variable_1 * 1 == 0:
                variable_1 = "0.0"
            else:
                variable_1 = "{:.{}f}".format(variable_1, selected_value)

            # 判断 variable_2 是否使用科学计数法表示，并且限制小数位数
            if (variable_2 != 0) and (variable_2 >= 10 ** 4 or variable_2 <= 10 ** -4) and selected_value != 0:
                variable_2 = "{:.{}e}".format(variable_2, selected_value)
            elif variable_2 * 1 == 0:
                variable_2 = "0.0"
            else:
                variable_2 = "{:.{}f}".format(variable_2, selected_value)

            result = " ".join([compound_name, "：",str(variable_2),"g/100mL", "=", str(variable), "mol/mol","=",str(variable_1),"g/100g"])

            result_1 = " ".join(
                [compound_name, "：", str(data_value), "mol/mol", "=", str(variable_2), "g/100mL",  "=", str(variable_1),
                 "g/100g"])
            if self.组合框3.GetValue() == '溶质(g)':
                self.编辑框7.SetValue(result)
            elif self.组合框3.GetValue() == '摩尔溶解度(mol/mol)':
                self.编辑框7.SetValue(result_1)

    def 整数微调框1_数值被调整(self, event):
        self.更新编辑框7内容(event)

    def 单位计算过程(self, event):
        concentration_str = self.编辑框3.GetValue()
        if concentration_str == '':
            concentration = decimal.Decimal(0)  # 设置一个默认值
        else:
            concentration = decimal.Decimal(concentration_str)

        mw_str_1 = self.编辑框4.GetValue()
        if mw_str_1 == '':
            self.mw1 = decimal.Decimal(1)   # 设置一个默认值
        else:
            self.mw1 = decimal.Decimal(mw_str_1)    # 设置self.mw1为溶质分子量

        mw_str_2 = self.编辑框8.GetValue()
        mw_str_3 = self.编辑框9.GetValue()
        mw_str_4 = self.编辑框10.GetValue()
        if mw_str_2 == '':
            mw2 = decimal.Decimal(1)  # 设置一个默认值
        else:
            mw2 = decimal.Decimal(mw_str_2)     # 设置mw2为溶剂1分子量

        if mw_str_3 == '':
            mw3 = decimal.Decimal(1)  # 设置一个默认值
        else:
            mw3 = decimal.Decimal(mw_str_3)     # 设置mw3为溶剂2分子量

        if mw_str_4 == '':
            mw4 = decimal.Decimal(1)  # 设置一个默认值
        else:
            mw4 = decimal.Decimal(mw_str_4)     # 设置mw4为溶剂3分子量

        m_str_1 = self.编辑框11.GetValue()    ##设置m_str_1 为溶剂1质量
        m_str_2 = self.编辑框12.GetValue()    ##设置m_str_2 为溶剂2质量
        m_str_3 = self.编辑框13.GetValue()    ##设置m_str_3 为溶剂3质量
        md_str_5 = self.编辑框14.GetValue()  ## 设置md_str_5为密度
        if m_str_1 == '':
            m_str_1 = decimal.Decimal(1)  # 设置一个默认值
        else:
            m_str_1 = decimal.Decimal(m_str_1)
        if m_str_2 == '':
            m_str_2 = decimal.Decimal(1)  # 设置一个默认值
        else:
            m_str_2 = decimal.Decimal(m_str_2)
        if m_str_3 == '':
            m_str_3 = decimal.Decimal(1)  # 设置一个默认值
        else:
            m_str_3 = decimal.Decimal(m_str_3)

        self.unit_1 = self.组合框3.GetValue()

        ##一元溶剂 ## unit_4 == "g/100g" or unit_4 == "mol/mol"
        if (mw_str_2 and m_str_1) != '' and (mw_str_3 and m_str_2)== ''and (mw_str_4 and m_str_3) == '':
            if self.unit_1 == '溶质(g)':
                self.variable = decimal.Decimal(concentration) / decimal.Decimal(
                    self.mw1) / ((decimal.Decimal(concentration) / decimal.Decimal(self.mw1))+(decimal.Decimal(m_str_1) / mw2))
                self.variable_1 = decimal.Decimal(concentration) / decimal.Decimal(m_str_1) * 100
                self.variable_2 = decimal.Decimal(concentration) / (decimal.Decimal(m_str_1) / decimal.Decimal(md_str_5))* 100
                return
            if self.unit_1 == '摩尔溶解度(mol/mol)':
                self.m1_str = (decimal.Decimal(concentration) * decimal.Decimal(self.mw1)) / (decimal.Decimal(1) - decimal.Decimal(concentration))  ## m1_str等于mol/mol转化对于的溶质量

                self.variable_1 = decimal.Decimal(self.m1_str) / decimal.Decimal(m_str_1) * 100

                self.variable_2 = decimal.Decimal(self.m1_str) / (
                            decimal.Decimal(m_str_1) / decimal.Decimal(md_str_5)) * 100
                return




        ##二元溶剂 ## unit_4 == "g/100g" or unit_4 == "mol/mol"
        if (mw_str_2 and m_str_1) != '' and (mw_str_3 and m_str_2) != '' and (mw_str_4 and m_str_3) == '':
            if self.unit_1 == '溶质(g)':
                self.variable = decimal.Decimal(concentration) / decimal.Decimal(
                    self.mw1) / ((decimal.Decimal(concentration) / decimal.Decimal(self.mw1)) + (
                            decimal.Decimal(m_str_1) / mw2) + (
                            decimal.Decimal(m_str_2) / mw3))
                self.variable_1 = decimal.Decimal(concentration) / (decimal.Decimal(m_str_1) + decimal.Decimal(m_str_2)) * 100
                self.variable_2 = decimal.Decimal(concentration) / ((decimal.Decimal(m_str_1) + (m_str_2)) / decimal.Decimal(md_str_5)) * 100
                return
            if self.unit_1 == '摩尔溶解度(mol/mol)':
                self.m1_str = (((decimal.Decimal(concentration) * decimal.Decimal(m_str_1) * decimal.Decimal(self.mw1))/decimal.Decimal(mw2)) + ((decimal.Decimal(concentration) * decimal.Decimal(m_str_2) * decimal.Decimal(self.mw1)))/ decimal.Decimal(mw3)) / (decimal.Decimal(1) - decimal.Decimal(concentration))  ## m1_str等于mol/mol转化对于的溶质量

                self.variable_1 = decimal.Decimal(self.m1_str) / (decimal.Decimal(m_str_1) + decimal.Decimal(m_str_2)) * 100

                self.variable_2 = decimal.Decimal(self.m1_str) / ((decimal.Decimal(m_str_1) + (m_str_2)) / decimal.Decimal(md_str_5)) * 100
                # print(decimal.Decimal(self.m1_str))
                return

        ##三元溶剂 ## unit_4 == "g/100g" or unit_4 == "mol/mol"
        if (mw_str_2 and m_str_1) != '' and (mw_str_3 and m_str_2) != '' and (mw_str_4 and m_str_3) != '':
            if self.unit_1 == '溶质(g)':
                self.variable = decimal.Decimal(concentration) / decimal.Decimal(
                    self.mw1) / ((decimal.Decimal(concentration) / decimal.Decimal(self.mw1)) + (
                        decimal.Decimal(m_str_1) / mw2) + (
                                    decimal.Decimal(m_str_2) / mw3) + (
                                    decimal.Decimal(m_str_3) / mw4))
                self.variable_1 = decimal.Decimal(concentration) / (decimal.Decimal(m_str_1) + decimal.Decimal(m_str_2) + decimal.Decimal(m_str_3)) * 100
                self.variable_2 = decimal.Decimal(concentration) / ((decimal.Decimal(m_str_1) + decimal.Decimal(m_str_2) + decimal.Decimal(m_str_3)) / decimal.Decimal(md_str_5)) * 100
                return

            if self.unit_1 == '摩尔溶解度(mol/mol)':
                self.m1_str = (((decimal.Decimal(concentration) * decimal.Decimal(m_str_1) * decimal.Decimal(self.mw1))/decimal.Decimal(mw2)) + ((decimal.Decimal(concentration) * decimal.Decimal(m_str_2) * decimal.Decimal(self.mw1)))/ decimal.Decimal(mw3) + ((decimal.Decimal(concentration) * decimal.Decimal(m_str_3) * decimal.Decimal(self.mw1))/ decimal.Decimal(mw4) )) / (decimal.Decimal(1) - decimal.Decimal(concentration))  ## m1_str等于mol/mol转化对于的溶质量

                self.variable_1 = decimal.Decimal(self.m1_str) / (decimal.Decimal(m_str_1) + decimal.Decimal(m_str_2) +decimal.Decimal(m_str_3)) * 100

                self.variable_2 = decimal.Decimal(self.m1_str) / ((decimal.Decimal(m_str_1) + decimal.Decimal(m_str_2) + decimal.Decimal(m_str_3)) / decimal.Decimal(md_str_5)) * 100
                # print(decimal.Decimal(self.m1_str))
                return



    def on_close(self, event):
        dlg = wx.MessageDialog(self, "是否退出程序？", "摩尔浓度换算", wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()

        if result == wx.ID_YES:
            self.Destroy()


class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame_solu()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()