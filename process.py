# opens file and allows it to be interacted with
log_file = open("um-server-01.txt")

# prints out the sales reports ofa particular day
def sales_reports(log_file):
    # for every line in the file,
    for line in log_file:
        # makes a line with all whitespace at the right end removed
        line = line.rstrip()
        # day looks for the first three chars of a day of the week
        day = line[0:3]
        # if the day is Tuesday, print the info for that line
        if day == "Mon":
            print(line)

# calling sales_reports
sales_reports(log_file)
