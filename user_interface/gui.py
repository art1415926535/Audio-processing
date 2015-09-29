# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import user_interface.icons


class UiForm(object):
    def __init__(self, form):
        form.setObjectName("Form")
        form.resize(1004, 565)
        form.setMinimumSize(QtCore.QSize(1004, 565))
        form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("RobotoDraft,Helvetica Neue,Helvetica,Arial")
        form.setFont(font)
        form.setMouseTracking(False)
        form.setStyleSheet("background-color:#ddd;\n"
                           "font-family: RobotoDraft, \'Helvetica Neue\', Helvetica, Arial;")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(form)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(5, 4, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.track_slider = QtWidgets.QSlider(form)
        self.track_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                        "background: #777;\n"
                                        "height: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::add-page:horizontal {\n"
                                        "background: #eee;\n"
                                        "height: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal {\n"
                                        "background: #bbb;\n"
                                        "width: 20px;\n"
                                        "height: 20px;\n"
                                        "margin-top: -8px;\n"
                                        "margin-bottom: -8px;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal:hover {\n"
                                        "background: #aaa;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::sub-page:horizontal:disabled {\n"
                                        "background: #eee;\n"
                                        "border-color: #999;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::add-page:horizontal:disabled {\n"
                                        "background: #eee;\n"
                                        "border-color: #999;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal:disabled {\n"
                                        "background: #eee;\n"
                                        "}")
        self.track_slider.setMaximum(100000)
        self.track_slider.setTracking(False)
        self.track_slider.setOrientation(QtCore.Qt.Horizontal)
        self.track_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.track_slider.setObjectName("track_slider")
        self.verticalLayout.addWidget(self.track_slider)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.center = QtWidgets.QHBoxLayout()
        self.center.setSpacing(8)
        self.center.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.center.setContentsMargins(5, 0, 5, 8)
        self.center.setObjectName("center")
        self.scrollArea = QtWidgets.QScrollArea(form)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(size_policy)
        self.scrollArea.setStyleSheet("QWidget{\n"
                                      "background: #ccc;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "    QScrollBar:vertical {\n"
                                      "        background: #fff;\n"
                                      "        width: 15px;\n"
                                      "    }\n"
                                      "    QScrollBar::handle:vertical {\n"
                                      "        background:rgba(38, 220, 214, 255);\n"
                                      "        min-height: 15px;\n"
                                      "    }\n"
                                      "    QScrollBar::add-line:vertical {\n"
                                      "        background: #fff;\n"
                                      "        height: 15px;\n"
                                      "    }\n"
                                      "    QScrollBar::sub-line:vertical {\n"
                                      "        background: #fff;\n"
                                      "        height: 15px;\n"
                                      "    }\n"
                                      "\n"
                                      "\n"
                                      "    QScrollBar:horizontal {\n"
                                      "        background: #fff;\n"
                                      "        height: 15px;\n"
                                      "    }\n"
                                      "    QScrollBar::handle:horizontal {\n"
                                      "        background: rgba(38, 220, 214, 255);\n"
                                      "        min-width: 15px;\n"
                                      "    }\n"
                                      "    QScrollBar::add-line:horizontal {\n"
                                      "        background: #fff;\n"
                                      "        width: 15px;\n"
                                      "    }\n"
                                      "    QScrollBar::sub-line:horizontal {\n"
                                      "        background: #fff;\n"
                                      "        width: 15px;\n"
                                      "    }\n"
                                      "")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 723, 526))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plots_layout = QtWidgets.QVBoxLayout()
        self.plots_layout.setSpacing(5)
        self.plots_layout.setContentsMargins(-1, 0, 0, -1)
        self.plots_layout.setObjectName("plots_layout")
        self.verticalLayout_2.addLayout(self.plots_layout)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacer_item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.center.addWidget(self.scrollArea)
        self.editors = QtWidgets.QVBoxLayout()
        self.editors.setSpacing(8)
        self.editors.setContentsMargins(-1, -1, -1, 0)
        self.editors.setObjectName("editors")
        self.horizontalWidget_3 = QtWidgets.QWidget(form)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.horizontalWidget_3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_3.setSizePolicy(size_policy)
        self.horizontalWidget_3.setStyleSheet("QWidget{\n"
                                              "background: #f6f6f6;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "    background: rgba(255,255,255,255)\n"
                                              "}")
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.play_pause_button = QtWidgets.QPushButton(self.horizontalWidget_3)
        self.play_pause_button.setEnabled(False)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.play_pause_button.sizePolicy().hasHeightForWidth())
        self.play_pause_button.setSizePolicy(size_policy)
        self.play_pause_button.setMinimumSize(QtCore.QSize(46, 0))
        font = QtGui.QFont()
        font.setFamily("RobotoDraft,Helvetica Neue,Helvetica,Arial")
        self.play_pause_button.setFont(font)
        self.play_pause_button.setAutoFillBackground(False)
        self.play_pause_button.setStyleSheet("/*\n"
                                             "border: none;\n"
                                             "width: 100px;\n"
                                             "height: 25px;\n"
                                             "background-color: rgb(210, 210, 210);\n"
                                             "*/\n"
                                             "\n"
                                             "\n"
                                             "border: none;")
        self.play_pause_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/color/ic_play_circle_fill_color_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pause_button.setIcon(icon)
        self.play_pause_button.setIconSize(QtCore.QSize(30, 30))
        self.play_pause_button.setAutoRepeat(False)
        self.play_pause_button.setObjectName("play_pause_button")
        self.horizontalLayout_3.addWidget(self.play_pause_button)
        self.open_file_button = QtWidgets.QPushButton(self.horizontalWidget_3)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.open_file_button.sizePolicy().hasHeightForWidth())
        self.open_file_button.setSizePolicy(size_policy)
        self.open_file_button.setMinimumSize(QtCore.QSize(46, 30))
        font = QtGui.QFont()
        font.setFamily("RobotoDraft,Helvetica Neue,Helvetica,Arial")
        self.open_file_button.setFont(font)
        self.open_file_button.setStyleSheet("color: #555;\n"
                                            "border: none;")
        self.open_file_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/folder_open_grey/ic_folder_open_grey600_48dp.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.open_file_button.setIcon(icon1)
        self.open_file_button.setIconSize(QtCore.QSize(30, 30))
        self.open_file_button.setObjectName("open_file_button")
        self.horizontalLayout_3.addWidget(self.open_file_button)
        self.time_of_track_label = QtWidgets.QPushButton(self.horizontalWidget_3)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.time_of_track_label.sizePolicy().hasHeightForWidth())
        self.time_of_track_label.setSizePolicy(size_policy)
        self.time_of_track_label.setMinimumSize(QtCore.QSize(85, 0))
        font = QtGui.QFont()
        font.setFamily("RobotoDraft,Helvetica Neue,Helvetica,Arial")
        font.setPointSize(12)
        self.time_of_track_label.setFont(font)
        self.time_of_track_label.setStyleSheet("\n"
                                               "QPushButton{\n"
                                               "  color: #555;\n"
                                               "  height: 26px;\n"
                                               "  width: 60px;\n"
                                               "  border: none;\n"
                                               "  padding-left: -20px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "  background: rgba(255,255,255,0)\n"
                                               "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/time/ic_access_time_gray_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.time_of_track_label.setIcon(icon2)
        self.time_of_track_label.setIconSize(QtCore.QSize(30, 30))
        self.time_of_track_label.setObjectName("time_of_track_label")
        self.horizontalLayout_3.addWidget(self.time_of_track_label)
        spacer_item_1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacer_item_1)
        spacer_item_2 = QtWidgets.QSpacerItem(0, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacer_item_2)
        self.editors.addWidget(self.horizontalWidget_3)
        self.horizontalWidget_31 = QtWidgets.QWidget(form)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.horizontalWidget_31.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_31.setSizePolicy(size_policy)
        self.horizontalWidget_31.setStyleSheet("QWidget{\n"
                                               "background: #f6f6f6;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "    background: rgba(255,255,255,255)\n"
                                               "}")
        self.horizontalWidget_31.setObjectName("horizontalWidget_31")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget_31)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.perform_algorithm_button = QtWidgets.QPushButton(self.horizontalWidget_31)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.perform_algorithm_button.sizePolicy().hasHeightForWidth())
        self.perform_algorithm_button.setSizePolicy(size_policy)
        self.perform_algorithm_button.setMinimumSize(QtCore.QSize(46, 0))
        self.perform_algorithm_button.setStyleSheet("color: #555;\n"
                                                    "height: 26px;\n"
                                                    "border: none;\n"
                                                    "")
        self.perform_algorithm_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/play_circle_fill_black/ic_play_circle_fill_black_48dp.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.perform_algorithm_button.setIcon(icon3)
        self.perform_algorithm_button.setIconSize(QtCore.QSize(30, 30))
        self.perform_algorithm_button.setObjectName("perform_algorithm_button")
        self.horizontalLayout_4.addWidget(self.perform_algorithm_button)
        self.new_code_button = QtWidgets.QPushButton(self.horizontalWidget_31)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.new_code_button.sizePolicy().hasHeightForWidth())
        self.new_code_button.setSizePolicy(size_policy)
        self.new_code_button.setMinimumSize(QtCore.QSize(46, 0))
        self.new_code_button.setStyleSheet("color: #555;\n"
                                           "height: 26px;\n"
                                           "border: none;")
        self.new_code_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/color/ic_note_add_color_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_code_button.setIcon(icon4)
        self.new_code_button.setIconSize(QtCore.QSize(30, 30))
        self.new_code_button.setObjectName("new_code_button")
        self.horizontalLayout_4.addWidget(self.new_code_button)
        self.open_code_button = QtWidgets.QPushButton(self.horizontalWidget_31)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.open_code_button.sizePolicy().hasHeightForWidth())
        self.open_code_button.setSizePolicy(size_policy)
        self.open_code_button.setMinimumSize(QtCore.QSize(46, 0))
        self.open_code_button.setStyleSheet("QPushButton{\n"
                                            "  color: #555 ;\n"
                                            "  height: 26px;\n"
                                            "  border: none;\n"
                                            "}")
        self.open_code_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/open/ic_folder_grey600_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_code_button.setIcon(icon5)
        self.open_code_button.setIconSize(QtCore.QSize(30, 30))
        self.open_code_button.setObjectName("open_code_button")
        self.horizontalLayout_4.addWidget(self.open_code_button)
        self.save_code_button = QtWidgets.QPushButton(self.horizontalWidget_31)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.save_code_button.sizePolicy().hasHeightForWidth())
        self.save_code_button.setSizePolicy(size_policy)
        self.save_code_button.setMinimumSize(QtCore.QSize(46, 0))
        self.save_code_button.setStyleSheet("color: #555;\n"
                                            "height: 26px;\n"
                                            "border: none;\n"
                                            "")
        self.save_code_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/save/ic_save_grey600_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_code_button.setIcon(icon6)
        self.save_code_button.setIconSize(QtCore.QSize(30, 30))
        self.save_code_button.setObjectName("save_code_button")
        self.horizontalLayout_4.addWidget(self.save_code_button)
        self.del_code_button = QtWidgets.QPushButton(self.horizontalWidget_31)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.del_code_button.sizePolicy().hasHeightForWidth())
        self.del_code_button.setSizePolicy(size_policy)
        self.del_code_button.setMinimumSize(QtCore.QSize(46, 0))
        self.del_code_button.setStyleSheet("QPushButton{\n"
                                           "  color: #555 ;\n"
                                           "  height: 26px;\n"
                                           "  border: none;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "Url: url(:/color/ic_delete_color_48dp_hover.png);\n"
                                           "}")
        self.del_code_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/color/ic_delete_color_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_code_button.setIcon(icon7)
        self.del_code_button.setIconSize(QtCore.QSize(30, 30))
        self.del_code_button.setObjectName("del_code_button")
        self.horizontalLayout_4.addWidget(self.del_code_button)
        spacer_item_3 = QtWidgets.QSpacerItem(1, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacer_item_3)
        self.editors.addWidget(self.horizontalWidget_31)
        self.layout_for_QCodeEdit = QtWidgets.QVBoxLayout()
        self.layout_for_QCodeEdit.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layout_for_QCodeEdit.setObjectName("layout_for_QCodeEdit")
        self.choice_algorithm_box = QtWidgets.QComboBox(form)
        font = QtGui.QFont()
        font.setFamily("RobotoDraft,Helvetica Neue,Helvetica,Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.choice_algorithm_box.setFont(font)
        self.choice_algorithm_box.setStyleSheet("QComboBox\n"
                                                "{\n"
                                                "    background: #f6f6f6;\n"
                                                "    border: none;\n"
                                                "    color: #333;\n"
                                                "    height: 25px;\n"
                                                "}\n"
                                                "\n"
                                                "QComboBox QListView::item:selected\n"
                                                "{\n"
                                                "    border-style: none;\n"
                                                "    background-color: #ccc;\n"
                                                "}\n"
                                                "\n"
                                                "QComboBox::drop-down\n"
                                                "{\n"
                                                "    width: 20px;\n"
                                                "    border-style: none;\n"
                                                "    height: 25px;\n"
                                                "}\n"
                                                "")
        self.choice_algorithm_box.setMaxVisibleItems(20)
        self.choice_algorithm_box.setMinimumContentsLength(0)
        self.choice_algorithm_box.setIconSize(QtCore.QSize(30, 30))
        self.choice_algorithm_box.setModelColumn(0)
        self.choice_algorithm_box.setObjectName("choice_algorithm_box")
        self.layout_for_QCodeEdit.addWidget(self.choice_algorithm_box)
        self.editors.addLayout(self.layout_for_QCodeEdit)
        self.center.addLayout(self.editors)
        self.center.setStretch(0, 8)
        self.center.setStretch(1, 2)
        self.verticalLayout_4.addLayout(self.center)

        self.translate_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def translate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Beat Beat Beat"))
