import json


class JsonFile:
    def __init__(self, file_adr):
        with open(file_adr, 'r') as f:
            self.data = json.load(f)

    def __str__(self):
        return json.dumps(self.data, indent=4)

    def print_keys(self, d=None, prefix=''):
        if d is None:
            d = self.data
        for key, value in d.items():
            print(f"{prefix}{key}")
            if isinstance(value, dict):
                self.print_keys(value, prefix=prefix + '\t')


if __name__ == '__main__':
    file_name = 'data/spm_data.json'
    jf = JsonFile(file_name)
    jf.print_keys()
    print(jf)