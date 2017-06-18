# Watson Visual Recognition Workshop

Simple workshop using the classify, train & similarity search features of Watson Visual Recognition

Slides at https://ibm.box.com/v/assembly-watsonvr

This app can be used to run Python code interactively through Bluemix, for example, the app code demo-ed in this article: [Ask Watson what Twitter is telling you: Part 3 - Analyze tweet pictures for categorization and recognition](https://www.ibm.com/developerworks/library/cc-ask-watson-part3-bluemix-trs/index.html)

## Prerequisites

1.    Python 2.7 [https://www.python.org/download/releases/2.7/], Pip [https://www.python.org/download/releases/2.7/]
2.    Twitter app credentials [https://apps.twitter.com/]
3.    Bluemix account & Watson Visual Recognition service credentials [https://www.ibm.com/watson/developercloud/doc/common/getting-started-credentials.html]   

## Files and folders

-    `Procfile`: Contains the command that tells Bluemix which file to launch when the app is opened. For this app, the iPython framework is specified as the launchpoint.
-    `README.md`: The file that you are reading at this moment.
-    `manifest.yml`: A file that tells Bluemix a bit more about the app.
-    `requirements.txt`: A file for listing the Python libraries that you need for your app code, with each library on a new line. Replace the libraries in this file with whatever you need for your app. For this app to run, the only required libraries are `tweepy` & `watson_developer_cloud`.
-    `getTweet.py`: Retrieve tweets being tracked, analyze for emotional tone & store JSON output in tweetdata.json
-    `getImage.py`: Extract Image content from tweet & store urls in images.txt
-    `getClassification.py`: Classify Image urls using Visual Recognition & store JSON output in classifiedImages.json
