import sqlite3
from sqlite3 import Connection
from typing import List

def get_post(connection: Connection) -> List[dict]:
    with connection:
        cur = connection.cursor()
        cur = cur.execute(
                '''
                SELECT post_title, post_text, user_id
                FROM posts;
                '''
        )
        return cur.fetchall()
    
def insert_posts(connection: Connection, post: dict):
    with connection:
        cur = connection.cursor()
        cur.execute(
            '''
            INSERT INTO posts (post_title, post_text, user_id)
            VALUES
            ( :post_title , :post_text , :user_id )
            ''',
            post
        )

if __name__ == "__main__":
    connection = sqlite3.connect('social.db')
    # test_post = {
    #     'post_title': 'Sample Three',
    #     'post_text': 'Test 3',
    #     'user_id': 3
    # }
    # insert_posts(connection, test_post)

    connection.row_factory = sqlite3.Row
    for post in get_post(connection):
        print(dict(post))