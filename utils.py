from version import Version
from patchmentation.utils import loader
import os, shutil

def generate(version: Version):
    print(f'generate version: {version.name}, to {version.version_folder}')
    version.generate()

def validate(version: Version):
    print(f'validate version: {version.name}, from {version.version_folder}')
    _validate_yolo(version.name, version.folder_images, version.folder_annotations, version.file_names)

def remove(version: Version):
    print(f'remove version: {version.name}, from {version.version_folder}')
    _rm(version.version_folder)

def zip(version: Version):
    print(f'zip version: {version.name}, from {version.version_folder}, to {version.file_zip}')
    _zip(version.version_folder, version.file_zip)

def unzip(version: Version):
    print(f'unzip version: {version.name}, from {version.file_zip} to {version.version_folder}')
    _unzip(version.file_zip, version.version_folder)

def remove_zip(version: Version):
    print(f'remove zip version: {version.name}, from {version.file_zip}')
    _rm(version.file_zip)

def upload(version: Version):
    print(f'upload version: {version.name}, from {version.file_zip}')
    _bash_upload(version.file_zip)

def download(version: Version, url: str):
    print(f'download version: {version.name}, from {url}, to {version.file_zip}')
    _bash_download(url, version.file_zip)

def _remove_ext(file: str):
    return os.path.splitext(file)[0]

def _zip(folder: str, file: str):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    shutil.make_archive(_remove_ext(file), 'zip', folder)

def _unzip(file: str, folder: str):
    os.makedirs(folder)
    shutil.unpack_archive(file, folder, 'zip')

def _rm(path: str):
    os.system(f'rm -rf {path}')

def _bash_upload(file: str):
    os.system(f'curl bashupload.com -T {file}')

def _bash_download(url: str, file: str):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    os.system(f'wget -c {url} -O {file}')
    
def _validate_yolo(name: str, folder_images: str, folder_annotations: str, file_names: str):
    dataset = loader.load_yolo_dataset(folder_images, folder_annotations, file_names)
    print(f'{name}: {dataset}')
