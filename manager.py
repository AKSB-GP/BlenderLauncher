import os
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from constants import *
import json
class BlenderManager:
    """Class to handle versions"""
    SETTINGS_FILE = SETTINGS
    
    def __init__(self):
        """Stores Blender versions"""
        self.versions = {
        }
        self.load_settings()

    def load_settings(self):
        '''Load the settings json'''
        if os.path.exists(self.SETTINGS_FILE):
            with open(self.SETTINGS_FILE,"r") as file:
                settings = json.load(file)
                self.versions = settings.get("blender_versions",{})
        else:
             self.versions = {}   
             
    def save_settings(self):
        '''Save versions to settings json'''
        with open(self.SETTINGS_FILE, "w") as file:
            json.dump({"blender_versions":self.versions},file,indent=4)

    def add_version(self, folder_path):
        """
        Adds a new Blender version to version dict, 
        by selecting the blender version folder
        """
        version_name = os.path.basename(folder_path)
        blender_executable = os.path.join(folder_path, "blender.exe")

        if os.path.exists(blender_executable):
            self.versions[version_name] = blender_executable
            self.save_settings()
            return True
        return False

    def remove_version(self,version_name):
        '''Remove a version from json based on the version_name'''
        if version_name in self.versions:
            del self.versions[version_name]
            self.save_settings()
            return True
        return False
    
    def get_version_path(self, version):
        """Returns the executable path for a version"""
        return self.versions.get(version)

    def get_all_versions(self):
        """Returns all versions by keys, I.e versions"""
        return list(self.versions.keys())
    
