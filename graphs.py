import matplotlib.pyplot as plt
plt.plot([1,2],[1,2])

#1
plt.scatter([0,1,5,10,15,30,50,100,1000],[0.61,0.64,0.63,0.627,0.623,0.622,0.619,0.618,0.615],color='red')
plt.plot([0,1,5,10,15,30,50,100,1000],[0.61,0.64,0.63,0.627,0.623,0.622,0.619,0.618,0.615],color='blue')
plt.title('change in no. of basis functions vs ERMS')

#2
plt.scatter([0.001,0.5,10,20,1000],[0.6278,0.6282,0.6282,0.6283,0.6352],color='red')
plt.plot([0.001,0.5,10,20,1000],[0.6278,0.6282,0.6282,0.6283,0.6352],color='blue')
plt.title('change in regularizer lambda vs ERMS')

#3
plt.scatter([2,10,50,100,500,1000],[0.70,0.640,0.626,0.627,0.6288,0.6288],color='red')
plt.plot([2,10,50,100,500,1000],[0.70,0.640,0.626,0.627,0.6288,0.6288],color='blue')
plt.title('Change in scale of variance vs ERMS')

#4
plt.scatter([0.01,0.05,0.1],[0.624,0.630,0.687],color='red')    
plt.plot([0.01,0.05,0.1],[0.624,0.630,0.687],color='blue')
plt.title('Change in learning rate vs ERMS')

#5
plt.title('intial weight scaler(SGD) vs ERMS')
plt.scatter([1,100,1000],[0.624,0.624,0.624],color='red')
plt.plot([1,100,1000],[0.624,0.624,0.624],color='blue')

plt.title('No of iterations(SGD) vs ERMS')
plt.scatter([10,100,200,400,800],[128.32,18.2826,0.711,0.624,0.624],color='red')
plt.plot([10,100,200,400,800],[128.32,18.2826,0.711,0.624,0.624],color='blue')
