# Connect Network Scraper

## Overview

This is a simple web scraper built with mostly selenium and beautiful soup that will login to the connectnetwork website. Once logged in
it will naviagate to the "Messaging" link and open / parse out any new messages from the sender of the emails.

Once the new messages have been parsed, it will send the collection of emails to 
the receipents designated by the config file from the smtp library with the google client.

## Tech Stack
Python

## Core Libraries
bs5
selenium
smtplib