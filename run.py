import os
import sys
import subprocess
import shutil
import venv

VENV_DIR = ".venv_space_race"
TEMP_DIR = ".temp_space_assets"

def create_venv():
    if not os.path.exists(VENV_DIR):
        print("[1/5] Создание изолированной виртуальной среды (.venv_space_race)...")
        venv.create(VENV_DIR, with_pip=True)

def get_venv_python():
    if sys.platform == "win32":
        return os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        return os.path.join(VENV_DIR, "bin", "python")

def run_bootstrap():
    print("=====================================================================")
    print("  3D ГЕНЕРАТОР ВИДЕО: SPACE RACE & ORBITAL TECH (1957 - OCT 2026)    ")
    print("=====================================================================")
    
    os.makedirs(TEMP_DIR, exist_ok=True)
    create_venv()
    venv_python = get_venv_python()
    
    print("[2/5] Установка библиотек и портативного кодека FFmpeg в виртуальную среду...")
    subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", "pip", "-q"])
    subprocess.check_call([
        venv_python, "-m", "pip", "install", 
        "pandas", "numpy", "matplotlib", "requests", "pillow", "imageio-ffmpeg", "-q"
    ])
    
    try:
        print("[3/5] Запуск 3D-рендеринга космоса, флагов, музыки и сборки MP4...")
        subprocess.check_call([venv_python, os.path.abspath(__file__), "--worker"])
    finally:
        print("[4/5] Самоочистка: удаление виртуальной среды и временных файлов...")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        shutil.rmtree(VENV_DIR, ignore_errors=True)
        print("[5/5] Очистка завершена! Готовый MP4-файл сохранен в папке проекта.")

