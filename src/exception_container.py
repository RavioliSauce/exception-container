import traceback
import json
from datetime import datetime

class ExceptionContainer:
    def __init__(self):
        self.exceptions = []

    def clear_exceptions(self):
        self.exceptions.clear()

    def add_exception(self, e):
        tb = traceback.extract_tb(e.__traceback__)
        exception_info = {
            'type': e.__class__.__name__,
            'message': str(e),
            'traceback': [{'filename': frame.filename, 'line': frame.lineno, 'function': frame.name, 'code': frame.line} for frame in tb],
            'time': datetime.now().isoformat()
        }
        self.exceptions.append(exception_info)

    def save_to_json(self, filepath):
        with open(filepath, 'w') as f:
            json.dump(self.exceptions, f, indent=4)
    
    def load_from_json(self, filepath):
        with open(filepath, 'r') as f:
            self.exceptions = json.load(f)

    def print_exceptions(self, format_func=None):
        for ex in self.exceptions:
            if format_func:
                format_func(ex)
            else:
                print(f"Exception type: {ex['type']}")
                print(f"Message: {ex['message']}")
                for frame in ex['traceback']:
                    print(f"  File \"{frame['filename']}\", line {frame['line']}, in {frame['function']}")
                    print(f"    {frame['code']}")
                print("\n")
