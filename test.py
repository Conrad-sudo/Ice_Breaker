import json

import requests

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
api_key = 'UthoyI8pfvYcgv7LOb3FaQ'
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'url': 'https://www.linkedin.com/in/bradgarlinghouse/',
    'fallback_to_cache': 'on-error',
    'use_cache': 'if-present',
    'skills': 'include',
    'inferred_salary': 'include',
    'personal_email': 'include',
    'personal_contact_number': 'include',
    'twitter_profile_id': 'include',
    'facebook_profile_id': 'include',
    'github_profile_id': 'include',
    'extra': 'include',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

print(json.loads(response))