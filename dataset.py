import utils
from typing import List

def get_args_parser():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', type=str, default=[], nargs='+', help='dataset version')
    parser.add_argument('--generate', action='store_true', help='generate dataset')
    parser.add_argument('--overwrite', action='store_true', help='delete existing if exists')
    parser.add_argument('--zip', action='store_true', help='zip version')
    parser.add_argument('--upload', action='store_true', help='upload dataset')
    parser.add_argument('--download', type=str, default=None, help='download_dataset')
    parser.add_argument('--unzip', action='store_true', help='zip version')
    parser.add_argument('--remove-zip', action='store_true', help='do not remove cache')
    parser.add_argument('--validate', action='store_true', help='validate dataset')
    parser.add_argument('--remove', action='store_true', help='remove dataset')
    args = parser.parse_args()
    return args

def main(args):
    versions: List[utils.Version] = []
    if 'valid-pascal-voc-2007' in args.version:
        versions.append(utils.VersionValidPascalVOC2007())
        
    if 'train-pascal-voc-2007-v1' in args.version:
        version.append(utils.VersionTrainPascalVOC2007v1())
    
    if 'train-pascal-voc-2007-v2' in args.version:
        version.append(utils.VersionTrainPascalVOC2007v2())
    
    if 'train-pascal-voc-2007-v3' in args.version:
        version.append(utils.VersionTrainPascalVOC2007v3())

    for version in versions:
        print(version.name)
        if args.generate:
            version.generate(args.overwrite)

        if args.zip:
            utils.zip(version.base_folder, version.file_zip)

        if args.upload:
            utils.upload(version.file_zip)

        if args.download is not None:
            utils.download(args.download, version.file_zip)
            if args.overwrite:
                utils.rm(version.base_folder)
            args.download = None

        if args.unzip:
            utils.os.makedirs(version.base_folder)
            utils.unzip(version.file_zip)

        if args.remove_zip:
            utils.rm(version.file_zip)

        if args.validate:
            dataset = utils.patchmentation.utils.loader.load_yolo_dataset(version.folder_images, version.folder_annotations, version.file_names)
            print(dataset)

        if args.remove:
            utils.rm(version.base_folder)
    
if __name__ == '__main__':
    args = get_args_parser()
    print(args)
    main(args)