# Steven Hunt
# CST 205 - Multimedia and Design
# 04.16.17

# ----------------------------------------------------------------------------

import calendar
from datetime import *

# Birthday: 05.21.1987

def birthDate(): 

  # 1:
  birthDay = 21
  birthMonth = 05
  birthYear = 1987
  
  # 2:
  nextBday = date(2017,birthMonth,birthDay)
  today = date.today()
  
  # 3: 
  DOI = date(1776,07,04)
  
  # Display: 
  print '\n',calendar.month(birthYear,birthMonth)
  print 'Next birthday is ', (nextBday - today), 'away.'
  print 'The Declaration of Independence was ratified by the Continental Congress on a', calendar.day_name[DOI.weekday()], '.'
