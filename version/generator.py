from patchmentation.collections import Dataset
from patchmentation.utils import loader
from patchmentation import patch_augmentation

import os
import random
from tqdm import tqdm

def generate(dataset: Dataset, n_images: int, folder_images: str, folder_annotations: str, **kwargs):
    patches = []
    for image_patch in dataset.image_patches:
        patches += image_patch.patches

    for i in tqdm(range(n_images), desc='generate'):
        image = random.choice(dataset.image_patches)
        result = patch_augmentation(patches, image, **kwargs)
        file_image = os.path.join(folder_images, f'{i}.jpg')
        file_annotation = os.path.join(folder_annotations, f'{i}.txt')
        loader.save_yolo_image_patch(result, dataset.classes, file_image, file_annotation)
    