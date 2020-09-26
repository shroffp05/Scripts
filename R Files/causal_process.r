#Generating phi1 and phi2 (x1 and x2) such that they satisfy the three inequalities
x1 <- runif(1,0, 1.5)
x2 <- runif(1, 0, 1.5)
while (x1>0 & x2 >0) {x1 <- runif(1,0,1.5); x2 <- runif(1, 0, 1.5); 
if (x1+x2 < 1 & x2-x1 < 1 & x2 > -1 & x2 <1) break; print(x1); print(x2)   }
# phi1 = 0.04339766 and phi2 = 0.09652273 
#AR(2) process: (1-0.04339766B-0.09652273B^2)Xt = et
#Generating the ACF and PACF plots for the above AR(2) process:
par(mfrow=c(2,1))
y=ARMAacf(ar = c(x1, x2), lag.max=5)
y=y[2:21]
plot(y,x=1:20, type="h", ylim=c(-0.2,0.2), xlab="h", ylab="Autocorrelation",
     main= "AR(2) Population ACF")
abline(h=0)
y = ARMAacf(ar = c(x1, x2), lag.max = 20,pacf=T)
plot(y, x = 1:20, type = "h", ylim = c(-0.2,0.5), xlab = "h",
     ylab = "Partial Autocorrelation", main = "AR(2) Population PACF")
abline(h = 0)
#Generating phi1 and phi2 (x3 and x4) such that they satisfy the three inequalities
x3 <- runif(1,-1.5, 0)
x4 <- runif(1, 0, 1.5)
while (x3 < 0 & x4 > 0) {x3 <- runif(1,-1.5,0); x4 <- runif(1, 0, 1.5); 
if (x3+x4 < 1 & x4-x3 < 1 & x4 > 0 & x4 <1 & x3 <0) break; print(x3); print(x4)   }
#phi1 = -0.20068183 and phi2 = 0.044833215
#AR(2) process: (1+0.20068183B-0.044833215B^2)Xt = et
#Generating the ACF and PACF plots for the above Ar(2) process:
par(mfrow=c(2,1))
y=ARMAacf(ar = c(x3, x4), lag.max=5)
y=y[2:21]
plot(y,x=1:20, type="h", ylim=c(-0.2,0.2), xlab="h", ylab="Autocorrelation",
     main= "AR(2) Population ACF")
abline(h=0)
y = ARMAacf(ar = c(x3, x4), lag.max = 20,pacf=T)
plot(y, x = 1:20, type = "h", ylim = c(-0.2,0.5), xlab = "h",
     ylab = "Partial Autocorrelation", main = "AR(2) Population PACF")
abline(h = 0)
#Generating phi1 and phi2 (x5 and x6) such that they satisfy the three inequalities
x5 <- runif(1,0, 1.5)
x6 <- runif(1, -1.5, 0)
while (x5 > 0 & x6 < 0) {x5 <- runif(1,0,1.5); x6 <- runif(1, -1.5, 0); 
if (x5+x6 < 1 & x6-x5 < 1 & x6 < 0 & x6 > -1) break ; print(x5); print(x6)   }
#phi1 = 0.3196590549 and phi2= -0.30074862787
#AR(2) process: (1-0.3196590549B+0.30074862787B^2)Xt = et
#Generating the ACF and PACF plots for the above AR(2) process:
par(mfrow=c(2,1))
y=ARMAacf(ar = c(x5, x6), lag.max=5)
y=y[2:21]
plot(y,x=1:20, type="h", ylim=c(-0.2,0.2), xlab="h", ylab="Autocorrelation",
     main= "AR(2) Population ACF")
abline(h=0)
y = ARMAacf(ar = c(x5, x6), lag.max = 20,pacf=T)
plot(y, x = 1:20, type = "h", ylim = c(-0.2,0.5), xlab = "h",
     ylab = "Partial Autocorrelation", main = "AR(2) Population PACF")
abline(h = 0)
#Generating phi1 and phi2 (x7 and x8) such that they satisfy the three inequalities
x7 <- runif(1,-1.5, 0)
x8 <- runif(1, -1.5, 0)
while (x7 < 0 & x8 < 0) {x7 <- runif(1,-1.5,0); x8 <-  runif(1, -1.5, 0); 
if (x7+x8 < 1 & x8-x7 < 1 & x8 < 0 & x8 > -1) break ; print(x7); print(x8)   }
#phi1 = -1.05023398355 and phi2= -0.11761471792
#AR(2) process: (1+1.05023398355B+0.11761471792B^2)Xt = et
#Generating the ACF and PACF plots for the above AR(2) process:
par(mfrow=c(2,1))
y=ARMAacf(ar = c(x7, x8), lag.max=5)
y=y[2:21]
plot(y,x=1:20, type="h", ylim=c(-0.2,0.2), xlab="h", ylab="Autocorrelation",
     main= "AR(2) Population ACF")
abline(h=0)
y = ARMAacf(ar = c(x7, x8), lag.max = 20,pacf=T)
plot(y, x = 1:20, type = "h", ylim = c(-0.2,0.5), xlab = "h",
     ylab = "Partial Autocorrelation", main = "AR(2) Population PACF")
abline(h = 0)
