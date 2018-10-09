##Suggestions for PUI2018_rms818's Assignment 2 by pyk222

Is your idea:
Are women on average faster bike riders than men?

or is:
Do women on average spend less time riding bikes than men?

Because trip duration measures seconds riding the bike, not the distance.

It might be better for the hypotheses to include formulas, just for clarity:

Null:
${\mu_{\mathrm{{W\:tripduration}}}} >= {\mu_{\mathrm{M\:tripduration}}}$

Alternative:
${\mu_{\mathrm{{W\:tripduration}}}} < {\mu_{\mathrm{M\:tripduration}}}$

The data supports the project, with the tripduration, gender and date. 
However, although date might clarify where the averages lie specifically, it might be better to state specifically in the null hypothesis that you are trying to base on the individual averages per date. 
The charts distinguishes total and average.

Since you are measuring trip duration, are you measuring their riding speed or how long they are on the bike?

If you are riding their speed, it might be interesting to include the start and end station ids. Ex: check the male and female ridership and their trip duration for a specific path that goes from the start station to the end station.

For a statistical test, I suggest a one-tailed ANOVA test. 
One tailed because you are testing if women are faster riders than men. 
A two-tailed test can be used if your null hypothesis states that there is no relationship between a person's gender and their trip durations:

${\mu_{\mathrm{{W\:tripduration}}}} =/= {\mu_{\mathrm{M\:tripduration}}}$

You have one category for the independent variable (that is gender) in your hypotheses, and the ANOVA allows one or more categories for the independent variable. 
(unless for your test you include the variable of date, then it would be two categories.) 
You have one continuous numerical dependent variable, (that is you are trying to find trip duration) with no control variables, and ANOVA supports that. 
The null hypothesis this test is answering is if there are differences between two or more groups on one dependent variable, and you are trying to find whether the ridership between the male and female groups determine their trip durations. 
Therefore, ANOVA is a good choice for this.