from coreapi import Error
from rest_framework.decorators import api_view
from rest_framework.response import Response
from project.game.documents import get_homepage, get_game
from project.game.models import Game
from project.game.serializers import PlayTurnSerializer


@api_view(['GET', 'POST'])
def homepage(request):
    if request.method == 'POST':
        instance = Game.objects.create()
        doc = get_game(instance)
        return Response(doc)

    doc = get_homepage()
    return Response(doc)


@api_view(['GET', 'PUT'])
def game_detail(request, pk):
    try:
        instance = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        error = Error(['Game not found.'])
        return Response(error, status=404)

    if request.method == 'PUT':
        serializer = PlayTurnSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        instance.play(serializer.validated_data['position'])

    doc = get_game(instance)
    return Response(doc)
