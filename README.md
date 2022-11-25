# csgoEsports

This project is a collection of the code, graphs and analyses that i've created while trying to answer some questions about the video game "Counter-Strike Global Offensive", developed by Valve, and it's esports domain

I've added a short description (question being answered, analysis methods used, conclusion, other thoughts) for each file



"IGLs.py":
The question I tried to answer here was to see if In-Game Leaders were statistically worse than their counterparts, as a lot of discussion in CSGO has revolved around the concept of "fragging IGL's".
I divided up a database of csgo players, binning a player into one(or more) categories(IGL, Rifler, Awpper). Then with the binned data, I examined if there was a statistical difference between each of the three groups by viewing their HLTV 2.0 rating using histograms and violin plots, along with performing independent t-tests across all the groups. 
The conclusion I came to was that while there is a statistical difference between Uppers and IGLs, there is nothing to suggest that IGL's perform worse than your typical rifler. 
After making this video, I’d actually also like to explore the performance of IGL/Awppers (Fallen, Jame, Cadian), along with looking at the performance change of an individual before/during/after they take on the IGL role (Niko, Hampus, Electronic come to mind). I’d also like to use an ANOVA test next time to see any possible differences across all 3 means, with also the possibility of adding more sample means/bins.

