import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
pd.options.mode.chained_assignment = None 


#Inputs: 'all' or desired variables

selected_leagues =  ['Premier League']      #['La Liga, 'Serie A']
selected_seasons = 'all'                    # ['2009/2010', '2015/2016'] etc
selected_teams = 'all'                      # ['Manchester United', 'Barcelona']
selected_ranks = 'all'

pc = 'principal component 2'

#Type of Legend: 'Leagues', 'Year', 'Teams', 'Rank'
type_of_plot = 'Year'

#Label for points: 'Team', 'Season', 'SelTeams', 'Key'
label = 'Team'

#to show specific teams only, select 'SelTeams for label'
selective_teams = ['']



#Load data
data = pd.read_csv (r'.\Complete Dataset 2.csv') 
data = data[data.League != 'Champions League' ]



#Grouping attributes 

club_string_var = {'Key','Team','League','Season','Rank','yearsplit' }
season_standings = {'Key','Rank','Games','Wins','Draws','Losses','GoalsFor','GoalsAgainst','GoalDifference'}

all_key_attributes = {'Key','Team','League','Season','Rank','yearsplit','PassSuccess','ShortPassesPerGame',
                  'TotalShotsPerGame', 
                  'CrossesPerGame','LongBallsPerGame', 'ThroughBallsPerGame', 
                  'ShotsOnTargetPer90','ShotsOnTargetAgainstPer90','AerialDuelsWonPerGame',
                  'SuccessfulDribblesPerGame', 'OffsidesPerGame','InterceptionsPerGame',
                  'FoulsPerGame','FouledPerGame', 'TotalTacklesPerGame'}  

passing_attributes = {'Key','Team','League','Season','Rank','yearsplit','Possession','PassSuccess','ShortPassesPerGame',
                  'CrossesPerGame','LongBallsPerGame', 'ThroughBallsPerGame','TotalPassesPerGame', 
                  'SuccessfulDribblesPerGame','TotalDribblesPerGame','TotalKeyPassesPerGame', 
                  'LongKeyPassesPerGame','ShortKeyPassesPerGame'} 

defensive_attributes = {'Key','Team','League','Season','Rank','yearsplit', 'DisspossedPergame',
                  'ShotsOnTargetAgainstPer90','AerialDuelsWonPerGame','ClearancesPerGame',
                  'DribbledPastPerGame', 'InterceptionsPerGame',
                  'FoulsPerGame','FouledPerGame', 'TotalTacklesPerGame'}  


#Creating attributes

data['OutOfBoxRatio']=data['OutOfBoxGoalsPerGame']/data['OutOfBoxShotsPerGame']
data['SixYardBoxRatio']=data['SixYardGoalsPerGame']/data['SixYardBoxShotsPerGame']
data['PenaltyAreaRatio']=data['PenaltyAreaGoalsPerGame']/data['PenaltyAreaShotsPerGame']
data['GoalsRatio']=data['GoalsPerGame']/data['ShotsOnTargetPer90']

shooting_attributes = {'Key','Team','League','Season','Rank','yearsplit','TotalShotsPerGame', 'ShotsOnTargetPer90', 
                       'OffsidesPerGame', 'OutOfBoxShotsPerGame', 'SixYardBoxShotsPerGame','PenaltyAreaShotsPerGame', 
                       'GoalsPerGame', 'SixYardGoalsPerGame', 'PenaltyAreaGoalsPerGame', 'OutOfBoxGoalsPerGame',
                        'OpenPlayGoals', 'CounterAttackGoals', 'SetPieceGoals'}  

shooting1_attributes = {'Key','Team','League','Season','Rank','yearsplit','TotalShotsPerGame', 
                       'OffsidesPerGame', 'OutOfBoxRatio','SixYardBoxRatio','PenaltyAreaRatio','GoalsRatio',
                        'OpenPlayGoals', 'CounterAttackGoals', 'SetPieceGoals'}  


defensive1_attributes = {'Key','Team','League','Season','Rank','yearsplit', 'TotalAttemptedTacklesPerGame',
                  'ShotsOnTargetAgainstPer90','AerialDuelsWonPerGame','ClearancesPerGame','Possession',
                  'DribbledPastPerGame', 'InterceptionsPerGame', 'YellowCardPerGame','RedCardPerGame',
                  'FoulsPerGame', 'TotalTacklesPerGame','ShotsBlockedPerGame','CrossesBlockedPerGame'} 

