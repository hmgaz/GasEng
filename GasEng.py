# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name			 	 : gas Engineering
Description          : Zooms to a point when the user hits the button.
Date                 : 03/Mar/15 
copyright            : (C) 2015 by Vasiliy Denisov
email                : vden@hmgaz.ru 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   T# -*- coding: utf-8 -*-his program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *

import os.path, sys
# Initialize Qt resources from file resources.py
import resources

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/tools'))


# Import the code for the dialog
from GasEngDialog import GasEngDialog
from argparse import Action

class GasEng:
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
    
    def initGui(self):
        # Добовляем пункт меню "ГАЗ сети"
        self.menu = QMenu()
        self.menu.setTitle(u"ГАЗ сети")
        
        # Добовляем в меню "ГАЗ сети" под меню "ПТО"
        self.ptoMenu = QMenu()
        self.ptoMenu.setTitle(u"ПТО")
        self.gaseng_pto2 = QAction(u"ПТО2", self.iface.mainWindow())
        self.gaseng_pto3 = QAction(u"ПТО3", self.iface.mainWindow())
        self.ptoMenu.addActions([self.gaseng_pto2, self.gaseng_pto3])
        self.menu.addMenu(self.ptoMenu)
        
        #Активизируем меню
        menu_bar = self.iface.mainWindow().menuBar()
        actions = menu_bar.actions()
        lastAction = actions[len( actions ) - 4]
        menu_bar.insertMenu(lastAction, self.menu)
        
        #Связь меню (действия) с функциями
        QObject.connect(self.gaseng_pto2, SIGNAL("triggered()"), self.run)
        QObject.connect(self.gaseng_pto3, SIGNAL("triggered()"), self.run)
    
    
    def unload(self):
        # Действия при выгрузке расширения
        #Удаляем пунты меню
        for every in self.menu.actions():
            del every
        #Удаляем меню
        del self.menu
        
    
    # run method that performs all the real work
    def run(self):
        # create and show the dialog
        dlg = GasEngDialog()
        # show the dialog
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass 
