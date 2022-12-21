# An Analysis of Tickborne Disease Treatment

This research aims to critically assess the adverse effects of antibiotic treatment for tickborne disease. Through the use of precise data visualizations, I hope to shed light on the threat that tickborne illnesses pose to our society, and in doing so, help contribute to the formation of future health policies. Countless people are currently struggling with these zoonotic, tickborne infections. Many do not recover in the manner that medical professionals expect, leaving them searching for relief from their unrelenting symptoms. These are the individuals most at risk of experiencing a dangerous, sometimes life-threatening, adverse event from extended antibiotic treatment. The data for this project was obtained from the FAERS database (FDA Adverse Events Reporting System) at [FIS FDA](https://fis.fda.gov). 

[<img src="./gif/tick.gif" width="300"/>]()

In this research I define tick-borne disease as any of the following:
- Lyme Disease (any Borrelia)
- Babesiosis
- Ehrlichiosis
- Rocky Mountain Spotted Fever (any Rickettsia)
- Anaplasmosis
- Southern Tick-Associated Rash Illness
- Tick-Borne Relapsing Fever
- Tularemia
- Q Fever
- Tick-Borne Viral Encephalitis
- Colorado tick fever

Tick-Borne Disease List Sources: 
[CDC](https://www.cdc.gov/ticks/diseases/index.html),
[ECDC](https://www.ecdc.europa.eu/en/tick-borne-diseases)

My research will focus on the results of antibiotic tick-borne disease treatment ([Treatment Options](https://www.columbia-lyme.org/treatment-options)). Specifically these antibiotics:
- Doxycycline
- Cefuroxime
- Ceftriaxone
- Azithromycin
- Amoxicillin
- Atovaquone
- Clindamycin

The ultimate questions & goals this project seeks to address are:

1. Which antibiotic during tick-borne disease treatment is most correlated with severe adverse events (i.e. hospitalization and death) and how does this compare to severe adverse events during non-tick-borne disease treatment? 

2. Is the quantity of reported adverse events substantially growing over time? Are tick-borne diseases a worsening epidemic? 


## Data and Methods

Data was collected by querying the FDA FAERS system for each respective antibiotic and viewing the ‘Listing of Cases’ option. This provides an excel sheet with information on each adverse reaction to the specified antibiotic. By repeating this process for each antibiotic, I collected excel sheets that could be put into pandas data frames in python. After joining them, 149,497 individual cases comprise my current dataset. Further processing was done by extracting only the case reports related to tickborne disease. 

## Summary Statistics

All Antibiotic Data     |  Tickborne Antibiotic Data
:-------------------------:|:-------------------------:
![](./svg/summary1.svg)  |  ![](./svg/summary2.svg)


## Investigation: Tickborne Disease Treatment vs. Other Infections
<p align="center">
<img src="./svg/adverse_comparison.svg" width="900">
</p>

This bar chart showcases the percent difference in hospitalization during treatment between non-tickborne and tickborne diseases (given that the individual experienced an adverse reaction). There are three key takeaways:
- Ceftriaxone, Atovaquone, and Cefuroxime had significantly lower hospitalization rates for tickborne disease treatment compared to non-tickborne disease treatment.  
- Clindamycin and Doxycycline are antibiotics where the hospitalization rate is increased when used for tickborne disease treatment (although not statistically significant with a significance level of 0.05).
- Amoxicillin is most associated with hospitalization during tickborne disease treatment compared to other antibiotics.

### Understanding the statistical significance of the visualization above:

Monte Carlo Simulation <br> Using a Normal Distribution as an Estimator of the Binomial Distribution    |  Statistical Significance Comments
:-------------------------:|:-------------------------:
![](./svg/histograms/histogramDoxycycline.svg)  | - No simulated data points were less than the left bound or greater than the right bound.  <br><br>- Mathematically computed binomial p-value is < 0.001. We **can** safely reject the null hypothesis.<br><br>- Tickborne Doxycycline hospitalization **is** statistically significant compared to random. 
![](./svg/histograms/histogramCefuroxime.svg)  | - No simulated data points were less than the left bound or greater than the right bound. <br><br>- Mathematically computed binomial p-value is < 0.001. We **can** safely reject the null hypothesis.<br><br>- Tickborne Cefuroxime hospitalization **is** statistically significant compared to random. 
![](./svg/histograms/histogramCeftriaxone.svg)  | - No simulated data points were less than the left bound or greater than the right bound. <br><br>- Mathematically computed binomial p-value is < 0.001. We **can** safely reject the null hypothesis.<br><br>- Tickborne Cefuroxime hospitalization **is** statistically significant compared to random.
![](./svg/histograms/histogramAzithromycin.svg)  |  - No simulated data points were less than the left bound or greater than the right bound. <br><br>- Mathematically computed binomial p-value is < 0.001. We **can** safely reject the null hypothesis.<br><br>- Tickborne Azithromycin hospitalization **is** statistically significant compared to random.
![](./svg/histograms/histogramAmoxicillin.svg)  |  - Some simulated data points were less than the left bound or greater than the right bound. <br><br>- Mathematically computed binomial p-value is > 0.05. We **cannot** safely reject the null hypothesis.<br><br>- Tickborne Amoxicillin hospitalization **is not** statistically significant compared to random.
![](./svg/histograms/histogramAtovaquone.svg)  |  - No simulated data points were less than the left bound or greater than the right bound. <br><br>- Mathematically computed binomial p-value is < 0.001. We **can** safely reject the null hypothesis.<br><br>- Tickborne Atovaquone hospitalization **is** statistically significant compared to random.
![](./svg/histograms/histogramClindamycin.svg)  |  - Some simulated data points were less than the left bound or greater than the right bound. <br><br>- Mathematically computed binomial p-value is < 0.05. We **can** reject the null hypothesis.<br><br>- Tickborne Clindamycin hospitalization **is** statistically significant compared to random.

These histograms serve to illustrate that the likelihood of tickborne hospitalization given an adverse event for each antibiotic is significant, and not due to random chance (except for Amoxicillin). 

## Investigation: Tickborne Disease Adverse Events During Treatment Over Time

<p align="center">
<img src="./svg/events_over_time.svg" width="900">
</p>

The graphic above shows how reported adverse events to antibiotic therapy for tickborne disease has changed over time. There was a 118 case rise in reported events between 2014 and 2017. 

Hypothesis: The Covid-19 pandemic greatly reduced the number of visits to ambulatory practices [decreased by nearly 60%](https://www.commonwealthfund.org/publications/2020/apr/impact-covid-19-outpatient-visits#:~:text=The%20number%20of%20visits%20to%20ambulatory%20practices%20declined%20nearly%2060,was%20seen%20before%20the%20pandemic.). It is possible that the decrease in reported adverse events to tickborne antibiotic treatment continued to fall since 2020 because of deferred clinician visits. 

Many researchers have noted that tickborne disease is on the rise. Climate change and global warming are frequently speculated to be the likely culprit for the increase in Lyme disease infections (and other tickborne diseases). The warmer temperatures have been better for tick reproduction and have increased their survivability during the winter. Troy Cullen wrote an article about this issue [New Jersey Hills](https://www.newjerseyhills.com/echoes-sentinel/opinion/letters_to_the_editor/letter-climate-change-and-lyme-disease-how-global-warming-is-already-wreaking-havoc-on-new/article_9e06ed84-676b-5c4a-9d7c-c82d2ef05387.html). 

## Additional Interest: NLP of Documented Adverse Reactions

Additional data-visualization showcase using word clouds. The first shows the reactions listed by individuals having an adverse event during treatment. The second graphic shows the reactions listed by individuals having an adverse event during (non-tickborne) antibiotic treatment.

Tickborne Antibiotic Reactions  |  All Antibiotic Reactions
:-------------------------:|:-------------------------:
![](./svg/tick_wordcloud.svg)  |  ![](./svg/antibiotics_wordcloud.svg)

## Curious about my data processing & calculations? 

Everything computed is publically available on my Data-Viz GitHub repository, which you can access here: 

[<img src="./buttons/githubbutton.png" width="100"/>](https://github.com/RonanChance/Data-Viz)