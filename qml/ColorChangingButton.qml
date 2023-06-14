import QtQuick
import QtQuick.Controls

// This defines a type ColorChangingButton
Rectangle {
    property int index: 0
    property list<string> colors: ["red", "blue", "green", "yellow"]
    color: colors[index % colors.length]

    MouseArea {
        anchors.fill: parent
        onClicked: { parent.index++ }
    }
}