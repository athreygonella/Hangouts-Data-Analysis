# Hangouts Wrapped

**A script that parses through chat data from Google Hangouts (which was retired by Google in 2022) and returns interesting data and insights.**

Note: In order to use this script, you should have your Hangouts data downloaded prior to Jan 1st, 2023. Starting on this date, Google has initiated deletion of Hangouts data from their servers, so there is no guarantee that your data is still available (you can check by trying to export data from https://takeout.google.com). 

### Functionality:  
  - Ranks all text recipients by # of direct messages and highlights top 5 friends
  - Ranks top 10 group chats that you've been most active in
  - Ranks top 10 most active group chats by total # of messages

## Usage
  1. Clone this repository or download & extract zip
  2. Place **Takeout** folder (which contains data exported from Google) into the **Hangouts-Wrapped-main** folder that was just downloaded
  3. Open Terminal, `cd` to **Hangouts-Wrapped-main** directory and run `python3 menu.py` 

  Developed by Athrey Gonella