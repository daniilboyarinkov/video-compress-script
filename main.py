import os

cur_dir = input("Введите корневую директорию: ")
hierarchy = os.walk(cur_dir)

video_extensions = ["mp4", "mov", "mkv", "flv", ".vid", "m4v", "avi", "asf"]

# for folder in hierarchy:
# folder[0] - path
# folder[1] - sub_folders
# folder[2] - files


def compress_video(file_path, file_name, file_ext, level=4):
    os.system(f'ffmpeg -v error -hide_banner -i "{file_path}/{file_name}.{file_ext}" -vcodec mpeg4 -q:v {level} "{file_path}/{file_name} - modified.{file_ext}" ')


for folder in hierarchy:
    print(f"\nFOLDER: {folder[0]}\n")
    for file in folder[2]:
        file_extension = file.split(".")[-1]
        if file_extension in video_extensions:
            print(f"Compressing: {file}")
            compress_video(file_path=folder[0], file_name=file.split(".")[0], file_ext=file_extension)
