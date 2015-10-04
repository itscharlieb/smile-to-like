

positive_emotions = [
    'Surprise',
    'Happy'
]

negative_emotions = [
    'Angry',
    'Sad',
    'Fear'
]

def evaluate_emotions(emotions):
    """
    :param sentiment: dictionary of emotion confidence values
    {
        'Angry': 0.045094480494860416,
        'Sad': 0.2778825610330746,
        'Neutral': 0.17818214943006888,
        'Surprise': 0.14929227925479832,
        'Fear': 0.2930846594989194,
        'Happy': 0.05646387028827803
    }

    :return: one of 'LIKE', 'NORESPONSE', 'DISLIKE'
    """
    epsilon = .1
    negativity = sum(map(lambda emotion: emotions[emotion], negative_emotions))
    positivity = sum(map(lambda emotion: emotions[emotion], positive_emotions))
    if positivity - negativity > 0:
        return 'LIKE'
    else:
        return 'DISLIKE'


emos = {
    'Angry': 0.045094480494860416,
    'Sad': 0.2778825610330746,
    'Neutral': 0.17818214943006888,
    'Surprise': 0.14929227925479832,
    'Fear': 0.2930846594989194,
    'Happy': 0.05646387028827803
}

print evaluate_emotions(emos)

