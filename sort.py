import os
import shutil

def normalize(name):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ь': '', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'YE', 'Ж': 'ZH', 'З': 'Z', 'И': 'I',
        'І': 'I', 'Ї': 'YI', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
        'Ь': '', 'Ю': 'YU', 'Я': 'YA'
    }
    normalized_name = ''
    for char in name:
        if char.isalnum():
            if char.lower() in translit_dict:
                normalized_name += translit_dict[char.lower()]
            else:
                normalized_name += char
        else:
            normalized_name += '_'
    return normalized_name


def sort_files(folder_path):
    image_extensions = ('.jpeg', '.png', '.jpg', '.svg')
    video_extensions = ('.avi', '.mp4', '.mov', '.mkv')
    document_extensions = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
    music_extensions = ('.mp3', '.ogg', '.wav', '.amr')
    archive_extensions = ('.zip', '.gz', '.tar', '.rar')

    for root, dirs, files in os.walk(folder_path, topdown=True):
        if 'archives' in dirs:
            dirs.remove('archives')
        if 'video' in dirs:
            dirs.remove('video')
        if 'audio' in dirs:
            dirs.remove('audio')
        if 'documents' in dirs:
            dirs.remove('documents')
        if 'images' in dirs:
            dirs.remove('images')

        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            file_name = os.path.splitext(file)[0]
            normalized_name = normalize(file_name)

            if file_extension in image_extensions:
                destination_folder = os.path.join(root, 'images')
            elif file_extension in video_extensions:
                destination_folder = os.path.join(root, 'video')
            elif file_extension in archive_extensions:
                destination_folder = os.path.join(root, 'archive')
            elif file_extension in document_extensions:
                destination_folder = os.path.join(root, 'documents')
            elif file_extension in music_extensions:
                destination_folder = os.path.join(root, 'audio')
            else:
                destination_folder = os.path.join(root, 'unknown')
            
            os.makedirs(destination_folder, exist_ok=True)
            
            new_file_path = os.path.join(destination_folder, normalized_name + file_extension)
            
            shutil.move(os.path.join(root, file), new_file_path)
    
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

folder_path = r'C:\Users\User\Desktop\Мотлох'
sort_files(folder_path)
