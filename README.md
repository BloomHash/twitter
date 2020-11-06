# Twint
Instructions for pulling Twitter Data with Twint. **For any data collected and used, make sure to upload python scripts/ CLI commands to GitHub as we will most likely need to include this with our final submission.**

## Setup
- If Python3.6+ is not installed, install latest version of Python3. Follow this link for further instructions: https://realpython.com/installing-python/
- Run the following from Terminal to install Twint:
```
pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```

## CLI Excecution:
- Here's an example of running Twint from the command line:
```
twint -s Trump --since "08/01/2020 00:00:00" -o trumpTweets.csv --csv
```
This will pull all tweets with the keyword "Trump" and output in working directory as a csv file "trumpTweets.csv"

## Python Execution
- Here's an example of executing Twint from a Python3 script:
```python3
import twint

c = twint.Config()
c.Search = "Trump"
c.Since = "2020-08-01 00:00:00"
c.Store_csv = True
c.Output = "trumpTweets.csv"


twint.run.Search(c)
```
This will also pull all tweets with the keyword "Trump" and output in working directory as a csv file "trumpTweets.csv"

## Further Information
For further information on using the Twint Scraper check out the GitHub page: https://github.com/twintproject/twint
