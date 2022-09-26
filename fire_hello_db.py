#!/usr/bin/env python

import fire
from dblib.test_query import querydb

class Anime(object):

    def call_anime_csv(self):
        querydb("SELECT * FROM anime_csv LIMIT 3")
        pass

    def call_anime_with_synopsis_csv(self):
        querydb("SELECT * FROM anime_with_synopsis_csv LIMIT 3")
        pass

    def call_animelist_csv(self):
        querydb("SELECT * FROM animelist_csv LIMIT 3")
        pass

    def call_rating_complete_csv(self):
        querydb("SELECT * FROM rating_complete_csv LIMIT 3")
        pass

    def call_watching_status_csv(self):
        querydb("SELECT * FROM watching_status_csv LIMIT 3")
        pass

# run the CLI
if __name__ == "__main__":
    anime = Anime()
    fire.Fire(anime)
