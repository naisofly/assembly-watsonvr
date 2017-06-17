# Watson Visual Recognition Workshop

Simple workshop using the classify, train & similarity search features of Watson Visual Recognition

Slides at https://ibm.box.com/v/assembly-watsonvr

This app can be used to run Python code interactively through Bluemix, for example, the app code demo-ed in this article: [Ask Watson what Twitter is telling you: Part 1](http://www.ibm.com/developerworks/library/cc-ask-watson-part1-bluemix-trs/index.html)

## Installation

1.    Deploy this app to Bluemix by clicking here: [![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/AninditaBasu/iPythonBluemix)
2.    Follow the onscreen directions. After the app is deployed and running, click the app's URL. You are taken to the iPython login page.
3.    Click __Log in__ without typing any password. Open a new notebook, import the `hello_world.py` script, and run it. You should be asked your name and shown some lines of text. You can now proceed to run Python code through the iPython framework.

## Files and folders

-    `Procfile`: Contains the command that tells Bluemix which file to launch when the app is opened. For this app, the iPython framework is specified as the launchpoint.
-    `README.md`: The file that you are reading at this moment.
-    `manifest.yml`: A file that tells Bluemix a bit more about the app.
-    `requirements.txt`: A file for listing the Python libraries that you need for your app code, with each library on a new line. Replace the libraries in this file with whatever you need for your app. For this app to run, the only required library is `ipython[notebook]`.
-    `getTweet.py`: Retreive tweets being tracked, analyze for emotional tone & store JSON output in tweetdata.json
-    `getImage.py`: Extract Image content from tweet & store urls in images.txt
-    `getClassification.py`: Classify Image urls using Visual Recognition & store JSON output in classifiedImages.json
