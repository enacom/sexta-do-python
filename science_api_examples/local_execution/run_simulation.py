import json

from science_api_examples.io import ExampleIO
from science_api_examples.utils import get_data_path

if __name__ == '__main__':

    with open(get_data_path("example.json"), encoding='utf-8') as f:
        input_data = json.load(f)

    io_instance = ExampleIO(input_data)

    out_data = io_instance.get_output()

    with open(f"output.json", 'w', encoding='utf8') as f:
        json.dump(out_data, f, ensure_ascii=False)
