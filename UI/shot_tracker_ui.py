# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shot_tracker.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QTreeView, QVBoxLayout,
    QWidget)

class Ui_shot_tracker(object):
    def setupUi(self, shot_tracker):
        if not shot_tracker.objectName():
            shot_tracker.setObjectName(u"shot_tracker")
        shot_tracker.resize(1099, 380)
        self.centralwidget = QWidget(shot_tracker)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(13)
        self.centralwidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tree_view = QTreeView(self.centralwidget)
        self.tree_view.setObjectName(u"tree_view")
        font1 = QFont()
        font1.setPointSize(12)
        self.tree_view.setFont(font1)

        self.verticalLayout.addWidget(self.tree_view)

        shot_tracker.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(shot_tracker)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1099, 20))
        shot_tracker.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(shot_tracker)
        self.statusbar.setObjectName(u"statusbar")
        shot_tracker.setStatusBar(self.statusbar)

        self.retranslateUi(shot_tracker)

        QMetaObject.connectSlotsByName(shot_tracker)
    # setupUi

    def retranslateUi(self, shot_tracker):
        shot_tracker.setWindowTitle(QCoreApplication.translate("shot_tracker", u"Shot Tracker", None))
    # retranslateUi

