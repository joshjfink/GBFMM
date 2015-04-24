library(lme4); library(dplyr); library(ggplot2)
m1 <- matrix(NA, ncol=10, nrow=500)
m2 <- matrix(NA, ncol=10, nrow=250)
m3 <- matrix(NA, ncol=10, nrow=250)
m4 <- matrix(NA, ncol=10, nrow=600)

# Purple
m1[,1] <- rbinom(500,1,.1)
m1[,2] <-rbinom(500,1,.3)
m1[,3] <-rbinom(500,1,.5)
m1[,4] <-rbinom(500,1,.6)
m1[,5] <-rbinom(500,1,.8)
m1[,6] <-rbinom(500,1,.75)
m1[,7] <-rbinom(500,1,.72)
m1[,8] <-rbinom(500,1,.7)
m1[,9] <-rbinom(500,1,.6)
m1[,10] <-rbinom(500,1,.4)

# Green
m2[,1] <- rbinom(250,1,.2)
m2[,2] <- rbinom(250,1,.35)
m2[,3] <- rbinom(250,1,.4)
m2[,4] <- rbinom(250,1,.41)
m2[,5] <- rbinom(250,1,.42)
m2[,6] <- rbinom(250,1,.4)
m2[,7] <- rbinom(250,1,.3)
m2[,8] <- rbinom(250,1,.25)
m2[,9] <- rbinom(250,1,.2)
m2[,10]<- rbinom(250,1,.15)

# Turk
m3[,1] <- rbinom(250,1,.15)
m3[,2] <- rbinom(250,1,.2)
m3[,3] <- rbinom(250,1,.25)
m3[,4] <- rbinom(250,1,.3)
m3[,5] <- rbinom(250,1,.4)
m3[,6] <- rbinom(250,1,.42)
m3[,7] <- rbinom(250,1,.41)
m3[,8] <- rbinom(250,1,.4)
m3[,9] <- rbinom(250,1,.35)
m3[,10]<- rbinom(250,1,.2)

# Red
m4[,1]  <- rbinom(600,1,.01)
m4[,2]  <- rbinom(600,1,.01)
m4[,3]  <- rbinom(600,1,.01)
m4[,4]  <- rbinom(600,1,.01)
m4[,5]  <- rbinom(600,1,.01)
m4[,6]  <- rbinom(600,1,.01)
m4[,7]  <- rbinom(600,1,.01)
m4[,8]  <- rbinom(600,1,.01)
m4[,9]  <- rbinom(600,1,.01)
m4[,10] <- rbinom(600,1,.01)

bin_dat <- data.frame(rbind(m1,m2,m3,m4))
bin_dat = bin_dat+1
f <- cbind(X1, X2, X3, X4, X5, X6, X7, X8, X9, X10)~1
pl <- poLCA(f, bin_dat, nclass=4)

post = pl$posterior
bin_dat$id <- rep(1:1600)
new_dat <- melt(bin_dat, id="id")
levels(new_dat$variable) <- c("6", "7","8", "9", "10", "11", "12", "13", "14", "15")
new_dat$age <- as.numeric(new_dat$variable)
new_dat$wt1 <- as.integer(rep(post[,1], 10)*100)
new_dat$wt2 <- as.integer(rep(post[,2], 10)*100)
new_dat$wt3 <- as.integer(rep(post[,3], 10)*100)
new_dat$wt4 <- as.integer(rep(post[,4], 10)*100)

new_dat$out <- as.integer(new_dat$value-1)
fit <- glm(out ~ bs(age, df = 3), data = new_dat, weights=wt1, family=binomial)
cl1 <- data.frame(Age=new_dat$age, Outcome=predict(fit, type= "response"), Cluster="1")
by_cl1_1 <- group_by(cl1, Age)
by_cl11 <- summarise(by_cl1_1, n = mean(Outcome), Cluster="1")

new_dat$out <- as.integer(new_dat$value-1)
fit <- glm(out ~ bs(age, df = 3), data = new_dat, weights=wt2, family=binomial)
cl2 <- data.frame(Age=new_dat$age, Outcome=predict(fit, type= "response"), Cluster="2")
by_cl1_2 <- group_by(cl2, Age)
by_cl12 <- summarise(by_cl1_2, n = mean(Outcome), Cluster="2")

new_dat$out <- as.integer(new_dat$value-1)
fit <- glm(out ~ bs(age, df = 3), data = new_dat, weights=wt3, family=binomial)
cl3 <- data.frame(Age=new_dat$age, Outcome=predict(fit, type= "response"), Cluster="3")
by_cl1_3 <- group_by(cl3, Age)
by_cl13 <- summarise(by_cl1_3, n = mean(Outcome), Cluster="3")

new_dat$out <- as.integer(new_dat$value-1)
fit <- glm(out ~ bs(age, df = 3), data = new_dat, weights=wt4, family=binomial)
cl4 <- data.frame(Age=new_dat$age, Outcome=predict(fit, type= "response"), Cluster="4")
by_cl1_4 <- group_by(cl4, Age)
by_cl14 <- summarise(by_cl1_4, n = mean(Outcome), Cluster="4")

dat <- rbind(by_cl11, by_cl12, by_cl13, by_cl14)

dat$Cluster <- factor(dat$Cluster)
ggplot(dat, aes(x=Age, y=n, color=Cluster)) +
	geom_line()


# write.csv(bin_dat, file="/Universe/GitHub/STA663_Project/Data/bindat.csv")


