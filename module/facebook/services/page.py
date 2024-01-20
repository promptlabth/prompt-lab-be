import requests
import json

# API endpoint with updated version to v18.0
url = "https://graph.facebook.com/v18.0/366157134100453/feed"
url_profile_image = "https://graph.facebook.com/v18.0/366157134100453/picture"

# Parameters including the access token
params = {
    "access_token": "EAA1oWnQsH3kBOZBeyfjhbmaNYMHluHqmdDtr9KprGIHoNvZAEKzoycB56IT2GH51qLCgMWcAR4stvVAmkPBCa5ZBagk0mlZBpwLiDWzJZBZAwd3vIz7bMUTmxkQ566gDMxVaDMOkZBThNZA7aVom51LsKPglqlb86z9mpqYzDxqHxWNZBVxELhrfgzZAwxN0TsAqQrw23ZClVQMPyZAH4lQCBviduULUwDKt4EOaauZCbe94ZD"
}
def get_facebook_page_data():

    # Making the GET request
    response = requests.get(url, params=params)

    # Decoding the Unicode escape sequences
    decoded_data = json.loads(response.text)
    page_data = decoded_data['data']
    final_data = []
    for data in page_data:
        if 'message' in data:
            post_and_date = {
                'message': data['message'],
                'created_time': data['created_time']
            }
            final_data.append(post_and_date)
    result = json.dumps(final_data, indent=2, ensure_ascii=False)
    return final_data

    # TODO: แก้ไขให้เป็นรูปแบบที่เราต้องการ
    # Making the GET request for the profile image
    # image_response = requests.get(url_profile_image, params=params, stream=True)

    # if image_response.status_code == 200:
    #     with open('facebook_profile_image.jpg', 'wb') as f:
    #         for chunk in image_response.iter_content(1024):
    #             f.write(chunk)
