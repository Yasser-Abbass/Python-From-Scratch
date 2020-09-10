import sys
import shutil
from pathlib import Path


all_args = sys.argv[1:]
opts = [opt for opt in all_args if opt.startswith("-")]
args = [opt for opt in all_args if not opt.startswith("-")]
fname = Path(__file__).name


def parse_options(opts):
    rec, comp, ext = False, False, '*.*'
    e = [opt for opt in opts if opt.startswith('-e')]
    if '-r' in opts:
        rec = True
    if '-c' in opts:
        comp = True
    if e:
        ext = e[0].split('=')[-1]
    return rec, comp, ext


def backup(src_path, dest_path, recursive, compress, extention):
    print('Begin backup process........')
    if recursive:
        files = list(src_path.rglob(extention))
    else:
        files = list(src_path.glob(extention))

    dest_path.mkdir(exist_ok=True)
    for file in files:
        dest_file = file.parts[len(src_path.parts):]
        file_name = file.name
        new_dir = dest_path.joinpath("/".join(dest_file[:-1]))
        if not new_dir.exists():
            new_dir.mkdir(parents=True)
        dest_file = new_dir.joinpath(file_name)
        shutil.copy(file, dest_file)
    if compress:
        shutil.make_archive(base_name=dest_path, format='zip', root_dir='./', base_dir=dest_path)
        shutil.rmtree(dest_path)
    print('Operation completed successfully')



if len(args) > 1:
    src_str, dest_str = args[0], args[1]
    src_path = Path(src_str)
    dest_path = Path(dest_str)

    if not src_path.exists():
        print("The src path does not exist")
    elif not src_path.is_dir():
        print('src is not a directory')
    elif src_path == dest_path:
        print('Src and destination are the same')
        quit()
    elif dest_path.exists():
        print('The destination path exist and it will be overwritten')
        response = input('Are you sure? (y/N)')
        if response in ('N', 'n'):
            quit()
        elif response in ('Y', 'y'):
            recursive, compress, extension = parse_options(opts)
            backup(src_path, dest_path, recursive, compress, extension)
    else:
        recursive, compress, extension = parse_options(opts)
        backup(src_path, dest_path, recursive, compress, extension)
elif '--help' in opts:
    help_msg = f"""
    Usage: {fname} SOURCE DESTINATION [OPTIONS]
        Backup SOURCE to DESTINATION

    OPTIONS:
        -r          recursive
        -c          compress backup folder to a file
        -e=*.*      file extension to include in the backup
"""
    print(help_msg)
else:
    print(f'{fname}: missing arguments')
    print(f'Try {fname} --help for more information')
