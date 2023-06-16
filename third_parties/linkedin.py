import  os
import requests

def scrape_linkedin_profile(linkedin_profile_url:str):
    """
    scrape information from linkedin profiles
    Manually scrape information from linkedin profile

    """
    """
    api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve'
    api_key = os.environ["PROXYCURL_API_KEY"]
    header_dic = {'Authorization': 'Bearer ' + api_key}
    
    params = {
    'url':linkedin_profile_url ,
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
    
    response = requests.get(api_endpoint,params=params,headers=header_dic)
    
    
    
    """

    response=requests.get("https://gist.githubusercontent.com/Conrad-sudo/cb7a81fa967c8630cf6eed17b71b1a06/raw/bea9779de3129e51a8a48a2bed20ff42deb2c65e/linkedinprofile.json")


    data=response.json()

    data={
        k: v
        for k,v in data.items()
        if v not in ([],"","", None)
           and k not in ["people_also_viewed","certifications"]

    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")


    return data





