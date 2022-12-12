import patchmentation
from patchmentation.collections import Dataset
from patchmentation.dataset import PASCAL_VOC_2007
from patchmentation.utils import generator
from patchmentation.utils import transform, filter, Comparator

import os, shutil
from tqdm import tqdm
from functools import cached_property

def generate_file_images(file_images: str, folder_images: str):
    with open(file_images, 'w') as f:
        for file_name in tqdm(os.listdir(folder_images), desc=f'generate_yolo_file_images'):
            if file_name.startswith('.'): continue
            if not file_name.endswith(('.jpg', '.png')): continue
            path = os.path.join(folder_images, file_name)
            f.write(f'{path}\n')

def generate_file_data(file_data: str, n_classes: int, file_images_train: str, file_images_valid: str, file_names: str, backup: str = 'backup/'):
    with open(file_data, 'w') as f:
        f.write(f'classes = {n_classes}\n')
        f.write(f'train = {file_images_train}\n')
        f.write(f'valid = {file_images_valid}\n')
        f.write(f'name = {file_names}\n')
        f.write(f'backup = {backup}\n')

def save_dataset(dataset: Dataset, folder: str):
    os.makedirs(folder, exist_ok=True)
    for i, image_patch in enumerate(dataset.image_patches):
        file_image = os.path.join(folder, f'{i}.jpg')
        file_annotation = os.path.join(folder, f'{i}.txt')
        generator.save_yolo_image_patch(file_image, file_annotation, image_patch, dataset.classes)

def generate_valid_dataset(dataset: Dataset, base_folder: str, folder_images: str, file_names: str, file_images: str, overwrite: bool = False):
    if overwrite and os.path.exists(base_folder):
        shutil.rmtree(base_folder)
    os.makedirs(base_folder)
    generator.save_yolo_names(file_names, dataset.classes)
    save_dataset(dataset, folder_images)
    generate_file_images(file_images, folder_images)
    
def generate_train_dataset(dataset: Dataset, n_images: int, base_folder: str, folder_images: str, file_names, file_images_train: str, file_images_valid: str, file_data: str, overwrite: bool = False, **kwargs):
    if overwrite and os.path.exists(base_folder):
        shutil.rmtree(base_folder)
    os.makedirs(base_folder)
    generator.generate_yolo_dataset(dataset, n_images, folder_images, folder_images, file_names, **kwargs)
    generate_file_images(file_images_train, folder_images)
    generate_file_data(file_data, dataset.n_classes, file_images_train, file_images_valid, file_names)

def upload(path):
    print(f'upload {path}')
    os.system(f'curl bashupload.com -T {path}')

def download(url, path):
    print(f'download from {url} to {path}')
    os.system(f'wget -c {url} -O {path}')

def zip(path, output_path):
    print(f'zip {path} to {output_path}')
    os.system(f'zip -q -r {output_path} {path}')

def unzip(path, output_path):
    print(f'unzip {path} to {output_path}')
    os.system(f'unzip -q {path} -d {output_path}')

def rm(path):
    print(f'remove {path}')
    shutil.rmtree(path)

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
    def base_folder(self):
        return os.path.join(self.root, self.name)

    @property
    def file_zip(self):
        return self.base_folder + '.zip'
    
    @property
    def folder_images(self):
        return os.path.join(self.base_folder, 'obj/')

    @property
    def folder_annotations(self):
        return self.folder_images

    @property
    def file_images_train(self):
        return os.path.join(self.base_folder, 'train.txt')

    @property
    def file_images_valid(self):
        return os.path.join(self.base_folder, 'valid.txt')

    @property
    def file_names(self):
        return os.path.join(self.base_folder, 'obj.names')

    @property
    def file_data(self):
        return os.path.join(self.base_folder, 'obj.data')

    def generate(self, overwrite: bool = False):
        raise NotImplementedError

class VersionValidPascalVOC2007(Version):
    @property
    def name(self):
        return 'valid-pascal-voc-2007'

    @property
    def dataset(self):
        return patchmentation.dataset.load(PASCAL_VOC_2007, categories='val')['val']

    def generate(self, overwrite: bool = False):
        generate_valid_dataset(self.dataset, self.base_folder, self.folder_images, self.file_names, self.file_images_valid, overwrite)

class VersionTrainPascalVOC2007v1(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007-v1'

    @property
    def dataset(self):
        return patchmentation.dataset.load(PASCAL_VOC_2007, categories='train')['train']

    def generate(self, overwrite: bool = False):
        n_images = 25000
        actions = [
            filter.FilterWidth(50, Comparator.GreaterEqual),
            filter.FilterHeight(50, Comparator.GreaterEqual),
            transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO),
        ]
        max_n_patches = 10
        generate_train_dataset(
            self.dataset, n_images, self.base_folder, self.folder_images, self.file_names,
            self.file_images_train, VersionValidPascalVOC2007().file_images_valid, self.file_data,
            overwrite, actions=actions, max_n_patches=max_n_patches
        )

class VersionTrainPascalVOC2007v2(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007-v2'

    @property
    def dataset(self):
        return patchmentation.dataset.load(PASCAL_VOC_2007, categories='train')['train']

    def generate(self, overwrite: bool = False):
        n_images = 25000
        actions = [
            filter.FilterWidth(50, Comparator.GreaterEqual),
            filter.FilterHeight(50, Comparator.GreaterEqual),
            transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO),
            transform.SoftEdge(13, 20)
        ]
        max_n_patches = 10
        generate_train_dataset(
            self.dataset, n_images, self.base_folder, self.folder_images, self.file_names,
            self.file_images_train, VersionValidPascalVOC2007().file_images_valid, self.file_data,
            overwrite, actions=actions, max_n_patches=max_n_patches
        )

class VersionTrainPascalVOC2007v3(Version):
    @property
    def name(self):
        return 'train-pascal-voc-2007-v3'

    @property
    def dataset(self):
        return patchmentation.dataset.load(PASCAL_VOC_2007, categories='train')['train']

    def generate(self, overwrite: bool = False):
        n_images = 25000
        actions = [
            filter.FilterWidth(50, Comparator.GreaterEqual),
            filter.FilterHeight(50, Comparator.GreaterEqual),
            transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO),
        ]
        max_n_patches = 20
        visibility_threshold = 1.0
        generate_train_dataset(
            self.dataset, n_images, self.base_folder, self.folder_images, self.file_names,
            self.file_images_train, VersionValidPascalVOC2007().file_images_valid, self.file_data,
            overwrite, actions=actions, max_n_patches=max_n_patches, visibility_threshold=visibility_threshold
        )