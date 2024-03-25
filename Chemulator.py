# -*- coding:utf-8 -*-
import wx.lib.agw.gradientbutton as lib_gb
import wx.lib.buttons as lib_button
import wx,os,wx.adv
import tkinter as tk
from tkinter import messagebox


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='摩尔浓度换算', size=(1013, 643),name='frame',style=541072384)
        icon = wx.Icon(r'.\ICO\volumetric-flask.png')
        self.SetIcon(icon)
        self.Bind(wx.EVT_CLOSE, self.on_close)  # 绑定关闭事件
        self.启动窗口 = wx.Panel(self)
        self.启动窗口.SetOwnBackgroundColour((240, 240, 240, 255))
        self.Centre()
        self.variable = float(0)
        图文按钮3_图片 = wx.Image(r'.\ICO\left arrow.png').ConvertToBitmap()
        self.图文按钮3 = lib_button.ThemedGenBitmapTextButton(self.启动窗口, size=(35, 30), pos=(290, 344), bitmap=图文按钮3_图片,
                                                          label='', name='genbutton')
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
        self.超级列表框1 = wx.ListCtrl(self.启动窗口, size=(275, 490), pos=(6, 85), name='listCtrl', style=32)
        self.超级列表框1.AppendColumn('化合物', 0, 151)
        self.超级列表框1.AppendColumn('分子量', 0, 125)
        self.超级列表框1.Append([' ', ''])
        self.超级列表框1.Append(['', ''])
        超级列表框1_字体 = wx.Font(12, 70, 90, 400, False, '华文新魏', 28)
        self.超级列表框1.SetFont(超级列表框1_字体)
        # 创建字典来存储选中的化合物和分子量数据
        self.selected_data = {}
        self.超级列表框1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.超级列表框1_选中表项)
        self.超级列表框1.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.超级列表框1_取消选中表项)
        图片框3_图片 = wx.Image(r'.\ICO\folder.png').ConvertToBitmap()
        self.图片框3 = wx.StaticBitmap(self.启动窗口, bitmap=图片框3_图片,size=(32, 30),pos=(271, 19),name='staticBitmap',style=0)
        self.图片框3.Bind(wx.EVT_LEFT_DOWN,self.图片框3_鼠标左键按下)
        self.图片框3.SetToolTip("打开项目根目录")
        图文按钮2_图片 = wx.Image(r'.\ICO\right-arrow.png').ConvertToBitmap()
        self.图文按钮2 = lib_button.ThemedGenBitmapTextButton(self.启动窗口, size=(35, 30), pos=(291, 262), bitmap=图文按钮2_图片,
                                                          label='', name='genbutton')
        self.图文按钮2.SetToolTip("填入选中化合物")
        self.图文按钮2.Bind(wx.EVT_BUTTON, self.图文按钮2_按钮被单击)
        self.超级列表框2 = wx.ListCtrl(self.启动窗口, size=(650, 150), pos=(342, 425), name='listCtrl', style=1059)
        self.超级列表框2.AppendColumn('化合物', 0, 130)
        self.超级列表框2.AppendColumn('分子量', 0, 75)
        self.超级列表框2.AppendColumn('数值', 0, 110)
        self.超级列表框2.AppendColumn('原单位', 0, 100)
        self.超级列表框2.AppendColumn('=', 0, 22)
        self.超级列表框2.AppendColumn('数值', 0, 110)
        self.超级列表框2.AppendColumn('转化单位', 0, 100)
        超级列表框2_字体 = wx.Font(12, 74, 90, 400, False, '华文新魏', 28)
        self.超级列表框2.SetFont(超级列表框2_字体)
        self.超级列表框2.Bind(wx.EVT_LIST_ITEM_SELECTED, self.超级列表框2_选中表项)
        图文按钮5_图片 = wx.Image(r'.\ICO\plus.png').ConvertToBitmap()
        self.图文按钮5 = lib_button.ThemedGenBitmapTextButton(self.启动窗口, size=(30, 28), pos=(473, 19), bitmap=图文按钮5_图片,
                                                          label='', name='genbutton')
        self.图文按钮5.SetToolTip("创建项目文件")
        self.图文按钮5.Bind(wx.EVT_BUTTON, self.图文按钮5_按钮被单击)
        图文按钮L1_图片 = wx.Image(r'.\ICO\copy.png').ConvertToBitmap()
        self.图文按钮L1 = lib_gb.GradientButton(self.启动窗口,size=(66, 33),pos=(927, 390),bitmap=图文按钮L1_图片,label='Copy',name='gradientbutton')
        self.图文按钮L1.SetForegroundColour((255, 255, 255, 255))
        self.图文按钮L1.Bind(wx.EVT_BUTTON,self.图文按钮L1_按钮被单击)
        self.编辑框1 = wx.TextCtrl(self.启动窗口, size=(130, 28), pos=(344, 136), value='', name='text', style=256)
        编辑框1_字体 = wx.Font(12, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.编辑框1.SetFont(编辑框1_字体)
        self.标签1 = wx.StaticText(self.启动窗口,size=(92, 27),pos=(359, 102),label='化合物',name='staticText',style=2321)
        标签1_字体 = wx.Font(14,74,90,400,False,'华文新魏',28)
        self.标签1.SetFont(标签1_字体)
        self.编辑框3 = wx.TextCtrl(self.启动窗口,size=(130, 28),pos=(596, 136),value='',name='text',style=256)
        编辑框3_字体 = wx.Font(12,72,90,400,False,'Times New Roman',33)
        self.编辑框3.SetFont(编辑框3_字体)
        self.标签2 = wx.StaticText(self.启动窗口,size=(92, 27),pos=(615, 102),label='数值',name='staticText',style=2321)
        标签2_字体 = wx.Font(14,74,90,400,False,'华文新魏',28)
        self.标签2.SetFont(标签2_字体)
        self.标签3 = wx.StaticText(self.启动窗口,size=(92, 27),pos=(734, 102),label='原单位',name='staticText',style=2321)
        标签3_字体 = wx.Font(14,74,90,400,False,'华文新魏',28)
        self.标签3.SetFont(标签3_字体)
        self.标签4 = wx.StaticText(self.启动窗口,size=(92, 27),pos=(864, 102),label='转化单位',name='staticText',style=2321)
        标签4_字体 = wx.Font(14,74,90,400,False,'华文新魏',28)
        self.标签4.SetFont(标签4_字体)
        self.标签5 = wx.StaticText(self.启动窗口, size=(92, 27), pos=(483, 103), label='分子量', name='staticText', style=2321)
        标签5_字体 = wx.Font(14, 74, 90, 400, False, '华文新魏', 28)
        self.标签5.SetFont(标签5_字体)
        self.编辑框4 = wx.TextCtrl(self.启动窗口, size=(110, 28), pos=(475, 136), value='', name='text', style=256)
        编辑框4_字体 = wx.Font(12, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.编辑框4.SetFont(编辑框4_字体)
        self.组合框3 = wx.ComboBox(self.启动窗口,value='',pos=(733, 137),name='comboBox',choices=['g/mL', 'mg/mL', 'µg/mL', 'ng/mL', 'pg/mL', 'fg/mL', '%', 'M', 'mM', 'µM', 'nM', 'pM'],style=16)
        self.组合框3.SetSize((120, 28))
        组合框3_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
        self.组合框3.SetFont(组合框3_字体)
        self.组合框4 = wx.ComboBox(self.启动窗口,value='',pos=(863, 138),name='comboBox',choices=['g/mL', 'mg/mL', 'µg/mL', 'ng/mL', 'pg/mL', 'fg/mL', '%', 'M', 'mM', 'µM', 'nM', 'pM'],style=16)
        self.组合框4.SetSize((120, 28))
        组合框4_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
        self.组合框4.SetFont(组合框4_字体)
        self.编辑框7 = wx.TextCtrl(self.启动窗口, size=(593, 32), pos=(342, 262), value='', name='text', style=16)
        编辑框7_字体 = wx.Font(12, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.编辑框7.SetFont(编辑框7_字体)
        图文按钮6_图片 = wx.Image(r'.\ICO\down.png').ConvertToBitmap()
        self.图文按钮6 = lib_button.ThemedGenBitmapTextButton(self.启动窗口, size=(35, 32), pos=(934, 262), bitmap=图文按钮6_图片,
                                                          label='', name='genbutton')
        self.图文按钮6.SetToolTip("结果移入历史数据")
        self.图文按钮6.Bind(wx.EVT_BUTTON, self.图文按钮6_按钮被单击)
        self.图文按钮L2 = lib_gb.GradientButton(self.启动窗口,size=(100, 32),pos=(341, 229),bitmap=None,label='计算结果',name='gradientbutton')
        图文按钮L2_字体 = wx.Font(12,74,90,400,False,'华文新魏',28)
        self.图文按钮L2.SetFont(图文按钮L2_字体)
        self.图文按钮L2.SetForegroundColour((255, 255, 255, 255))
        self.图文按钮L3 = lib_gb.GradientButton(self.启动窗口,size=(101, 32),pos=(341, 394),bitmap=None,label='历史记录',name='gradientbutton')
        图文按钮L3_字体 = wx.Font(12,74,90,400,False,'华文新魏',28)
        self.图文按钮L3.SetFont(图文按钮L3_字体)
        self.图文按钮L3.SetForegroundColour((255, 255, 255, 255))
        图文按钮7_图片 = wx.Image(r'.\ICO\plus.png').ConvertToBitmap()
        self.图文按钮7 = lib_button.ThemedGenBitmapTextButton(self.启动窗口, size=(30, 28), pos=(317, 138), bitmap=图文按钮7_图片,
                                                          label='', name='genbutton')
        self.图文按钮7.SetToolTip("新增化合物到项目")
        self.图文按钮7.Bind(wx.EVT_BUTTON, self.图文按钮7_按钮被单击)
        self.组合框5 = wx.ComboBox(self.启动窗口, value='3', pos=(899, 234), name='comboBox',
                                choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', ''], style=16)
        self.组合框5.SetSize((36, 25))
        组合框5_字体 = wx.Font(11, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.组合框5.SetFont(组合框5_字体)
        self.组合框5.Bind(wx.EVT_COMBOBOX, self.组合框5_选中列表项)
        self.标签6 = wx.StaticText(self.启动窗口, size=(192, 24), pos=(708, 238), label='设置计算结果的小数位数：', name='staticText',
                                 style=2321)
        标签6_字体 = wx.Font(12, 70, 90, 400, False, '华文新魏', 28)
        self.标签6.SetFont(标签6_字体)
        图文按钮9_图片 = wx.Image(r'.\ICO\refresh.png').ConvertToBitmap()
        self.图文按钮9 = lib_button.ThemedGenBitmapTextButton(self.启动窗口, size=(28, 26), pos=(502, 20), bitmap=图文按钮9_图片,
                                                          label='', name='genbutton')
        self.图文按钮9.Bind(wx.EVT_BUTTON, self.图文按钮9_按钮被单击)
        self.图文按钮9.SetToolTip("刷新项目文件")

        # 在初始化方法中添加事件绑定
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框1)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框4)
        self.Bind(wx.EVT_TEXT, self.更新编辑框7内容, self.编辑框3)
        self.Bind(wx.EVT_COMBOBOX, self.更新编辑框7内容, self.组合框3)
        self.Bind(wx.EVT_COMBOBOX, self.更新编辑框7内容, self.组合框4)

    def 图文按钮3_按钮被单击(self, event):
        # Clear the data in 编辑框1, 编辑框4, 编辑框3, 组合框3, and 组合框4
        self.编辑框1.SetValue('')
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
        self.超级列表框1.AppendColumn('化合物', 0, 151)
        self.超级列表框1.AppendColumn('分子量', 0, 125)

        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.strip().split('\t')  # 使用制表符作为分隔符
                self.超级列表框1.Append([data[0], data[1]])


    def refresh_folder_names(self):
        project_dir = "./Project"  # 替换为实际的 "Project" 目录路径
        folder_names = os.listdir(project_dir)
        self.组合框2.Set(folder_names)

    def 超级列表框1_选中表项(self, event):
        selected_index = self.超级列表框1.GetFirstSelected()  # 获取选中的第一个表项的索引

        while selected_index != -1:
            compound_name = self.超级列表框1.GetItemText(selected_index)
            molecular_weight = self.超级列表框1.GetItemText(selected_index, 1)

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

    def 图片框3_鼠标左键按下(self, event):
        directory_path = "./Project"
        os.system(f'explorer {os.path.abspath(directory_path)}')


    def 图文按钮2_按钮被单击(self, event):
        # Get the selected compound name and molecular weight from 超级列表框1
        selected_index = self.超级列表框1.GetFirstSelected()
        if selected_index != -1:
            compound_name = self.超级列表框1.GetItemText(selected_index)
            molecular_weight = self.超级列表框1.GetItemText(selected_index, 1)

            # Set the compound name and molecular weight in 编辑框1 and 编辑框4
            self.编辑框1.SetValue(compound_name)
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

                # 刷新Combobox的选项
                self.refresh_folder_names()

                wx.MessageBox("文件夹和文件已成功创建！", "成功", wx.OK | wx.ICON_INFORMATION)

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
        compound_name = self.编辑框1.GetValue()
        conversion_unit = self.组合框4.GetValue()
        data_value = self.编辑框3.GetValue()
        data_unit = self.组合框3.GetValue()
        molecular_weight = self.编辑框4.GetValue()

        variable = self.variable  # 引用self.variable中的variable
        # 获取选中列表项的数值并转换为整数
        selected_value = int(self.组合框5.GetValue())

        # 设置保留指定位数的小数
        variable = float(variable)
        variable = round(variable, selected_value)

        if str(variable) != "0.0":
            # 填充超级列表框2的内容
            self.超级列表框2.Append(
                [compound_name, molecular_weight, data_value, data_unit, "=", variable, conversion_unit])
        else:
            wx.MessageBox("没有正确计算结果", "提示", wx.OK | wx.ICON_INFORMATION)

    def 图文按钮7_按钮被单击(self, event):
        compound_name = self.编辑框1.GetValue()
        data_value = self.编辑框4.GetValue()

        # 拼接要写入文件的内容
        content = compound_name + "\t" + data_value

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

    def 更新编辑框7内容(self, event):
        compound_name = self.编辑框1.GetValue()
        molecular_weight = self.组合框4.GetValue()
        data_value = self.编辑框3.GetValue()
        data_unit = self.组合框3.GetValue()

        # 获取选中列表项的数值
        selected_value = float(self.组合框5.GetValue())

        # 调用单位计算过程函数来计算variable变量的值
        self.单位计算过程(event)
        # 添加变量的声明和初始化
        variable = self.variable

        # 获取选中列表项的数值并转换为整数
        selected_value = int(self.组合框5.GetValue())

        # 设置保留指定位数的小数
        variable = float(variable)
        variable = round(variable, selected_value)
        # print(variable)

        result = " ".join([compound_name, "：", data_value, data_unit, "=", "{:.{}f}".format(variable, selected_value), molecular_weight])
        self.编辑框7.SetValue(result)

    def 组合框5_选中列表项(self, event):
        self.更新编辑框7内容(event)

    def 单位计算过程(self, event):
        # 获取组合框3和组合框4当前选中的单位
        unit_3 = self.组合框3.GetValue()
        unit_4 = self.组合框4.GetValue()

        concentration_str = self.编辑框3.GetValue()
        if concentration_str == '':
            concentration = float(0)  # 设置一个默认值
        else:
            concentration = float(concentration_str)

        mw_str = self.编辑框4.GetValue()
        if mw_str == '':
            mw = float(1)   # 设置一个默认值
        else:
            mw = float(mw_str)

        # 判断组合框3为"g/mL"和组合框4的单位并执行相应的计算
        if unit_3 == "g/mL" and unit_4 == "g/mL":
            self.variable = float(concentration)
        elif unit_3 == "g/mL" and unit_4 == "mg/mL":
            self.variable = float(concentration) * (10 ** 3)
        elif unit_3 == "g/mL" and unit_4 == "µg/mL":
            self.variable = float(concentration) * (10 ** 6)
        elif unit_3 == "g/mL" and unit_4 == "ng/mL":
            self.variable = float(concentration) * (10 ** 9)
        elif unit_3 == "g/mL" and unit_4 == "pg/mL":
            self.variable = float(concentration) * (10 ** 12)
        elif unit_3 == "g/mL" and unit_4 == "fg/mL":
            self.variable = float(concentration) * (10 ** 15)
        elif unit_3 == "g/mL" and unit_4 == "%":
            self.variable = float(concentration) * (10 ** 2)
        elif unit_3 == "g/mL" and unit_4 == "M":
            self.variable = float(concentration) * (10 ** 3) / float(mw)
        elif unit_3 == "g/mL" and unit_4 == "mM":
            self.variable = float(concentration) * (10 ** 6) / float(mw)
        elif unit_3 == "g/mL" and unit_4 == "µM":
            self.variable = float(concentration) * (10 ** 9) / float(mw)
        elif unit_3 == "g/mL" and unit_4 == "nM":
            self.variable = float(concentration) * (10 ** 12) / float(mw)
        elif unit_3 == "g/mL" and unit_4 == "pM":
            self.variable = float(concentration) * (10 ** 15) / float(mw)

        # 判断组合框3为"mg/mL"和组合框4的单位并执行相应的计算
        elif unit_3 == "mg/mL" and unit_4 == "g/mL":
            self.variable = float(concentration) / (10 ** 3)
        elif unit_3 == "mg/mL" and unit_4 == "mg/mL":
            self.variable = float(concentration)
        elif unit_3 == "mg/mL" and unit_4 == "µg/mL":
            self.variable = float(concentration) * (10 ** 3)
        elif unit_3 == "mg/mL" and unit_4 == "ng/mL":
            self.variable = float(concentration) * (10 ** 6)
        elif unit_3 == "mg/mL" and unit_4 == "pg/mL":
            self.variable = float(concentration) * (10 ** 9)
        elif unit_3 == "mg/mL" and unit_4 == "fg/mL":
            self.variable = float(concentration) * (10 ** 12)
        elif unit_3 == "mg/mL" and unit_4 == "%":
            self.variable = float(concentration) / (10 ** 1)
        elif unit_3 == "mg/mL" and unit_4 == "M":
            self.variable = float(concentration) / float(mw)
        elif unit_3 == "mg/mL" and unit_4 == "mM":
            self.variable = float(concentration) * (10 ** 3) / float(mw)
        elif unit_3 == "mg/mL" and unit_4 == "µM":
            self.variable = float(concentration) * (10 ** 6) / float(mw)
        elif unit_3 == "mg/mL" and unit_4 == "nM":
            self.variable = float(concentration) * (10 ** 9) / float(mw)
        elif unit_3 == "mg/mL" and unit_4 == "pM":
            self.variable = float(concentration) * (10 ** 12) / float(mw)

        # 判断组合框3为"µg/mL"和组合框4的单位并执行相应的计算
        elif unit_3 == "µg/mL" and unit_4 == "g/mL":
            self.variable = float(concentration) / (10 ** 6)
        elif unit_3 == "µg/mL" and unit_4 == "mg/mL":
            self.variable = float(concentration) / (10 ** 3)
        elif unit_3 == "µg/mL" and unit_4 == "µg/mL":
            self.variable = float(concentration)
        elif unit_3 == "µg/mL" and unit_4 == "ng/mL":
            self.variable = float(concentration) * (10 ** 3)
        elif unit_3 == "µg/mL" and unit_4 == "pg/mL":
            self.variable = float(concentration) * (10 ** 6)
        elif unit_3 == "µg/mL" and unit_4 == "fg/mL":
            self.variable = float(concentration) * (10 ** 9)
        elif unit_3 == "µg/mL" and unit_4 == "%":
            self.variable = float(concentration) / (10 ** 4)
        elif unit_3 == "µg/mL" and unit_4 == "M":
            self.variable = float(concentration) * (10 ** -3) / float(mw)
        elif unit_3 == "µg/mL" and unit_4 == "mM":
            self.variable = float(concentration) / float(mw)
        elif unit_3 == "µg/mL" and unit_4 == "µM":
            self.variable = float(concentration) * (10 ** 3) / float(mw)
        elif unit_3 == "µg/mL" and unit_4 == "nM":
            self.variable = float(concentration) * (10 ** 6) / float(mw)
        elif unit_3 == "µg/mL" and unit_4 == "pM":
            self.variable = float(concentration) * (10 ** 9) / float(mw)

        # 判断组合框3为"ng/mL"和组合框4的单位并执行相应的计算
        elif unit_3 == "ng/mL" and unit_4 == "g/mL":
            self.variable = float(concentration) / (10 ** 9)
        elif unit_3 == "ng/mL" and unit_4 == "mg/mL":
            self.variable = float(concentration) / (10 ** 6)
        elif unit_3 == "ng/mL" and unit_4 == "µg/mL":
            self.variable = float(concentration) / (10 ** 3)
        elif unit_3 == "ng/mL" and unit_4 == "ng/mL":
            self.variable = float(concentration)
        elif unit_3 == "ng/mL" and unit_4 == "pg/mL":
            self.variable = float(concentration) * (10 ** 3)
        elif unit_3 == "ng/mL" and unit_4 == "fg/mL":
            self.variable = float(concentration) * (10 ** 6)
        elif unit_3 == "ng/mL" and unit_4 == "%":
            self.variable = float(concentration) / (10 ** 7)
        elif unit_3 == "ng/mL" and unit_4 == "M":
            self.variable = float(concentration) * (10 ** -6) / float(mw)
        elif unit_3 == "ng/mL" and unit_4 == "mM":
            self.variable = float(concentration) * (10 ** -3) / float(mw)
        elif unit_3 == "ng/mL" and unit_4 == "µM":
            self.variable = float(concentration)  / float(mw)
        elif unit_3 == "ng/mL" and unit_4 == "nM":
            self.variable = float(concentration) * (10 ** 3) / float(mw)
        elif unit_3 == "ng/mL" and unit_4 == "pM":
            self.variable = float(concentration) * (10 ** 6) / float(mw)

        # 判断组合框3为"pg/mL"和组合框4的单位并执行相应的计算
        elif unit_3 == "pg/mL" and unit_4 == "g/mL":
            self.variable = float(concentration) / (10 ** 12)
        elif unit_3 == "pg/mL" and unit_4 == "mg/mL":
            self.variable = float(concentration) / (10 ** 9)
        elif unit_3 == "pg/mL" and unit_4 == "µg/mL":
            self.variable = float(concentration) / (10 ** 6)
        elif unit_3 == "pg/mL" and unit_4 == "ng/mL":
            self.variable = float(concentration) / (10 ** 3)
        elif unit_3 == "pg/mL" and unit_4 == "pg/mL":
            self.variable = float(concentration)
        elif unit_3 == "pg/mL" and unit_4 == "fg/mL":
            self.variable = float(concentration) * (10 ** 3)
        elif unit_3 == "pg/mL" and unit_4 == "%":
            self.variable = float(concentration) / (10 ** 10)
        elif unit_3 == "pg/mL" and unit_4 == "M":
            self.variable = float(concentration) * (10 ** -9) / float(mw)
        elif unit_3 == "pg/mL" and unit_4 == "mM":
            self.variable = float(concentration) * (10 ** -6) / float(mw)
        elif unit_3 == "pg/mL" and unit_4 == "µM":
            self.variable = float(concentration) * (10 ** -3) / float(mw)
        elif unit_3 == "pg/mL" and unit_4 == "nM":
            self.variable = float(concentration) / float(mw)
        elif unit_3 == "pg/mL" and unit_4 == "pM":
            self.variable = float(concentration) * (10 ** 3) / float(mw)

        # 判断组合框3为"%"和组合框4的单位并执行相应的计算
        elif unit_3 == "%" and unit_4 == "g/mL":
            self.variable = float(concentration) * (10 ** -2)
        elif unit_3 == "%" and unit_4 == "mg/mL":
            self.variable = float(concentration) * (10 ** 1)
        elif unit_3 == "%" and unit_4 == "µg/mL":
            self.variable = float(concentration) * (10 ** 4)
        elif unit_3 == "%" and unit_4 == "ng/mL":
            self.variable = float(concentration) * (10 ** 7)
        elif unit_3 == "%" and unit_4 == "pg/mL":
            self.variable = float(concentration) * (10 ** 10)
        elif unit_3 == "%" and unit_4 == "fg/mL":
            self.variable = float(concentration) * (10 ** 13)
        elif unit_3 == "%" and unit_4 == "%":
            self.variable = float(concentration)
        elif unit_3 == "%" and unit_4 == "M":
            self.variable = float(concentration) * (10 ** 1) / float(mw)
        elif unit_3 == "%" and unit_4 == "mM":
            self.variable = float(concentration) * (10 ** 4) / float(mw)
        elif unit_3 == "%" and unit_4 == "µM":
            self.variable = float(concentration) * (10 ** 7) / float(mw)
        elif unit_3 == "%" and unit_4 == "nM":
            self.variable = float(concentration) * (10 ** 10) / float(mw)
        elif unit_3 == "%" and unit_4 == "pM":
            self.variable = float(concentration) * (10 ** 13) / float(mw)

        # 判断组合框3为"M"和组合框4的单位并执行相应的计算
        elif unit_3 == "M" and unit_4 == "g/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 3)
        elif unit_3 == "M" and unit_4 == "mg/mL":
            self.variable = float(concentration) * float(mw)
        elif unit_3 == "M" and unit_4 == "µg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** -3)
        elif unit_3 == "M" and unit_4 == "ng/mL":
            self.variable = float(concentration) * float(mw) / (10 ** -6)
        elif unit_3 == "M" and unit_4 == "pg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** -9)
        elif unit_3 == "M" and unit_4 == "fg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** -12)
        elif unit_3 == "M" and unit_4 == "%":
            self.variable = float(concentration) * float(mw) / (10 ** 1)
        elif unit_3 == "M" and unit_4 == "M":
            self.variable = float(concentration)
        elif unit_3 == "M" and unit_4 == "mM":
            self.variable = float(concentration) * (10 ** 3)
        elif unit_3 == "M" and unit_4 == "µM":
            self.variable = float(concentration) * (10 ** 6)
        elif unit_3 == "M" and unit_4 == "nM":
            self.variable = float(concentration) * (10 ** 9)
        elif unit_3 == "M" and unit_4 == "pM":
            self.variable = float(concentration) * (10 ** 12)

        # 判断组合框3为"mM"和组合框4的单位并执行相应的计算
        elif unit_3 == "mM" and unit_4 == "g/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 6)
        elif unit_3 == "mM" and unit_4 == "mg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 3)
        elif unit_3 == "mM" and unit_4 == "µg/mL":
            self.variable = float(concentration) * float(mw)
        elif unit_3 == "mM" and unit_4 == "ng/mL":
            self.variable = float(concentration) * float(mw) / (10 ** -3)
        elif unit_3 == "mM" and unit_4 == "pg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** -6)
        elif unit_3 == "mM" and unit_4 == "fg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** -9)
        elif unit_3 == "mM" and unit_4 == "%":
            self.variable = float(concentration) * float(mw) / (10 ** 4)
        elif unit_3 == "mM" and unit_4 == "M":
            self.variable = float(concentration) * (10 ** -3)
        elif unit_3 == "mM" and unit_4 == "mM":
            self.variable = float(concentration)
        elif unit_3 == "mM" and unit_4 == "µM":
            self.variable = float(concentration) * (10 ** 3)
        elif unit_3 == "mM" and unit_4 == "nM":
            self.variable = float(concentration) * (10 ** 6)
        elif unit_3 == "mM" and unit_4 == "pM":
            self.variable = float(concentration) * (10 ** 9)

        # 判断组合框3为"µM"和组合框4的单位并执行相应的计算
        elif unit_3 == "µM" and unit_4 == "g/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 9)
        elif unit_3 == "µM" and unit_4 == "mg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 6)
        elif unit_3 == "µM" and unit_4 == "µg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 3)
        elif unit_3 == "µM" and unit_4 == "ng/mL":
            self.variable = float(concentration) * float(mw)
        elif unit_3 == "µM" and unit_4 == "pg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** -3)
        elif unit_3 == "µM" and unit_4 == "fg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** -6)
        elif unit_3 == "µM" and unit_4 == "%":
            self.variable = float(concentration) * float(mw) / (10 ** 7)
        elif unit_3 == "µM" and unit_4 == "M":
            self.variable = float(concentration) * (10 ** -6)
        elif unit_3 == "µM" and unit_4 == "mM":
            self.variable = float(concentration) * (10 ** -3)
        elif unit_3 == "µM" and unit_4 == "µM":
            self.variable = float(concentration)
        elif unit_3 == "µM" and unit_4 == "nM":
            self.variable = float(concentration) * (10 ** 3)
        elif unit_3 == "µM" and unit_4 == "pM":
            self.variable = float(concentration) * (10 ** 6)

        # 判断组合框3为"nM"和组合框4的单位并执行相应的计算
        elif unit_3 == "nM" and unit_4 == "g/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 12)
        elif unit_3 == "nM" and unit_4 == "mg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 9)
        elif unit_3 == "nM" and unit_4 == "µg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 6)
        elif unit_3 == "nM" and unit_4 == "ng/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 3)
        elif unit_3 == "nM" and unit_4 == "pg/mL":
            self.variable = float(concentration) * float(mw)
        elif unit_3 == "nM" and unit_4 == "fg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** -3)
        elif unit_3 == "nM" and unit_4 == "%":
            self.variable = float(concentration) * float(mw) / (10 ** 10)
        elif unit_3 == "nM" and unit_4 == "M":
            self.variable = float(concentration) * (10 ** -9)
        elif unit_3 == "nM" and unit_4 == "mM":
            self.variable = float(concentration) * (10 ** -6)
        elif unit_3 == "nM" and unit_4 == "µM":
            self.variable = float(concentration) * (10 ** -3)
        elif unit_3 == "nM" and unit_4 == "nM":
            self.variable = float(concentration)
        elif unit_3 == "nM" and unit_4 == "pM":
            self.variable = float(concentration) * (10 ** 3)

        # 判断组合框3为"pM"和组合框4的单位并执行相应的计算
        elif unit_3 == "pM" and unit_4 == "g/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 15)
        elif unit_3 == "pM" and unit_4 == "mg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 12)
        elif unit_3 == "pM" and unit_4 == "µg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 9)
        elif unit_3 == "pM" and unit_4 == "ng/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 6)
        elif unit_3 == "pM" and unit_4 == "pg/mL":
            self.variable = float(concentration) * float(mw) / (10 ** 3)
        elif unit_3 == "pM" and unit_4 == "fg/mL":
            self.variable = float(concentration) * float(mw)
        elif unit_3 == "pM" and unit_4 == "%":
            self.variable = float(concentration) * float(mw) / (10 ** 13)
        elif unit_3 == "pM" and unit_4 == "M":
            self.variable = float(concentration) * (10 ** -12)
        elif unit_3 == "pM" and unit_4 == "mM":
            self.variable = float(concentration) * (10 ** -9)
        elif unit_3 == "pM" and unit_4 == "µM":
            self.variable = float(concentration) * (10 ** -6)
        elif unit_3 == "pM" and unit_4 == "nM":
            self.variable = float(concentration) * (10 ** -3)
        elif unit_3 == "pM" and unit_4 == "pM":
            self.variable = float(concentration)

        else:
            # 如果组合框3和组合框4的单位不匹配，可以定义一个默认值或提示错误信息
            self.variable = float(0)

    def 图文按钮9_按钮被单击(self,event):
        # 刷新Combobox的选项
        self.refresh_folder_names()

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