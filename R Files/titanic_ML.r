dat <- read.csv("train.csv")
attach(dat)
##
## Step1: Data Cleaning ##
##
## Convert variable survived into Boolean ##
##
dat$Survived <-  as.logical(dat$Survived)
levels(dat$Survived) <- c("Not SUrvived", "Survived")
##
## Remove all NA's from the data ##
##
#dat <- dat[complete.cases(dat),]
##
## Remove all the blank variables 
##
#dat <- dat[!(dat$Embarked==""),]
##
## Convert PClass from an integer into a factor ##
##dat$Pclass <- as.factor(dat$Pclass)
## 
## Convert Name from a factor to a character ##
##
dat$Name <- as.character(dat$Name)
##
## Add another Variable for total family size ##
## To check does bigger family decrease chance of survival ? ##
##
dat$familysize <- dat$SibSp+dat$Parch+1
##
## Make Embarked into a factor with three levels ##
dat$Embarked <- factor(dat$Embarked, labels=c("C","Q","S"))
dat$familysize <- as.integer(dat$familysize)
## Step2: Testing ##
##
## Separate the training data into two: train test ##
##
library(caret)
set.seed(820)
trainingset <- createDataPartition(dat$Survived, p=0.5, list=FALSE)
train <- dat[trainingset,]
test <- dat[-trainingset,]
##

library(rpart)
tree <- rpart(Survived ~ Pclass+Sex+Age+SibSp+Parch+Embarked+familysize, data=train, method="class")
plot(tree)
text(tree)

testing <- predict(tree, data=test, type="class")
x <- as.data.frame(table(testing))
y <- as.data.frame(table(test$Survived))

## Create a function to check accuracy ##
accuracy <- function(testdata, actualdata) {
  value <- ((testdata[1,c("Freq")]-actualdata[1,c("Freq")])/(testdata[1,c("Freq")]+testdata[2,c("Freq")]))*100
  return(value)
}
##
## Check to see the accuracy
accuracy(x,y)

## Check different model 
tree2 <- rpart(Survived ~ Sex+Age+Embarked+familysize, data=train, method="class")
testing2 <- predict(tree2, data=test, type="class")
a <- as.data.frame(table(testing2))
accuracy(a,y)

## ANother model
tree3 <- rpart(Survived ~ Sex+Age+familysize+Fare, data=train, method="class")
testing3 <- predict(tree3, data=test, type="class")
b <- as.data.frame(table(testing3))
accuracy(b,y)

testdata <- read.csv("test.csv")
attach(testdata)
##
## Step1: Data Cleaning ##
##
##
## Remove all NA's from the data ##
##
##testdata <- testdata[complete.cases(testdata),]
##
## Remove all the blank variables 
##
##testdata <- testdata[!(testdata$Embarked==""),]
##
## Convert PClass from an integer into a factor ##
##testdata$Pclass <- as.factor(testdata$Pclass)
## 
## Convert Name from a factor to a character ##
##
testdata$Name <- as.character(testdata$Name)
##
## Add another Variable for total family size ##
## To check does bigger family decrease chance of survival ? ##
##
testdata$familysize <- testdata$SibSp+testdata$Parch+1
testdata$familysize <- as.integer(testdata$familysize)
##
## Make Embarked into a factor with three levels ##
testdata$Embarked <- factor(testdata$Embarked, labels=c("C","Q","S"))
##
##tree4 <- rpart(Survived ~ Sex+Age+familysize, data=testdata, method="class")
testing4 <- predict(tree3, newdata=testdata, type="class")
c <- as.data.frame(table(testing4))
result <- data.frame(testing4)
result
