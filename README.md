# Connect Network Scraper

## Overview

This is a simple web scraper built mostly with selenium and beautiful soup that will login to the connectnetwork website. Once logged in
it will naviagate to the "Messaging" link and open / parse out any new messages from the sender of the emails.

Once the new messages have been parsed, it will send the collection of emails to 
the receipents designated by the config file from the smtp library with the google client.

## How To Run
* Python 3.6 or above is required
* Install dependencies with 'pip install -r requirements.txt'
* Create your own config.py with relevant variables for logging into ConnectNetwork and Gmail
    * Note - Prior to May 30, 2022, it was possible to connect to Gmail’s SMTP server using your regular Gmail password if “2-step verification” was activated. For a higher security standard, Google now requires you to use an “App Password“. This is a 16-digit passcode that is generated in your Google account and allows less secure apps or devices that don’t support 2-step verification to sign in to your Gmail Account. More information can be found at this link: https://mailtrap.io/blog/python-send-email-gmail/#:~:text=To%20send%20an%20email%20with%20Python%20via%20Gmail%20SMTP%2C%20you,Transfer%20Protocol%20(SMTP)%20server.
* Run the python app with your method of choice.

## Tech Stack
Python

## Core Libraries
beautifulSoup
selenium
smtplib