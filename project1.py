#given m ballons in the box with variable r and mu to find a optimal value of r and mu which maximize
import math
class circle(object):
	"""circle class"""
	def __init__(self,r,x,y):
		#print "init a circle with r:" + str(r) + "position:(" + str(x) + "," + str(y) + ")"
		self.r = r
		self.x = x
		self.y = y
	def check(self):
		if self.x >= 1.0 or self.x <= -1.0 or self.y >= 1.0 or self.y <= -1.0:
			
			return False
		if self.r + self.x > 1.0 or self.x - self.r < -1.0:
			
			return False
		if self.r + self.y > 1.0 or self.y - self.r < -1.0:
			return False

def distance(c1,c2):
	return math.sqrt((c1.x-c2.x)*(c1.x-c2.x) + (c1.y-c2.y)*(c1.y-c2.y))

def checkSpace(circleList,newCircle):
	if newCircle.check() == False:
		#if str(newCircle.r) == str(0.5):
			#print '0.5 check error'
		return False
	for i in circleList:
		if distance(i,newCircle) < (i.r + newCircle.r):
			#print 'distance wrong'
			#print distance(i,newCircle)
			
			return False
	return True
def showList(circleList):
	for i in circleList:
		print 'x,y,r:' + str(i.x) + ' ' + str(i.y) + ' ' + str(i.r)
def sumRR(circleList):
	sum = 0
	for i in circleList:
		sum += i.r*i.r
	return sum

def ballonsInBox(m,e):
	R = 1.0/m
	sum = 0
	while True:
		if R > 1:
			print 'R > 1'
			break
		circleList = []
		firstCircle  = circle(R,-1+R,1-R)
		circleList.append(firstCircle)
		x=-1
		y=1
		while x<=1:
			y=1
			while y >= -1:
				#print "x,y:" + str(x) + ' ' + str(y) + ' r:' +str(R)
				if R == 0.5:
					print R
				testCircle = circle(R,x,y)
				if checkSpace(circleList,testCircle):
					if len(circleList) < m:
						
						circleList.append(testCircle)
						#print "add a new circle"
				y = y - e
			x = x + e


		if sumRR(circleList) > sum and len(circleList) == m:
			sum = sumRR(circleList)
			print "get a new sum:" + str(sum)
			showList(circleList)
		
		R = R + e
		
		

if __name__ == "__main__":
	ballonsInBox(3,0.01)




