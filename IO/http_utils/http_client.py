import logging
import os
from http import HTTPStatus

import requests


class Client():
    @staticmethod
    def generate_auth_token(username, password):
        url = 'http://localhost:5000/auth'

        payload = "{\"username\": \"" + username +  "\", \"password\": \"" + password + "\"}"

        headers = {
        'Content-Type': 'application/json'
        }

        # import ipdb; ipdb.set_trace()

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code != HTTPStatus.OK:
            logging.info("[ERROR] Something is wrong with the authentication service.")

        return response.json().get("access_token")
