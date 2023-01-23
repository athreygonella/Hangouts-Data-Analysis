# Hangouts Wrapped

**A script that parses through chat data from Google Hangouts (which was retired by Google in 2022) and returns interesting data and insights.**  

### Functionality:  
  - Ranks all text recipients by # of direct messages and highlights top 5 friends
  - *Coming Soon*

## Usage
  1. Clone this repository or download & extract zip
  2. Login to https://takeout.google.com
  3. Select data to download (deselect all except for Hangouts)
  4. Follow instructions and export data (this should usually take ~30 minutes to an hour)
  5. Unzip downloaded zip file and move Takeout folder so that it's in the same directory as 'analysis.py'
  6. Open Terminal, `cd` to the directory and run `python3 analysis.py` 