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
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui 
from Ui_GasEng import Ui_GasEng
# create the dialog for GasEng
class GasEngDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_GasEng ()
    self.ui.setupUi(self)