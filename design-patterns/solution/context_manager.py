from dataclasses import dataclass
from typing import Union


FILE = '/tmp/context-manager.txt'


@dataclass
class File:
    name: str
    mode: str = 'w'
    content: Union[list, tuple] = ()
    encoding: str = 'utf-8'

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self.write()

    def append_line(self, line):
        self.content.append(line)

    def write(self):
        with open(self.name, mode=self.mode, encoding=self.encoding) as file:
            for line in self.content:
                file.write(f'{line}\n')


f = File(FILE, content=['hello'])
print(f.content)
f.write()


with File(FILE) as file:
    file.append_line('first line')
    file.append_line('second line')
    file.append_line('third line')
