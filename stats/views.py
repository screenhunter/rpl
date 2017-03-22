from django.shortcuts import render
from django.conf import settings
db = settings.FIREBASE_DB

# Create your views here.
def list_stats(request):
	#pull data from db here
	#compute information
	return render(request, 'teams.html', {'items': ""})

def view_teams(request):
	teamList = {}
	pulled_data = db.get().val()
	for member in pulled_data["rplmember"]:
		teamList[member] = pulled_data["rplmember"][member]
	teamData = {}
	teamList["-"] = "None"
	for team in pulled_data["teams"]:
		team = pulled_data["teams"][team]
		teamData[team["team"]] = {
			"top": teamList[str(team["top"])],
			"jgl": teamList[str(team["jgl"])],
			"mid": teamList[str(team["mid"])],
			"adc": teamList[str(team["adc"])],
			"sup": teamList[str(team["sup"])]
		}
		if (team["coach"] != "-"):
			teamData[team["team"]]["coach"] = teamList[str(team["coach"])]
		if (team["sub1"] != "-"):
			teamData[team["team"]]["sub1"] = teamList[str(team["sub1"])]
		if (team["sub2"] != "-"):
			teamData[team["team"]]["sub1"] = teamList[str(team["sub2"])]

	print(teamData)

	return render(request, 'teams.html', {"teamData" : teamData})
