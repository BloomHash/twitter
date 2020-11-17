import sys
import twint

def getUsers(f_in, f_out):
    f = open(f_in, "r")
    for line in f.readlines():
        user = line.strip()
        c = twint.Config()
        c.User_id = user
        c.Store_csv = True
        c.Output = f_out
        try:
            twint.run.Lookup(c)
        except ValueError:
            print(f"Unable to pull user: {user}")
            pass
    f.close()


# argv[1] = input file (txt file of user ids)
# argv[2] = output file (csv)
if __name__ == '__main__':
    getUsers(sys.argv[1], sys.argv[2])
