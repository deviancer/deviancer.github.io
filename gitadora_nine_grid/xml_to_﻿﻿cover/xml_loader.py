"""基于官方 mdb_gw.xml + img_jk 封面目录的数据加载模块。

放在 cache/xml_to_cover/ 目录下，由外层 data_loader.py 调用。
"""
import os
import xml.etree.ElementTree as ET
from src.models import Song, Sheet

# xg_diff_list 15个数的索引映射
# 格式: 0 G_BAS G_ADV G_EXT G_MAS 0 D_BAS D_ADV D_EXT D_MAS 0 B_BAS B_ADV B_EXT B_MAS
_DIFF_MAP = {
    "guitar": {"basic": 1, "advanced": 2, "extreme": 3, "master": 4},
    "drum":   {"basic": 6, "advanced": 7, "extreme": 8, "master": 9},
    "bass":   {"basic": 11, "advanced": 12, "extreme": 13, "master": 14},
}


def _music_id_to_cover_path(base_dir: str, music_id: int) -> str:
    """根据 music_id 计算封面图路径。

    规则: ID 补足 4 位，前 2 位是文件夹编号。
    例如 ID=102 -> 0102 -> img_jk01/img_jk0102.png
    """
    mid_str = str(music_id).zfill(4)
    prefix = mid_str[:2]
    return os.path.join(base_dir, f"img_jk{prefix}", f"img_jk{mid_str}.png")


def load_songs_from_xml(xml_path: str) -> list[Song]:
    """从 mdb_gw.xml 解析歌曲列表。"""
    tree = ET.parse(xml_path)
    root = tree.getroot()

    songs = []
    for entry in root.findall("mdb_data"):
        music_id = int(entry.findtext("music_id", "0"))
        title = entry.findtext("title_name", "").strip()
        diff_text = entry.findtext("xg_diff_list", "")
        diff_values = [int(x) for x in diff_text.split()]

        if len(diff_values) < 15:
            continue

        # 跳过所有难度为 0 的歌曲（无效条目）
        if all(d == 0 for d in diff_values):
            continue

        # 构建 sheets
        sheets = []
        for inst_type, idx_map in _DIFF_MAP.items():
            for diff_name, idx in idx_map.items():
                raw_val = diff_values[idx]
                if raw_val == 0:
                    continue
                level_value = raw_val / 100
                sheets.append(Sheet(
                    type=inst_type,
                    difficulty=diff_name,
                    level=f"{level_value:.2f}",
                    level_value=level_value,
                ))

        if not sheets:
            continue

        # image_name 存储 music_id 的 4 位补足字符串
        mid_str = str(music_id).zfill(4)
        songs.append(Song(
            song_id=str(music_id),
            title=title,
            image_name=mid_str,
            sheets=sheets,
        ))

    return songs


def load_hot_ids_from_txt(txt_path: str, songs: list[Song]) -> set[str]:
    """从 gw新曲.txt 读取 HOT 歌曲标题，匹配返回 song_id 集合。"""
    if not os.path.exists(txt_path):
        return set()

    with open(txt_path, "r", encoding="utf-8") as f:
        hot_titles = {line.strip() for line in f if line.strip()}

    title_to_id: dict[str, str] = {}
    for song in songs:
        title_to_id[song.title] = song.song_id

    hot_ids = set()
    for title in hot_titles:
        if title in title_to_id:
            hot_ids.add(title_to_id[title])
    return hot_ids


def get_cover_path(base_dir: str, image_name: str) -> str:
    """根据 image_name（4 位 ID 字符串）返回封面图完整路径。"""
    return _music_id_to_cover_path(base_dir, int(image_name))
