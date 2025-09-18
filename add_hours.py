def handle(commit):
    "Reset the timezone of all commits."
    author_date_str = commit.author_date.decode('utf-8')
    [author_seconds_str, timezone] = author_date_str.split()

    # print(int(seconds_str))  # "Debugging"
    # print(timezone)  # "Debugging"
    new_seconds = int(author_seconds_str) + 3600 * (3)
    new_date_str = f"{new_seconds} {timezone}"
    new_date = new_date_str.encode('utf-8')
    commit.author_date = new_date
    commit.committer_date = new_date

handle(commit)
