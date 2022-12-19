from patchmentation.collections import Dataset
from patchmentation.utils import functional as F
from patchmentation.utils import loader
from patchmentation import patch_augmentation

import os
import random
from tqdm import tqdm

def generate(dataset: Dataset, n_images: int, folder_images: str, folder_annotations: str, version_folder_batch: str = None, ratio_negative_patch: float = 0, **kwargs):
    patches = []
    for image_patch in dataset.image_patches:
        patches += image_patch.patches

    negative_patches = []
    while len(negative_patches) < int(len(patches) * ratio_negative_patch):
        image = random.choice(dataset.image_patches)
        negative_patch = F.get_negative_patch(image, 0.0)
        if negative_patch is not None:
            negative_patches.append(negative_patch)
    
    patches += negative_patches

    if version_folder_batch is not None:
        desc = f'generate - {version_folder_batch}'
    else:
        desc = f'generate'

    for i in tqdm(range(n_images), desc=desc):
        image = random.choice(dataset.image_patches)
        result = patch_augmentation(patches, image, **kwargs)
        result.patches = [patch for patch in result.patches if patch.class_name is not F.NEGATIVE_PATCH_CLASS_NAME]
        file_image = os.path.join(folder_images, f'{i}.jpg')
        file_annotation = os.path.join(folder_annotations, f'{i}.txt')
        loader.save_yolo_image_patch(result, dataset.classes, file_image, file_annotation)
