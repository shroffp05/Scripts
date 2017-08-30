##' The Data that I am trying to model is the EUR/USD 30 min Exchange rate for the past
##' 6 months using time series analysis
data1 <- read.csv("exchange.csv")
attach(data1)
plot.ts(EUR.USD.Close, type="l", font.main=1, family="serif", main="Time Series plot of EUR/USD exchange rate for past 6 years",
        ylab="Exchange rate", col="Blue", col.main="Black")
grid(nx= NULL, ny= NULL, lty = "solid")

##' Using the fpp package to help with forecasting and testing the time series data
library(fpp)
##' Performing an Augmented Dickey Fuller Test to test for stationarity. 
adf.test(EUR.USD.Close)

##' Since the p-value of the Dickey fuller test is 0.6027, it suggests that 
##' the data is non-stationary and we need to perform appropriate smoothing methods
##' to make the data stationary
##' Using first order Differencing we make the data stationary.

train <- ts(data1$EUR.USD.Close[1:1466])
testing <- ts(EUR.USD.Close[1467:1566])
n1 <- ts(diff(diff(EUR.USD.Close)), frequency=1, start=c(1.4640,1))
plot(n1, ylab="diff(1,12)", font.main=1, family="serif", 
     main="Difference data", col="Blue")
grid(nx=NULL, ny=NULL, lty=1)

##' We perform the Dickey Fuller test again just to verify if the differencing
##' actually made the data stationary.

adf.test(n1)

##' The p-value of the data after the first order differencing is <0.01 
##' Therefore we can reject the Null Hypothesis and conclude that the data is
##' now stationary. 

par(mfrow=c(2,2))
samacf <- acf(n1, main="Sample ACF for EUR.USD.Close")
sampacf <- pacf(n1, main="Sample PACF for EUR.USD.Close")
samacf2 <- acf(train, main="Sample ACF for EUR.USD.Close")
sampacf2 <- pacf(train, main="Sample PACF for EUR.USD.Close")

##' Looking at the sample ACF and PACF we can say approximately the model is 
##' a subset of ARMA(25,12) with the AR part being significant at lag 12,24,25
##' and the MA part being significant at lag 12
##' we can fit a subset model using the arima function

model1 <- Arima(train, order=c(0,1,31), fixed=c(rep(0,11), NA, rep(0,18),NA),method="ML",
                transform.pars=FALSE, include.mean=TRUE)
model1

##' the AIC of this model is -10374.13 and AICc is -10374.11
##' we need to check whether this model is adequate. 
##' we use the residuals to check

tsdiag(model1)
qqnorm(residuals(model1))
qqline(residuals(model1))
resd <- auto.arima(residuals(model1), max.q=0)

##' since the ACF of the residuals lie within the 95% CI line we can say
##' that the model is adequate. 
##' Next we check the forecast power using ARMA forecasting and Holt Winter forecasting.


forc.exchange <- forecast(model1, h=100)
plot(forc.exchange)
lines(EUR.USD.Close)
grid(nx=NULL, ny=NULL, lty=1)

HWForc.exchange <- HoltWinters(train, gamma=F)
fit1 <- forecast(HWForc.exchange, h=100)
plot(fit1)
lines(EUR.USD.Close)
grid(nx=NULL, ny=NULL, lty=1)

##' Next step is to check using the auto.arima function to see which model fits the best
##' according to R and compare it to our model1
fit2 <- auto.arima(train, max.p=32, max.q=32)
fit2
forc.exchange2 <- forecast(fit2, h=100)
plot(forc.exchange2)
lines(EUR.USD.Close)
grid(nx=NULL, ny=NULL, lty=1)

tsdiag(fit2)
qqnorm(residuals(fit2))
qqline(residuals(fit2))

### from the ACF and PACF plots to find the parameters to use in 
###the armasubset algorithm to find a model that 
### could possibly used.

library(TSA)
fit <- armasubsets(train, nar=12, nma=31, y.name="arma")
plot(fit)

### According to the subset model algorithm the best model could be a ARMA(1,31) process
### with only lag1 and lag 31 being the significant one. However, fitting an ARIMA
### model gives us an ARIMA(2,0,1) model. 

model2 <- Arima(train, order=c(1,1,31), fixed=c(NA, rep(0,30), NA), transform.pars=FALSE,
                method="ML")
model2

##' AICc for this model is -10374.51

tsdiag(model2)
qqnorm(residuals(model2))
qqline(residuals(model2))

forc.exchange3 <- forecast(model2, h=100)
plot(forc.exchange3)
lines(EUR.USD.Close)
grid(nx=NULL, ny=NULL, lty=1)

##' Comparing forecasting accuracy to check which model is better
##' using rmse, mae, mape

##' Function for RMSE
rmse <- function(error) {
  sqrt(mean(error^2))
}
##' Create a function for MAE
mae <-  function(error) {
  mean(abs(error))
}
##' Create a function for MAPE
mape <-  function(error, y) {
  mean(abs((error/y)*100))
}

##' calculating forecast error 
error1 <- ts(data1$EUR.USD.Close[1467:1566])-ts(forc.exchange$mean)
error2 <- ts(data1$EUR.USD.Close[1467:1566])-ts(forc.exchange2$mean)
error3 <- ts(data1$EUR.USD.Close[1467:1566])-ts(forc.exchange3$mean)

forcast1 <- c(rmse(error1), mae(error1), mape(error1, ts(data1$EUR.USD.Close[1467:1566])))

forcast2 <- c(rmse(error2), mae(error2), mape(error2, ts(data1$EUR.USD.Close[1467:1566])))

forcast3 <- c(rmse(error3), mae(error3), mape(error3, ts(data1$EUR.USD.Close[1467:1566])))

x <- min(model1$aic, fit2$aic, model2$aic)
y <- min(model1$aicc, fit2$aicc, model2$aicc)
