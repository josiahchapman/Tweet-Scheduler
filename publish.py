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

    for i in range(len(lines)):
        temp = lines[i].split("#####")

        date = temp[0]
        text = temp[1]

        if date == current_time:
            api.PostUpdate(text)
            # delete line from the file after publishing tweet


if __name__ == "__main__":
    while True:
        check()
        time.sleep(60)
