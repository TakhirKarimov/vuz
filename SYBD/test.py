import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

def foo():
    conn = sqlite3.connect('SYBD.db')
    cursor = conn.cursor()
    app = QApplication([])
    window = QMainWindow()
    tableWidget = QTableWidget()
    cursor.execute("""SELECT * FROM НИР INNER JOIN ВУЗы ON ВУЗы.код_ВУЗа = НИР.код_ВУЗа""")
    users = cursor.fetchall()
    tableWidget.setRowCount(len(users))
    tableWidget.setColumnCount(11)
    for i, user in enumerate(users):
        for j, value in enumerate(user):
            item = QTableWidgetItem(str(value))
            tableWidget.setItem(i, j, item)
    window.setCentralWidget(tableWidget)
    window.show()
    app.exec()

def filter_Save_func():
    conn = sqlite3.connect('SYBD.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM НИР INNER JOIN ВУЗы ON ВУЗы.код_ВУЗа = НИР.код_ВУЗа""")
    data = cursor.fetchall()

    tableWidget = QTableWidget()
    tableWidget.setRowCount(len(data))
    tableWidget.setColumnCount(11)
    for i, user in enumerate(data):
        for j, value in enumerate(user):
            item = QTableWidgetItem(str(value))
            tableWidget.setItem(i, j, item)
    window.setCentralWidget(tableWidget)
    window.show()

def filter_Save_func():
    data = request_for_filter()
    tableWidget = QTableWidget()
    tableWidget.setRowCount(len(data))
    tableWidget.setColumnCount(11)
    for i, user in enumerate(data):
        for j, value in enumerate(user):
            item = QTableWidgetItem(str(value))
            tableWidget.setItem(i, j, item)
    tableWidget.setHorizontalHeaderLabels(['код_ВУЗа', 'ВУЗ кратко', 'НТП', 'рег. номер', 'проект', 'код ГРНТИ', 'руководитель', 'должность рук.', 'налич. экспаната', 'выставка', 'назван экспаната'])
    overlay.setCentralWidget(tableWidget)
    overlay.show()
