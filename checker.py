import datetime
import pandas as pd


class Checker:
    """Creates a class that contains methods for checking the hours on a particular spreadsheet.
    """
    
    def __init__(self, url: str):
        """Creates a new instance of the Checker class for a specific speadsheet.

        Parameters:
            url (str): URL to a Google Sheet with hours (in the correct format).
        """
        self.sheet_url = url
        self.download_url = self.sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
    

    def check(self) -> list[tuple[str, int, int]]:
        """Checks the Google Sheet file for any incorrectly written dates and hours.
    
        Returns:
            list[tuple[str,int,int]]: Returns a list of every incorrectly written date. List returns as [date, minutes_actual, minutes_reported].
        """
        
        incorrect_dates = []

        df = pd.read_csv(self.download_url, sep=',')
        df = df.dropna(how='all')
        total_minutes = 0
        for _, row in df.iterrows():
            minutes = 0

            hour_rows = 0
            while f"Hours {hour_rows + 1}" in row.keys() and not pd.isnull(row[f"Hours {hour_rows + 1}"]):
                if not f"Hours {hour_rows + 1}" in row.keys() or pd.isnull(row[f"Hours {hour_rows + 1}"]):
                    continue
                
                difference_mins = Checker.get_difference(row[f"Hours {hour_rows + 1}"])
                minutes += divmod(difference_mins.days * 86400 + difference_mins.seconds, 60)[0] % 720

                hour_rows += 1
            total_minutes += minutes
        
            if minutes != row["Minutes"] and hour_rows > 0:
                incorrect_dates.append((row["Date"], minutes, int(row["Minutes"])))

        return incorrect_dates


    def parse_timestamp(time_hour: str) -> datetime.timedelta:
        """Converts a timestamp of the hour into a timedelta.

        Parameters:
            time_hour (str): Hour in time (e.g. "5:00 PM").
    
        Returns:
            datetime.timedelta: A timedelta representing the exact time.
        """

        hour = int(time_hour.split(" ")[0].split(":")[0])
        minute = int(time_hour.split(" ")[0].split(":")[1])

        return datetime.timedelta(hours = hour, minutes = minute)
    

    def get_difference(line: str) -> datetime.timedelta:
        """Calculates the time difference between two timestamps.

        Parameters:
            line (str): Timespan in hours (e.g. "5:00 PM - 6:00 PM").
    
        Returns:
            datetime.timedelta: A timedelta representing the exact time difference.
        """

        lines = line.split(" ")
        start = lines[0] + " " + lines[1]
        end = lines[3] + " " + lines[4]

        return Checker.parse_timestamp(end) - Checker.parse_timestamp(start)
