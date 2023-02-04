# Calculates number weeks pregnant and estimates due date
# by Emily Arnold 12/2021

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5.QtCore import QDate, QSize

from datetime import date, datetime, timedelta
import calendar
import os

class CalendarDemo(qtw.QWidget):
    global currentYear, currentMonth

    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    def __init__(self):
        super().__init__()
        self.calendar = qtw.QCalendarWidget(self)
        
             
    
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EDD Calculator")
        self.setGeometry(300, 300, 450, 600)
        self. setMinimumSize(500,500)
        self.setLayout(qtw.QVBoxLayout())
       
        self.uiComponents()

        self.show()

 
    def uiComponents(self):

        # Instruction Label        
        my_label = qtw.QLabel("Choose a Calculation Method:")
        my_label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)

        # Combo Box
        my_combo =qtw.QComboBox(self,
            editable = False
            )
        my_combo.setFont(qtg.QFont('Helvetica',20))
        my_combo.addItem("Last Menstural Period")
        my_combo.addItem("Conception Date")
        my_combo.addItem("Estimated Due Date")
        self.layout().addWidget(my_combo)

        #date widget
        calendarWid = CalendarDemo()        
        calendarWid.setFixedSize(QSize(400, 300))
        
        self.layout().addWidget(calendarWid)

        # button
        my_button = qtw.QPushButton("PRESS",
            clicked = lambda: pressed())
        self.layout().addWidget(my_button)
       
        # combo label
        combo_label= qtw.QLabel()
        combo_label.setText("")
        combo_label.setWordWrap(True)
        combo_label.setFont(qtg.QFont('Helvetica', 14))
        self.layout().addWidget(combo_label)

                       
        def pressed():
            qDate = calendarWid.calendar.selectedDate()
            calcType =my_combo.currentText()
            now = qDate.currentDate()
           # 280 days in a 40 week gestation
            if calcType == "Last Menstural Period":
                dayOfYear = qDate.dayOfYear()
                edd = dayOfYear + 280
                year = qDate.year()
                start_date = date(int(year), 1, 1)
                estDueDate = start_date + timedelta(days = int(edd)-1)
                eDD = estDueDate.strftime("%m/%d/%Y")

                # Calculate Weeks gestation
                weeks = int(qDate.daysTo(now)/7)
                combo_label.setText(f'Based on your LMP, your estimated due date is {eDD}.{os.linesep}You are {weeks} weeks pregnant.')
                
            elif calcType == "Conception Date":
                dayOfYear = qDate.dayOfYear()
                edd = dayOfYear + 266
                year = qDate.year()
                start_date = date(int(year), 1, 1)
                estDueDate = start_date + timedelta(days = int(edd)-1)
                eDD = estDueDate.strftime("%m/%d/%Y")
               
                # Calculate Weeks gestation
                weeks = int((qDate.daysTo(now)+14)/7)
                combo_label.setText(f'Based on your conception date, your estimated due date is {eDD}.{os.linesep}You are {weeks} weeks pregnant.')
                       
            else:
                edd_format = '{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year())
                # Calculate Weeks gestation
                weeks = int(40-(now.daysTo(qDate)/7))
                combo_label.setText(f'Your estimated due date is {edd_format}.{os.linesep}You are {weeks} weeks pregnant.')

           
            
# create app
app = qtw.QApplication([])
#create instance of window
mw = MainWindow()
# start app
app.exec_()