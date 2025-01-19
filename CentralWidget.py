from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PyQt6.QtCore import QDateTime


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        # Layout und Textfeld
        self.layout = QVBoxLayout(self)
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)  # Nur lesbar machen
        self.layout.addWidget(self.text_edit)

        # Initialisiere die Datenverarbeitung
        self.file_path = "daten.txt"
        self.format_string = "yyyy-MM-ddThh:mm:ss"

        # Verarbeite die Datei und zeige die Ergebnisse an
        self.display_data()

    def display_data(self):
        try:
            # Datei öffnen und Zeilen lesen
            with open(self.file_path, "r") as file:
                lines = file.readlines()

            # Jede Zeile verarbeiten
            for line in lines:
                date_string = line.strip()  # Entferne Leerzeichen
                date_time = QDateTime.fromString(date_string, self.format_string)

                if date_time.isValid():
                    # Datum als String formatieren
                    output_string = date_time.toString(self.format_string)
                    parts = output_string.split("-")  # Zerlege den String an Bindestrichen

                    year = parts[0]  # Jahr
                    month = parts[1]  # Monat
                    day_time = parts[2]  # Tag und Uhrzeit (z. B. "17T14:30:00")

                    # Extrahiere den Tag und die Uhrzeit
                    day, time = day_time.split("T")

                    # Text ins Textfeld einfügen
                    self.text_edit.append(f"Jahr: {year}")
                    self.text_edit.append(f"Monat: {month}")
                    self.text_edit.append(f"Tag: {day}")
                    self.text_edit.append(f"Uhrzeit: {time}")
                    self.text_edit.append("")  # Leerzeile für Lesbarkeit
                else:
                    self.text_edit.append(f"Ungültiges Datum: {date_string}\n")

        except FileNotFoundError:
            self.text_edit.append(f"Die Datei {self.file_path} wurde nicht gefunden.\n")

        except Exception as e:
            self.text_edit.append(f"Ein Fehler ist aufgetreten: {e}\n")
