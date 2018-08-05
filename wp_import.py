import requests
import csv


OLD_WP_URL = 'http://bcheights.com/wp-json/wp/v2/'
NEW_WP_URL = 'http://18.219.114.43/wp-json/wp/v2/'
WP_NONCE_URL = 'http://18.219.114.43/wp-json/bcheights/v1/nonce'


def get_wp_nonce():
    """ Gets the WP Nonce cookie to include in request headers
    """
    resp = requests.get(WP_NONCE_URL)

    if resp.status_code != 200:
        print('Error with getting WP nonce... Retrying')
        resp = requests.get(WP_NONCE_URL)

    nonce = resp.text.replace('"', '')
    return nonce


def get_posts():
    req = requests.get()
    print(req)


def setup_csv(headers):
    """ Sets up the CSV file for posts
        Adds the headers into the file if CSV file doesn't exist
    """
    with open('posts.csv', 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(headers)


# if __name__ == '__main__':
#     nonce = get_wp_nonce()
#     print(nonce)
