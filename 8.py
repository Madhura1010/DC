from datetime import datetime, timedelta
def berkeley_algo(servertime, time1, time2):
    print(f"Server Clock   = {servertime}")
    print(f"Clienr Clock1  = {time1}")
    print(f"Clienr Clock2  = {time2}")

    # Parse times in mm:ss format
    sdf = "%M:%S"
    s = datetime.strptime(servertime, sdf)
    t1 = datetime.strptime(time1, sdf)
    t2 = datetime.strptime(time2, sdf)

    # Convert to milliseconds 
    s_ms = s.minute * 60 * 1000 + s.second * 1000
    t1_ms = t1.minute * 60 * 1000 + t1.second * 1000
    t2_ms = t2.minute * 60 * 1000 + t2.second * 1000

    st1 = t1_ms - s_ms
    print("t1 - s =", st1 // 1000)
    st2 = t2_ms - s_ms
    print("t1 - s =", st2 // 1000)
    avg = (st1 + st2) // 2
    print(" (st1 + st2) / 2 =", avg // 1000)

    adjserver = avg + s_ms
    adj_t1 = avg - st1
    adj_t2 = avg - st2
    print(" t1 adjustment =", adj_t1 // 1000)
    print(" t2 adjustment =", adj_t2 // 1000)

    # Convert ms back to datetime for display
    def format_time(ms):
        total_seconds = ms // 1000
        minutes = (total_seconds // 60) % 60
        seconds = total_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    print(" Synchronized Server Clock =", format_time(adjserver))
    print(" Synchronized Client1 Clock =", format_time(t1_ms + adj_t1))
    print(" Synchronized Client2 Clock =", format_time(t2_ms + adj_t2))

def main():
    servertime = input("Enter Server Time (mm:ss): ")
    time1 = input("Enter Client 1 Time (mm:ss): ")
    time2 = input("Enter Client 2 Time (mm:ss): ")
    berkeley_algo(servertime, time1, time2)

if __name__ == "__main__":
    main()
