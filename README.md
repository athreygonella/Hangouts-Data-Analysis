# Hangouts Wrapped

**A script that parses through chat data from Google Hangouts (which was retired by Google in 2022) and returns interesting data and insights.**  

### Functionality:  
  - Ranks all text recipients by # of direct messages and highlights top 5 friends
  - Ranks top 10 group chats that you've been most active in
  - Ranks top 10 most active group chats by total # of messages

## Usage
  1. Clone this repository or download & extract zip
  2. Login to https://takeout.google.com
  3. Select data to download (deselect all except for Hangouts)
  4. Follow instructions and export data (this should usually take ~30 minutes to an hour)
  5. Unzip downloaded zip file and move Takeout folder so that it's in the same directory as 'menu.py'
  6. Open Terminal, `cd` to the directory and run `python3 menu.py` 

  Developed by Athrey Gonella