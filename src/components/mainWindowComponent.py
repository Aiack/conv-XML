# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalGroupBox_4 = QtWidgets.QGroupBox(self.verticalGroupBox)
        self.horizontalGroupBox_4.setObjectName("horizontalGroupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit__local_certificado = QtWidgets.QLineEdit(self.horizontalGroupBox_4)
        self.lineEdit__local_certificado.setEnabled(False)
        self.lineEdit__local_certificado.setObjectName("lineEdit__local_certificado")
        self.horizontalLayout_5.addWidget(self.lineEdit__local_certificado)
        self.pushButton_local_certificado = QtWidgets.QPushButton(self.horizontalGroupBox_4)
        self.pushButton_local_certificado.setObjectName("pushButton_local_certificado")
        self.horizontalLayout_5.addWidget(self.pushButton_local_certificado)
        self.verticalLayout_2.addWidget(self.horizontalGroupBox_4)
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.verticalGroupBox)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_senha_certificado = QtWidgets.QLineEdit(self.horizontalGroupBox)
        self.lineEdit_senha_certificado.setEnabled(False)
        self.lineEdit_senha_certificado.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha_certificado.setObjectName("lineEdit_senha_certificado")
        self.horizontalLayout.addWidget(self.lineEdit_senha_certificado)
        self.verticalLayout_2.addWidget(self.horizontalGroupBox)
        self.verticalLayout.addWidget(self.verticalGroupBox)
        self.horizontalGroupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.horizontalGroupBox_2.setObjectName("horizontalGroupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_input_xml = QtWidgets.QLineEdit(self.horizontalGroupBox_2)
        self.lineEdit_input_xml.setEnabled(False)
        self.lineEdit_input_xml.setObjectName("lineEdit_input_xml")
        self.horizontalLayout_2.addWidget(self.lineEdit_input_xml)
        self.pushButton_input_xml = QtWidgets.QPushButton(self.horizontalGroupBox_2)
        self.pushButton_input_xml.setObjectName("pushButton_input_xml")
        self.horizontalLayout_2.addWidget(self.pushButton_input_xml)
        self.verticalLayout.addWidget(self.horizontalGroupBox_2)
        self.horizontalGroupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.horizontalGroupBox_3.setObjectName("horizontalGroupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_output_xml = QtWidgets.QLineEdit(self.horizontalGroupBox_3)
        self.lineEdit_output_xml.setEnabled(False)
        self.lineEdit_output_xml.setObjectName("lineEdit_output_xml")
        self.horizontalLayout_3.addWidget(self.lineEdit_output_xml)
        self.pushButton_output_xml = QtWidgets.QPushButton(self.horizontalGroupBox_3)
        self.pushButton_output_xml.setObjectName("pushButton_output_xml")
        self.horizontalLayout_3.addWidget(self.pushButton_output_xml)
        self.verticalLayout.addWidget(self.horizontalGroupBox_3)
        self.verticalGroupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox1.setObjectName("verticalGroupBox1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalGroupBox1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_exclud_xml = QtWidgets.QCheckBox(self.verticalGroupBox1)
        self.checkBox_exclud_xml.setObjectName("checkBox_exclud_xml")
        self.verticalLayout_4.addWidget(self.checkBox_exclud_xml)
        self.verticalLayout.addWidget(self.verticalGroupBox1)
        self.pushButton_process = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_process.setEnabled(False)
        self.pushButton_process.setObjectName("pushButton_process")
        self.verticalLayout.addWidget(self.pushButton_process)
        self.verticalGroupBox2 = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox2.setObjectName("verticalGroupBox2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plainTextEdit_log = QtWidgets.QPlainTextEdit(self.verticalGroupBox2)
        self.plainTextEdit_log.setReadOnly(True)
        self.plainTextEdit_log.setObjectName("plainTextEdit_log")
        self.verticalLayout_3.addWidget(self.plainTextEdit_log)
        self.verticalLayout.addWidget(self.verticalGroupBox2)
        self.progressBar = QtWidgets.QProgressBar(self.verticalGroupBox2)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 273, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conversor de XML"))
        self.verticalGroupBox.setTitle(_translate("MainWindow", "Certificado A1"))
        self.horizontalGroupBox_4.setTitle(_translate("MainWindow", "Local"))
        self.pushButton_local_certificado.setText(_translate("MainWindow", "Encontrar"))
        self.horizontalGroupBox.setTitle(_translate("MainWindow", "Senha"))
        self.horizontalGroupBox_2.setTitle(_translate("MainWindow", "Pasta de entrada do XML (Input)"))
        self.pushButton_input_xml.setText(_translate("MainWindow", "Encontrar"))
        self.horizontalGroupBox_3.setTitle(_translate("MainWindow", "Pasta de Saída do XML (Output)"))
        self.pushButton_output_xml.setText(_translate("MainWindow", "Encontrar"))
        self.verticalGroupBox1.setTitle(_translate("MainWindow", "Configurações"))
        self.checkBox_exclud_xml.setText(_translate("MainWindow", "Excluir XML processados"))
        self.pushButton_process.setText(_translate("MainWindow", "Processar"))
        self.verticalGroupBox2.setTitle(_translate("MainWindow", "Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
