import random
from app.data.hashtags import HASHTAGS

def get_hashtags(topic, count):
    tags = HASHTAGS[topic]
    return random.sample(tags, min(count, len(tags)))