class Report:
    def __init__(self, result):
        self.result = result

    def generate(self):
        print("\n=== FINAL REPORT ===")
        print(f"Analysis completed for {self.result.get('total_students')} students.")
        print(f"Average GPA across group: {self.result.get('average_gpa')}")
        print("====================\n")