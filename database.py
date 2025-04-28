import sqlite3
from sqlite3 import Connection
from typing import List
from models import Post, Posts

def get_post(connection: Connection) -> Posts:
    with connection:
        cur = connection.cursor()
        cur = cur.execute(
                '''
                SELECT post_title, post_text, user_id FROM posts;
                '''
        )
        return [Post.model_validate(dict(post)) for post in cur]
    
def insert_posts(connection: Connection, post: Post):
    with connection:
        cur = connection.cursor()
        cur.execute(
            '''
            INSERT INTO posts (post_title, post_text, user_id)
            VALUES
            ( :post_title , :post_text , :user_id )
            ''',
            post.model_dump()
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
    # for post in get_post(connection):
    #     print(dict(post))

    # test_post = Post(post_title = 'Pydantic Test', post_text = 'Another test', user_id = 2)
    # insert_posts(connection, test_post)

    print(get_post(connection))