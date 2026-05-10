#test_analyse_twice (tests.test_analyser.TestGpaAnalyser.test_analyse_twice) ... ok
#test_result_has_required_keys (tests.test_analyser.TestGpaAnalyser.test_result_has_required_keys) ... ok
#test_result_is_not_empty (tests.test_analyser.TestGpaAnalyser.test_result_is_not_empty) ... ok
#test_total_students (tests.test_analyser.TestGpaAnalyser.test_total_students) ... ok
#
#----------------------------------------------------------------------
#Ran 4 tests in 0.000s
#
#OK

import unittest
from analytics.analyser import GpaAnalyser

class TestGpaAnalyser(unittest.TestCase):

    def setUp(self):
        self.sample = [
            {"student_id": "1", "GPA": "3.8", "age": "20", "gender": "M", "country": "USA"},
            {"student_id": "2", "GPA": "2.5", "age": "21", "gender": "F", "country": "India"},
            {"student_id": "3", "GPA": "3.9", "age": "19", "gender": "M", "country": "USA"},
            {"student_id": "4", "GPA": "1.8", "age": "22", "gender": "F", "country": "Canada"},
            {"student_id": "5", "GPA": "3.5", "age": "20", "gender": "M", "country": "India"},
        ]

    def test_result_is_not_empty(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)

    def test_result_has_required_keys(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        required_keys = ["average_gpa", "max_gpa", "min_gpa", "high_performers"]
        for key in required_keys:
            self.assertIn(key, analyser.result)

    def test_analyse_twice(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        result1 = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, result1)

if __name__ == '__main__':
    unittest.main()