from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QDateTime

class CentralWidget(QWidget):


    # Pfad zur Textdatei
    file_path = "daten.txt"

    # Format des Datumsstrings
    format_string = "yyyy-MM-ddThh:mm:ss"

    # Öffne die Datei und lese die Zeilen
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Verarbeite jede Zeile
        for line in lines:
            date_string = line.strip()  # Entferne führende/trailende Leerzeichen
            date_time = QDateTime.fromString(date_string, format_string)

            if date_time.isValid():
                # Konvertiere das Datum in einen String und teile es auf
                output_string = date_time.toString(format_string)
                parts = output_string.split("-")  # Zerlege den String an den Bindestrichen

                year = parts[0]  # Jahr
                month = parts[1]  # Monat
                day_time = parts[2]  # Tag und Uhrzeit (z. B. "17T14:30:00")

                # Extrahiere den Tag und die Uhrzeit
                day, time = day_time.split("T")

                print("Jahr:", year)  # Ausgabe: z.B. 2025
                print("Monat:", month)  # Ausgabe: z.B. 01
                print("Tag:", day)  # Ausgabe: z.B. 17
                print("Uhrzeit:", time)  # Ausgabe: z.B. 14:30:00
            else:
                print(f"Ungültiges Datum: {date_string}")

    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
