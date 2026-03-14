import json
import random

print("啟動 B 計畫：正在生成 Stephen Curry 模擬投籃數據...")

shots_data = []
# 模擬 500 次投籃
for _ in range(500):
    shot_type = random.random()
    
    # 60% 機率是三分球 (Curry 的招牌)
    if shot_type < 0.60:
        # 模擬三分線外的座標 (大約 23-28 呎)
        x = random.uniform(-250, 250)
        y = random.uniform(237, 300) if abs(x) < 220 else random.uniform(-47, 100)
        made = 1 if random.random() < 0.42 else 0 # 命中率約 42%
        action = "3PT Jump Shot"
        
    # 30% 機率是禁區切入上籃
    elif shot_type < 0.90:
        x = random.uniform(-50, 50)
        y = random.uniform(-40, 50)
        made = 1 if random.random() < 0.65 else 0 # 命中率約 65%
        action = "Layup"
        
    # 10% 機率是中距離跳投
    else:
        x = random.uniform(-150, 150)
        y = random.uniform(50, 200)
        made = 1 if random.random() < 0.45 else 0 # 命中率約 45%
        action = "Jump Shot"

    shots_data.append({
        "LOC_X": x,
        "LOC_Y": y,
        "SHOT_MADE_FLAG": made,
        "ACTION_TYPE": action
    })

# 存成 JSON 檔案
with open('shot_data.json', 'w', encoding='utf-8') as f:
    json.dump(shots_data, f, ensure_ascii=False, indent=2)

print("✅ 成功！已生成 500 筆模擬投籃座標，並存為 shot_data.json")