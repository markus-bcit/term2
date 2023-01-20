# Lab 2
# Markus Afonso

library(mosaic)

examscores <- read.delim("C:/Users/Markus/OneDrive - BCIT/Desktop/Term2/MATH 1350 Statistics for IT/Week2/examscores.txt", comment.char="#")

with(examscores,stem(Score))
par(mfrow=c(1,2))
histogram(Score~Set, data=examscores)
histogram(~Score|Set, data=examscores,layout=c(1,2), main = "Exam Scores",
          xlab = "Scores", ylab = "Percentage of Students", type = "p",
          col="black", breaks=seq(30,80,5), width=10)


examscores$Set=as.factor(examscores$Set)

mean(~Score,data=examscores)
median(~Score,data=examscores)
sd(~Score,data=examscores)
var(~Score,data=examscores)
min(~Score,data=examscores)
max(~Score,data=examscores)
IQR(~Score,data=examscores)

favstats(Score~Set,data=examscores)

sum(Score~Set,data=examscores)

with(examscores, quantile(Score, 0.99))


histogram(~Score|Set,data=examscores)
