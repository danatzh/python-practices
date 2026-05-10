class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        pass

class GpaAnalyser(DataAnalyser):
    def analyse(self):
        gpas = []
        high_performers = 0
        for s in self.students:
            try:
                val = float(s['GPA'])
                gpas.append(val)
                if val > 3.5:
                    high_performers += 1
            except (ValueError, KeyError):
                continue

        avg_gpa = round(sum(gpas) / len(gpas), 2) if gpas else 0
        self.result = {
            "total_students": len(self.students),
            "average_gpa": avg_gpa,
            "max_gpa": max(gpas) if gpas else 0.0,
            "min_gpa": min(gpas) if gpas else 0.0,
            "high_performers": high_performers
        }
        return self.result

    def print_results(self):
        print("\n" + "-" * 30)
        print("GPA Analysis")
        print("-" * 30)
        print(f'Total students: {len(self.students)}')
        print(f'Average GPA: {self.result.get("average_gpa")}')
        print("\nLambda / Map / Filter")
        print("-" * 30)
        top_students = list(filter(lambda s: float(s['GPA']) > 3.8, self.students))
        gpa_list = list(map(lambda s: float(s['GPA']), self.students))
        print(f"GPA > 3.8 : {len(top_students)}")
        print(f"GPA values (first 5) : {gpa_list[:5]}")
        print("-" * 30)