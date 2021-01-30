#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
   Author :        xdong@wandtec.com
   date：          2021/1/30
   Change Activity:
                   2021/1/30:
"""
from enum import Enum


class SPIcon(Enum):

    """
    定义Qt内置SP icon的枚举类型，搬运工，共71个
    """
    SP_ArrowBack = 54
    SP_ArrowDown = 51
    SP_ArrowForward = 55
    SP_ArrowLeft = 52
    SP_ArrowRight = 53
    SP_ArrowUp = 50
    SP_BrowserReload = 59
    SP_BrowserStop = 60
    SP_CommandLink = 57
    SP_ComputerIcon = 15
    SP_CustomBase = -268435456
    SP_DesktopIcon = 13
    SP_DialogAbortButton = 74
    SP_DialogApplyButton = 45
    SP_DialogCancelButton = 40
    SP_DialogCloseButton = 44
    SP_DialogDiscardButton = 47
    SP_DialogHelpButton = 41
    SP_DialogIgnoreButton = 76
    SP_DialogNoButton = 49
    SP_DialogNoToAllButton = 72
    SP_DialogOkButton = 39
    SP_DialogOpenButton = 42
    SP_DialogResetButton = 46
    SP_DialogRetryButton = 75
    SP_DialogSaveAllButton = 73
    SP_DialogSaveButton = 43
    SP_DialogYesButton = 48
    SP_DialogYesToAllButton = 71
    SP_DirClosedIcon = 22
    SP_DirHomeIcon = 56
    SP_DirIcon = 38
    SP_DirLinkIcon = 23
    SP_DirLinkOpenIcon = 24
    SP_DirOpenIcon = 21
    SP_DockWidgetCloseButton = 8
    SP_DriveCDIcon = 18
    SP_DriveDVDIcon = 19
    SP_DriveFDIcon = 16
    SP_DriveHDIcon = 17
    SP_DriveNetIcon = 20
    SP_FileDialogBack = 37
    SP_FileDialogContentsView = 35
    SP_FileDialogDetailedView = 33
    SP_FileDialogEnd = 30
    SP_FileDialogInfoView = 34
    SP_FileDialogListView = 36
    SP_FileDialogNewFolder = 32
    SP_FileDialogStart = 29
    SP_FileDialogToParent = 31
    SP_FileIcon = 25
    SP_FileLinkIcon = 26
    SP_LineEditClearButton = 70
    SP_MediaPause = 63
    SP_MediaPlay = 61
    SP_MediaSeekBackward = 67
    SP_MediaSeekForward = 66
    SP_MediaSkipBackward = 65
    SP_MediaSkipForward = 64
    SP_MediaStop = 62
    SP_MediaVolume = 68
    SP_MediaVolumeMuted = 69
    SP_MessageBoxCritical = 11
    SP_MessageBoxInformation = 9
    SP_MessageBoxQuestion = 12
    SP_MessageBoxWarning = 10
    SP_RestoreDefaultsButton = 77
    SP_TitleBarCloseButton = 3
    SP_TitleBarContextHelpButton = 7
    SP_TitleBarMaxButton = 2
    SP_TitleBarMenuButton = 0
    SP_TitleBarMinButton = 1
    SP_TitleBarNormalButton = 4
    SP_TitleBarShadeButton = 5
    SP_TitleBarUnshadeButton = 6
    SP_ToolBarHorizontalExtensionButton = 27
    SP_ToolBarVerticalExtensionButton = 28
    SP_TrashIcon = 14
    SP_VistaShield = 58



class Color(Enum):
    # 为序列值指定value值
    red = 1
    green = 2
    blue = 3

# #调用枚举成员的 3 种方式
# print(Color.red)
# print(Color['red'])
# print(Color(1))
# #调取枚举成员中的 value 和 name
# print(Color.red.value)
# print(Color.red.name)
# #遍历枚举类中所有成员的 2 种方式
# for color in Color:
#     print(color)