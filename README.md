# Desktop Organizer

This Python script organizes your desktop by categorizing and moving files into specific folders based on their types. It creates a folder named "DesktopOrganizer" on your desktop and organizes files into subfolders like documents, images, and others.

## How to Use

1. Clone or download this repository to your local machine.
2. Make sure you have Python installed on your system.
3. Run the `desktop_organizer.py` script.
4. The script will create a folder named "DesktopOrganizer" on your desktop and organize files accordingly.

## Folder Structure

- `DesktopOrganizer/`: The main folder created by the script.
  - `Alles/`: Contains all files that don't fit into the predefined categories.
  - `Documents/`: Contains document files (pdf, docx, etc.).
  - `Images/`: Contains image files (png, jpg, etc.).
  - `Videos/`: Contains video files (mp4, mkv, etc.).
  - ... (Additional folders for other file types)

## Note

- The script ignores its own file and the "DesktopOrganizer" folder.
- If a file type is not recognized, it will be moved to the "Alles" folder.

Feel free to customize the script or contribute to its improvement.

Happy organizing!

