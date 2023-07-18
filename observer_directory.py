from apk_pure.api import Api
from apk_pure.models import ItemList
from pathlib import Path


def get_apk_file(package_name: str):
    api = Api()
    item_list = ItemList(data=[
        {'download_url': f'https://d.apkpure.com/b/APK/{package_name}?version=latest'}
    ])
    directory_path = r'C:\Users\YOU\PycharmProjects\app_date'
    api.temp_path = directory_path
    api.download(item_list)
    return Path(directory_path) / f"{package_name.replace('.', '_')}.apk"


if __name__ == "__main__":
    get_apk_file("com.tencent.mm")
