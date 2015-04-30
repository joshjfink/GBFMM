Pseudo code

1. The likelihood function, for each $Y_i$ (panel unit): 
	* Cumulative sum of the probability of $Y_i$ membership in group $j$ and the overall probability of membership in group $j$
2. Regress the logarithm of the probability $Y_it^j$ on an intercept term, a cubic function of Age, and an error term 
3. Set the probability according to the specification of the model, with three options based on user input:
	1. If zero-inflated Poisson, set $p=0$ with probability $r$, or Poisson($lambda$) with probability $1-r$. 
		* Set the natural log of $lambda$ = an intercept and a cubic function for age 
		* Set $r=$ exponentiated cubic age function over $1+$ the exponentiated cubic age function
	2. If logistic, set, $p(y=1)=$ and exponentiated cubic age function with an intercept over $1+$ and exponentiated cubic age function with an intercept. 
4. Using a hierarchical linear model with normally distributed random effects for membership in group $j$, sample from the posterior.
5. Return the maximum a posteriori (MAP) estimates of probability of membership in group $j$ at time $t$ for respondent $i$

