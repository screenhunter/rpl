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
	for member in db.child("rplmember").get().each():
		teamList[int(member.key())] = str(member.val())
	teamData = {}
	for team in db.child("teams").shallow().get().each():
		team = str(team)
		teamData[team] = {}
		teamData[team]["positions"] = {}
		for item in db.child("teams").child(team).get().each():
			if str(item.key()) == 'abbr' or str(item.val()) == '-':
				continue
			elif str(item.key()) == 'team':
				teamData[team]['name'] = str(item.val())
			else:
				teamData[team]["positions"][str(item.key())] = teamList[item.val()]

	return render(request, 'teams.html', {"teamData" : teamData})
