# Lab 3
# Markus Afonso

library(mosaic)

gametimes <- read.delim("C:/Users/Markus/OneDrive - BCIT/Desktop/Term2/MATH 1350 Statistics for IT/Week3/lab3.txt", comment.char="#")

bwplot(~Time,data=gametimes, main='Times Boxplot')

bwplot(Time~Set,data=gametimes, main='Times Boxplot', ylab='Set', xlab='Time')

favstats(Time~Set,data=gametimes)

#Stage 2 - Probability Experiments in R
n <- 1:20000
cointosses <- sample(c(0,1), length(n),replace=TRUE) 
payout <- 0*n
#let a 0 represent a heads up coin, a 1 represent a tails up coin 
for (i in n) {
  if (cointosses [i]==1) {
    payout [i] <- 1
  }
  else {
    payout [i] <- 0
  }
}

mean(payout)
## Cards

n <- 1:20000
cards <- sample(c(1,2,3,4,5,6,7,8,9,10,11,12,13), length(n),replace=TRUE)
dierolls <- sample(c(1,2,3,4,5,6), length(n),replace=TRUE) 
 
payout <- 0
#let a 0 represent a heads up coin, a 1 represent a tails up coin 
for (i in n) {
  if (cards[i] < 5) {
    payout[i]<- 5*dierolls[i]
  }
  else {
    payout [i] <- dierolls[i]
  }
}

mean(payout)
