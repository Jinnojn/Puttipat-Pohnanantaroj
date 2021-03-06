# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(659, 541)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 90, 571, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignRight)
        self.label.text
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("1"))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_eq = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.math_it())
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.gridLayout.addWidget(self.pushButton_eq, 4, 2, 1, 1)
        self.pushButton_Clear = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("Clear"))
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.gridLayout.addWidget(self.pushButton_Clear, 0, 0, 1, 1)
        self.pushButton_Del = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.remove_it(""))
        self.pushButton_Del.setObjectName("pushButton_Del")
        self.gridLayout.addWidget(self.pushButton_Del, 0, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("2"))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("0"))
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 4, 0, 1, 1)
        self.pushButton_dec = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.dot_it("."))
        self.pushButton_dec.setObjectName("pushButton_dec")
        self.gridLayout.addWidget(self.pushButton_dec, 4, 1, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("+"))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 4, 3, 1, 1)
        self.pushButton_min = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("-"))
        self.pushButton_min.setObjectName("pushButton_min")
        self.gridLayout.addWidget(self.pushButton_min, 3, 3, 1, 1)
        self.pushButton_times = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("*"))
        self.pushButton_times.setObjectName("pushButton_times")
        self.gridLayout.addWidget(self.pushButton_times, 2, 3, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("/"))
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 1, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("3"))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("4"))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("5"))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("6"))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("7"))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("8"))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget, clicked= lambda: self.press_it("9"))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def remove_it(self):
        screen = self.label.text()
        screen = screen[:-1]
        self.label.setText(screen)

    def math_it(self):
        screen = self.label.text()
        try:
            answer = eval(screen)
            self.label.setText(str(answer))
        except:
            self.label.setText("ERROR")


    def dot_it(self, pressed):
        screen = self.label.text()
        if screen[-1] == ".":
            pass
        else:
            self.label.setText(f'{screen}.')

    def press_it(self, pressed):
        if pressed == "Clear":
            self.label.setText("0")
        else:
            #check to see if start 0 and delete 0
            if self.label.text() == "0":
                self.label.setText("")
            # Concatenate the pressed button with what was there already
            self.label.setText(f'{self.label.text()}{pressed}')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "0"))
        self.pushButton.setText(_translate("Form", "1"))
        self.pushButton_eq.setText(_translate("Form", "="))
        self.pushButton_Clear.setText(_translate("Form", "Clear"))
        self.pushButton_Del.setText(_translate("Form", "Del"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.pushButton_dec.setText(_translate("Form", "."))
        self.pushButton_plus.setText(_translate("Form", "+"))
        self.pushButton_min.setText(_translate("Form", "-"))
        self.pushButton_times.setText(_translate("Form", "*"))
        self.pushButton_div.setText(_translate("Form", "/"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_9.setText(_translate("Form", "9"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
