from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .serializers import ClubSerializer, PlayerSerializer, CoachSerializer
from .services import (
    create_club, create_player, create_coach, get_clubs,
    delete_club, update_player, delete_player, update_coach, delete_coach, get_individual_club, getPlayer
)
# Create your views here.


@extend_schema(
    request=ClubSerializer,
    responses={201: dict},
)
class ClubCreateView(APIView):
    def post(self, request):
        serializer = ClubSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        club_id = create_club(serializer.validated_data)
        return Response({"club_id": club_id}, status=201)


@extend_schema(
    responses={204: None, 404: dict},
)
class ClubDeleteView(APIView):
    def delete(self, request, club_id):
        if delete_club(club_id):
            return Response(status=204)
        return Response({"error": "Club not found"}, status=404)


@extend_schema(
    request=PlayerSerializer,
    responses={201: dict, 400: dict},
)
class PlayerCreateView(APIView):
    def post(self, request, club_id):
        serializer = PlayerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            player_id = create_player(club_id, serializer.validated_data)
            return Response({"player_id": player_id}, status=201)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)


@extend_schema(
    request=PlayerSerializer,
    responses={200: dict, 404: dict},
)
class PlayerUpdateView(APIView):
    def put(self, request, player_id):
        serializer = PlayerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if update_player(player_id, serializer.validated_data):
            return Response({"message": "Player updated successfully"}, status=200)
        return Response({"error": "Player not found"}, status=404)


@extend_schema(
    responses={204: None, 404: dict},
)
class PlayerDeleteView(APIView):
    def delete(self, request, player_id):
        if delete_player(player_id):
            return Response(status=204)
        return Response({"error": "Player not found"}, status=404)


@extend_schema(
    request=CoachSerializer,
    responses={201: dict},
)
class CoachCreateView(APIView):
    def post(self, request, club_id):
        serializer = CoachSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        coach_id = create_coach(club_id, serializer.validated_data)
        return Response({"coach_id": coach_id}, status=201)


@extend_schema(
    request=CoachSerializer,
    responses={200: dict, 404: dict},
)
class CoachUpdateView(APIView):
    def put(self, request, coach_id):
        serializer = CoachSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if update_coach(coach_id, serializer.validated_data):
            return Response({"message": "Coach updated successfully"}, status=200)
        return Response({"error": "Coach not found"}, status=404)


@extend_schema(
    responses={204: None, 404: dict},
)
class CoachDeleteView(APIView):
    def delete(self, request, coach_id):
        if delete_coach(coach_id):
            return Response(status=204)
        return Response({"error": "Coach not found"}, status=404)


@extend_schema(
    responses={200: dict},
)
class ClubListView(APIView):
    def get(self, request):
        clubs = get_clubs()
        return Response(clubs, status=200)


@extend_schema(
    responses={200: dict, 404: dict},)
class GetIndividualClubView(APIView):
    def get(self, request, club_id):
        club = get_individual_club(club_id)
        if club:
            return Response(club, status=200)
        return Response({"error": "Club not found"}, status=404)


@extend_schema(
    responses={200: dict, 404: dict},)
class GetIndividualPlayerView(APIView):
    def get(self, request, player_id):
        player = getPlayer(player_id)
        if player:
            return Response(player, status=200)
        return Response({"error": "Player not found"}, status=404)
