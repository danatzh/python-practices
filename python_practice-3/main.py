import os
import csv
import json
import sys

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
class DataLoader:
    def __init__(self,filename):
        self.filename = filename
        self.students=[]
    def load(self):
        print("\nLoading data...")
        try:
            with open(self.filename, mode='r', encoding='utf-8') as f:
                self.students = list(csv.DictReader(f))
                print(f"Data loaded successfully: {len(self.students)} students")
                return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred during loading: {e}")
            return None
    def preview(self, n=5):
        print(f"\nFirst {n} rows: ")
        print("-"*30)
        for student in self.students[:n]:
            print(f'{student["student_id"]} | {student["age"]} | {student["gender"]} | {student["country"]} | GPA: {student["GPA"]}')
        print("-"*30)
class DataAnalyser:
    def __init__(self,students):
        self.students = students
        self.result=[]
    def analyse(self):
        gpas = []
        high_performers = 0
        for s in self.students:
            try:
                val = float(s['GPA'])
                gpas.append(val)
                if val > 3.5:
                    high_performers = high_performers + 1
            except ValueError:
                print(f"Warning: could not convert value for student {s.get('student_id', 'Unknown')} - skipping row.")
                continue
        avg_gpa = round(sum(gpas) / len(gpas), 2) if gpas else 0
        self.result= {"total_students": len(self.students),
                "average_gpa": avg_gpa,
                "max_gpa": max(gpas) if gpas else 0.0,
                "min_gpa": min(gpas) if gpas else 0.0,
                "high_performers": high_performers
                }
        return self.result
    def print_results(self):
        print("\n" + "-"*30)
        print("GPA Analysis")
        print("-"*30)
        print(f'Total students: {len(self.students)}')
        print(f'Average GPA: {self.result["average_gpa"]}')
        print(f'Highest GPA: {self.result["max_gpa"]}')
        print(f'Lowest GPA: {self.result["min_gpa"]}')
        print(f'Students GPA>3.5: {self.result["high_performers"]}')
        print("-"*30)
class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path
    def save_json(self):
        try:
            self.result["analysis"] = "GPA Statistics"
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"\nResult saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")
if __name__ == '__main__':
    fn = FileManager('students.csv')
    if not fn.check_file():
        print('Stopping program.')
        exit()
    fn.create_output_folder()
    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()
    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()
    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()
