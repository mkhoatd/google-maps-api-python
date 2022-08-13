# This is a sample Python script.
import os
from typing import Tuple

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import googlemaps


def search_nearby_places(api_key: str, keyword: str, current_location: Tuple[float, float], radius: int,
                         page_token: str = None) -> object:
    client = googlemaps.Client(api_key)
    response = client.places_nearby(
        location=current_location,
        keyword=keyword,
        radius=radius,
        page_token=page_token,
        language="vi"
    )
    return response, response['next_page_token']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api_key = os.getenv('GOOGLE_API_KEY')
    keyword = "nhà hàng"
    location = (16.4776291, 107.5808452)
    radius = 1000
    page_token = "AeJbb3fQLptfUhrsQT8bLTVMLNC5rSB6N07FtV88L5hGVriXoM03KlKnd3T-wrB4bsE_EyOnqCgy0oBXiqRuUDihcDG9gRqeQkYXRJ6y-b1LvOi0ZwcC1p6H0j0r_N09TJzY4kv9VgOeeOHCbiyKeWBrgwtfalWbMEXHQPL5DUNbCYAcwjk8FW0zQN1OhwC_Ljm7wwMhQO6aYMSdd_qGyiuisglX8LOAPObh0r1cONJ-5rpWmfhKo-WlY6mnUXtlS-zQXM5_Rt-1i_-HNVoGOUP0UFKaNHxjIELGsvKKCbCAO0LZ4WLD51wpX0jujObkfVxm8Cvru1_8N7myWSEIKeLkMK-dDYqZK2BPvpB3gOEtN6XQDiF8QMCsG5PIZTm24QxhCKULhgOSAjg-qLo8He8xae2xJTMEKU-H8E3GLMsUp8R6k86Af9sZo_-a"
    print(search_nearby_places(api_key, keyword, location, radius, page_token))
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
