from django.shortcuts import render
from django.conf import settings
db = settings.FIREBASE_DB

# Create your views here.
def list_stats(request):
	#pull data from db here
	#compute information
	return render(request, 'teams.html', {'items': ""})

def view_teams(request):
	pulled_data = db.child("winter2017").get().val()
	teamData = {}
	for team in pulled_data["teams"]:
		team = pulled_data["teams"][team]
		teamData[team["abbr"]] = {
			"top": team["top"],
			"jgl": team["jgl"],
			"mid": team["mid"],
			"adc": team["adc"],
			"sup": team["sup"]
		}
		if (team["coach"] != "-"):
			teamData[team["abbr"]]["coach"] = team["coach"]
		if (team["sub1"] != "-"):
			teamData[team["abbr"]]["sub1"] = team["sub1"]
		if (team["sub2"] != "-"):
			teamData[team["abbr"]]["sub1"] = team["sub2"]

	return render(request, 'teams.html', {"teamData" : teamData})
