import commands as c
from commands import db
import unittest
from database import DatabaseManager
from datetime import datetime
from unittest import mock
# from commands import db

# db = DatabaseManager('bookmark.db')


class RmTestCase(unittest.TestCase):
    @mock.patch('commands.db.add')
    # data = dict()
    def test_AddBookmarkCommand(self, mock_db):
        data = {'title': 'kapil',
                'url': 'wwww',
                'notes': 'test ',
                'date_added': datetime.utcnow().isoformat()}
        c.AddBookmarkCommand(data)
        # self.assertTrue(mock_db.called)
        # mock_db.assert_called_with('bookmarks', data)
        mock_db.assert_called_with(data)
        # self.assertEqual('Bookmark added!', c.AddBookmarkCommand(data))


if __name__ == '__main__':
    unittest.main()
