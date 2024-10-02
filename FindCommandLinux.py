from abc import ABC, abstractmethod
import fnmatch

class Item(ABC):
    '''
    This is the composite class which can either be a file(leaf) or a directory(composite)
    '''
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def search(self, patten):
        pass

class File(Item):
    def __init__(self, name):
        super().__init__(name)
    
    def search(self, pattern):
        if fnmatch.fnmatch(self.name, pattern):

            return [self.name]
        return []

class Directory(Item):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, item: Item):
        self.children.append(item)
    
    def remove(self, item: Item):
        self.children.remove(item)

    def search(self, pattern):
        result = []
        for child in self.children:
            result += child.search(pattern)
        return result

class FindCommandLinux:
    def __init__(self, root):
        self.root = root

    def search(self, pattern):
        return self.root.search(pattern)

# Usage
class FindCommandLinuxTest:
    def main(self):
        root = Directory('root')
        dir1 = Directory('dir1')
        dir2 = Directory('dir2')
        file1 = File('file1.txt')
        file2 = File('file2.py')
        file3 = File('file3.java')
        root.add(dir1)
        root.add(dir2)
        dir1.add(file1)
        dir1.add(file2)
        dir2.add(file3)
        findCommand = FindCommandLinux(root)
        results = findCommand.search('file*')
        print(results)
        results = findCommand.search('*.txt')
        print(results)
    
if __name__ == '__main__':
    FindCommandLinuxTest().main()
