import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup, Comment
import re
import os
from pathlib import Path

games_path = Path("/Users/camsmithers/Desktop/Camalytics/CamalyticsEnv/Projects/Sports/NFL/Data/Games")

expected_pts_df = []
for game in os.listdir(games_path):
    with open(f"/Users/camsmithers/Desktop/Camalytics/CamalyticsEnv/Projects/Sports/NFL/Data/Games/{game}", encoding="utf-8") as f:
        page = f.read()

    soup = BeautifulSoup(page, "html.parser")

    scorebox_meta = soup.find("div", class_="scorebox_meta")
    game_date = scorebox_meta.find_all("div")[0].text.strip()

    comment = next(c for c in soup.find_all(string=lambda text: isinstance(text, Comment)) if "expected_points" in c)

    table = BeautifulSoup(comment, "html.parser").find(id="expected_points")
    df = pd.read_html(StringIO(str(table)))[0]
    df["game_date"]=game_date
    df["game_id"]=game
    expected_pts_df.append(df)

expected_pts_df_combined = pd.concat(expected_pts_df, ignore_index=True)

expected_pts_df_combined.head()