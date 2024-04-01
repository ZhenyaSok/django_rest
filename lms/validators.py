from rest_framework import serializers

SCAM_URL = 'youtube.com'
def validator_scam_url(link):
    if SCAM_URL not in link:
        raise serializers.ValidationError('Необходимо прикрепить ссылку на YOUTUBE')

