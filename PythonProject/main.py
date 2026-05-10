from analytics import FileManager, DataLoader, ResultSaver, Report, GpaAnalyser
import sys

def main():
    input_file = 'students.csv'
    output_file = 'output/result.json'
    fm = FileManager(input_file)
    if not fm.check_file():
        sys.exit()
    fm.create_output_folder()
    dl = DataLoader(input_file)
    data = dl.load()
    if data:
        dl.preview()
        analyser = GpaAnalyser(data)
        result = analyser.analyse()
        analyser.print_results()
        saver = ResultSaver(result, output_file)
        saver.save_json()
        rep = Report(result)
        rep.generate()
if __name__ == "__main__":
    main()