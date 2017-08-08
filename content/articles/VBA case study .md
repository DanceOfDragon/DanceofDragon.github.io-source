Title: VBA-case study 1
Date: 2015-08-30 18:40
Modified: 2015-08-30 18:50
Tags: tech-iT
Category:Blog/English
Slug: vba case study 1
Author: JIN Lin

This is the case study I was given at an interview with [Mars Singapore](http://www.mars.com/global/index.aspx). Only in real fight does the truth be revealed. Obviously, ~~I need to practice more, much more~~ Practicing!

**Objective** 

> At the end of the 1 hr, you should have created a chart to display **retention rate** per quarter, and you will also be asked to explain your steps / logic. May ignore quarters that aren't complete (e.g. Q3 2013)

**Definition**

- Retention rate is calculated for experience entrepreneurs (EE) only.
- Experienced entrepreneur (EE): Entrepreneur who has at least 3 months of sales data (i.e. He/She becomes EE at the end of the 3rd months with sales). Entrepreneurs with less than 3 months of experience are considered as new entrepreneurs (NE).
- Retention rate for EE: Out of all the EE that started a period, how many % ended that period. Calculation of retention rate = (EE at start of period - EE dropped during period) / EE at start of period
- EE at start of period + EE joined during period - EE dropped during period = EE at end of period
- How does an EE drop out? When there are 3 consecutive months of no sales (i.e. drops at the end of the 3rd month without sales)
- After an EE dropped and joins again, he is an EE immediately.


**Examples**

![example](https://dl.dropboxusercontent.com/u/18094167/BlogImages/VBA%20Examples1.png)

sample retention rate for Q2, Q3

Q2: month4 - month6 

EE at start of the period: 7

EE dropped out during the period: 3

retention rate:  4/7x100%  =  57%

Q3:moth7 - month9

EE at start of the period: 5

EE dropped out during the period: 3

retention rate: 40%


**Full Dataset**

Download full dataset [here @ VBA-case study 1](https://dl.dropboxusercontent.com/u/18094167/VBA%20case%20study%201.xlsx).

**My Approach**

*Analysis*

- Q1 starts from January and ends in March,rigorously. The same logic applies to Q2,Q3,Q4. ( Each company has its own fisical year, define in this way to avoid complexity coming from random starting of a quarter. Otherwise, a more complex model to calcualte retention rate per month).
- Algorithm:
	1. Convert sales data to rating of the entrepreneurs (NE,EE or dropout). All data needed to calculate the retention rate should be by far ready.
	2. Count the EE at the start of each quater, N1_start;
	3. Count the EE dropouts within each quarter,N1_dropuouts; 
	4. Count the newly joined EE during the period,N1_new;
	5. Calculate the retention rate for each quater,(N1_start -N1_dropuouts)/N1_start.  


- divide and conquer the essential first step

	- EE: 
		- at least 3 months of sales data (no need to be consecutive; 0 could indicate no sale, in Excel it will be empty cell);
		- returning EE dropouts become EE immediately; 
	- NE: less than 3 months' sales; 
	- Dropuouts: 3 or more consecutive months of no sales;
	- Entrepreneurs are independent from each other, so the method of converting sales data to rating will be apply to each one repeatedly.(Iteration) 

	
**Note**
After checking abnormal results calculated from the codes, I found that some "empty-appearing" cells are actually not empty, which causes big problems. One way to solve the problem is to *clear contents* of those "empty cells". 


	sample code to clear contents of 'empty cell'
		
		For Each c In Selection
     		If Len(c) = 0 Then c.ClearContents
		Next c

Algorithm:


	1) Conversion
	
	  matrix consisting of four different status: 
	 	Empty
	 	NE
	 	EE
	 	Dropout 
	 	
	 a counts Number of EE; b counts number of empty cells
	 
	 a = 0: empty
	 a = 1, 2: NE
	 	b < 3 NE
	 	b = 3 (consecutive, no data+1,data reset to 0):dropuout;
	 	b >= 4 empty
	 	
	 a >= 3: EE
	 	b < 3 EE
	 	b = 3 (consecutive, no data+1,data reset to 0):dropuout;
	 	b >= 4 empty
	 
	 2)Calculation
	 
	 for Quater k (row i, column j,j+1,j+2)
	 
	 	retented EE: (i,j)&(i,j+1)&(i,j+2) true 
	 	EE at the start: All EE at column j
	 	retention rate:   
	 
	 
	
**Code**


	Option Explicit
 End Sub

There's more could be done with this set of data. For example, evaluate the performance of the area officers based on the retention rate of the entrepreneurs.Or evaluate the performance of the entrepreneurs. 

