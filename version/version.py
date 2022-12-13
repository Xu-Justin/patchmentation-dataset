import os
from functools import cached_property

class Version:
    @property
    def name(self):
        raise NotImplementedError

    @property
    def dataset(self):
        raise NotImplementedError

    @property
    def root(self):
        _root = 'data/'
        os.makedirs(_root, exist_ok=True)
        return _root

    @cached_property
    def version_folder(self):
        return os.path.join(self.root, self.name)

    @property
    def file_zip(self):
        return self.version_folder + '.zip'
    
    @property
    def folder_images(self):
        return os.path.join(self.version_folder, 'images/')

    @property
    def folder_annotations(self):
        return os.path.join(self.version_folder, 'labels/')

    @property
    def file_names(self):
        return os.path.join(self.version_folder, 'obj.names')

    def generate(self):
        raise NotImplementedError
