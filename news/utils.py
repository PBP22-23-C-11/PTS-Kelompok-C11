from .models import Subscribe

def get_subscribed_id(user):
    ret = []
    subscribe_list = Subscribe.objects.filter(user__id=user.id)
    for subscribe in subscribe_list:
        ret.append(subscribe.user.id)
    return ret