def create_cosmic_flag(code, width=78, height=50):
    from PIL import Image, ImageDraw
    import numpy as np

    canvas = Image.new("RGBA", (width + 8, height + 8), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (width, height), (8, 4, 20, 190))
    canvas.paste(shadow, (5, 5))

    img = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    w, h = width, height

    if code == "us":
        stripe_h = h / 13.0
        for i in range(13):
            color = (178, 34, 52) if i % 2 == 0 else (245, 247, 250)
            draw.rectangle([0, int(i * stripe_h), w, int((i + 1) * stripe_h)], fill=color)
        draw.rectangle([0, 0, int(w * 0.42), int(h * 7 / 13.0)], fill=(40, 53, 107))
        for r in range(3):
            for c in range(4):
                cx = int(w * 0.06 + c * (w * 0.09))
                cy = int(h * 0.08 + r * (h * 0.16))
                draw.ellipse([cx-1, cy-1, cx+1, cy+1], fill=(255, 255, 255))
    elif code == "cn":
        draw.rectangle([0, 0, w, h], fill=(222, 41, 16))
        draw.ellipse([int(w*0.1), int(h*0.15), int(w*0.28), int(h*0.42)], fill=(255, 222, 0))
    elif code == "ru":
        draw.rectangle([0, 0, w, h//3], fill=(248, 250, 252))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(0, 57, 166))
        draw.rectangle([0, 2*h//3, w, h], fill=(213, 43, 30))
    elif code == "gb":
        draw.rectangle([0, 0, w, h], fill=(1, 33, 105))
        draw.line([(0, 0), (w, h)], fill=(255, 255, 255), width=7)
        draw.line([(0, h), (w, 0)], fill=(255, 255, 255), width=7)
        draw.line([(0, 0), (w, h)], fill=(200, 16, 46), width=3)
        draw.line([(0, h), (w, 0)], fill=(200, 16, 46), width=3)
        draw.rectangle([w//2 - 6, 0, w//2 + 6, h], fill=(255, 255, 255))
        draw.rectangle([0, h//2 - 6, w, h//2 + 6], fill=(255, 255, 255))
        draw.rectangle([w//2 - 3, 0, w//2 + 3, h], fill=(200, 16, 46))
        draw.rectangle([0, h//2 - 3, w, h//2 + 3], fill=(200, 16, 46))
    elif code == "jp":
        draw.rectangle([0, 0, w, h], fill=(248, 250, 252))
        r = int(h * 0.3)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], fill=(188, 0, 45))
    elif code == "in":
        draw.rectangle([0, 0, w, h//3], fill=(255, 153, 51))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(248, 250, 252))
        draw.rectangle([0, 2*h//3, w, h], fill=(19, 136, 8))
        r = int(h * 0.12)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], outline=(0, 0, 128), width=2)
    elif code == "fr":
        draw.rectangle([0, 0, w//3, h], fill=(0, 38, 84))
        draw.rectangle([w//3, 0, 2*w//3, h], fill=(248, 250, 252))
        draw.rectangle([2*w//3, 0, w, h], fill=(237, 41, 57))
    elif code == "de":
        draw.rectangle([0, 0, w, h//3], fill=(20, 20, 20))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(210, 16, 26))
        draw.rectangle([0, 2*h//3, w, h], fill=(255, 206, 0))
    elif code == "ca":
        draw.rectangle([0, 0, w//4, h], fill=(216, 6, 33))
        draw.rectangle([w//4, 0, 3*w//4, h], fill=(248, 250, 252))
        draw.rectangle([3*w//4, 0, w, h], fill=(216, 6, 33))
        r = int(h * 0.18)
        draw.polygon([(w//2, h//2 - r), (w//2 - r, h//2 + r//2), (w//2 + r, h//2 + r//2)], fill=(216, 6, 33))
    elif code == "it":
        draw.rectangle([0, 0, w//3, h], fill=(0, 140, 69))
        draw.rectangle([w//3, 0, 2*w//3, h], fill=(248, 250, 252))
        draw.rectangle([2*w//3, 0, w, h], fill=(205, 33, 42))
    elif code == "lu":
        draw.rectangle([0, 0, w, h//3], fill=(239, 51, 64))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(248, 250, 252))
        draw.rectangle([0, 2*h//3, w, h], fill=(0, 163, 224))
    elif code == "kr":
        draw.rectangle([0, 0, w, h], fill=(248, 250, 252))
        r = int(h * 0.22)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], fill=(205, 46, 58))
        draw.chord([w//2 - r, h//2 - r, w//2 + r, h//2 + r], start=0, end=180, fill=(0, 71, 160))
    elif code == "il":
        draw.rectangle([0, 0, w, h], fill=(248, 250, 252))
        draw.rectangle([0, int(h*0.12), w, int(h*0.25)], fill=(0, 56, 184))
        draw.rectangle([0, int(h*0.75), w, int(h*0.88)], fill=(0, 56, 184))
        r = int(h * 0.18)
        draw.polygon([(w//2, h//2 - r), (w//2 - r, h//2 + r//2), (w//2 + r, h//2 + r//2)], outline=(0, 56, 184), width=2)
        draw.polygon([(w//2, h//2 + r), (w//2 - r, h//2 - r//2), (w//2 + r, h//2 - r//2)], outline=(0, 56, 184), width=2)
    elif code == "ar":
        draw.rectangle([0, 0, w, h//3], fill=(116, 172, 223))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(248, 250, 252))
        draw.rectangle([0, 2*h//3, w, h], fill=(116, 172, 223))
        draw.ellipse([w//2 - 4, h//2 - 4, w//2 + 4, h//2 + 4], fill=(246, 180, 14))
    elif code == "es":
        draw.rectangle([0, 0, w, h//4], fill=(170, 21, 27))
        draw.rectangle([0, h//4, w, 3*h//4], fill=(241, 191, 0))
        draw.rectangle([0, 3*h//4, w, h], fill=(170, 21, 27))
    elif code == "au":
        draw.rectangle([0, 0, w, h], fill=(1, 33, 105))
        draw.line([(0, 0), (w//2, h//2)], fill=(255, 255, 255), width=3)
        draw.line([(0, h//2), (w//2, 0)], fill=(255, 255, 255), width=3)
        draw.rectangle([w//4 - 2, 0, w//4 + 2, h//2], fill=(200, 16, 46))
        draw.rectangle([0, h//4 - 2, w//2, h//4 + 2], fill=(200, 16, 46))
    elif code == "br":
        draw.rectangle([0, 0, w, h], fill=(0, 156, 59))
        draw.polygon([(w//2, int(h*0.12)), (int(w*0.88), h//2), (w//2, int(h*0.88)), (int(w*0.12), h//2)], fill=(255, 223, 0))
        r = int(h * 0.18)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], fill=(0, 39, 118))
    elif code == "tr":
        draw.rectangle([0, 0, w, h], fill=(227, 10, 23))
        r = int(h * 0.22)
        draw.ellipse([w//2 - r - 4, h//2 - r, w//2 + r - 4, h//2 + r], fill=(255, 255, 255))
        r2 = int(h * 0.17)
        draw.ellipse([w//2 - r2, h//2 - r2, w//2 + r2, h//2 + r2], fill=(227, 10, 23))

    canvas.paste(img, (0, 0))
    return np.array(canvas)

def run_worker():
    import math
    import wave
    import pandas as pd
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.patches import Polygon, FancyBboxPatch
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox
    import imageio_ffmpeg

    FPS = 30
    DURATION_SEC = 40
    TOTAL_FRAMES = FPS * DURATION_SEC

    COUNTRIES_ISO = {
        "United States": "us", "Russia / USSR": "ru", "China": "cn", "United Kingdom": "gb",
        "Japan": "jp", "France": "fr", "India": "in", "Germany": "de",
        "Canada": "ca", "Luxembourg": "lu", "Italy": "it", "South Korea": "kr",
        "Argentina": "ar", "Israel": "il", "Spain": "es", "Australia": "au",
        "Brazil": "br", "Turkey": "tr"
    }

    START_YEAR = 1957.75
    END_YEAR = 2026.83
    TITLE_MAIN = "SPACE RACE: ORBITAL SPACECRAFT"
    TITLE_SUB = "CUMULATIVE SATELLITES & SPACECRAFT IN ORBIT (1957 – OCT 2026)"
    TITLE_META = "OFFICIAL UNOOSA • NASA • COSMOS ORBITAL TELEMETRY"
    FINAL_OUTPUT = "space_race_orbital_1957_2026_shorts.mp4"

    # Historical Orbital Spacecraft & Satellites (1957 Sputnik-1 to Oct 2026)
    ANCHORS = {
        "Russia / USSR":  {1957: 2.0,  1960: 12.0, 1965: 165.0, 1970: 590.0, 1980: 1680.0, 1990: 2790.0, 2000: 3260.0, 2010: 3440.0, 2020: 3630.0, 2026: 3840.0},
        "United States":  {1957: 0.5,  1960: 38.0, 1965: 310.0, 1970: 640.0, 1980: 980.0,  1990: 1340.0, 2000: 1790.0, 2010: 2150.0, 2020: 3480.0, 2026: 6420.0},
        "China":          {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 1.0,   1980: 9.0,    1990: 32.0,   2000: 85.0,   2010: 240.0,  2020: 980.0,  2026: 2680.0},
        "United Kingdom": {1957: 0.0,  1960: 0.0,  1965: 2.0,   1970: 6.0,   1980: 15.0,   1990: 28.0,   2000: 52.0,   2010: 95.0,   2020: 340.0,  2026: 980.0},
        "Japan":          {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 2.0,   1980: 22.0,   1990: 58.0,   2000: 115.0,  2010: 195.0,  2020: 390.0,  2026: 620.0},
        "France":         {1957: 0.0,  1960: 0.0,  1965: 1.0,   1970: 8.0,   1980: 26.0,   1990: 54.0,   2000: 98.0,   2010: 165.0,  2020: 320.0,  2026: 540.0},
        "India":          {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 0.0,   1980: 3.0,    1990: 14.0,   2000: 36.0,   2010: 82.0,   2020: 215.0,  2026: 430.0},
        "Germany":        {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 3.0,   1980: 11.0,   1990: 24.0,   2000: 48.0,   2010: 92.0,   2020: 210.0,  2026: 390.0},
        "Canada":         {1957: 0.0,  1960: 0.0,  1965: 2.0,   1970: 5.0,   1980: 12.0,   1990: 22.0,   2000: 38.0,   2010: 68.0,   2020: 165.0,  2026: 340.0},
        "Luxembourg":     {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 0.0,   1980: 0.0,    1990: 4.0,    2000: 28.0,   2010: 65.0,   2020: 175.0,  2026: 310.0},
        "Italy":          {1957: 0.0,  1960: 0.0,  1965: 1.0,   1970: 3.0,   1980: 8.0,    1990: 16.0,   2000: 34.0,   2010: 62.0,   2020: 145.0,  2026: 280.0},
        "South Korea":    {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 0.0,   1980: 0.0,    1990: 1.0,    2000: 12.0,   2010: 32.0,   2020: 110.0,  2026: 240.0},
        "Argentina":      {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 0.0,   1980: 0.0,    1990: 2.0,    2000: 10.0,   2010: 22.0,   2020: 95.0,   2026: 195.0},
        "Israel":         {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 0.0,   1980: 0.0,    1990: 3.0,    2000: 14.0,   2010: 34.0,   2020: 88.0,   2026: 165.0},
        "Spain":          {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 1.0,   1980: 2.0,    1990: 6.0,    2000: 18.0,   2010: 42.0,   2020: 92.0,   2026: 155.0},
        "Australia":      {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 2.0,   1980: 4.0,    1990: 10.0,   2000: 19.0,   2010: 35.0,   2020: 84.0,   2026: 145.0},
        "Brazil":         {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 0.0,   1980: 1.0,    1990: 7.0,    2000: 17.0,   2010: 31.0,   2020: 72.0,   2026: 125.0},
        "Turkey":         {1957: 0.0,  1960: 0.0,  1965: 0.0,   1970: 0.0,   1980: 0.0,    1990: 1.0,    2000: 9.0,    2010: 21.0,   2020: 58.0,   2026: 110.0}
    }

    print(" -> Подготовка прямоугольных 3D-флагов стран...")
    flags = {country: create_cosmic_flag(code, 78, 50) for country, code in COUNTRIES_ISO.items()}

    print(" -> Генерация космического саундтрека (Cosmic Odyssey Synth - CC0 License)...")
    audio_path = os.path.join(TEMP_DIR, "cosmic_music.wav")
    license_lines = [
        "MUSIC LICENSE CERTIFICATE (CC0 1.0 Universal - Public Domain Dedication)",
        "=======================================================================",
        "Track Title: Cosmic Odyssey Telemetry (Space Synthwave & Ambient Score)",
        "License: Creative Commons Zero (CC0 1.0 Universal)",
        "Status: 100% Royalty-Free / Safe for YouTube Shorts, Instagram Reels, TikTok monetization.",
        "Permissions: Commercial and non-commercial use, modification, and distribution permitted without attribution."
    ]
    with open("MUSIC_LICENSE_CC0.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(license_lines) + "\n")

    sample_rate = 44100
    n_samples = sample_rate * DURATION_SEC
    t = np.linspace(0, DURATION_SEC, n_samples, endpoint=False)

    # Space chord progression: D minor -> Bb major -> F major -> C major
    freqs_base = np.select(
        [(t % 10) < 2.5, (t % 10) < 5.0, (t % 10) < 7.5, (t % 10) >= 7.5],
        [73.42, 58.27, 87.31, 65.41]
    )
    sub_bass = 0.28 * np.sin(2 * math.pi * freqs_base * t)
    space_pad1 = 0.16 * np.sin(2 * math.pi * (freqs_base * 2.0) * t + 0.3 * np.sin(2 * math.pi * 0.5 * t))
    space_pad2 = 0.12 * np.sin(2 * math.pi * (freqs_base * 3.0) * t + 0.8)
    # Crystalline orbital telemetry arpeggio
    arp_gate = 0.5 + 0.5 * np.sin(2 * math.pi * 6.0 * t)
    shimmer = 0.07 * np.sin(2 * math.pi * (freqs_base * 6.0) * t) * arp_gate

    envelope = np.ones_like(t)
    fade_len = sample_rate * 2
    envelope[:fade_len] = np.linspace(0, 1, fade_len)
    envelope[-fade_len:] = np.linspace(1, 0, fade_len)

    stereo_left = np.clip((sub_bass + space_pad1 + shimmer) * envelope, -0.95, 0.95)
    stereo_right = np.clip((sub_bass + space_pad2 + shimmer) * envelope, -0.95, 0.95)

    interleaved = np.empty((n_samples * 2,), dtype=np.int16)
    interleaved[0::2] = (stereo_left * 32767).astype(np.int16)
    interleaved[1::2] = (stereo_right * 32767).astype(np.int16)

    with wave.open(audio_path, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(interleaved.tobytes())

    print(" -> Построение матрицы орбитальных данных (1957 - 2026) с плавной интерполяцией...")
    fine_years = np.linspace(START_YEAR, END_YEAR, TOTAL_FRAMES)
    val_dict = {}
    for country, anchors in ANCHORS.items():
        yrs = sorted(list(anchors.keys()))
        vals = [anchors[y] for y in yrs]
        val_dict[country] = np.interp(fine_years, yrs, vals)

    df_values = pd.DataFrame(val_dict, index=fine_years)
    df_values = df_values.where(df_values > 0, np.nan)
    df_ranks = df_values.rank(axis=1, method='first', ascending=True).fillna(0.0)

    win_size = 35
    hann_win = np.hanning(win_size)
    hann_win /= hann_win.sum()
    df_ranks_smooth = df_ranks.apply(
        lambda col: np.convolve(np.pad(col.values, (win_size//2, win_size//2), mode='edge'), hann_win, mode='valid')[:len(col)]
    )

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    plt.rcParams['animation.ffmpeg_path'] = ffmpeg_exe

    print(f" -> Рендеринг 40-секундного 3D-видео HD 9:16 ({TOTAL_FRAMES} кадров, 30 FPS)...")
    BG_OUTER = '#090614'
    BG_PLOT = '#110b24'

    fig = plt.figure(figsize=(9, 16), dpi=120)
    fig.patch.set_facecolor(BG_OUTER)

    # Background starfield layer
    star_ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    star_ax.set_xlim(0, 1)
    star_ax.set_ylim(0, 1)
    star_ax.set_xticks([])
    star_ax.set_yticks([])
    np.random.seed(108)
    sx = np.random.uniform(0.02, 0.98, 110)
    sy = np.random.uniform(0.02, 0.98, 110)
    ss = np.random.uniform(1.5, 16, 110)
    sa = np.random.uniform(0.12, 0.50, 110)
    for x_i, y_i, s_i, a_i in zip(sx, sy, ss, sa):
        star_ax.scatter([x_i], [y_i], s=s_i, color='#ddd6fe', alpha=a_i, edgecolors='none')

    # Futuristic Sci-Fi Header Panel at top (never touches top bar!)
    header_box = FancyBboxPatch(
        (0.04, 0.885), 0.92, 0.088,
        boxstyle="round,pad=0.01,rounding_size=0.018",
        transform=fig.transFigure,
        facecolor='#170f30', edgecolor='#7c3aed', linewidth=1.6, alpha=0.95, zorder=2
    )
    fig.patches.append(header_box)

    fig.text(
        0.5, 0.946, TITLE_MAIN,
        color='#ffffff', fontsize=20.5, fontweight='bold', fontfamily='DejaVu Sans', ha='center', va='center', zorder=4
    )
    fig.text(
        0.5, 0.916, TITLE_SUB,
        color='#fbbf24', fontsize=10.0, fontweight='bold', fontfamily='DejaVu Sans Mono', ha='center', va='center', zorder=4
    )
    fig.text(
        0.5, 0.896, TITLE_META,
        color='#c4b5fd', fontsize=8.8, fontfamily='DejaVu Sans Mono', ha='center', va='center', zorder=4
    )

    # Left 39% reserved for Rank Badge (#01) + Country Name + Flag!
    ax = fig.add_axes([0.39, 0.06, 0.57, 0.80])

    top_n = 12
    max_rank = len(COUNTRIES_ISO)
    min_visible_rank = max_rank - top_n + 1.0
    cmap = plt.cm.plasma

    def update(frame_idx):
        ax.clear()
        ax.set_facecolor(BG_PLOT)

        current_time = df_values.index[frame_idx]
        year_int = int(current_time)
        month_int = min(12, max(1, int((current_time - year_int) * 12) + 1))
        month_names = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        date_str = f"{month_names[month_int - 1]} {year_int}"

        vals_row = df_values.iloc[frame_idx]
        ranks_row = df_ranks_smooth.iloc[frame_idx]

        visible = ranks_row[ranks_row >= min_visible_rank - 0.7].dropna()
        max_val = max(vals_row.max(), 5.0)
        if pd.isna(max_val) or max_val <= 0:
            max_val = 5.0

        ax.set_xlim(0, max_val * 1.32)
        ax.set_ylim(min_visible_rank - 0.65, max_rank + 0.80)

        ax.xaxis.grid(True, color='#3b2d54', linestyle=':', linewidth=1.1, alpha=0.75, zorder=0)
        ax.set_axisbelow(True)

        dx = max_val * 0.026
        dy = 0.165
        bar_h = 0.46

        for country, smooth_y in visible.items():
            val = vals_row[country]
            if pd.isna(val) or val <= 0:
                continue

            alpha = 1.0
            if smooth_y < min_visible_rank:
                alpha = max(0.0, min(1.0, (smooth_y - (min_visible_rank - 0.7)) / 0.7))

            norm_rank = np.clip((smooth_y - min_visible_rank) / max(1, top_n - 1), 0, 1)
            rank_num = max(1, min(top_n, int(round(max_rank - smooth_y + 1))))

            c_base = cmap(0.16 + 0.74 * norm_rank)
            c_front = (c_base[0], c_base[1], c_base[2], alpha)
            c_bottom_strip = tuple(max(0.0, c_base[i] * 0.72) for i in range(3)) + (0.65 * alpha,)
            c_top = tuple(min(1.0, c_base[i] * 1.35 + 0.14) for i in range(3)) + (alpha,)
            c_side = tuple(max(0.0, c_base[i] * 0.52) for i in range(3)) + (alpha,)

            y0 = smooth_y - bar_h / 2.0
            y1 = smooth_y + bar_h / 2.0

            # 1. Deep 3D Drop Shadow
            shadow_poly = Polygon([
                (0, y0 - 0.10),
                (val + dx * 1.15, y0 - 0.10),
                (val + dx * 1.65, y1 - 0.10 + dy * 0.75),
                (0, y1 - 0.10)
            ], closed=True, facecolor='#04020a', alpha=0.80 * alpha, edgecolor='none', zorder=2)
            ax.add_patch(shadow_poly)

            # 2. Main Front Face + Lower Cylindrical Shade
            front_poly = Polygon([
                (0, y0), (val, y0), (val, y1), (0, y1)
            ], closed=True, facecolor=c_front, edgecolor='none', zorder=3)
            ax.add_patch(front_poly)

            bottom_shade_poly = Polygon([
                (0, y0), (val, y0), (val, y0 + bar_h * 0.35), (0, y0 + bar_h * 0.35)
            ], closed=True, facecolor=c_bottom_strip, edgecolor='none', zorder=3.5)
            ax.add_patch(bottom_shade_poly)

            # 3. Specular Glass Highlight
            glass_poly = Polygon([
                (0, y1 - bar_h * 0.22), (val, y1 - bar_h * 0.22), (val, y1), (0, y1)
            ], closed=True, facecolor='#ffffff', alpha=0.22 * alpha, edgecolor='none', zorder=4)
            ax.add_patch(glass_poly)

            # 4. TRUE 3D TOP EXTRUSION FACE
            top_poly = Polygon([
                (0, y1), (val, y1), (val + dx, y1 + dy), (dx, y1 + dy)
            ], closed=True, facecolor=c_top, edgecolor='none', zorder=4)
            ax.add_patch(top_poly)

            # 5. TRUE 3D RIGHT SIDE EXTRUSION FACE
            side_poly = Polygon([
                (val, y0), (val + dx, y0 + dy), (val + dx, y1 + dy), (val, y1)
            ], closed=True, facecolor=c_side, edgecolor='none', zorder=4)
            ax.add_patch(side_poly)

            # 6. 3D Wireframe Edge Highlights
            ax.plot([0, val], [y1, y1], color='#ffffff', alpha=0.45 * alpha, linewidth=0.9, zorder=5)
            ax.plot([val, val + dx], [y1, y1 + dy], color='#ffffff', alpha=0.55 * alpha, linewidth=1.0, zorder=5)
            ax.plot([val, val], [y0, y1], color='#ffffff', alpha=0.35 * alpha, linewidth=0.8, zorder=5)

            # 7. RANK BADGE on far left (-0.64 axes fraction)
            rank_color = '#fbbf24' if rank_num <= 3 else '#a78bfa'
            ax.text(
                -0.64, smooth_y, f"#{rank_num:02d}",
                transform=ax.get_yaxis_transform(),
                color=rank_color, fontsize=10.5, fontweight='bold', fontfamily='DejaVu Sans Mono',
                va='center', ha='left', alpha=alpha, zorder=6, clip_on=False
            )

            # 8. COUNTRY NAME in fixed column (-0.165 axes fraction)
            ax.text(
                -0.165, smooth_y, country.upper(),
                transform=ax.get_yaxis_transform(),
                color='#f8fafc', fontsize=11.0, fontweight='bold', fontfamily='DejaVu Sans',
                va='center', ha='right', alpha=alpha, zorder=6, clip_on=False
            )

            # 9. RECTANGULAR FLAG in fixed column (-0.078 axes fraction)
            if country in flags:
                imagebox = OffsetImage(flags[country], zoom=0.44, alpha=alpha)
                ab = AnnotationBbox(
                    imagebox, (-0.078, smooth_y),
                    xycoords=('axes fraction', 'data'),
                    frameon=False,
                    box_alignment=(0.5, 0.5),
                    zorder=5,
                    annotation_clip=False
                )
                ax.add_artist(ab)

            # 10. VALUE LABEL (right of the 3D side face)
            val_int = max(1, int(round(val)))
            ax.text(
                val + dx + max_val * 0.020, smooth_y + dy * 0.30, f"{val_int:,}",
                color='#fde68a' if rank_num <= 3 else '#e9d5ff',
                fontsize=12.0, fontweight='bold', fontfamily='DejaVu Sans Mono',
                va='center', ha='left', alpha=alpha, zorder=6
            )

        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#8b5cf6')
        ax.spines['left'].set_linewidth(1.8)
        ax.spines['bottom'].set_color('#4c1d95')
        ax.tick_params(axis='x', colors='#c4b5fd', labelsize=9.5)
        for label in ax.get_xticklabels():
            label.set_fontfamily('DejaVu Sans Mono')

        # Futuristic Telemetry HUD Box in bottom-right corner
        hud_box = FancyBboxPatch(
            (0.53, 0.025), 0.43, 0.145,
            boxstyle="round,pad=0.015,rounding_size=0.02",
            transform=ax.transAxes,
            facecolor='#1a1133', edgecolor='#7c3aed', linewidth=1.5, alpha=0.92, zorder=5
        )
        ax.add_patch(hud_box)

        ax.text(
            0.93, 0.122, f"{year_int}", transform=ax.transAxes,
            color='#ffffff', fontsize=38, fontweight='bold', fontfamily='DejaVu Sans Mono',
            ha='right', va='center', zorder=6
        )
        ax.text(
            0.93, 0.072, f"{date_str}", transform=ax.transAxes,
            color='#fbbf24', fontsize=13.5, fontweight='bold', fontfamily='DejaVu Sans Mono',
            ha='right', va='center', zorder=6
        )
        total_sats = int(vals_row.dropna().sum())
        ax.text(
            0.93, 0.042, f"ORBIT TOTAL: {total_sats:,}", transform=ax.transAxes,
            color='#c4b5fd', fontsize=9.0, fontweight='bold', fontfamily='DejaVu Sans Mono',
            ha='right', va='center', zorder=6
        )

        if frame_idx % 120 == 0 or frame_idx == TOTAL_FRAMES - 1:
            pct = int((frame_idx + 1) / TOTAL_FRAMES * 100)
            print(f"    Прогресс 3D-рендеринга: {pct}% ({frame_idx + 1}/{TOTAL_FRAMES} кадров)")

    temp_video = os.path.join(TEMP_DIR, "silent_space_video.mp4")
    writer = animation.FFMpegWriter(fps=FPS, codec='libx264', bitrate=5500, extra_args=['-pix_fmt', 'yuv420p'])
    anim = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, repeat=False)
    anim.save(temp_video, writer=writer)
    plt.close(fig)

    print(" -> Наложение космической музыки и сборка финального MP4...")
    subprocess.check_call([
        ffmpeg_exe, "-y",
        "-i", temp_video,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        FINAL_OUTPUT
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f" -> УСПЕХ! Готовый видеофайл сохранен: {FINAL_OUTPUT}")

if __name__ == "__main__":
    if "--worker" in sys.argv:
        run_worker()
    else:
        run_bootstrap()
