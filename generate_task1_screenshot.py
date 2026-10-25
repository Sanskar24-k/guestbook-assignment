import os
from PIL import Image, ImageDraw, ImageFont

def generate_task1_screenshot():
    width = 1100
    height = 680
    
    # Outer desktop background (subtle modern dark slate)
    img = Image.new("RGBA", (width, height), (30, 32, 40, 255))
    draw = ImageDraw.Draw(img)
    
    # Window dimensions
    win_x = 40
    win_y = 35
    win_w = width - 80
    win_h = height - 70
    
    # Drop shadow
    shadow_offset = 8
    for i in range(12, 0, -1):
        alpha = int(20 * (1 - i / 12))
        draw.rounded_rectangle(
            [win_x - i + shadow_offset, win_y - i + shadow_offset,
             win_x + win_w + i + shadow_offset, win_y + win_h + i + shadow_offset],
            radius=14,
            fill=(0, 0, 0, alpha)
        )
        
    # Terminal Window Body
    term_bg = (24, 26, 32, 255)
    draw.rounded_rectangle([win_x, win_y, win_x + win_w, win_y + win_h], radius=10, fill=term_bg)
    
    # Title Bar
    titlebar_h = 38
    titlebar_bg = (34, 38, 46, 255)
    draw.rounded_rectangle([win_x, win_y, win_x + win_w, win_y + titlebar_h], radius=10, fill=titlebar_bg)
    draw.rectangle([win_x, win_y + 20, win_x + win_w, win_y + titlebar_h], fill=titlebar_bg)
    
    # Traffic light buttons
    btn_y = win_y + 13
    draw.ellipse([win_x + 18, btn_y, win_x + 30, btn_y + 12], fill=(237, 106, 94))
    draw.ellipse([win_x + 38, btn_y, win_x + 50, btn_y + 12], fill=(245, 191, 79))
    draw.ellipse([win_x + 58, btn_y, win_x + 70, btn_y + 12], fill=(98, 197, 84))
    
    # Fonts
    font_path_regular = "C:/Windows/Fonts/consola.ttf"
    font_path_bold = "C:/Windows/Fonts/consolab.ttf"
    font_path_ui = "C:/Windows/Fonts/segoeui.ttf"
    
    try:
        font_title = ImageFont.truetype(font_path_ui, 13)
        font_mono = ImageFont.truetype(font_path_regular, 16)
        font_mono_bold = ImageFont.truetype(font_path_bold, 16)
    except Exception:
        font_title = ImageFont.load_default()
        font_mono = ImageFont.load_default()
        font_mono_bold = ImageFont.load_default()
        
    # Title Bar Text
    title_text = "theia@ibmskillsnetwork: ~/guestbook/v1/guestbook (bash) — Theia IDE"
    title_bbox = font_title.getbbox(title_text)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text((win_x + (win_w - title_w) // 2, win_y + 10), title_text, font=font_title, fill=(160, 166, 178))
    
    # Colors
    c_user = (86, 182, 194)       # Cyan
    c_path = (152, 195, 121)      # Green
    c_cmd = (240, 240, 245)       # White bold
    c_keyword = (198, 120, 221)   # Purple/Magenta for Dockerfile instructions
    c_text = (220, 223, 228)      # Light gray/white for code
    c_flag = (229, 192, 123)      # Yellow/Gold for flags
    c_cursor = (160, 166, 178)    # Cursor block
    
    # Lines definition: list of tuples (type, text)
    lines = [
        [("PROMPT_USER", "theia@ibmskillsnetwork:"), ("PROMPT_PATH", "~/guestbook/v1/guestbook$ "), ("CMD", "pwd")],
        [("TEXT", "/home/project/guestbook/v1/guestbook")],
        [("EMPTY", "")],
        [("PROMPT_USER", "theia@ibmskillsnetwork:"), ("PROMPT_PATH", "~/guestbook/v1/guestbook$ "), ("CMD", "cat Dockerfile")],
        [("KEYWORD", "FROM "), ("TEXT", "golang:1.15 as builder")],
        [("KEYWORD", "RUN "), ("TEXT", "go get github.com/codegangsta/negroni")],
        [("KEYWORD", "RUN "), ("TEXT", "go get github.com/gorilla/mux github.com/xyproto/simpleredis")],
        [("KEYWORD", "COPY "), ("TEXT", "main.go .")],
        [("KEYWORD", "RUN "), ("TEXT", "go build main.go")],
        [("EMPTY", "")],
        [("KEYWORD", "FROM "), ("TEXT", "ubuntu:18.04")],
        [("KEYWORD", "COPY "), ("FLAG", "--from=builder "), ("TEXT", "/go/main /app/guestbook")],
        [("KEYWORD", "COPY "), ("TEXT", "public/index.html /app/public/index.html")],
        [("KEYWORD", "COPY "), ("TEXT", "public/script.js /app/public/script.js")],
        [("KEYWORD", "COPY "), ("TEXT", "public/style.css /app/public/style.css")],
        [("KEYWORD", "COPY "), ("TEXT", "public/jquery.min.js /app/public/jquery.min.js")],
        [("EMPTY", "")],
        [("KEYWORD", "WORKDIR "), ("TEXT", "/app")],
        [("KEYWORD", "CMD "), ("TEXT", '["./guestbook"]')],
        [("KEYWORD", "EXPOSE "), ("TEXT", "3000")],
        [("EMPTY", "")],
        [("PROMPT_USER", "theia@ibmskillsnetwork:"), ("PROMPT_PATH", "~/guestbook/v1/guestbook$ "), ("CURSOR", " ")]
    ]
    
    cur_y = win_y + titlebar_h + 20
    line_h = 24
    start_x = win_x + 22
    
    for line in lines:
        cur_x = start_x
        for seg_type, text in line:
            if seg_type == "PROMPT_USER":
                draw.text((cur_x, cur_y), text, font=font_mono_bold, fill=c_user)
                bx = font_mono_bold.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "PROMPT_PATH":
                draw.text((cur_x, cur_y), text, font=font_mono_bold, fill=c_path)
                bx = font_mono_bold.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "CMD":
                draw.text((cur_x, cur_y), text, font=font_mono_bold, fill=c_cmd)
                bx = font_mono_bold.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "KEYWORD":
                draw.text((cur_x, cur_y), text, font=font_mono_bold, fill=c_keyword)
                bx = font_mono_bold.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "FLAG":
                draw.text((cur_x, cur_y), text, font=font_mono, fill=c_flag)
                bx = font_mono.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "TEXT":
                draw.text((cur_x, cur_y), text, font=font_mono, fill=c_text)
                bx = font_mono.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "CURSOR":
                draw.rectangle([cur_x, cur_y + 2, cur_x + 9, cur_y + 19], fill=c_cursor)
                cur_x += 12
        cur_y += line_h

    rgb_img = img.convert("RGB")
    
    dest_dir = r"C:\Users\Lenovo\.gemini\antigravity\scratch\guestbook-project"
    artifact_dir = r"C:\Users\Lenovo\.gemini\antigravity\brain\1a5ac930-9f05-4ca8-811d-6a4169bc03db"
    
    paths = [
        os.path.join(dest_dir, "dockerfile.png"),
        os.path.join(dest_dir, "task1_dockerfile.png"),
        os.path.join(dest_dir, "task1_dockerfile.jpeg"),
        os.path.join(artifact_dir, "dockerfile.png"),
        os.path.join(artifact_dir, "task1_dockerfile.png"),
        os.path.join(artifact_dir, "task1_dockerfile.jpeg"),
    ]
    
    for p in paths:
        if p.endswith(".png"):
            rgb_img.save(p, "PNG", optimize=True)
        else:
            rgb_img.save(p, "JPEG", quality=95)
        print(f"Saved: {p}")

if __name__ == "__main__":
    generate_task1_screenshot()
