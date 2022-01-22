import json
import sqlite3

with open('./private_constants.json') as file:
    private_constants = json.load(file)

class ViewDatabase:
    def __init__(self):
        self.con = sqlite3.connect(private_constants["SQLITE_DB_CONNECTION"])
        self.cur = self.con.cursor()

    def get_vidoes(self):
        video_data = self.cur.execute("SELECT rowid, * FROM videos_model")
        get_videos = video_data.fetchall();

        for video in get_videos:
            print(f"{video[1]}, {video[3]}, {video[4]}, {video[5]}, {video[6]}, {video[7]}")


def main():
    db = ViewDatabase()
    db.get_vidoes()

if __name__ == "__main__":
    main()