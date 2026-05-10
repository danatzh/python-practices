import os

class FileManager:
    def __init__(self,filename):
        self.filename = filename
    def check_file(self):
        print("Checking file...")
        exists=os.path.exists(self.filename)
        if exists:
            print(f"File found: {self.filename}")
        else:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
        return exists
    def create_output_folder(self, folder='output'):
        print("\nCreating output file...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")