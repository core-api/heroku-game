from coreapi import Document, Link, required


def get_homepage():
    """
    Return the top level Document object for the API root.
    """
    return Document(
        url='/',
        title='Home',
        content={
            'new_game': Link(trans='create')
        }
    )


def get_game(instance):
    """
    Return a Document object for a single game instance.
    """
    content = {
        'description': instance.get_description(),
        'board': instance.get_board_string(),
        'play': Link(trans='update', fields=['position']),
        'new_game': Link(url='/', trans='create')
    }
    if instance.is_finished():
        del content['play']

    return Document(
        url='/%s' % instance.pk,
        title='Game',
        content=content
    )
