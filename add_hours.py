def handle(commit):
    "Reset the timezone of all commits."
    date_str = commit.author_date.decode('utf-8')
    [seconds_str, timezone] = date_str.split()
    # print(int(seconds_str))  # "Debugging"
    # print(timezone)  # "Debugging"
    new_seconds = int(seconds_str) + 3600 * (3)
    new_date = f"{new_seconds} {timezone}"
    commit.author_date = new_date.encode('utf-8')

handle(commit)
