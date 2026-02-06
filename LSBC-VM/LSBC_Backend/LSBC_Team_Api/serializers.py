from rest_framework import serializers


class ClubSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    club_logo = serializers.URLField(required=False, allow_blank=True)
    address = serializers.CharField(
        max_length=200, required=False, allow_blank=True)
    Lga = serializers.CharField(
        max_length=100, required=False, allow_blank=True)
    contact_information = serializers.CharField(
        max_length=100, required=False, allow_blank=True)
    club_status = serializers.ChoiceField(choices=['away', 'home'])


class PlayerSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    photo = serializers.URLField(required=False, allow_blank=True)
    position = serializers.CharField(
        max_length=50, required=False, allow_blank=True)
    height = serializers.FloatField(required=False)
    weight = serializers.FloatField(required=False)
    dob = serializers.DateField(required=False)
    jersey_number = serializers.IntegerField(required=False)
    jersey_color = serializers.CharField(
        max_length=20, required=False, allow_blank=True)
    phone_number = serializers.CharField(
        max_length=20, required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    sex = serializers.ChoiceField(choices=['male', 'female'], required=False)


class CoachSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=50)
    photo = serializers.URLField(required=False, allow_blank=True)
    address = serializers.CharField(
        max_length=200, required=False, allow_blank=True)
    contact_information = serializers.CharField(
        max_length=100, required=False, allow_blank=True)
    sex = serializers.ChoiceField(choices=['male', 'female'], required=False)
    email = serializers.EmailField(required=False, allow_blank=True)
    role = serializers.ChoiceField(
        choices=['Head Coach', 'Assistant Coach'], required=False)
