import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 200
    height: 200

    ColumnLayout {
        anchors.fill: parent
        spacing: 5

        RowLayout {
            ColorChangingButton {
                index: 0
                Layout.fillWidth: true
                Layout.fillHeight: true
            }

            ColorChangingButton {
                index: 1
                Layout.fillWidth: true
                Layout.fillHeight: true
            }
        }

        RowLayout {
            ColorChangingButton {
                index: 2
                Layout.fillWidth: true
                Layout.fillHeight: true
            }

            ColorChangingButton {
                index: 3
                Layout.fillWidth: true
                Layout.fillHeight: true
            }
        }
    }
}