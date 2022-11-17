General Overview:

The attributes chosen, and their correlation with the principal components can be seen in the following figure. 

![Overall General Variables](https://user-images.githubusercontent.com/110342143/202425183-49a0b290-9913-4fe7-9a24-751f5a98721c.png)

Short passes and pass success are both positively correlated with the first principal component, 
where as defensive attributes such as tackles and fouls correlate more positively with the second
principal component.
The projected data across all 13 seasons between 2009 and 2022 can be seen in the following figure. 

![Overall General PCA](https://user-images.githubusercontent.com/110342143/202425432-ca4cde42-17c2-40d3-b321-d3bc10051f00.png)

It is interesting to see that each season forms distinct clusters, with the oldest season at the top and each successive season below
it. A lot of defensive attributes correlate positively with the second principal
component, and point towards the top left as seen in figure 5. That is also where most of the teams before 2013 are, showing us that teams were more
defensive back then relative to now, since each successive season has drifted away towards the bottom right, the opposite direction.

Short passes and pass success both correlate positively with the first principal component, and it is no surprise to see extremely successful teams
like Barcelona and Real Madrid far to the right of the rest of the teams.
Each season, they both form a distinct group, however, other teams can be seen gravitating towards them with each season, especially after 2016. This
could show the general style of football changing, from a more defensive to aggressive style across this period of time.

Defensive Overview: 

Since we know, from the general analysis, that teams have become less defensive over the years, we can analyse this in more detail by using defensive
attributes only, such as tackles, fouls and aerials won per game. 

![Overall Defensive Variables](https://user-images.githubusercontent.com/110342143/202426740-058ef7fb-a64e-4cf7-85d4-8e3274b953ed.png)


As seen in the figure above, most attributes negatively correlate with the first principal,
suggesting that teams further to the left are more defensive. Blocked shots,
red cards and shots against per game all point towards the bottom left,
suggesting teams received more shots and blocked that much more. Teams
placed towards the left generally make more tackles and interceptions per
game, where as the higher they are along the y axis, the more times their
players get dribbled past.

![Overall Defensive PCA](https://user-images.githubusercontent.com/110342143/202426999-a20cb33f-367a-4bee-81f6-9b6a2b6a8706.png)

The teams from 2009/2010 and 2010/2011 are in the bottom left of the plot in the figure above, where as newer seasons are towards the top right, further highlighting the change in defensive tactics. The lack of fouls per game in newer seasons suggests that teams now have a less aggressive style of defending and that the general quality of defending is better. As fouls are more likely to occur when a tackle or a challenge is made with a lack of precision. There is another angle to consider when explaining this change, which will be explained when discussing passing attributes.

Dribbled past correlates positively with the second principal component, therefore teams placed higher up tend to get dribbled past more then others. Newer seasons are relatively higher on the plot, suggesting that teams now have more aggressive players who like to dribble more towards opponents. This observation makes sense as a lot of successful teams rely on very skilled wingers. For example Liverpool and Manchester City, who have Mo Salah and Ryiad Mahrez respectively, players who thrive on beating defenders with their dribbling and pace. 

Passing Overview:

While tactics may differ from team to team, passing is an integral part of the sport. However, there are many types of passes which will depend on the teams playing style. Some teams prefer to play short passes to build up play, while others prefer playing long balls. Using data relating to different types, we can see if there are any distinct groups. The selected attributes are shown in  the figure below.

![Overall Passing Variables](https://user-images.githubusercontent.com/110342143/202428176-63eea25e-5633-43e8-9262-f73cf483150b.png)

Long passes, crosses and through balls correlate positively with the second principal component, therefore teams placed further up like to get the ball forward from the back quicker, Whereas short passes and possession correlate positively with the first principal component, teams placed further to the right like to build up play through short passes and possession. Teams in the lower right have players who like to dribble through the opposition. 

![Overall Passing PCA](https://user-images.githubusercontent.com/110342143/202428541-f7501538-f060-44ff-be09-89a66e8216c3.png)

While it is possible to see some sort of clustering in the figure above, it is more distinct in the figure below, which divides the data before and after the 2016/2017 season.

![Overall Passing PCA2](https://user-images.githubusercontent.com/110342143/202428891-ef6af0f2-d5cd-4b0d-8da2-59eb0ad48867.png)

Observing both plots, it is no surprise to see Barcelona standing out, almost like an outlier, towards the extreme right hand side. Barcelona are known for their "Tiki Taka" playing style, playing quick short passes to build up play, as well as one of the greatest players of our generation, Lionel Messi. Who is one of the best dribblers of the ball in the world, Therefore Barcelona gravitating towards both of those attributes is no surprise. 

However, it is still clear that teams played with more long balls and crosses before then now, while the opposite is true for short passes and dribbles. This leads back to understanding the change in defending. Fouls are more likely to occur when the ball is in the air and two players both try to gain possession of it, since the moment you have less control over your body once you are in the air. Considering the fact that teams played more crosses and long passes before, you were much more likely to be in the aforementioned state back then compared to now. Hence the chances for fouls was much higher. 

Furthermore, with teams playing more short passes, it is vital for teams to maintain their defensive formation, rather then having players charge towards the opposition, since short passes are harder to intercept then others, unless you force the opposition to make mistakes with high pressure. If a gap opens up in the defense, it is very easy for current forwards, who have great pace and dribbling skills to exploit it. Hence, from this angle, it makes sense why there are less tackles in games compared to before.


Shooting Overview:

Scoring goals is the main aim in football, analysing how and where players score from may give us some insights into other aspects. In the figure below, attributes with ratio in their name is the number of goals scored per shot from that distance.

![Overall Goals Variables](https://user-images.githubusercontent.com/110342143/202429634-7d07cfa0-b927-434d-8c29-813554e2c269.png)

The goals ratio, number of goals scored per shot is positively correlated with both principal components. While most other attributes correlate positively with the first principal component, with some relationship with the second principal component. 

![Overall Goals PCA](https://user-images.githubusercontent.com/110342143/202429538-6d6049ca-e41c-48ce-a31e-71603557cbf8.png)

Once again in the figure above, we see a distinction between each season, with the newer seasons at the top, showing a transition over the years. Teams score more per shot in general from various locations now then before yet take less shots per game in general. An interesting point to note is that there were more offsides per game in the older seasons, which makes sense as there were more through-balls per game in the older seasons as seen in figure \ref{OPVB}. More through balls means that players make a run behind the defence line more often, therefore you are more likely to get caught offside if you mistime your run or if the opposition plays an offside trap.

We will now focus on analysing the top 5 leagues in Europe. Since the focus is their playing styles, the best method using the data at hand is to use passing attributes shown in figure \ref{OPVB}. The way teams pass tells us a lot about their playing style, teams with more long passes prefer more direct football by getting the ball forward as quickly as possible, where as more short passes suggests teams prefer to slowly build up play. Since the data we have is for the last 13 seasons, we will use data from the 09/10, 15/16 and 21/22 seasons for the analysis. This shows us how teams played 13 years ago, how they play now and see if we can notice a transition in between. 

