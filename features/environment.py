from Utilities.configurations import getconfig
from Utilities.resources import apiresources
import requests

def after_scenario(context,scenario):
    if "library" in scenario.tags:
        url = getconfig()['API']['endpoint'] + apiresources.deletebook
        headers = {"Content-Type": "application/json"}
        deletebook_response = requests.post(url,
                                            json={"ID": context.bookid
                                                  }, headers=headers, )
        print(deletebook_response)
        assert deletebook_response.status_code == 200
        response_json = deletebook_response.json()
        print(response_json['msg'])
        assert response_json['msg'] == "book is successfully deleted "