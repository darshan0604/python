import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(wait_time, "Wait time \n", attempts, " Attempts\n")
    attempts+1
    time.sleep(wait_time)
    