playing_attributes = {'Key','Team','League','Season','Rank','yearsplit','Touches', 'TouchesDefPen',
       'TouchesDefThird', 'TouchesMidThird', 'TouchesAttThird',
       'TouchesAttPen', 'LiveTouches', 'NumOfPlayersDribbledPast', 'Nutmegs',
       'Controlled', 'DistMovedWithBall', 'ProgressiveDistMoved', 'ProgC',
       'ProgressiveIntoFinalThird', 'ProgressiveInto18Yard', 'Miscontrols',
       'MiscontrolsAfterTackle', 'ProgressivePassReceived'}

playing1_attributes = {'Key','Team','League','Season','Rank','yearsplit','Touches', 'TouchesDefPen',
       'TouchesDefThird', 'TouchesMidThird', 'TouchesAttThird','TouchesAttPen', 'OpenPlayGoals',
       'CounterAttackGoals', 'SetPieceGoals'}


pad = {'Key', 'Team', 'League', 'Season', 'Rank','yearsplit', 'Possession', 'Touches', 
    'SixYardGoalsPerGame', 'PenaltyAreaGoalsPerGame', 'OutOfBoxGoalsPerGame', 
       'OpenPlayGoals', 'CounterAttackGoals'}


gk = { 'Key','Team','League','Season','Rank','yearsplit','ShotsBlockedPerGame',
       'CrossesBlockedPerGame', 'TiotalSavesPerGame', 'SixYardSavesPerGame',
       'PenaltyAreaSavesPerGame', 'OutOfBoxSavesPerGame'}

#Choose attributes for analysis 
key_attributes = pad


#sort out data
selected_data = pd.DataFrame(data, columns= key_attributes)
selected_data.fillna(0, inplace=True)
team_profile = pd.DataFrame(data, columns= club_string_var)
team_standings = pd.DataFrame(data, columns= season_standings)

sorted_data = selected_data
top_data = sorted_data.reset_index(drop=True)
top_teams_profile = pd.DataFrame(top_data, columns = club_string_var)
top_data.drop(club_string_var,axis=1, inplace=True)


#PCA Calculation

data_centered = top_data.apply(lambda x: x-x.mean()) 
scaler = StandardScaler()
data_centered[data_centered.columns]= scaler.fit_transform(data_centered[data_centered.columns])
pca = PCA(n_components= len(key_attributes)-len(club_string_var))
principalComponents = pca.fit_transform(data_centered) 

principalDf = pd.DataFrame(data = principalComponents[:,0:3]
             , columns = ['principal component 1', 'principal component 2','principal component 3'])
finalDf = pd.concat([principalDf, top_teams_profile], axis = 1)



#Select Data to be shown

if selected_leagues == 'all':
    finalDf = finalDf
    unique_leagues = finalDf.League.unique()
else: 
    finalDf = finalDf[finalDf['League'].isin(selected_leagues)]
    unique_leagues = selected_leagues

if selected_seasons == 'all':
    finalDf = finalDf
    unique_seasons = finalDf.Season.unique()
else:
    finalDf = finalDf[finalDf['Season'].isin(selected_seasons)]
    unique_seasons = selected_seasons

if selected_teams == 'all':
    finalDf = finalDf
    unique_teams = finalDf.Team.unique()
else:
    finalDf = finalDf[finalDf['Team'].isin(selected_teams)]
    unique_teams = selected_teams

if selected_ranks == 'all':
    finalDf = finalDf
    unique_ranks = finalDf.Rank.unique()
else:
    finalDf = finalDf[finalDf.Rank <= selected_ranks]
    unique_ranks = finalDf.Rank.unique()


#Plotting 

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel(pc, fontsize = 15)
ax.set_title('2 Component PCA for the Bundesliga', fontsize = 20)


fig2 = plt.figure(figsize = (8,8))
ax2 = fig2.add_subplot(1,1,1) 
ax2.set_xlabel('Principal Component')
ax2.set_ylabel('Explained Variance (%)')
ax2.set_title('Plot of Variance explained against Principal Components')
ax2.set_ylim([0 , 100])
ax2.plot(range(1,len(pca.explained_variance_ratio_)+1), (pca.explained_variance_ratio_.cumsum())*100, 'r',label ='Cumulative' )
ax2.bar(range(1,len(pca.explained_variance_ratio_)+1), (pca.explained_variance_ratio_*100),label = 'Individual')
ax2.legend()
ax2.grid()


