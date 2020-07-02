from database import DatabaseManager
from datetime import datetime
import sys

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
    data['date_added'] = datetime.utcnow().isoformat()
    db.add('bookmarks', data)
    return 'Bookmark added!'


def ListBookmarksCommand(orderBy='date_added'):
    return db.select('bookmarks', order_by=orderBy).fetchall()


def QuitCommand():
    sys.exit()
