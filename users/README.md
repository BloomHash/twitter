## Scraping for Users
This script will take in a list of unique user ids and scrape for user information. This will be used to obtain location information for tweets.

### Before using:
Make sure to install this branch of twint as there will be a URL exception thrown on almost ever user otherwise. Note that there will still be a handful of values dropped if the user is "restricted."
```
pip3 install --upgrade git+https://github.com/himanshudabas/twint.git@origin/twint-fixes#egg=twint
```

### Executing the Script:
To execute the script, you will need an input text file where each line is a unique twitter user's id. This can be obtained using Apache Spark (will have scala code in repo). Execute the following to run:
```
python3 UserScrape.py UserList.txt OutputFile.csv
```
