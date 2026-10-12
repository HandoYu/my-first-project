"""桌面文件自动整理工具 v1.0 —— 只整理图片"""

import shutil
from pathlib import Path

TARGET_DIR = Path(r"C:\Users\Lenovo\Desktop\my-first-project\test_data")

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}


def organize_images(target):
    """把 target 目录里的图片移动到 target/Images/，返回移动的文件个数"""
    images_dir = target / "Images"
    images_dir.mkdir(exist_ok=True)

    moved = 0
    for item in target.iterdir():
        if not item.is_file():
            continue

        if item.suffix.lower() in IMAGE_EXTS:
            shutil.move(str(item), str(images_dir / item.name))
            moved += 1
            print(f"已移动：{item.name}")

    return moved


if __name__ == "__main__":
    count = organize_images(TARGET_DIR)
    print(f"完成，共移动 {count} 个图片文件。")
