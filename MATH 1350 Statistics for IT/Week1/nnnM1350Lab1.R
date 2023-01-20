server1data <- read.delim("C:/Users/Markus/OneDrive - BCIT/Desktop/Term2/MATH 1350 Statistics for IT/Week1/server1data.txt", comment.char="#")
?read.delim
setwd("C:/Users/Markus/OneDrive - BCIT/Desktop/Term2/MATH 1350 Statistics for IT/Week1")
Server2Data=read.delim("server2data.txt",header=TRUE,sep="\t",na.strings="NA",comment.char="#")
histogram(~log(Time), data=server1data)
histogram(~log(Time), data=Server2Data)
mean(~Time, data=server1data)
mean(~Time, data=Server2Data)