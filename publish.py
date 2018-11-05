import time
import twitter


# user should enter corresponding Twitter account information
api = twitter.Api(consumer_key=[consumer_key],
                  consumer_secret=[consumer_secret],
                  access_token_key=[access_token_key],
                  access_token_secret=[access_token_secret])


# publishes Tweet at given date/time
def check():
    current_time = time.strftime("%m%d%Y%H%M")
    output = open("output.txt", "r+")
    lines = output.readlines()
    output.close()

    for i in range(len(lines)):
        if lines[i][0] == '#':  # checks if line contains date/time (first char is '#' when line contains date/time)
            date_time = lines[i][1:]  # remove the '#' from line
            text = lines[i+1][1:]  # removes the '$' from line

            if int(date_time) == int(current_time):
                api.PostUpdate(text)
                # delete line from the file after publishing tweet


if __name__ == "__main__":
    while True:
        check()
        time.sleep(60)
