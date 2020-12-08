import requests
import json


url = 'https://api.prosody-tts.com/api/ttsapi/voice-generation/'

payload = json.dumps({
	'text': 'test123',  # 음성으로 추출하고자하는 문장을 입력합니다.
	'actor': 'Min-jae',  # 사용하고자하는 화자를 입력합니다.
	'language': 'kor',  # 사용하고자하는 언어를 선택합니다. 해당 필드를 payload에 넣지 않을 시 화자의 기본 언어가 자동으로 선택됩니다.
	'sex': 'm',  # 사용하고자하는 성별을 선택합니다. 해당 필드를 payload에 넣지 않을 시 화자의 기본 성별이 선택됩니다.
})

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Api-Key {}'.format('홈페이지에서 발급받은 APIKey')
}

res = requests.post(url, headers=headers, data=payload)

# VoiceGeneration 에서 필요한 signature를 저장합니다.
signature = res.json()['data']['signature']
