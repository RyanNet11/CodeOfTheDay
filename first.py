import requests, time, random
from datetime import datetime

q4_songName = "SONG NAME"
q5_artistName = "ARTIST"
q3_yourSchool = "SCHOOL NAME"
def sendRequest():
    formID = '232288375176061'
    url = "https://api.jotform.com/formInitCatchLogger/" + formID
    headers = {
        "authority": "api.jotform.com",
        "method": "POST",
        "path": "/formInitCatchLogger/232288375176061",
        "scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Length": "822",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://myboomtour.com",
        "Referer": "https://myboomtour.com/",
        "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    current_time = datetime.utcnow().isoformat() + 'Z'

    payload_data = {
        "data": {
            "stack": {
                "data": {
                    "formID": {"hasValue": True, "required": False},
                    "": {"hasValue": False, "required": False},
                    "q4_songName": {"hasValue": True, "required": False},
                    "q5_artistName": {"hasValue": True, "required": False},
                    "q3_yourSchool": {"hasValue": True, "required": False},
                    "website": {"hasValue": False, "required": False},
                    "simple_spc": {"hasValue": True, "required": False},
                    "embedUrl": {"hasValue": True, "required": False},
                    "event_id": {"hasValue": True, "required": False},
                },
                "validatedNewRequiredFieldIDs": {},
                "event_id": "1695078540058_232288375176061_Z9KRGxQ",
                "formID": "232288375176061",
                "time": current_time,  # Set the current time here
                "hasWidget": 0,
            },
            "agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "referrer": "https://myboomtour.com/song-request-form/",
        },
        "title": "BLANK_SUBMISSION_TRACK_FE"
    }

    respone = requests.post(url, headers=headers, data=payload_data)
    print("API RSC", respone.status_code)
    #print("respone.raw", respone.raw)
    #print("respone.headers", respone.headers)
    #print("respone.text", respone.text)
    url = "https://submit.jotform.com/submit/" + formID
    headers = {
        "authority": "submit.jotform.com",
        "method": "POST",
        "path": "/submit/232288375176061",
        "scheme": "https",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Content-Length": "323",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://myboomtour.com",
        "Referer": "https://myboomtour.com/",
        "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    data = {
        "formID": "232288375176061",
        "q4_songName": f"{q4_songName}",
        "q5_artistName": f"{q5_artistName}",
        "q3_yourSchool": f"{q3_yourSchool}",
        "website": "",
        "embedUrl": "https://myboomtour.com/song-request-form/",
        "validatedNewRequiredFieldIDs": "No validated required fields"
    }
    respone = requests.post(url, headers=headers, data=data)
    #print()
    #print()
    print("submit RSC", respone.status_code)
    #print("respone.raw", respone.raw)
    #print("respone.headers", respone.headers)
    return
i = 100
while i > 1 :
    sendRequest()
    i = i - 1
    print(i)
    x = random.randint(1, 100)
    x = x*60
    print("waiting", x, "seconds")
    time.sleep(x)
    

