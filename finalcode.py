import numpy as np
import matplotlib.pyplot as plot 
import csv 
import timeit
ind_var=[]
open_price=[]
mean=0
meanY=0
Sxx=0
Sxy=0
B0=0
B1=0
i=0
j=0
def DataExtraction() :
	gg=input("Please Enter the name of the Csv file to be analysed")
	with open(gg,"r")as pfile :
		pfileReader=csv.reader(pfile)
		for row in pfileReader:
			ind_var.append(float(row[0]))
			open_price.append(float(row[1]))
	print(ind_var)
	print(open_price)

def CrossDeviation(ind_var,open_price):
		global B1,B0
		mean=np.mean(ind_var)
		meanY=np.mean(open_price)
		n=np.size(ind_var)
		e=n*mean*meanY
		Sxy=np.sum((np.array(ind_var)-mean)*(np.array(open_price)-meanY))
		Sxx=np.sum((np.array(ind_var)-mean)**2)
		print(Sxx)
		B1=(Sxy/Sxx)
		B0=(meanY-B1*mean)
		print("The value of Sxx is ",Sxx)
		print("\n The value of Sxy is ",Sxy)
		
def GraphPlotter(ind_var,open_price,B1,B0):
		plot.xlabel('Dates')
		plot.ylabel('Opening Price of Stock')
		x=ind_var
		y=open_price
		x1=ind_var
		y1=np.array(x)*B1+B0
		plot.scatter(x,y,label="dot",color="r",marker=".",s=30)
		plot.plot(x,y1)
		plot.show()
		
def main():
		start=timeit.default_timer()
		global checkpred,predstock
		DataExtraction()
		CrossDeviation(ind_var,open_price)
		stop=timeit.default_timer()
		GraphPlotter(ind_var,open_price,B1,B0)
		print("The value of B1 is",B1)
		print("\n The value of B0 is ",B0)
		print("\n Enter the day for which you want the predicted opening stock price:")
		checkpred=int(input("\n"))
		predstock=checkpred*B1+B0
		print(predstock)
		print("Time to compute data was",(stop-start))
		
main()
