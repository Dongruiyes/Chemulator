# -*- coding:utf-8 -*-
import wx.adv,decimal
import tkinter as tk
from tkinter import messagebox
from Taowa_wx import *
from Taowa_skin import *

皮肤_加载(皮肤.QQ2011)


class Frame(wx.Frame):
    def __init__(self):
        wx_Frame.__init__(self, None, title='化学浓度换算', size=(1014, 612),name='frame',style=541072384)
        icon = wx.Icon(r'.\ICO\volumetric-flask.png')
        self.SetIcon(icon)
        self.Bind(wx.EVT_CLOSE, self.on_close)  # 绑定关闭事件
        self.启动窗口 = wx.Panel(self)
        self.启动窗口.SetOwnBackgroundColour((240, 240, 240, 255))
        self.Centre()
        self.variable = decimal.Decimal(0)
        图文按钮3_图片 = wx.Image(r'.\ICO\left arrow.png').ConvertToBitmap()
        self.图文按钮3 = lib_button_ThemedGenBitmapTextButton(self.启动窗口,size=(35, 30),pos=(291, 343),bitmap=图文按钮3_图片,label='',name='genbutton')
        self.图文按钮3.SetToolTip("清除所有数据")
        self.图文按钮3.Bind(wx.EVT_BUTTON, self.图文按钮3_按钮被单击)
        project_dir = "./Project"  # 将此处修改为 "Project" 目录的路径
        folder_names = os.listdir(project_dir)
        self.组合框2 = wx.ComboBox(self.启动窗口, value='', pos=(301, 20), name='comboBox', choices=folder_names, style=16)
        self.组合框2.SetSize((172, 28))
        # 刷新Combobox的选项
        self.refresh_folder_names()
        组合框2_字体 = wx.Font(11, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.组合框2.SetFont(组合框2_字体)
        self.组合框2.SetOwnBackgroundColour((224, 224, 224, 255))
        self.组合框2.Bind(wx.EVT_COMBOBOX, self.组合框2_选中列表项)
        self.组合框2.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.组合框2_弹出列表项)
        self.超级列表框1 = wx_ListCtrl(self.启动窗口,size=(285, 490),pos=(1, 79),name='listCtrl',style=32)
        self.超级列表框1.AppendColumn('名称', 0, 118)
        self.超级列表框1.AppendColumn('化学式', 0, 85)
        self.超级列表框1.AppendColumn('分子量', 0, 85)
        self.超级列表框1.Append(['', '', ''])
        超级列表框1_字体 = wx.Font(12, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.超级列表框1.SetFont(超级列表框1_字体)
        # 创建字典来存储选中的化合物和分子量数据
        self.selected_data = {}
        self.超级列表框1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.超级列表框1_选中表项)
        self.超级列表框1.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.超级列表框1_取消选中表项)
        self.超级列表框1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.超级列表框1_右键单击表项)
        图片框3_图片 = wx.Image(r'.\ICO\folder.png').ConvertToBitmap()
        self.图片框3 = wx.StaticBitmap(self.启动窗口, bitmap=图片框3_图片,size=(32, 30),pos=(271, 19),name='staticBitmap',style=0)
        self.图片框3.Bind(wx.EVT_LEFT_DOWN,self.图片框3_鼠标左键按下)
        self.图片框3.SetToolTip("打开项目根目录")
        图文按钮2_图片 = wx.Image(r'.\ICO\right-arrow.png').ConvertToBitmap()
        self.图文按钮2 = lib_button_ThemedGenBitmapTextButton(self.启动窗口,size=(35, 30),pos=(291, 235),bitmap=图文按钮2_图片,label='',name='genbutton')
        self.图文按钮2.SetToolTip("填入选中化合物")
        self.图文按钮2.Bind(wx.EVT_BUTTON, self.图文按钮2_按钮被单击)
        self.超级列表框2 = wx_ListCtrl(self.启动窗口, size=(650, 150), pos=(336, 419), name='listCtrl', style=1059)
        self.超级列表框2.AppendColumn('化合物', 0, 130)
        self.超级列表框2.AppendColumn('分子量', 0, 80)
        self.超级列表框2.AppendColumn('数值', 0, 100)
        self.超级列表框2.AppendColumn('原单位', 0, 100)
        self.超级列表框2.AppendColumn('=', 0, 20)
        self.超级列表框2.AppendColumn('数值', 0, 118)
        self.超级列表框2.AppendColumn('转化单位', 0, 100)
        超级列表框2_字体 = wx.Font(12, 74, 90, 400, False, '华文新魏', 28)
        self.超级列表框2.SetFont(超级列表框2_字体)
        self.超级列表框2.Bind(wx.EVT_LIST_ITEM_SELECTED, self.超级列表框2_选中表项)
        self.超级列表框2.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.超级列表框2_右键单击表项)
        图文按钮5_图片 = wx.Image(r'.\ICO\plus.png').ConvertToBitmap()
        self.图文按钮5 = lib_button.ThemedGenBitmapTextButton(self.启动窗口, size=(30, 28), pos=(473, 19), bitmap=图文按钮5_图片,
                                                          label='', name='genbutton')
        self.图文按钮5.SetToolTip("创建项目文件")
        self.图文按钮5.Bind(wx.EVT_BUTTON, self.图文按钮5_按钮被单击)
        图文按钮L1_图片 = wx.Image(r'.\ICO\copy.png').ConvertToBitmap()
        self.图文按钮L1 = lib_gb_GradientButton(self.启动窗口, size=(66, 33), pos=(920, 386), bitmap=图文按钮L1_图片, label='Copy',
                                            name='gradientbutton')
        self.图文按钮L1.SetForegroundColour((255, 255, 255, 255))
        self.图文按钮L1.Bind(wx.EVT_BUTTON,self.图文按钮L1_按钮被单击)
        self.图文按钮L1.SetToolTip("全选复制")
        self.标签1 = wx_StaticTextL(self.启动窗口,size=(92, 27),pos=(336, 100),label='化合物',name='staticText',style=257)
        标签1_字体 = wx.Font(14,74,90,400,False,'华文新魏',28)
        self.标签1.SetFont(标签1_字体)
        self.编辑框3 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(616, 140), value='', name='text', style=256)
        编辑框3_字体 = wx.Font(12, 72, 90, 400, False, 'Microsoft YaHei UI', 33)
        self.编辑框3.SetFont(编辑框3_字体)
        self.标签2 = wx_StaticTextL(self.启动窗口,size=(92, 27),pos=(616, 100),label='数值',name='staticText',style=257)
        标签2_字体 = wx.Font(14,74,90,400,False,'华文新魏',28)
        self.标签2.SetFont(标签2_字体)
        self.标签3 = wx_StaticTextL(self.启动窗口,size=(92, 27),pos=(736, 100),label='原单位',name='staticText',style=257)
        标签3_字体 = wx.Font(14,74,90,400,False,'华文新魏',28)
        self.标签3.SetFont(标签3_字体)
        self.标签4 = wx_StaticTextL(self.启动窗口,size=(92, 27),pos=(866, 100),label='转化单位',name='staticText',style=257)
        标签4_字体 = wx.Font(14,74,90,400,False,'华文新魏',28)
        self.标签4.SetFont(标签4_字体)
        self.标签5 = wx_StaticTextL(self.启动窗口,size=(92, 27),pos=(496, 100),label='分子量',name='staticText',style=257)
        标签5_字体 = wx.Font(14, 74, 90, 400, False, '华文新魏', 28)
        self.标签5.SetFont(标签5_字体)
        self.编辑框4 = wx_TextCtrl(self.启动窗口, size=(110, 28), pos=(496, 140), value='', name='text', style=256)
        编辑框4_字体 = wx.Font(12, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.编辑框4.SetFont(编辑框4_字体)
        self.编辑框4.SetForegroundColour((128, 0, 0, 255))
        self.组合框3 = wx.ComboBox(self.启动窗口,value='',pos=(736, 140),name='comboBox',choices=['g/mL', 'mg/mL', 'μg/mL', 'ng/mL', 'pg/mL', 'fg/mL', 'ng/dL', '%', 'M', 'mM', 'μM', 'nM', 'pM'],style=16)
        self.组合框3.SetSize((120, 28))
        组合框3_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
        self.组合框3.SetFont(组合框3_字体)
        self.组合框4 = wx.ComboBox(self.启动窗口,value='',pos=(866, 139),name='comboBox',choices=['g/mL', 'mg/mL', 'μg/mL', 'ng/mL', 'pg/mL', 'fg/mL', 'ng/dL', '%', 'M', 'mM', 'μM', 'nM', 'pM'],style=16)
        self.组合框4.SetSize((120, 28))
        组合框4_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
        self.组合框4.SetFont(组合框4_字体)
        self.编辑框7 = wx_TextCtrl(self.启动窗口, size=(590, 32), pos=(336, 269), value='', name='text', style=16)
        编辑框7_字体 = wx.Font(12, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.编辑框7.SetFont(编辑框7_字体)
        图文按钮6_图片 = wx.Image(r'.\ICO\down.png').ConvertToBitmap()
        self.图文按钮6 = lib_button_ThemedGenBitmapTextButton(self.启动窗口, size=(35, 32), pos=(925, 269), bitmap=图文按钮6_图片,
                                                          label='', name='genbutton')
        self.图文按钮6.SetToolTip("结果移入历史记录")
        self.图文按钮6.Bind(wx.EVT_BUTTON, self.图文按钮6_按钮被单击)
        self.图文按钮L2 = lib_gb_GradientButton(self.启动窗口, size=(100, 32), pos=(336, 235), bitmap=None, label='计算结果',
                                            name='gradientbutton')
        图文按钮L2_字体 = wx.Font(12, 74, 90, 400, False, '华文新魏', 28)
        self.图文按钮L2.SetFont(图文按钮L2_字体)
        self.图文按钮L2.SetForegroundColour((255, 255, 255, 255))
        self.图文按钮L3 = lib_gb_GradientButton(self.启动窗口, size=(101, 32), pos=(336, 386), bitmap=None, label='历史记录',
                                            name='gradientbutton')
        图文按钮L3_字体 = wx.Font(12, 74, 90, 400, False, '华文新魏', 28)
        self.图文按钮L3.SetFont(图文按钮L3_字体)
        self.图文按钮L3.SetForegroundColour((255, 255, 255, 255))
        图文按钮7_图片 = wx.Image(r'.\ICO\plus.png').ConvertToBitmap()
        self.图文按钮7 = lib_button_ThemedGenBitmapTextButton(self.启动窗口,size=(30, 28),pos=(306, 140),bitmap=图文按钮7_图片,label='',name='genbutton')
        self.图文按钮7.SetToolTip("新增化合物到本项目")
        self.图文按钮7.Bind(wx.EVT_BUTTON, self.图文按钮7_按钮被单击)
        self.组合框5 = wx_ComboBox(self.启动窗口, value='3', pos=(890, 241), name='comboBox',
                                choices=['1', '2', '3', '4', '5', '6', '7', '8', '9'], style=16)
        self.组合框5.SetSize((36, 28))
        组合框5_字体 = wx.Font(11, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.组合框5.SetFont(组合框5_字体)
        self.组合框5.Bind(wx.EVT_COMBOBOX, self.组合框5_选中列表项)
        self.标签6 = wx_StaticTextL(self.启动窗口, size=(192, 24), pos=(698, 245), label='设置计算结果的小数位数：', name='staticText',
                                  style=256)
        标签6_字体 = wx.Font(12, 74, 90, 400, False, '华文新魏', 28)
        self.标签6.SetFont(标签6_字体)
        self.填充组合框6数据()
        self.组合框6 = wx_ComboBox(self.启动窗口, value='', pos=(336, 140), name='comboBox', choices=self.choices, style=32)
        self.组合框6.SetSize((150, 28))
        组合框6_字体 = wx.Font(11, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.组合框6.SetFont(组合框6_字体)
        self.组合框6.SetForegroundColour((128, 0, 0, 255))

        # 在初始化方法中添加以下代码
        self.组合框6.AutoComplete(self.组合框6.GetItems())
        self.标签7 = wx_StaticTextL(self.启动窗口,size=(72, 24),pos=(928, 6),label='帮助(help)',name='staticText',style=1)
        标签7_字体 = wx.Font(11, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.标签7.SetFont(标签7_字体)
        self.标签7.SetToolTip("查看帮助文档")
        self.标签7.Bind(wx.EVT_LEFT_DOWN, self.标签7_鼠标左键按下)
        图片框4_图片 = wx.Image(r'.\ICO\document.png').ConvertToBitmap()
        self.图片框4 = wx_StaticBitmap(self.启动窗口, bitmap=图片框4_图片,size=(22, 24),pos=(905, 4),name='staticBitmap',style=0)

        # 在初始化方法中添加事件绑定
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.组合框6)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框4)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框3)
        self.Bind(wx.EVT_COMBOBOX, self.更新编辑框7内容, self.组合框3)
        self.Bind(wx.EVT_COMBOBOX, self.更新编辑框7内容, self.组合框4)

    def 填充组合框6数据(self):
        project_dir = "./Project"
        folder_names = os.listdir(project_dir)
        self.choices = []
        for folder_name in folder_names:
            folder_path = os.path.join(project_dir, folder_name)
            file_path = os.path.join(folder_path, "化合物.txt")
            with open(file_path, 'r', encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split()
                    if len(data) >= 2:
                        choice = data[0] + "  " + data[1]
                        self.choices.append(choice)


    def 图文按钮3_按钮被单击(self, event):
        # Clear the data in 组合框6, 编辑框4, 编辑框3, 组合框3, and 组合框4
        self.组合框6.SetValue('')
        self.编辑框4.SetValue('')
        self.编辑框3.SetValue('')
        self.组合框3.SetValue('')
        self.组合框4.SetValue('')



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

            # 设置化合物名称和分子量 组合框6 and 编辑框4
            self.组合框6.SetValue(compound_name + "  " + chemical_formula)
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
            # 创建一个删除的菜单项
            menu = wx.Menu()
            delete_item = menu.Append(wx.ID_ANY, "删除")

            # 绑定菜单项的单击事件
            self.Bind(wx.EVT_MENU, self.删除列表框2选中行, delete_item)

            # 显示菜单
            self.PopupMenu(menu)

            # 销毁菜单
            menu.Destroy()

    def 删除列表框2选中行(self, event):
        selected_index = self.超级列表框2.GetFirstSelected()

        if selected_index != -1:
            self.超级列表框2.DeleteItem(selected_index)


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

    def 图文按钮L1_按钮被单击(self, event):
        clipboard = wx.Clipboard.Get()
        selected_items = []

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


    def 图文按钮6_按钮被单击(self, event):
        compound_name = self.组合框6.GetValue()
        conversion_unit = self.组合框4.GetValue()
        data_value = self.编辑框3.GetValue()
        data_unit = self.组合框3.GetValue()
        molecular_weight = self.编辑框4.GetValue()

        variable = self.variable  # 引用self.variable中的variable
        # 获取选中列表项的数值并转换为整数
        selected_value = int(self.组合框5.GetValue())

        # 判断是否使用科学计数法表示，并受到小数位数限制
        if (variable != 0) and (variable >= 10 ** 4 or variable <= 10 ** -4) and selected_value != 0:
            variable = "{:.{}e}".format(variable, selected_value)
        elif variable * 1 == 0:
            variable = "0.0"
        else:
            variable = "{:.{}f}".format(variable, selected_value)

        if str(variable) != "0.0":
            # 填充超级列表框2的内容
            self.超级列表框2.Append(
                [compound_name, molecular_weight, data_value, data_unit, "=", variable, conversion_unit])
        else:
            wx.MessageBox("没有正确计算结果", "提示", wx.OK | wx.ICON_INFORMATION)

    def 标签7_鼠标左键按下(self, event):
        # 打开帮助文档
        current_dir = os.getcwd()
        help_file_path = os.path.join(current_dir, "help.chm")
        os.system(f'explorer {help_file_path}')

    def 图文按钮7_按钮被单击(self, event):
        compound_name = self.组合框6.GetValue()
        data_value = self.编辑框4.GetValue()

        # 分析compound_name内容并分组
        compound_name_list = compound_name.split("  ")
        compound_name_1 = compound_name_list[0]
        compound_name_2 = compound_name_list[1] if len(compound_name_list) > 1 else ""

        # 拼接要写入文件的内容
        content = compound_name_1 + "\t" + compound_name_2 + "\t" + data_value

        # 检查是否存在完全相同的数据
        folder_name = self.组合框2.GetValue()
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
            tk.messagebox.showinfo("重复", "该数据已存在，无需再次添加！")

        else:
            # 弹出确认对话框
            confirm = tk.messagebox.askyesno("确认添加", "是否确认添加数据?")

            if confirm:
                try:
                    # 打开文件并以追加模式写入内容
                    with open(file_path, "a", encoding="utf-8") as file:
                        file.write(content + "\n")

                    # 提示添加成功
                    tk.messagebox.showinfo("成功", "数据添加成功！")

                except Exception as e:
                    # 提示添加失败
                    tk.messagebox.showerror("失败", "数据添加失败！")
            else:
                # 提示取消添加
                tk.messagebox.showinfo("提示", "已取消添加数据！")

        self.组合框2_选中列表项(event)

    def 更新编辑框7内容(self, event):
        compound_name = self.组合框6.GetValue()
        molecular_weight = self.组合框4.GetValue()
        data_value = self.编辑框3.GetValue()
        data_unit = self.组合框3.GetValue()

        # 获取选中列表项的数值
        selected_value = int(self.组合框5.GetValue())

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

        result = " ".join([compound_name, "：", data_value, data_unit, "=", variable, molecular_weight])
        self.编辑框7.SetValue(result)

    def 组合框5_选中列表项(self, event):
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
        elif unit_3 == "g/mL" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "g/mL" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif unit_3 == "g/mL" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)
        elif unit_3 == "g/mL" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 12)
        elif unit_3 == "g/mL" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 15)
        elif unit_3 == "g/mL" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 2)
        elif unit_3 == "g/mL" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3) / decimal.Decimal(mw)
        elif unit_3 == "g/mL" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6) / decimal.Decimal(mw)
        elif unit_3 == "g/mL" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9) / decimal.Decimal(mw)
        elif unit_3 == "g/mL" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 12) / decimal.Decimal(mw)
        elif unit_3 == "g/mL" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 15) / decimal.Decimal(mw)
        elif unit_3 == "g/mL" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 11)

        # 判断组合框3为"mg/mL"和组合框4的单位并执行相应的计算
        elif unit_3 == "mg/mL" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 3)
        elif unit_3 == "mg/mL" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "mg/mL" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "mg/mL" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif unit_3 == "mg/mL" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)
        elif unit_3 == "mg/mL" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 12)
        elif unit_3 == "mg/mL" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 1)
        elif unit_3 == "mg/mL" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(mw)
        elif unit_3 == "mg/mL" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3) / decimal.Decimal(mw)
        elif unit_3 == "mg/mL" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6) / decimal.Decimal(mw)
        elif unit_3 == "mg/mL" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9) / decimal.Decimal(mw)
        elif unit_3 == "mg/mL" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 12) / decimal.Decimal(mw)
        elif unit_3 == "mg/mL" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 8)

        # 判断组合框3为"μg/mL"和组合框4的单位并执行相应的计算
        elif unit_3 == "μg/mL" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 6)
        elif unit_3 == "μg/mL" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 3)
        elif unit_3 == "μg/mL" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "μg/mL" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "μg/mL" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif unit_3 == "μg/mL" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)
        elif unit_3 == "μg/mL" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 4)
        elif unit_3 == "μg/mL" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3) / decimal.Decimal(mw)
        elif unit_3 == "μg/mL" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(mw)
        elif unit_3 == "μg/mL" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3) / decimal.Decimal(mw)
        elif unit_3 == "μg/mL" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6) / decimal.Decimal(mw)
        elif unit_3 == "μg/mL" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9) / decimal.Decimal(mw)
        elif unit_3 == "μg/mL" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 5)

        # 判断组合框3为"ng/mL"和组合框4的单位并执行相应的计算
        elif unit_3 == "ng/mL" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 9)
        elif unit_3 == "ng/mL" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 6)
        elif unit_3 == "ng/mL" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 3)
        elif unit_3 == "ng/mL" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "ng/mL" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "ng/mL" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif unit_3 == "ng/mL" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 7)
        elif unit_3 == "ng/mL" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6) / decimal.Decimal(mw)
        elif unit_3 == "ng/mL" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3) / decimal.Decimal(mw)
        elif unit_3 == "ng/mL" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration)  / decimal.Decimal(mw)
        elif unit_3 == "ng/mL" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3) / decimal.Decimal(mw)
        elif unit_3 == "ng/mL" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6) / decimal.Decimal(mw)
        elif unit_3 == "ng/mL" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 2)

        # 判断组合框3为"pg/mL"和组合框4的单位并执行相应的计算
        elif unit_3 == "pg/mL" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 12)
        elif unit_3 == "pg/mL" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 9)
        elif unit_3 == "pg/mL" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 6)
        elif unit_3 == "pg/mL" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 3)
        elif unit_3 == "pg/mL" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "pg/mL" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "pg/mL" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 10)
        elif unit_3 == "pg/mL" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -9) / decimal.Decimal(mw)
        elif unit_3 == "pg/mL" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6) / decimal.Decimal(mw)
        elif unit_3 == "pg/mL" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3) / decimal.Decimal(mw)
        elif unit_3 == "pg/mL" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(mw)
        elif unit_3 == "pg/mL" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3) / decimal.Decimal(mw)
        elif unit_3 == "pg/mL" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -1)

        # 判断组合框3为"fg/mL"和组合框4的单位并执行相应的计算
        elif unit_3 == "fg/mL" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 15)
        elif unit_3 == "fg/mL" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 12)
        elif unit_3 == "fg/mL" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 9)
        elif unit_3 == "fg/mL" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 6)
        elif unit_3 == "fg/mL" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 3)
        elif unit_3 == "fg/mL" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "fg/mL" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(10 ** 13)
        elif unit_3 == "fg/mL" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -12) / decimal.Decimal(mw)
        elif unit_3 == "fg/mL" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -9) / decimal.Decimal(mw)
        elif unit_3 == "fg/mL" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6) / decimal.Decimal(mw)
        elif unit_3 == "fg/mL" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3) / decimal.Decimal(mw)
        elif unit_3 == "fg/mL" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration) / decimal.Decimal(mw)
        elif unit_3 == "fg/mL" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -4)

        # 判断组合框3为"%"和组合框4的单位并执行相应的计算
        elif unit_3 == "%" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -2)
        elif unit_3 == "%" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 1)
        elif unit_3 == "%" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 4)
        elif unit_3 == "%" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 7)
        elif unit_3 == "%" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 10)
        elif unit_3 == "%" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 13)
        elif unit_3 == "%" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "%" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 1) / decimal.Decimal(mw)
        elif unit_3 == "%" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 4) / decimal.Decimal(mw)
        elif unit_3 == "%" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 7) / decimal.Decimal(mw)
        elif unit_3 == "%" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 10) / decimal.Decimal(mw)
        elif unit_3 == "%" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 13) / decimal.Decimal(mw)
        elif unit_3 == "%" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)

        # 判断组合框3为"M"和组合框4的单位并执行相应的计算
        elif unit_3 == "M" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 3)
        elif unit_3 == "M" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw)
        elif unit_3 == "M" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -3)
        elif unit_3 == "M" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -6)
        elif unit_3 == "M" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -9)
        elif unit_3 == "M" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -12)
        elif unit_3 == "M" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 1)
        elif unit_3 == "M" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "M" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "M" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif unit_3 == "M" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)
        elif unit_3 == "M" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 12)
        elif unit_3 == "M" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -8)

        # 判断组合框3为"mM"和组合框4的单位并执行相应的计算
        elif unit_3 == "mM" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 6)
        elif unit_3 == "mM" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 3)
        elif unit_3 == "mM" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw)
        elif unit_3 == "mM" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -3)
        elif unit_3 == "mM" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -6)
        elif unit_3 == "mM" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -9)
        elif unit_3 == "mM" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 4)
        elif unit_3 == "mM" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3)
        elif unit_3 == "mM" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "mM" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "mM" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif unit_3 == "mM" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 9)
        elif unit_3 == "mM" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -5)

        # 判断组合框3为"μM"和组合框4的单位并执行相应的计算
        elif unit_3 == "μM" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 9)
        elif unit_3 == "μM" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 6)
        elif unit_3 == "μM" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 3)
        elif unit_3 == "μM" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw)
        elif unit_3 == "μM" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -3)
        elif unit_3 == "μM" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -6)
        elif unit_3 == "μM" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 7)
        elif unit_3 == "μM" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6)
        elif unit_3 == "μM" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3)
        elif unit_3 == "μM" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "μM" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "μM" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 6)
        elif unit_3 == "μM" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -2)

        # 判断组合框3为"nM"和组合框4的单位并执行相应的计算
        elif unit_3 == "nM" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 12)
        elif unit_3 == "nM" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 9)
        elif unit_3 == "nM" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 6)
        elif unit_3 == "nM" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 3)
        elif unit_3 == "nM" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw)
        elif unit_3 == "nM" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** -3)
        elif unit_3 == "nM" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 10)
        elif unit_3 == "nM" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -9)
        elif unit_3 == "nM" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6)
        elif unit_3 == "nM" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3)
        elif unit_3 == "nM" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "nM" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 3)
        elif unit_3 == "nM" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 1)

        # 判断组合框3为"pM"和组合框4的单位并执行相应的计算
        elif unit_3 == "pM" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 15)
        elif unit_3 == "pM" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 12)
        elif unit_3 == "pM" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 9)
        elif unit_3 == "pM" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 6)
        elif unit_3 == "pM" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 3)
        elif unit_3 == "pM" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw)
        elif unit_3 == "pM" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 13)
        elif unit_3 == "pM" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -12)
        elif unit_3 == "pM" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -9)
        elif unit_3 == "pM" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -6)
        elif unit_3 == "pM" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -3)
        elif unit_3 == "pM" and unit_4 == "pM":
            self.variable = decimal.Decimal(concentration)
        elif unit_3 == "pM" and unit_4 == "ng/dL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(mw) / decimal.Decimal(10 ** 4)

        # 判断组合框3为"ng/dL"和组合框4的单位并执行相应的计算
        elif unit_3 == "ng/dL" and unit_4 == "g/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -11)
        elif unit_3 == "ng/dL" and unit_4 == "mg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -8)
        elif unit_3 == "ng/dL" and unit_4 == "μg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -5)
        elif unit_3 == "ng/dL" and unit_4 == "ng/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -2)
        elif unit_3 == "ng/dL" and unit_4 == "pg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 1)
        elif unit_3 == "ng/dL" and unit_4 == "fg/mL":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 4)
        elif unit_3 == "ng/dL" and unit_4 == "%":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -9)
        elif unit_3 == "ng/dL" and unit_4 == "M":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -8) / decimal.Decimal(mw)
        elif unit_3 == "ng/dL" and unit_4 == "mM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -5) / decimal.Decimal(mw)
        elif unit_3 == "ng/dL" and unit_4 == "μM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** -2) / decimal.Decimal(mw)
        elif unit_3 == "ng/dL" and unit_4 == "nM":
            self.variable = decimal.Decimal(concentration) * decimal.Decimal(10 ** 1) / decimal.Decimal(mw)
        elif unit_3 == "ng/dL" and unit_4 == "pM":
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