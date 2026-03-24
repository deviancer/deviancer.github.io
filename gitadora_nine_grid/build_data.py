"""从 mdb_gw.xml 提取歌曲数据，生成 songs.json 供前端使用。"""
import json
import os
import xml.etree.ElementTree as ET

# xg_diff_list 15个数的索引映射
# 格式: 0 G_BAS G_ADV G_EXT G_MAS 0 D_BAS D_ADV D_EXT D_MAS 0 B_BAS B_ADV B_EXT B_MAS
_DIFF_MAP = {
    "guitar": {"basic": 1, "advanced": 2, "extreme": 3, "master": 4},
    "drum":   {"basic": 6, "advanced": 7, "extreme": 8, "master": 9},
    "bass":   {"basic": 11, "advanced": 12, "extreme": 13, "master": 14},
}

BASE_DIR = os.path.join(os.path.dirname(__file__), "xml_to_\ufeff\ufeffcover")
XML_PATH = os.path.join(BASE_DIR, "mdb_gw.xml")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "songs.json")


def main():
    tree = ET.parse(XML_PATH)
    root = tree.getroot()

    songs = []
    for entry in root.findall("mdb_data"):
        music_id = int(entry.findtext("music_id", "0"))
        title = entry.findtext("title_name", "").strip()
        artist = entry.findtext("artist_title_ascii", "").strip()
        bpm = int(entry.findtext("bpm", "0"))
        diff_text = entry.findtext("xg_diff_list", "")
        diff_values = [int(x) for x in diff_text.split()]

        if len(diff_values) < 15:
            continue
        if all(d == 0 for d in diff_values):
            continue

        # 构建难度信息
        difficulties = {}
        for inst_type, idx_map in _DIFF_MAP.items():
            inst_diffs = {}
            for diff_name, idx in idx_map.items():
                raw_val = diff_values[idx]
                if raw_val > 0:
                    inst_diffs[diff_name] = round(raw_val / 100, 2)
            if inst_diffs:
                difficulties[inst_type] = inst_diffs

        if not difficulties:
            continue

        mid_str = str(music_id).zfill(4)
        prefix = mid_str[:2]
        cover_path = f"xml_to_\ufeff\ufeffcover/img_jk{prefix}/img_jk{mid_str}.png"

        # 检查封面文件是否存在
        full_cover_path = os.path.join(os.path.dirname(__file__), cover_path)
        if not os.path.exists(full_cover_path):
            continue

        songs.append({
            "id": music_id,
            "title": title,
            "artist": artist,
            "bpm": bpm,
            "cover": cover_path,
            "difficulties": difficulties,
        })

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(songs, f, ensure_ascii=False, indent=None)

    print(f"已导出 {len(songs)} 首歌曲到 {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
