from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30, default="")
    titles = models.IntegerField(default=0, null=True)
    top_scorer = models.CharField(max_length=50, default="")
    fifa_code = models.CharField(max_length=3, unique=True, default="")
    first_cup = models.DateField(null=True)

    def __repr__(self) -> str:
        return f"<[{self.id}] {self.name} - {self.fifa_code}>"
