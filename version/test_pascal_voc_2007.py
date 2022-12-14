from .version import Version

import patchmentation
from patchmentation.utils import loader

def pascal_voc_2007_test():
    return patchmentation.dataset.load_pascal_voc_2007('test')['test']

class TestPascalVoc2007(Version):
    @property
    def name(self):
        return 'test-pascal-voc-2007'

    @property
    def dataset(self):
        return pascal_voc_2007_test()

    def generate(self):
        loader.save_yolo_dataset(self.dataset, self.folder_images, self.folder_annotations, self.file_names)
        