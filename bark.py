import commands
import json


class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name
        self.command = command
        self.prep_call = prep_call

    def run(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command(
            data) if data else self.command()
        print(message)

    def __str__(self):
        return self.name


def print_options(options):
    for shortcut, option in options.items():
        print(f'({shortcut}) {option}')
    print("test")


# def option_choice_is_valid(choice, options):
#     return choice in options or choice.upper() in options


# def get_option_choice(options):
#     choice = input('Choose an option: ')
#     while not option_choice_is_valid(choice, options):
#         print('Invalid choice')
#         choice = input('Choose an option: ')
#     return options[choice.upper()]


def get_user_input(label, required=True):
    value = input(f'{label}: ') or None
    while required and not value:
        value = input(f'{label}: ') or None
    return value


def get_new_bookmark_data():
    return {
        'title': get_user_input('Title'),
        'url': get_user_input('URL'),
        'notes': get_user_input('Notes', required=False),
    }


def get_github_user():
    return get_user_input("GitHub UserName", required=True)


def input_choice():
    choice = input('Choose an option: ')
    while choice not in options:
        print('Invalid choice')
        choice = input('Choose an option: ')
    return choice


if __name__ == '__main__':
    commands.CreateBookmarksTableCommand().execute()
    options = {
        'A': Option('Add a bookmark', commands.AddBookmarkCommand, prep_call=get_new_bookmark_data),
        'B': Option('List bookmarks by date',
                    commands.ListBookmarksCommand),
        # 'T': Option('List bookmarks by title',
        #             commands.ListBookmarksCommand(order_by='title')),
        # 'D': Option('Delete a bookmark', commands.DeleteBookmarkCommand()),
        'G': Option('github stars', commands.starGithubRepoCommand, get_github_user),
        'Q': Option('Quit', commands.QuitCommand)
    }
    print_options(options)
#     chosen_option = get_option_choice(options)
#     choice = input('Choose an option: ')
    while True:
        choice = input_choice()
        chosen_option = options[choice]
        chosen_option.run()
