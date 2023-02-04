import datetime
import pandas as pd


class Checker:
    def __init__(self, url):
        self.sheet_url = url
        self.download_url = self.sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
    

    def check(self):
        df = pd.read_csv(self.download_url, sep=',')
        df = df.dropna(how='all')
        total_minutes = 0
        for index, row in df.iterrows():
            time_entries = 0
            minutes = 0
            for i in range(1, 4):
                if not f"Hours {i}" in row.keys() or pd.isnull(row[f"Hours {i}"]):
                    continue
                time_entries += 1
                
                difference_mins = self.get_minutes(row[f"Hours {i}"])

                minutes += divmod(difference_mins.days * 86400 + difference_mins.seconds, 60)[0] % 720
            total_minutes += minutes
        
            if minutes != row["Minutes"] and time_entries > 0:
                print("wrong" + row["Date"])
            
        print(total_minutes)


    def parseTimestamp(self, s: str) -> datetime.timedelta:    
        hour = int(s.split(" ")[0].split(":")[0])
        minute = int(s.split(" ")[0].split(":")[1])

        return datetime.timedelta(hours = hour, minutes = minute)
    

    def get_minutes(self, line: str) -> datetime.timedelta:
        lines = line.split(" ")
        start = lines[0] + " " + lines[1]
        end = lines[3] + " " + lines[4]

        return self.parseTimestamp(end) - self.parseTimestamp(start)
