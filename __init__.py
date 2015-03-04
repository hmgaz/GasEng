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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "gas Engineering" 
def description():
  return "Zooms to a point when the user hits the button."
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "2.0"
def classFactory(iface): 
  # load GasEng class from file GasEng
  from GasEng import GasEng 
  return GasEng(iface)
