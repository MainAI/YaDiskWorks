import requests


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(disk_file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        return


if __name__ == '__main__':
    path_to_file = 'text.txt'
    token = ''
    yandex = YandexDisk(token)
    yandex.upload_file_to_disk(path_to_file)
