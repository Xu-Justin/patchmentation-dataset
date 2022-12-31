import utils
import version
from version import Version
from typing import List

def get_args_parser():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', type=str, default=[], nargs='+', help='dataset version')
    parser.add_argument('--generate', action='store_true', help='generate dataset')
    parser.add_argument('--validate', action='store_true', help='validate dataset')
    parser.add_argument('--remove', action='store_true', help='remove dataset')
    parser.add_argument('--zip', action='store_true', help='zip dataset')
    parser.add_argument('--unzip', action='store_true', help='unzip dataset')
    parser.add_argument('--remove-zip', action='store_true', help='remove zip dataset')
    parser.add_argument('--upload', action='store_true', help='upload dataset zip')
    parser.add_argument('--download', type=str, default=[], nargs='+', help='download dataset zip')
    parser.add_argument('--overwrite', action='store_true', help='overwrite existing dataset / zip')
    parser.add_argument('--batch', type=int, default=1, help='number of batch to be generated')
    args = parser.parse_args()
    return args

map_versions = {}

def init_map_versions():
    def add_version(version: Version):
        map_versions[version.name] = version
    add_version(version.valid_pascal_voc_2007.ValidPascalVoc2007())
    add_version(version.test_pascal_voc_2007.TestPascalVoc2007())
    add_version(version.train_pascal_voc_2007.TrainPascalVoc2007())
    add_version(version.train_pascal_voc_2007.TrainPascalVoc2007v1())
    add_version(version.train_pascal_voc_2007.TrainPascalVoc2007v2())
    add_version(version.train_pascal_voc_2007.TrainPascalVoc2007v3())
    add_version(version.train_pascal_voc_2007.TrainPascalVoc2007v4())
    add_version(version.train_pascal_voc_2007.TrainPascalVoc2007tiny())
    add_version(version.penn_fudan_ped.TrainPennFudanPedPerson())
    add_version(version.penn_fudan_ped.ValidPennFudanPedPerson())
    add_version(version.campus.TrainCampus())
    add_version(version.campus.ValidCampus())
    add_version(version.campus.TestCampus())

def main(args):
    init_map_versions()

    versions: List[Version] = []

    for args_version in args.version:
        if args_version in map_versions.keys():
            versions.append(map_versions[args_version])
        else:
            raise ValueError(f'version {args_version} not found.')

    for index, version in enumerate(versions):
        print(version.name)

        if args.generate:
            if args.overwrite:
                utils.remove(version)
            utils.generate(version, args.batch)

        if args.zip:
            if args.overwrite:
                utils.remove_zip(version)
            utils.zip(version)

        if args.upload:
            utils.upload(version)

        if args.remove_zip:
            utils.remove_zip(version)

        if len(args.download) > index:
            if args.overwrite:
                utils.remove_zip(version)
            utils.download(version, args.download[index])

        if args.unzip:
            if args.overwrite:
                utils.remove(version)
            utils.unzip(version)

        if args.validate:
            utils.validate(version)

        if args.remove:
            utils.remove(version)

if __name__ == '__main__':
    args = get_args_parser()
    print(args)
    main(args)