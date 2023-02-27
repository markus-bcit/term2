# lab 6
# markus afonso

library(mosaic)

#1
pnorm(2.52)
pnorm(2.14) - pnorm(-1.06)
pnorm(-0.72)
1 - pnorm(-2.03)
#2
pnorm(90,97.27,10.84)
pnorm(120,97.27,10.84) - pnorm(100,97.27,10.84)
1 - pnorm(95,97.27,10.84)
#3
0.06731862 <= pnorm(x,44.9, 1.27) <= 0.9926756

pnorm(x,44.9, 1.27)

(qnorm(pnorm(48,44.9, 1.27),44.9, 1.27) + qnorm(pnorm(43,44.9, 1.27),44.9, 1.27))

(1 - (pnorm(48,44.9, 1.27) - pnorm(43,44.9, 1.27))) * 100

#4
qnorm(.02, 5570, 237)

#5 
qnorm(.99,65.24, 7.42)
pnorm(60,51.22, 10.67)

u1 <-65.24
o1 <-7.24
u2 <-51.22
o2 <-10.67

#Question 5
#a
sqrt(sqrt(o1)+ sqrt(o2))

o12 <- sqrt(sqrt(o1)+ sqrt(o2))
1- pnorm(120, (u1 +u2), o12)

#b
pnorm(100, (bat1_mean +bat2_mean), comb_sd)

#6

pnorm(5.168, 5.168, 1.23)


pnorm(log(115,2.7182818284590452353602874713527), 5.168, 1.23)

1 - pnorm(log(180,2.7182818284590452353602874713527), 5.168, 1.23) 





