import json
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

# 1. 取得 Stephen Curry 的球員 ID
curry = [player for player in players.get_players() if player['full_name'] == 'Stephen Curry'][0]
curry_id = curry['id']

# 2. 呼叫 API 取得生涯數據
career = playercareerstats.PlayerCareerStats(player_id=curry_id)
df = career.get_data_frames()[0]

# 3. 整理出網頁前端需要的格式 (提取賽季與總得分)
data = {
    "seasons": df['SEASON_ID'].tolist(),
    "pts": df['PTS'].tolist()
}

# 4. 將資料存成 JSON 檔案
with open('player_stats.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

print("資料抓取完成！已儲存為 player_stats.json")