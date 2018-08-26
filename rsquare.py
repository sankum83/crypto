#R-Square

print "Geting R-Square"
#X coordinate 
xcoord = [1,5,9,2,7,5]
#Y coordinate 
ycoord = [2,4,7,4,8,9]

xlen = len(xcoord)
ylen = len(ycoord)

if xlen == ylen:
    print "Coordinates are same lenght"
else:
    print "Coordinates are diffrent lenght"

#get the mean of xcoord and ycoord
xmean = sum(xcoord)
ymean = sum(ycoord)

xmean = xmean/xlen
ymean = ymean/ylen

print ("X-Mean: %.5f , and Y-Mean: %.5f"%(xmean, ymean))

#print(xmean)
print " x bar "
xbar = []
ybar = []


for x in xcoord:
    xbar.append(xmean - x)

for y in ycoord:
    ybar.append(ymean - y)


print xbar

print ybar


