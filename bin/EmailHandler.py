import hashlib
import random
import string

import requests


class EmailHandler:
    def __init__(self):
        pass

    def generate_mail_id(self):
        rand = self._generate_random_string()
        mail_provider = self._get_mail_provider()
        mail = '{0}{1}'.format(rand, mail_provider)
        md5_mail = self._create_md5_string(mail)

        return mail, md5_mail

    @staticmethod
    def _generate_random_string(size=10, chars=string.ascii_lowercase + string.digits):
        random_string = (random.choice(chars) for _ in range(size))
        return ''.join(random_string)

    @staticmethod
    def _create_md5_string(target):
        md5string = hashlib.md5(target).hexdigest()
        return md5string

    @staticmethod
    def _get_mail_provider():
        provider = '@katztube.com'
        return provider

    @staticmethod
    def get_mail_content(api, mail):
        api = '{0}{1}{2}'.format(api, mail, '/format/html')
        r = requests.get(api)
        if not r.status_code == 200:
            return

        content = r.content
        return content

    @staticmethod
    def get_mail_api_host():
        api = "https://api.temp-mail.org/request/mail/id/"
        return api
