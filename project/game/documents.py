from coreapi import Document, Link, required


def get_homepage():
    """
    Return the top level Document object for the API root.
    """
    return Document(
        url='/',
        title='Home',
        content={
            'new_game': Link(action='post')
        }
    )


def get_game(instance):
    """
    Return a Document object for a single game instance.
    """
    content = {
        'description': instance.get_description(),
        'board': instance.get_board_string(),
        'play': Link(action='put', fields=['position']),
        'new_game': Link(url='/', action='post')
    }
    if instance.is_finished():
        del content['play']

    return Document(
        url='/%s' % instance.pk,
        title='Game',
        content=content
    )
