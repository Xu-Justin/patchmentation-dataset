from .version import Version
from . import generator

import patchmentation
from patchmentation.utils import loader
from patchmentation.utils import transform
from patchmentation.utils import filter
from patchmentation.utils import Comparator

def pascal_voc_2007_train():
    return patchmentation.dataset.load_pascal_voc_2007('train')['train']

class TrainPascalVoc2007tiny(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007-tiny'

    @property
    def dataset(self):
        return pascal_voc_2007_train()

    def generate(self):
        dataset = self.dataset
        n_images = 100
        loader.save_yolo_names(dataset.classes, self.file_names)
        generator.generate(dataset, n_images, self.folder_images, self.folder_annotations)

class TrainPascalVoc2007v1(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007-v1'

    @property
    def dataset(self):
        return pascal_voc_2007_train()

    def generate(self):
        dataset = self.dataset
        n_images = 25
        actions = [
            filter.FilterWidth(50, Comparator.GreaterEqual),
            filter.FilterHeight(50, Comparator.GreaterEqual),
            transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)
        ]
        kwargs = {
            'max_n_patches' : 10,
        }
        loader.save_yolo_names(dataset.classes, self.file_names)
        generator.generate(dataset, n_images, self.folder_images, self.folder_annotations, actions=actions, **kwargs)

class TrainPascalVoc2007v2(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007-v2'

    @property
    def dataset(self):
        return pascal_voc_2007_train()

    def generate(self):
        dataset = self.dataset
        n_images = 20
        actions = [
            filter.FilterWidth(50, Comparator.GreaterEqual),
            filter.FilterHeight(50, Comparator.GreaterEqual),
            transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO),
            filter.FilterWidth(30, Comparator.GreaterEqual),
            filter.FilterHeight(30, Comparator.GreaterEqual),
            transform.SoftEdge(13, 20)
        ]
        kwargs = {
            'max_n_patches' : 10,
        }
        loader.save_yolo_names(dataset.classes, self.file_names)
        generator.generate(dataset, n_images, self.folder_images, self.folder_annotations, actions=actions, **kwargs)

class TrainPascalVoc2007v3(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007-v3'

    @property
    def dataset(self):
        return pascal_voc_2007_train()

    def generate(self):
        dataset = self.dataset
        n_images = 15
        actions = [
            filter.FilterWidth(50, Comparator.GreaterEqual),
            filter.FilterHeight(50, Comparator.GreaterEqual),
            transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)
        ]
        kwargs = {
            'max_n_patches' : 10,
            'visibility_threshold': 1.0
        }
        loader.save_yolo_names(dataset.classes, self.file_names)
        generator.generate(dataset, n_images, self.folder_images, self.folder_annotations, actions=actions, **kwargs)