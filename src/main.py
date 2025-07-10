import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from controllers

def main():
    # Create the application instance. QApplication manages application-wide resources and settings.
    app = QApplication(sys.argv)

    # Create a main window widget. QWidget is the base class for all user interface objects.
    window = QWidget()
    window.setWindowTitle('Hello PySide6 World!') # Set the window title

    # Create a vertical layout. QVBoxLayout arranges widgets vertically.
    layout = QVBoxLayout()
    window.setLayout(layout) # Apply the layout to the window

    # Create a label widget with the desired text. QLabel displays text or images.
    label = QLabel("Hello PySide6 World!")
    layout.addWidget(label) # Add the label to the layout

    # Display the window on the screen. By default, widgets are not shown until show() is called.
    window.show()

    # Start the application's event loop. This makes the application responsive to user interactions.
    # sys.exit() ensures a clean exit when the event loop terminates.
    sys.exit(app.exec())

if __name__ == "__main__":
    main()