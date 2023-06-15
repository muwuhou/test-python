import QtQuick 2.0
import QtQuick.Controls 2.0

ApplicationWindow {
    visible: true
    width: 200
    height: 200

    Rectangle {
        anchors.fill: parent

        ListModel {
            id: fruitModel
            ListElement {
                name: "banana"
                cost: "3.4"
            }
            ListElement {
                name: "apple"
                cost: "4.0"
            }
            ListElement {
                name: "orange"
                cost: "2.5"
            }
        }

        Component {
            id: fruitDelegate
            Row {
                spacing: 10
                Text { text: name }
                Text {
                    text: '$' + cost
                    color: "green"
                }
            }
        }

        ListView {
            anchors.fill: parent
            model: fruitModel
            delegate: fruitDelegate
        }
    }
}