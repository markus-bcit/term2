# Lab 4
# Markus Afonso

library(mosaic)

doordata <- read.delim("C:/Users/Markus/OneDrive - BCIT/Desktop/Term2/MATH 1350 Statistics for IT/Week4/doordata.txt", comment.char="#")
h <- 1:50
nums <- list()
for (x in h){

n <- 1:1000
winning_door <- sample(c(1,2,3), length(n),replace=TRUE)
first_pick <- sample(c(1,2,3), length(n),replace=TRUE) 
win_counter <- 0
loss_counter <- 0  
for (i in n) {
  if (winning_door[i]== first_pick[i]) {
    loss_counter <- loss_counter+1
  }
  else {
    win_counter <- win_counter +1
  }
}

nums <- append(nums, list(win_counter))
}
nums <- unlist(nums, use.names = FALSE)

histogram(nums, main = "Chances of Picking Door",
          xlab = "Scores", ylab = "Percentage of Scores", type = "p",
          col="grey", breaks=seq(620,720,10))
mean(nums)

rep(c(1:100), each=5, width=20)