fig1 = plt.figure(figsize = (8,8))
ax1 = fig1.add_subplot(1,1,1) 
ax1.set_xlabel('Principal Component 1', fontsize = 15)
ax1.set_ylabel(pc, fontsize = 15)
ax1.set_title('Plot of projected variables using PCA', fontsize = 20)

 

   
if type_of_plot == 'Leagues':
    
    colors = ['black','red','greenyellow',
              'deepskyblue', 'midnightblue','violet']
    for league, color in zip(unique_leagues,colors):
        indicesToKeep = finalDf['League'] == league
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, pc]
               , c = color
               , s = 50)
    ax.legend(unique_leagues,loc = 'lower right',bbox_to_anchor=(1.25, 0.5))
    
elif type_of_plot == 'Year':
   
#    colors = ['black','grey','lightcoral','red','bisque','orange','greenyellow','forestgreen',
 #             'aquamarine','deepskyblue', 'midnightblue','violet','purple']
    
    colors = ['red','greenyellow','midnightblue', 'aquamarine','purple','orange','black',
              'violet','aquamarine','deepskyblue','grey',
              'lightcoral' ,'bisque']
    for season, color in zip(unique_seasons,colors):
        indicesToKeep = finalDf['Season'] == season
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, pc]
               , c = color
               , s = 50)
    ax.legend(unique_seasons,loc = 'lower right',bbox_to_anchor=(1.25, 0.5))

elif type_of_plot == 'Teams':
   
    colors = ['black','red', 'midnightblue','forestgreen','orange','greenyellow',
              'violet','aquamarine','deepskyblue','purple','grey',
              'lightcoral' ,'bisque']
    for team, color in zip(unique_teams,colors):
        indicesToKeep = finalDf['Team'] == team
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, pc]
               , c = color
               , s = 50)
    ax.legend(unique_teams,loc = 'lower right',bbox_to_anchor=(1.25, 0.5))


elif type_of_plot == 'Rank':
   
    colors = ['black','red', 'midnightblue','forestgreen','orange','greenyellow',
              'violet','aquamarine','deepskyblue','purple','grey',
              'lightcoral' ,'bisque']
    for rank, color in zip(unique_ranks,colors):
        indicesToKeep = finalDf['Rank'] == rank
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, pc]
               , c = color
               , s = 50)
    ax.legend(unique_ranks,loc = 'lower right',bbox_to_anchor=(1.25, 0.5))


ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
 

#Plot Variance graph

pca_values=pca.components_

  #Create broken lines
minylim = min(pca_values[1,:])-0.25
maxylim = max(pca_values[1,:])+0.25
minxlim = min(pca_values[0,:])-0.25
maxxlim = max(pca_values[0,:])+0.25

ax1.set_xlim([minxlim , maxxlim ])
ax1.set_ylim([minylim , maxylim ])
ax1.axhline(y=0, color='k')
ax1.axvline(x=0, color='k')

colors = ['r', 'b', 'k','y', 'g','c','m']
if len(pca_values[0]) > 6:
        colors=colors*(int(len(pca_values[0])/6)+1)


add_string=""
for i in range(len(pca_values[0])):
        xi=pca_values[0][i]
        yi=pca_values[1][i]
        plt.arrow(0,0, 
              dx=xi, dy=yi, 
              head_width=0.03, head_length=0.03, 
              color=colors[i], length_includes_head=True)
        add_string=f" ({round(xi,2)} {round(yi,2)})"
        plt.text(pca_values[0, i], 
             pca_values[1, i] , 
             s=top_data.columns[i]  )


#Assign labels to  plot

labels = finalDf 

if label == 'Team':
    
    annotations=labels['Team'].values
    xi=labels[ 'principal component 1'].values          
    yi=labels[ pc].values       

    for i in range(len(labels)):
        ax.text(xi[i],yi[i],s=annotations[i])

elif label == 'Season':
    
    annotations=labels['Season'].values
    xi=labels[ 'principal component 1'].values          
    yi=labels[ pc].values       

    for i in range(len(labels)):
        ax.text(xi[i],yi[i],s=annotations[i])

elif label == 'Key':
    
    annotations=labels['Key'].values
    xi=labels[ 'principal component 1'].values          
    yi=labels[ pc].values       

    for i in range(len(labels)):
        ax.text(xi[i],yi[i],s=annotations[i])
 
elif label == 'SelTeams':
    
    labels = labels[labels['Team'].isin(selective_teams)]
    
    annotations=labels['Team'].values
    xi=labels[ 'principal component 1'].values          
    yi=labels[ pc].values       

    for i in range(len(labels)):
        ax.text(xi[i],yi[i],s=annotations[i])
        
      
ax.grid()
ax1.grid()
print(pca.explained_variance_ratio_)

#/kaggle/input/performance-data-on-football-teams-09-to-22/Complete Dataset 2.csv