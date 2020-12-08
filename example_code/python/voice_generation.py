import requests

# https://dashboard.prosody-tts.com/ 에서 발급받은 API_KEY 입니다.
API_KEY = "API_KEY"

url = f'https://api.prosody-tts.com/api/ttsapi/voice-generation/{signature}/generate/'

headers = {
  'Authorization': 'Api-Key {}'.format('홈페이지에서 발급받은 APIKey')
}

res = requests.get(url, headers=headers)

# media_path 는 직접 지정하여 파일을 저장할 위치를 설정해줍니다.
with open(media_path.format(signature), 'wb') as fd:
	for chunk in res.iter_content(chunk_size=128):
		fd.write(chunk)
