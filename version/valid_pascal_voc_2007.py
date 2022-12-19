from .version import Version

import os
import patchmentation
from patchmentation.utils import loader

def pascal_voc_2007_val():
    return patchmentation.data.PascalVOC2007().load('val')

class ValidPascalVoc2007(Version):
    @property
    def name(self):
        return 'valid-pascal-voc-2007'

    @property
    def dataset(self):
        return pascal_voc_2007_val()

    def generate(self, batch: int):
        for i in range(batch):
            if os.path.exists(self.version_folder_batch(i)):
                continue
            loader.save_yolo_dataset(self.dataset, self.folder_images(i), self.folder_annotations(i), self.file_names(i))
        