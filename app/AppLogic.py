from app.LogHandle import script
import subprocess
import json
import requests

__HOST_IP__ = '192.168.1.95'

def scan():
    subprocess.run(["../bat/PC_Hardware_Scan.bat"])
    parse_result = script()
    with open('LogFile.json', 'w', encoding='utf-8') as f:
        json.dump(parse_result, f, ensure_ascii=False, indent=4)
    print(parse_result)


def send_post_request(file_path: str='LogFile.json', server_url: str = f"http://{__HOST_IP__}:8000/DataFrame"):
    try:
        if not file_path.endswith('.json'):
            raise ValueError("Файл должен иметь расширение .json")

        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f, 'application/json')}

            response = requests.post(server_url, files=files)
            response.raise_for_status()
            return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Ошибка при отправке запроса: {str(e)}")
    except Exception as e:
        raise Exception(f"Произошла ошибка: {str(e)}")

def send_ip(server_url:str = f"http://{__HOST_IP__}:8000/get_ip"):
    print(requests.get(server_url).text)

if __name__ == '__main__':
    scan()
    send_post_request()