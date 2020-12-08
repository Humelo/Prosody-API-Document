# Prosody API Document
## API 사용법
1. APIKey 발급
    - https://dashboard.prosody-tts.com/ 에 접속하여 오른쪽 상단에 있는 *API KEY 발급* 버튼을 눌러 *APIKey* 를 발급받아주세요. (APIKey는 모든 API의 헤더에 담아 사용하게 됩니다.)
2. 음성 생성
    <details>
    <summary>음성 데이터 생성</summary>

    - API URL: <https://api.prosody-tts.com/api/ttsapi/voice-generation/>
    - Method: POST
    ### Headers

    | Key | Value |
    | --- | :---: |
    | `Content-Type` | `application/json` |
    | `Authorization` | `Api-Key {api_key}` |

    ### Body

    | Key | Type | Required |
    | --- | :---: | :---: |
    | `text` | `String` | `true` |
    | `actor` | `String` | `true` |
    | `language` | `String` | `false`<br>`('kor' | 'en-US')` |
    | `sex` | `String` | `false`<br>`('m' | 'f')` |
    | `dur` | `String` | `false` |
    | `pitch` | `String` | `false` |
    | `overall_pitch` | `String` | `false`<br>`(-20 ~ 20)` |
    | `overall_speed` | `String` | `false`<br>`(0.8 ~ 1.2)` |

    ### Response

    status code: 201
    
    | Key | Type |
    | --- | :---: |
    | `success` | `ture` |
    | `data.signature` | `String` |
    | `data.text` | `String` |
    | `data.ssml` | `String` |
    | `data.emotion` | `String` |
    | `data.dur` | `String` |
    | `data.pitch` | `String` |
    | `data.language` | `String` |
    | `data.sex` | `String` |
    | `data.overall_pitch` | `String` |
    | `data.overall_speed` | `String` |

    </details>
    <details>
    <summary>음성 추출</summary>

    - API URL: https://api.prosody-tts.com/api/ttsapi/voice-generation/{signature}/generate/
    - Method: GET
    ### Headers

    | Key | Value |
    | --- | :---: |
    | `Authorization` | `Api-Key {api_key}` |

    ### Response

    status code: 200

    #### Response Headers

    | Key | Type |
    | --- | :---: |
    | `Voice-Token` | `String` |
    | `Voice-Duration` | `String` |
    | `Voice-Pitch` | `String` |

    Response 로 wav 파일이 옵니다.
    </details>

## 사용 가능한 Actor List
<details>
<summary>감정 조절이 가능한 actor</summary>

- 감정: (A: 화남, C: 차분, D: 실망, E: 흥분, F: 공포, H: 행복, N: 중립, L: 졸림, S: 슬픔)
- Katelyn_(A,C,D,E,F,H,N,L,S) (여성, 20대, 영어)
- Sam_(A,C,D,E,F,H,N,L,S) (남성, 20대, 영어)
- Ju-yeong_(A,C,D,E,F,H,N,L,S) (여성, 20대, 한국어)
- Byeong-chan_(A,C,D,E,F,H,N,L,S) (여성, 20대, 한국어)
</details>
<details>
<summary>감정 조절이 불가능한 actor</summary>

- Min-jeong
- Eun-jeong
- Yu-jeong
- Min-jae
- Emily
- Jennifer
- Susan
- Paul
- Michale
</details>

## 추가 기능들
<details>
<summary>추가 기능들</summary>

- overall_pitch 변경 (화자 말의 음 높낮이를 조절하는데 사용됩니다.) - 추천 설정 값 범위: (-20 ~ 20)
- overall_speed 변경 (화자의 말하기 속도를 조절하는데 사용됩니다.) - 추천 설정 값 범위: (0.8 ~ 1.2)
- language 변경 (화자의 기본 언어 대신 다른 언어를 적용하고 싶다면, language 값을 직접 설정하여 커스텀할 수 있습니다.) - 한국어: kor, 영어: en-US
- sex 변경 (화자의 기본 성별 대신 다른 성별을 적용하고 싶다면, sex 값을 직접 설정하여 커스텀할 수 있습니다.) - 남성: m, 여성: f
</details>

## 피드백 & 질문
- 궁금하신 저;이나 문의 사항이 있으시면 언제든지 contact@humelo.com 으로 연락 주시길 바랍니다.