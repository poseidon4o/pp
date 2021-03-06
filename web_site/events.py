
from django.shortcuts import get_object_or_404
from django_socketio import events

from web_site.models import Pair


@events.on_connect
def connect(request, socket, context):
    print request



@events.on_subscribe
def subscribe(request, socket, context, channel):
    return

@events.on_message(channel="^pair-code-")
def message(request, socket, context, message):
    """
    Event handler for pair data channel
    """
    print(request)


    socket.broadcast_channel(message=message)
    return
    #if 'pair_id' not in message or 'user_id' not in message:
    #    return
    #
    #pair = get_object_or_404(Pair, id=message['pair_id'])
    #
    #if pair.l_u_id != int(message['user_id']) and pair.r_u_id != int(message['user_id']):
    #    return

