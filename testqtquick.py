import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine

def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    if len(sys.argv) == 2:
        qmlfile = sys.argv[1]
    else:
        qmlfile = 'qml/app1.qml'
    print("loading %s" % qmlfile)
    engine.load(qmlfile)
    app.exec()

main()
