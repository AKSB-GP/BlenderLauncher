# Blender Launcher App

A app using Python Tkinter to manage multiple Blender versions. With this launcher, you can select, launch, add, remove, and manage Blender installations.

---

## Features

**Select and Launch a Blender Version**  
  Choose a Blender version from the dropdown menu and launch it directly.

**Open a Version's Folder**  
  Open the folder of the selected Blender version. 

**Add a New Version**  
  Add a new Blender version by selecting its folder. Select the "Blender VERSIONNUMBER" folder to add it to the launcher

**Remove a Version**  
  Remove a version from the launcher by selecting a version and pressing the remove button. 

**Download a Version**  
  -Access Blender's official download page to add a version

---

## Getting Started

### Prerequisites
**Python 3.12.7**  
- Project is tested on Python 3.12.7
**Pyinstaller**  
- Project is using Pyinstaller to create the .exe

---

## Installation

### 1. Clone repo
- Clone the project.

### 2. Setup a python environment
- Open the project in an environment of your choose and setup Python related prerequistes. 

### 3. Add a settings.json file
- Launcher uses a json to keep track of Blender versions.

- A settings.json file has the following structure:
```
{
    "blender_versions": {
        "Blender 4.3": "C:/Program Files/Blender Foundation/Blender 4.3\\blender.exe"
    }
}
```

### 4. Create a constants python file
- Stores constants used in the launcher.

- Content of a constants file:
```python
BLENDER_FOUNDATION_PATH = "C:/Program Files/Blender Foundation"
BLENDER_DOWNLOAD_URL = "https://www.blender.org/download/"
SETTINGS = "settings.json"
```

 ### 5. Create .exe:
- In the root project run the following pyinstaller cmd to create the .exe:
```
pyinstaller --onefile --icon="Launcher_icon.ico" --noconsole app.py
```
