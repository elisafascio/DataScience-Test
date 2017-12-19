# Your code here
import scipy as s
# ploteamos sin filtrar
plt.plot(ice['year'], ice['extent'],"o", alpha=0.3)
plt.show()

outliers=ice['extent'].mean()-2*ice['extent'].std() 
ice2=ice[ice['extent']>outliers]

# ploteamos por año
plt.plot(ice2['year'], ice2['extent'], "o", alpha=0.3);
plt.show()

# ploteamos por mes
plt.plot(ice2['mo'], ice2['extent'], "o", alpha=0.3);
plt.show()

m_month=s.zeros(12) # Inicializo el vector
# Media de cada mes
for i in range(12):
    m_month[i]=ice2[ice2['mo']==i+1]['extent'].mean()

#print(m_month)

# ploteamos por mes juntamente con la media calculada
plt.plot(ice2['mo'], ice2['extent'], "o", alpha=0.3);
plt.plot(range(1,13),m_month)
plt.show()

ice3=ice2.copy()
# divido los datos por la media del mes correspondiente
for i in range(12):
      ice3.loc[ice2['mo']==i+1,'extent']=ice3.loc[ice2['mo']==i+1,'extent']/m_month[i]

plt.plot(ice3['mo'], ice3['extent'], "o", alpha=0.3)        
plt.show()  

# Grafica de regresión
sns.lmplot("year", "extent", ice3,size=5.2,aspect=2);
