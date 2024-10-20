import os
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from constants import *

class BlenderManager:
    """Class to handle versions and related"""
    
    def __init__(self):
        """Stores Blender versions"""
        self.versions = {
        }
        self.find_existing_versions()

    def add_version(self, folder_path):
        """Adds a new Blender version to version dict"""
        tail, version_name = os.path.split(folder_path)
        if tail == BLENDER_FOUNDATION_PATH:
            exe_path = os.path.join(folder_path, "blender.exe").replace("\\", "/")
            self.versions[version_name] = os.path.normpath(exe_path)
            return True
        else:
            return False
    
  

    def get_version_path(self, version_name):
        """Returns the executable path for a version"""
        return self.versions.get(version_name, None)

    def find_existing_versions(self):
        install_root_path = BLENDER_FOUNDATION_PATH
        #Check if blender_foundation folder evem exists
        if install_root_path:
            for folder in os.listdir(install_root_path):
                version_folder= os.path.join(install_root_path,folder).replace("\\", "/")
                if os.path.isdir(version_folder) and "blender.exe" in os.listdir(version_folder):
                    self.add_version(version_folder)
        else:
            messagebox.showinfo("No versions installed",text="You have no versions installed of Blender")
            

    def get_all_versions(self):
        """Returns all versions by keys, I.e versions"""

        return list(self.versions.keys())
    
