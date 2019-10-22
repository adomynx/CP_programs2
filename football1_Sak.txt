
#teams ka input
no_teams=int(input())
teams=[]
for i in range(no_teams):
    name=input()
    teams.append(name)

#games kitne khele kiske against and goals uska input
no_games=int(input())
games=[]
for i in range(no_games):
    g=input()
    games.append(g)
    
#no. of games played
value=[0 for x in range(len(teams))]

no_games_played=dict(zip(teams,value))

no_games_win=dict(zip(teams,value))

no_games_loss=dict(zip(teams,value))

no_games_tie=dict(zip(teams,value))

no_points_earn=dict(zip(teams,value))

no_goals_own=dict(zip(teams,value))

no_goals_against=dict(zip(teams,value))

for i in games:
    x=i.split("#")
    no_games_played[x[0]]=no_games_played[x[0]]+1
    no_games_played[x[2]]=no_games_played[x[2]]+1

    #goals kitne kiye and kitne oponent team ne kiye
    no_goals_own[x[0]]=no_goals_own[x[0]]+int(x[1][0])
    no_goals_against[x[0]]=no_goals_against[x[0]]+int(x[1][2])

    no_goals_own[x[2]]=no_goals_own[x[2]]+int(x[1][2])
    no_goals_against[x[2]]=no_goals_against[x[2]]+int(x[1][0])

    if(int(x[1][0])>int(x[1][2])):
        no_games_win[x[0]]=no_games_win[x[0]]+1
        no_points_earn[x[0]]=no_points_earn[x[0]]+3 #win add points
        no_games_loss[x[2]]=no_games_loss[x[2]]+1
        no_points_earn[x[2]]=no_points_earn[x[2]]+0 #loss 0 points
    elif(int(x[1][0])<int(x[1][2])):
        no_games_win[x[2]]=no_games_win[x[2]]+1
        no_points_earn[x[2]]=no_points_earn[x[2]]+3 #win add points
        no_games_loss[x[0]]=no_games_loss[x[0]]+1
        no_points_earn[x[0]]=no_points_earn[x[0]]+0 #loss 0 points
    else:
        no_games_tie[x[0]]=no_games_tie[x[0]]+1
        no_games_tie[x[2]]=no_games_tie[x[2]]+1
        no_points_earn[x[0]]=no_points_earn[x[0]]+1
        no_points_earn[x[2]]=no_points_earn[x[2]]+1

   

print(no_points_earn)
print(no_games_win)
print(no_games_tie)
print(no_games_loss)
print(no_games_played)
print(no_goals_own)
print(no_goals_against)

for i in teams:
    print(i," ",no_points_earn[i],"p"," ",no_games_played[i],"g"," ","(",no_games_win[i],"-",no_games_tie[i],"-",no_games_tie[i],")")
