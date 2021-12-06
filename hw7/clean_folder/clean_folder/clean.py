from pathlib import Path
import sys
import shutil
import os

CYRILLIC = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'і', "є", "ї", "ґ")

LATIN = ('a', 'b', 'v', 'g', 'd', 'e', 'e', 'zh', 'z', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '"', 'ui', "'", 'e', 'yu', 'ya', 'i', 'ye', 'yi', 'g')

TRANSLATED = {}

for c, l in zip(CYRILLIC, LATIN):
    TRANSLATED[ord(c)] = l
    TRANSLATED[ord(c.upper())] = l.upper()

FOLDERS = ('images', 'audio', 'video', 'documents',
           'archives')

IMAGES_TYPES = ('.jpeg', '.png', '.jpg', '.svg')
VIDEO_TYPES = ('.avi', '.mp4', '.mov', '.mkv')
DOCS_TYPES = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
AUDIO_TYPES = ('.mp3', '.ogg', '.wav', '.amr')
ARCHIVES_TYPES= ('.zip', '.gz', '.tar')

def normalize(filename: str) -> str:
    new_filename = ''
    for simbol in filename:
        new_simbol = TRANSLATED.get(ord(simbol))
        if 49 <= ord(simbol) <= 57 or 65 <= ord(simbol) <= 90 or 97 <= ord(simbol) <= 122:
            new_filename += simbol
        elif new_simbol:
            new_filename += new_simbol
        else:
            new_filename += '_'
    return new_filename
        
def sorter_and_rename_folder(path: Path) -> None:
    for file in path.iterdir():
        if file.is_dir():
            if file.name in FOLDERS:
                continue
            elif len(os.listdir(file)) == 0:
                shutil.rmtree(file)
            else:
                new_filename = normalize(file.name)
                new_filepath = Path(f'{file.parent}/{new_filename}')
                os.rename(file, new_filepath)
                sorter_and_rename_folder(new_filepath)
        elif file.is_file:
            sorter_and_rename_file(file)

def sorter_and_rename_file(path: Path) -> None:
    filetype = path.suffix
    filename = path.stem
    new_filename = normalize(filename)
    path.rename(Path(path.parent, new_filename + filetype))
    new_filepath = Path(new_filename + filetype)

    if filetype in IMAGES_TYPES:
        images_files.append(new_filename + filetype)
        known_types.add(filetype)
        new_file_folder = 'images'
    elif filetype in VIDEO_TYPES:
        video_files.append(new_filename + filetype)
        known_types.add(filetype)
        new_file_folder = 'video'
    elif filetype in DOCS_TYPES:
        documents_files.append(new_filename + filetype)
        known_types.add(filetype)
        new_file_folder = 'documents'
    elif filetype in AUDIO_TYPES:
        audio_files.append(new_filename + filetype)
        known_types.add(filetype)
        new_file_folder = 'audio'
    elif filetype in ARCHIVES_TYPES:
        archives_files.append(new_filename + filetype)
        known_types.add(filetype)
        new_file_folder = 'archives'
    else:
        unknown_files.append(new_filename + filetype)
        if filetype:
            unknown_types.add(filetype)
            new_file_folder = ''
    
    if new_file_folder == 'images' or new_file_folder == 'video' or new_file_folder == 'documents' or new_file_folder == 'audio':
        shutil.move(f'{path.parent}/{new_filepath}', f'{HOME_FOLDER}/{new_file_folder}/{new_filepath}') 
    elif new_file_folder == 'archives':
        shutil.unpack_archive(f'{path.parent}/{new_filepath}', f'{HOME_FOLDER}/{new_file_folder}/{new_filepath}')
        os.remove(f'{path.parent}/{new_filepath}')

def main():
    global HOME_FOLDER, images_files, video_files, documents_files, audio_files, archives_files, unknown_files, known_types, unknown_types
    images_files = []
    video_files = []
    documents_files = []
    audio_files = []
    archives_files = []
    unknown_files = []

    known_types = set()
    unknown_types = set()

    try:
        path = Path(sys.argv[1])
    except:
        print("Please enter one argument - a path of the folder")
    HOME_FOLDER = path

    if path.is_dir():
        for folder in FOLDERS:
            if not os.path.exists(f'{HOME_FOLDER}/{folder}'):
                os.makedirs(f'{HOME_FOLDER}/{folder}')
        
        sorter_and_rename_folder(path)

        print(f'Images: {images_files}\n'
              f'Video: {video_files}\n'
              f'Audio: {audio_files}\n'
              f'Documents: {documents_files}\n'
              f'Archives: {archives_files}\n'
              f'Known extensions: {known_types}\n'
              f'Unknown extensions: {unknown_types}')

    else:
        print("It isn't a folder")

if __name__ == '__main__':
    main()
