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

    def version_folder_batch(self, batch: int):
        return os.path.join(self.version_folder, str(batch).zfill(3))

    @property
    def file_zip(self):
        return self.version_folder + '.zip'
    
    def folder_images(self, batch: int):
        return os.path.join(self.version_folder_batch(batch), 'images/')

    def folder_annotations(self, batch: int):
        return os.path.join(self.version_folder_batch(batch), 'labels/')

    def file_names(self, batch: int):
        return os.path.join(self.version_folder_batch(batch), 'obj.names')

    def generate(self, batch: int):
        raise NotImplementedError
