First, download the data directory from the Google Drive link attached in the title of our project report.  This should be extracted to a directory called data in the main level of this repo.

The analysis directory includes code used to create the natural language model.  Running classify_tweets will train and test the model.

The scripts directory includes code used to find the crime rate in different zip codes and different times of day.

The app directory contains the code used to create the front end for the user.  Running updatelocation with a command line argument to a file name (we used temp.txt) will output time-stamped location traces to temp.txt that are the crimes that happened in the last hour.  Running makehtml will create the HTML for the heatmap, which will be output to hm.html in that directory.  This file can then be opened in a browser for the user to interact with.
