import os
import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
import webbrowser
from manager import BlenderManager
from constants import *
from pathlib import Path

class BlenderLauncherApp:
    """Main App and its widgets"""
    def __init__(self, root):
        self.root = root
        self.root.title("Blender Launcher")
        self.root.iconbitmap("Launcher_icon.ico")
        self.root.geometry("400x400")
        self.root.configure(bg="darkgray")
        
        #Class Used to handle blender versions
        self.manager = BlenderManager()          
        
        #text for selected version, defaults to 'Select version'when launcher first runs
        self.selected_version = tk.StringVar(self.root)
        self.selected_version.set("Select version")
        self.starting_selection_text ="Select version"
        self.run_setup()

    def run_setup(self):
        '''Run setup methods'''
        #Render UI
        self.setup_styles()
        self.create_widgets()
        self.create_widgets()
        
        #Update dropdown for Blender versions
        self.update_dropdown()
        
    def setup_styles(self):
        """ Styling for widgets"""
        style = ttk.Style()
        style.configure("TButton", font=("Yu Gothic Medium", 14), background='black', foreground="black")
        style.configure("TLabel", font=("Yu Gothic Medium", 14),background='gray',foreground="red")
        style.configure("TMenubutton", font=("Yu Gothic Medium", 14), background='cyan', foreground="black")
        
    def create_widgets(self):
        """Create and position all widgets"""
        #the Dropdown for selecting  versions
        self.dropdown = ttk.OptionMenu(self.root, self.selected_version, "Select version", *self.manager.get_all_versions())
        self.dropdown.pack(pady=10, padx=10)
        self.dropdown.place(y=40, x=40)
        
        #the Launch button
        launch_button = ttk.Button(self.root, text="Start", command=self.launch_blender)
        launch_button.pack(pady=10, padx=10)
        launch_button.place(y=80, x=40)
       
        #the Open folder button
        folder_button = ttk.Button(self.root, text="Open Folder", command=self.open_folder)
        folder_button.pack(pady=10, padx=10)
        folder_button.place(y=120, x=40)
       
        #the version button
        add_button = ttk.Button(self.root, text="Add Version", command=self.add_version)
        add_button.pack(pady=10, padx=10)
        add_button.place(y=160, x=40)
      
        #the Download button
        download_button = ttk.Button(self.root, text="Download a version", command=self.open_download_link)
        download_button.pack(pady=10, padx=10)
        download_button.place(y=200,x=40)
      
        #The remove version button:        
        remove_button = ttk.Button(self.root, text="Remove version", command=self.remove_version)
        remove_button.pack(pady=10, padx=10)
        remove_button.place(y=240, x=40)
        
    """-----------------------Methods used in interactions----------------------------"""
      
    def open_download_link(self):
        """Opens the link to the blender.org download page"""
        webbrowser.open_new_tab(BLENDER_DOWNLOAD_URL)

    def add_version(self):
        """Prompts user to open a folder for the version they want to add"""
        folder_select = filedialog.askdirectory(initialdir=BLENDER_FOUNDATION_PATH)
        
        #updates dropdown to include added version
        if self.manager.add_version(folder_select):
            self.update_dropdown()
        if "blender" not in folder_select.lower() or "blender foundation" not in folder_select.lower():
            messagebox.showerror("Invalid folder selected", "Folder doesnt contain blender or blender foundation in the filepath, aborting...'")
        
    def remove_version(self):
        """Removes version from launcher, note! it does not remove from computer"""
        version = self.selected_version.get()
       
        #if version is the starting selection text 
        if version ==self.starting_selection_text:
            messagebox.showwarning("No version selected",text="Please select a version to delete")
            return
        confirmation = messagebox.askyesno("Remove Blender Version", f"Are you sure you want to remove {version}?")
        
        #if user confirms, remove version
        if confirmation:
            if self.manager.remove_version(version):
                self.selected_version.set(self.starting_selection_text)
                self.update_dropdown()
            else:
                messagebox.showinfo("Version not found",text="Version was not found, maybe it has already been deleted?")
   
    def update_dropdown(self):
        """Updates the dropdown menu to ensure all versions are shown"""
        menu = self.dropdown["menu"]
        menu.delete(0, "end")
        all_versions = self.manager.get_all_versions()
        
        #Check if there are any versions
        if not all_versions:
            self.selected_version.set("No version in launcher")
        if all_versions and self.selected_version.get() =="No version in launcher":
            self.selected_version.set(self.starting_selection_text)    
        for version in self.manager.get_all_versions():
            menu.add_command(label=version, command=lambda v=version: self.selected_version.set(v))

    def open_folder(self):
        """Opens the folder of the selected Blender version"""
        version = self.selected_version.get()
        if version == self.starting_selection_text:
            messagebox.showwarning("Warning", "Please select a version of Blender.")
            return
        path = Path(self.manager.get_version_path(version)).parent
        if path:
            subprocess.Popen(f'explorer "{path}"')
        else:
            messagebox.showerror("Invalid version selected", "You have selected an invalid Blender version.")

    def launch_blender(self):
        """Launches the selected Blender version"""
        version = self.selected_version.get()
       
        #Check if version selection is correct and launch blender based on path
        if version in self.manager.get_all_versions():
            path = self.manager.get_version_path(version)
            if path:
                try:
                    subprocess.Popen(path)
                    messagebox.showinfo("Launching", f"Launching Blender version {version}")
                except Exception as e:
                    messagebox.showerror("Failed to launch", f"Failed to launch Blender: {str(e)}")
                    return
            else:
                messagebox.showerror("Executable not found", "Executable not found for selected version. Double check that you have downloaded the version")
                return
        else:
            messagebox.showwarning("Warning", "Please select a valid Blender version.")
            return
    
if __name__ == "__main__":
    root = tk.Tk()
    app = BlenderLauncherApp(root)
    root.mainloop()
