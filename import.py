import requests
import csv


OLD_WP_URL = 'http://bcheights.com/wp-json/wp/v2/'
NEW_WP_URL = 'http://18.219.114.43/wp-json/wp/v2/'


def get_posts():
    req = requests.get()
    print(req)


def add_post_to_csv(writer, post):
    """ Add a single post to the CSV file

        Adds the headers into the file if CSV file doesn't exist
    """
    try:
        with open('posts.csv'):
            pass
    except IOError:
        # Necessary rows
        rows = [
            'date',
            'content',
        ]
        with open('posts.csv', 'w+') as f:
            writer = csv.writer(f)
            writer.writerow(rows)
    finally:
        writer.writerow(post)
