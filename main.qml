import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 300
    height: 500
    title: "HelloApp"

    ColumnLayout {
        anchors.fill: parent
        spacing: 5
        RowLayout {
            spacing: 5
            Text {
                text: "hello world"
                color: "red"
            }

            Button {
                text: "Ok"
            }

            Button {
                text: "Cancel"
            }
        }

        RowLayout {
            Rectangle {
                color: "red"
                Layout.fillWidth: true
                Layout.fillHeight: true
            }

            Rectangle {
                color: "blue"
                Layout.fillWidth: true
                Layout.fillHeight: true
            }
        }

        RowLayout {
            Rectangle {
                color: "yellow"
                Layout.fillWidth: true
                Layout.fillHeight: true
            }

            Rectangle {
                color: "cyan"
                Layout.fillWidth: true
                Layout.fillHeight: true
            }
        }
    }
}