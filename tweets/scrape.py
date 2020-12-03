import twint
import sys

keyword = sys.argv[1]
date1 = sys.argv[2] # date as yyyy-mm-dd TT:TT:TT
date2 = sys.argv[3] # date as yyyy-mm-dd TT:TT:TT (set this to 24h past desired date range)
fileout = sys.argv[4] # .csv filename

c = twint.Config()
c.Search = keyword
c.Since = date1
c.Until = date2
c.Store_csv = True
c.Output = fileout


twint.run.Search(c)
