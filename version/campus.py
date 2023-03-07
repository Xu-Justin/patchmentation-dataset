from .version import Version
from . import generator

import os
import random
import patchmentation
from patchmentation.collections import Dataset, ImagePatch, Patch, Image, Mask
from patchmentation.utils import loader
from patchmentation.utils import transform
from patchmentation.utils import filter
from patchmentation.utils import Comparator
from typing import List, Tuple

class TrainCampus(Version):
    @property
    def name(self):
        return 'train-campus'

    def get_annotation_file_name(self, image_file_name: str):
        return os.path.splitext(image_file_name)[0] + '.txt'
    
    def get_distribution_file_name(self, image_file_name: str):
        return os.path.splitext(image_file_name)[0] + '_distribution.jpg'

    @property
    def background_images_with_distribution(self) -> List[Tuple[ImagePatch, Mask]]:
        folder_images = 'dataset/train-campus/images'
        folder_annotations = 'dataset/train-campus/annotations'
        folder_distributions = 'dataset/train-campus/distributions'
        file_names = 'dataset/train-campus/obj.names'
        classes = loader.load_yolo_names(file_names)
        assert classes == self.classes
        results = []
        for image_file_name in os.listdir(folder_images):
            annotation_file_name = self.get_annotation_file_name(image_file_name)
            distribution_file_name = self.get_distribution_file_name(image_file_name)
            image = Image(os.path.join(folder_images, image_file_name))
            patches = loader.load_yolo_patches(image, os.path.join(folder_annotations, annotation_file_name), classes)
            image_patch = ImagePatch(image, patches)
            distribution = Mask(os.path.join(folder_distributions, distribution_file_name))
            results.append((image_patch, distribution))
        return results
        
    @property
    def patches(self) -> List[Patch]:
        _patches = []
        for image_patch in patchmentation.data.PennFudanPed().load().image_patches:
            _patches += image_patch.patches
        for patch in _patches:
            patch.class_name = 'person'
        return _patches

    @property
    def classes(self) -> List[str]:
        return ['person']

    def generate(self, batch: int):
        n_images = 100
        actions = [
            filter.FilterWidth(20, Comparator.GreaterEqual),
            filter.FilterHeight(20, Comparator.GreaterEqual),
            transform.RandomResize(height_range=(150, 600), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO),
            transform.SoftEdge(5, 10)
        ]
        kwargs = {
            'max_n_patches' : 30,
            'visibility_threshold': 0.8
        }
        background_images_with_distribution = self.background_images_with_distribution
        patches = self.patches
        for i in range(batch):
            if os.path.exists(self.version_folder_batch(i)):
                continue
            loader.save_yolo_names(self.classes, self.file_names(i))
            background_image, distribution = random.choice(background_images_with_distribution)
            generator.generateV2(background_image, patches, self.classes, n_images, self.folder_images(i), self.folder_annotations(i), actions=actions, patch_distribution=distribution, **kwargs, version_folder_batch=self.version_folder_batch(i))

class ValidCampus(Version):
    @property
    def name(self):
        return 'valid-campus'

    @property
    def dataset(self):
        image_patches: List[ImagePatch] = []
        image_patches += patchmentation.data.campus.Garden1.IP1().load().image_patches[1:65]
        image_patches += patchmentation.data.campus.Garden1.Contour2().load().image_patches[1:65]
        image_patches += patchmentation.data.campus.Garden1.HC2().load().image_patches[1:65]
        image_patches += patchmentation.data.campus.Garden1.HC3().load().image_patches[1:65]
        for image_patch in image_patches:
            for patch in image_patch.patches:
                patch.class_name = 'person'
        return Dataset(image_patches)
    
    def generate(self, batch: int):
        dataset = self.dataset
        for i in range(batch):
            if os.path.exists(self.version_folder_batch(i)):
                continue
            loader.save_yolo_dataset(dataset, self.folder_images(i), self.folder_annotations(i), self.file_names(i))

class TestCampus(Version):
    @property
    def name(self):
        return 'test-campus'

    @property
    def dataset(self):
        image_patches: List[ImagePatch] = []
        image_patches += patchmentation.data.campus.Garden1.IP1().load().image_patches[65:]
        image_patches += patchmentation.data.campus.Garden1.Contour2().load().image_patches[65:]
        image_patches += patchmentation.data.campus.Garden1.HC2().load().image_patches[65:]
        image_patches += patchmentation.data.campus.Garden1.HC3().load().image_patches[65:]
        for image_patch in image_patches:
            for patch in image_patch.patches:
                patch.class_name = 'person'
        return Dataset(image_patches)
    
    def generate(self, batch: int):
        dataset = self.dataset
        for i in range(batch):
            if os.path.exists(self.version_folder_batch(i)):
                continue
            loader.save_yolo_dataset(dataset, self.folder_images(i), self.folder_annotations(i), self.file_names(i))
