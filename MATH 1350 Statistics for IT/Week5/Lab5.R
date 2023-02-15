# Lab 5
# Markus Afonso

library(mosaic)
# 6 a
dbinom(94,1000,0.094)
#b
1 - pbinom(81,1000,0.094)
#c
pbinom(65,1000,0.094)
#d
pbinom(99,1000,0.094)
#e
1 - pbinom(74,1000,0.094)
#f
pbinom(19,1000,0.094)
#g
pbinom(90,1000,0.094) - pbinom(50,1000,0.094)
#h
dbinom(32,1000,0.094)


#7 using u = np = lamda
p <- 1.1/1000

#a
dpois(2,p*200)
#b
dpois(1,p*500) + (dpois(2,p*500) - dpois(2,p*1000))
#c
ppois(10,p*5000) - ppois(4,p*5000)

#8
a <- 0.4/60 

dpois(2, a*60)

ppois(3, a*300)

1 - ppois(2, a*120)

