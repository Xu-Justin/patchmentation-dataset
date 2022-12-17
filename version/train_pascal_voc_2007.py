from .version import Version
from . import generator

import patchmentation
from patchmentation.utils import loader
from patchmentation.utils import transform
from patchmentation.utils import filter
from patchmentation.utils import Comparator

def pascal_voc_2007_train():
    return patchmentation.data.PascalVOC2007().load('train')

class TrainPascalVoc2007(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007'

    @property
    def dataset(self):
        return pascal_voc_2007_train()

    def generate(self, batch: int):
        for i in range(batch):
            loader.save_yolo_dataset(self.dataset, self.folder_images(i), self.folder_annotations(i), self.file_names(i))

class TrainPascalVoc2007tiny(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007-tiny'

    @property
    def dataset(self):
        return pascal_voc_2007_train()

    def generate(self, batch: int):
        dataset = self.dataset
        n_images = 200
        for i in range(batch):
            loader.save_yolo_names(dataset.classes, self.file_names(i))
            generator.generate(dataset, n_images, self.folder_images(i), self.folder_annotations(i), version_folder_batch=self.version_folder_batch(i))

class TrainPascalVoc2007v1(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007-v1'

    @property
    def dataset(self):
        return pascal_voc_2007_train()

    def generate(self, batch: int):
        dataset = self.dataset
        n_images = 2500
        actions = [
            filter.FilterWidth(50, Comparator.GreaterEqual),
            filter.FilterHeight(50, Comparator.GreaterEqual),
            transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)
        ]
        kwargs = {
            'max_n_patches' : 10,
        }
        for i in range(batch):
            loader.save_yolo_names(dataset.classes, self.file_names(i))
            generator.generate(dataset, n_images, self.folder_images(i), self.folder_annotations(i), actions=actions, **kwargs, version_folder_batch=self.version_folder_batch(i))

class TrainPascalVoc2007v2(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007-v2'

    @property
    def dataset(self):
        return pascal_voc_2007_train()

    def generate(self, batch: int):
        dataset = self.dataset
        n_images = 2500
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
        for i in range(batch):
            loader.save_yolo_names(dataset.classes, self.file_names(i))
            generator.generate(dataset, n_images, self.folder_images(i), self.folder_annotations(i), actions=actions, **kwargs, version_folder_batch=self.version_folder_batch(i))

class TrainPascalVoc2007v3(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007-v3'

    @property
    def dataset(self):
        return pascal_voc_2007_train()

    def generate(self, batch: int):
        dataset = self.dataset
        n_images = 2500
        actions = [
            filter.FilterWidth(50, Comparator.GreaterEqual),
            filter.FilterHeight(50, Comparator.GreaterEqual),
            transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)
        ]
        kwargs = {
            'max_n_patches' : 10,
            'visibility_threshold': 1.0
        }
        for i in range(batch):
            loader.save_yolo_names(dataset.classes, self.file_names(i))
            generator.generate(dataset, n_images, self.folder_images(i), self.folder_annotations(i), actions=actions, **kwargs, version_folder_batch=self.version_folder_batch(i))
