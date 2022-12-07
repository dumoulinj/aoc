from aocd.models import Puzzle 
# from aocd import numbers
from aocd import lines

# a: 
# b:  

puzzle = Puzzle(year=2022, day=7)

res_a = 0

fs = {}

class File(object):
    def __init__(self):
        self.file_name = ""
        self.size = 0

class Folder(object):
    def __init__(self):
        self.folder_name = ""
        self.files = {} 
        self.folders = {} 
        self.parent_folder = None
    
    def get_size(self):
        s = 0
        for k, f in self.files.items():
            s += f.size
        
        for k, f in self.folders.items():
            s += f.get_size()
        
        return s
    
    def add_folder(self, folder_name):
        if folder_name not in self.folders:
            _f = Folder()
            _f.folder_name = folder_name
            _f.parent_folder = self
            self.folders[folder_name] = _f
            return _f 
        else:
            return self.folders[folder_name]

    def add_file(self, file_name, size):
        if file_name not in self.files:
            _f = File()
            _f.file_name = file_name 
            _f.size = size
            self.files[file_name] = _f
            return _f 


crt_dir = "/"
crt_cmd = ""
f = Folder()
f.folder_name = "/"
folders = []
folders.append(f)

for l in lines[1:]:
    if l.startswith('$'):
        # command
        _l = l.split(' ')
        crt_cmd = _l[1]
        if crt_cmd == 'cd':
            crt_dir = _l[2]
            if crt_dir == '..':
                f = f.parent_folder
            else:
                f = f.folders[crt_dir]
    else:
        if l.startswith('dir'):
            # dir
            dir_name = l.split(' ')[1]
            _f = f.add_folder(dir_name)
            if _f:
                folders.append(_f)
        else:
            # file
            _l = l.split(' ')
            size = int(_l[0])
            file_name = _l[1]
            f.add_file(file_name, size)

total = folders[0].get_size()
to_del = 30000000 - (70000000 - total)

acc = 0
candidates = []
for f in folders:
    s = f.get_size()
    if s <= 100000:
        acc += s
    if s >= to_del:
        candidates.append(s)

res_a = acc
print("part a: {}".format(res_a))
#puzzle.answer_a = res_a

res_b = sorted(candidates)[0]
print("part b: {}".format(res_b))
# puzzle.answer_b = res_b