import requests
from bs4 import BeautifulSoup

from bin import EmailHandler
_EmailHandler = EmailHandler.EmailHandler()


class RequestHandler:
    def __init__(self):
        pass

    def vote(self, email, user_id=123):
        values = self._get_post_values(email, user_id)
        headers = self._get_headers()
        url = self._get_post_url()

        # send post request
        status = self.send_post_request(url, values, headers)

        if status:
            return True
        else:
            return

    @staticmethod
    def get_activation_url(md5_email):
        api = _EmailHandler.get_mail_api_host()
        html = _EmailHandler.get_mail_content(api, md5_email)
        if not html:
            return

        b_soup = BeautifulSoup(html, "lxml")
        urls = b_soup.find_all('a')
        for tag in urls:
            link = tag.get('href', None)
            activation_link = link
            if activation_link:
                return activation_link
            else:
                return

    @staticmethod
    def send_post_request(url, data, headers):
        try:
            request = requests.post(url, data=data, headers=headers)
        except requests.ConnectionError:
            return

        response = request.status_code
        if response == 200:
            return True
        else:
            return

    @staticmethod
    def send_get_request(url):
        try:
            request = requests.get(url)
        except requests.ConnectionError:
            return

        response = request.status_code
        if response == 200:
            return True
        else:
            return

    @staticmethod
    def _get_email():
        mail_handler = _EmailHandler
        email_tuple = mail_handler.generate_mail_id()
        return email_tuple

    @staticmethod
    def _get_post_values(email, user_id):
        values = {
            'userId': user_id,
            'email': email
        }
        return values

    @staticmethod
    def _get_headers():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/39.0.2171.95 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        return headers

    @staticmethod
    def _get_post_url():
        schema = 'https://'
        host = 'expeditierobinson-zoektocht.livewallcampaigns.com'
        url = '/api/voteEmail/'
        full_path = '{0}{1}{2}'.format(schema, host, url)
        return full_path
