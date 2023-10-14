from rest_framework.views import APIView, Request, Response, status
from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError
from utils import data_processing
from .models import Team
from django.forms import model_to_dict


class TeamsView(APIView):
    def get(self, req: Request) -> Response:
        teams = Team.objects.all()
        converted_teams = []
        for teams in teams:
            current_team = model_to_dict(teams)
            converted_teams.append(current_team)
        return Response(converted_teams, status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        try:
            data_processing(req.data)
        except (
            NegativeTitlesError,
            InvalidYearCupError,
            ImpossibleTitlesError,
        ) as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        try:
            teams = Team.objects.create(**req.data)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        converted_teams = model_to_dict(teams)
        return Response(converted_teams, status.HTTP_201_CREATED)


class TeamViewDetail(APIView):
    def get(self, req: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )
        converted_team = model_to_dict(team)
        return Response(converted_team, status.HTTP_200_OK)

    def delete(self, req: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, req: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )
        for k, v in req.data.items():
            setattr(team, k, v)

        team.save()
        converted_team = model_to_dict(team)
        return Response(converted_team, status=status.HTTP_200_OK)
