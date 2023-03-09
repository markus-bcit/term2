# lab 7
# markus afonso

library(mosaic)

A00digits <- read.delim("C:/Users/Markus/OneDrive - BCIT/Desktop/Term2/MATH 1350 Statistics for IT/Week9/A00numbers.csv", comment.char="#")

histogram(~Digits,data=A00digits, main = "Digits",
          xlab = "Digits", ylab = "Density",width=1)

favstats(~Digits,data=A00digits)


n <- 1:100
sample_sizes <- c(2,4,8,16,32,64) 
samplemeans <- matrix(0,length(n), 6)

for (j in 1:6) {
  for (i in n) {
    y <- sample (A00digits, sample_sizes [j],replace=TRUE) 
    samplemeans [i, j] <- mean (~Digits, data=y)
  }
}

size2 <- samplemeans [,1]
size4 <- samplemeans [,2]
size8 <- samplemeans [,3]
size16<- samplemeans [,4]
size32 <- samplemeans [,5]
size64 <- samplemeans [,6]

histogram(size8, main = "Size8",
         xlab = "Digits", ylab = "Density",width=1)

favstats(size2)
favstats(size4)
favstats(size8)
favstats(size16)
favstats(size32)
favstats(size64)

histogram(size16, main = "size16",
          xlab = "Digits", ylab = "Density",width=1)

heights <- read.delim("C:/Users/Markus/OneDrive - BCIT/Desktop/Term2/MATH 1350 Statistics for IT/Week9/heights.csv", comment.char="#")

n <- 1:100
sample_sizes <- c(2,4,8,16,32,64) 
samplemeans <- matrix(0,length(n), 6)

for (j in 1:6) {
  for (i in n) {
    y <- sample (heights, sample_sizes [j],replace=TRUE) 
    samplemeans [i, j] <- mean (~Height, data=y)
  }
}

size2 <- samplemeans [,1]
size4 <- samplemeans [,2]
size8 <- samplemeans [,3]
size16<- samplemeans [,4]
size32 <- samplemeans [,5]
size64 <- samplemeans [,6]

histogram(size16, main = "Size16 of Heights",
          xlab = "Height", ylab = "Density",width=1)


favstats(size2)
favstats(size4)
favstats(size8)
favstats(size16)
favstats(size32)
favstats(size64)

#1
#a
1-pnorm(31000, 30000, 4500)
#b
1-pnorm(31000, 30000, 711.5)
#c
1-pnorm(31000, 30000, 201.2461)

#2
pnorm(2890, 2900, 3.6770)

#3
1-pnorm(55000, 50000, 1732.0508)