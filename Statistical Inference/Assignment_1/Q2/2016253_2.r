# Data
y<-c(10.4, 19.6, 18.8, 13.9, 17.8, 16.8, 21.6, 17.9,12.5, 11.1, 4.9, 12.8, 14.8, 22.8, 20.0,
     15.9,16.3, 13.4,17.1,14.5, 19.0, 22.8, 1.3, 0.7, 8.9, 11.9, 10.9, 7.3, 5.9, 3.7, 17.9, 19.2,
     9.8, 5.8, 6.9, 2.6, 5.8, 21.7, 11.8, 3.4, 2.1, 4.5, 6.3, 10.7, 8.9, 9.4, 9.4, 7.6, 10.0, 3.3,
     6.7, 7.8, 11.6, 13.8, 18.6)
n = length(y)  #length of the data

# Log-likelihood function
logL <- function(theta) 
{
    print(theta)
    #maxvar<-theta[2]; minvar<-theta[1]
    like_func = -n*(log(theta)) 
    
 return (-like_func)
}
# Finding the maximum likelihood estimate using routine(optimize)
xmax <- optimize(logL, lower=0.7, upper=22.8, maximum=TRUE)

# generating a sequence of lambda
theta.values<-seq(0.1,22.8,by=0.02) 
ll.uniform<-logL(theta.values)

data.pois<-data.frame(cbind(theta.values,ll.uniform))

# Plot of log-likelihood estimate for different values of theta
plot(data.pois[,1],data.pois[,2],xlab="Thetas",ylab="Log-Likelihood",
     xlim=c(0.1,22.8),ylim=c(min(ll.uniform),max(ll.uniform)))



