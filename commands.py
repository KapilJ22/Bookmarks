from database import DatabaseManager
from datetime import datetime
import sys
import requests
import pprint
import json
from exceptions import InvalidGithubUser
from unittest import mock
import unittest

db = DatabaseManager('bookmark.db')


class CreateBookmarksTableCommand:
    def execute(self):
        db.create_table('bookmarks', {
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
            'notes': 'text',
            'date_added': 'text not null',
        })


def AddBookmarkCommand(data):
    if not 'date_added' in data:
        data['date_added'] = datetime.utcnow().isoformat()
    db.add('bookmarks', data)
    return 'Bookmark added!'


def ListBookmarksCommand(orderBy='date_added'):
    return db.select('bookmarks', order_by=orderBy).fetchall()


def starGithubRepoCommand(github_username):
    try:
        response = requests.get(
            'https://api.github.com/users/KapilJ22/starred')
        # raise InvalidGithubUser(github_username)
    except InvalidGithubUser as e:
        print("caught and thrown again")
        raise

    print(response.links)
    # return pprint.pformat(response.json())
    # print(json.dumps(response, indent=4, sort_keys=True))
    # for repo_info in response.json():
    #     repo = repo_info['repo']
    data = {}
    data['title'] = "repo_name"
    data['url'] = "www.kj"
    data['notes'] = "temp "
    data['date_added'] = datetime.utcnow().isoformat()
    print(f"data:{data} ")
    return (AddBookmarkCommand(data))
    # print(repo)


def QuitCommand():
    sys.exit()


# class RmTestCase(unittest.TestCase):
#     @mock.patch('add')
#     # data = dict()
#     def test_AddBookmarkCommand(self, mock_db):
#         data = {'title': 'kapil',
#                 'url': 'wwww',
#                 'notes': 'test ',
#                 'date_added': datetime.utcnow().isoformat()}
#         AddBookmarkCommand(data)
#         # self.assertTrue(mock_db.called)
#         mock_db.assert_called_with('bookmarks', data)
#         # self.assertEqual('Bookmark added!', c.AddBookmarkCommand(data))


# if __name__ == '__main__':
#     unittest.main()
