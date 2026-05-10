import csv

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