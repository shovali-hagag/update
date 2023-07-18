from apk_pure.api import Api
from apk_pure.models import ItemList
from pathlib import Path
from ppadb.client import Client as AdbClient


def get_apk_file(package_name: str):
    api = Api()
    item_list = ItemList(data=[
        {'download_url': f'https://d.apkpure.com/b/APK/{package_name}?version=latest'}
    ])
    directory_path = r'C:\Users\YOU\opensource_projects\NewApkPure-main'
    api.temp_path = directory_path
    api.download(item_list)
    return Path(directory_path) / f"{package_name.replace('.', '_')}.apk"


def adb_install_on_device(apk_path: Path, package_name: str):
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.devices()[0]
    device.uninstall(package_name)
    device.install(apk_path)


def main(package_name: str):
    apk_path = get_apk_file(package_name)
    # adb_install_on_device(apk_path, package_name)

if __name__ == "__main__":
    main("com.whatsapp")