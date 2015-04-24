m1 <- matrix(NA, ncol=10, nrow=100)
m2 <- matrix(NA, ncol=10, nrow=75)
m3 <- matrix(NA, ncol=10, nrow=75)
m4 <- matrix(NA, ncol=10, nrow=200)


# Purple
m1[,1] <- rbinom(100,1,.1)
m1[,2] <-rbinom(100,1,.3)
m1[,3] <-rbinom(100,1,.5)
m1[,4] <-rbinom(100,1,.6)
m1[,5] <-rbinom(100,1,.8)
m1[,6] <-rbinom(100,1,.75)
m1[,7] <-rbinom(100,1,.72)
m1[,8] <-rbinom(100,1,.7)
m1[,9] <-rbinom(100,1,.6)
m1[,10] <-rbinom(100,1,.4)

# Green
m2[,1] <- rbinom(75,1,.2)
m2[,2] <- rbinom(75,1,.35)
m2[,3] <- rbinom(75,1,.4)
m2[,4] <- rbinom(75,1,.41)
m2[,5] <- rbinom(75,1,.42)
m2[,6] <- rbinom(75,1,.4)
m2[,7] <- rbinom(75,1,.3)
m2[,8] <- rbinom(75,1,.25)
m2[,9] <- rbinom(75,1,.2)
m2[,10]<- rbinom(75,1,.15)

# Turk
m3[,1] <- rbinom(75,1,.15)
m3[,2] <- rbinom(75,1,.2)
m3[,3] <- rbinom(75,1,.25)
m3[,4] <- rbinom(75,1,.3)
m3[,5] <- rbinom(75,1,.4)
m3[,6] <- rbinom(75,1,.42)
m3[,7] <- rbinom(75,1,.41)
m3[,8] <- rbinom(75,1,.4)
m3[,9] <- rbinom(75,1,.35)
m3[,10]<- rbinom(75,1,.2)

# Red
m4[,1]  <- rbinom(200,1,.01)
m4[,2]  <- rbinom(200,1,.01)
m4[,3]  <- rbinom(200,1,.01)
m4[,4]  <- rbinom(200,1,.01)
m4[,5]  <- rbinom(200,1,.01)
m4[,6]  <- rbinom(200,1,.01)
m4[,7]  <- rbinom(200,1,.01)
m4[,8]  <- rbinom(200,1,.01)
m4[,9]  <- rbinom(200,1,.01)
m4[,10] <- rbinom(200,1,.01)


bin_dat <- data.frame(rbind(m1,m2,m3,m4))
names(bin_dat) <- c("Age_16", "Age_17", "Age_18", "Age_19", "Age_20", "Age_21", "Age_22", "Age_23", "Age_24", "Age_25")

write.csv(bin_dat, file="bindat.csv")




