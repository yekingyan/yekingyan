#-------------------------------------------------------------------------------
# Name:        overtak the basketball soure
# Purpose:     Calculat the probability of a basketball score being overtaken
# Author:      yekingyan
# Created:     24/04/2018
#-------------------------------------------------------------------------------

points = int(input('what\'points now?:')) #输入分数
cut3 = points - 3
hasball = raw_input('Do the leading  team has ball (yes/no)')#确认控球
if hasball == "yes":
    cut3 += 0.5
else:
    cut3 -= 0.5
if cut3 <= 0:
    cut3 =0
time = int(raw_input('how much second if left?'))#终场时间
if cut3 ** 2 > time:
    print 'safe'
else:
    print 'dangerouse'