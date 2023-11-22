import os
import shutil
from pathlib import Path

def create_desktop_organize_folder():
    desktop_path = Path.home() / "Desktop"
    organize_folder_path = desktop_path / "DesktopOrganizer"

    # Überprüfen, ob der Ordner bereits existiert, andernfalls erstellen
    if not organize_folder_path.is_dir():
        organize_folder_path.mkdir()
        print(f"Der Ordner '{organize_folder_path}' wurde erstellt.")

    return organize_folder_path

def organize_desktop(desktop_folder, organize_folder):
    # Alle Dateien und Ordner auf dem Desktop auswählen
    all_files = [file for file in desktop_folder.iterdir()]

    # Ordner für verschiedene Dateitypen erstellen
    file_type_folders = {}

    for file in all_files:
        # Ignoriere das aktuelle Skript und den Ordner "DesktopOrganizer"
        if file.name.lower() == "desktoporganizer.py" or file.name.lower() == "desktoporganizer":
            continue

        # Zielordner für die Datei
        destination_folder = organize_folder / file.suffix[1:].lower()

        # Zielordner für 'Alles'
        alles_folder = organize_folder / "Alles"

        try:
            # Versuche, die Datei in den entsprechenden Ordner zu verschieben
            shutil.move(file, destination_folder)
            print(f"Die Datei '{file.name}' wurde in '{destination_folder}' verschoben.")
        except FileNotFoundError:
            # Falls die Datei nicht gefunden wird, verschiebe sie in 'Alles'
            shutil.move(file, alles_folder)
            print(f"Die Datei '{file.name}' wurde in '{alles_folder}' verschoben.")
        except IsADirectoryError:
            # Falls es sich um einen Ordner handelt, verschiebe ihn in 'Alles'
            shutil.move(file, alles_folder)
            print(f"Der Ordner '{file.name}' wurde in '{alles_folder}' verschoben.")
        except Exception as e:
            print(f"Fehler beim Verschieben der Datei '{file.name}': {e}")

    print(f"Desktop wurde organisiert! Dateien befinden sich in '{organize_folder}'.")

def main():
    # Desktop-Ordner
    desktop_folder = Path.home() / "Desktop"

    # Ordner für die Desktop-Organisation erstellen oder abrufen
    organize_folder = create_desktop_organize_folder()

    # Desktop organisieren
    organize_desktop(desktop_folder, organize_folder)

if __name__ == "__main__":
    main()
