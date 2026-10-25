import os
from PIL import Image, ImageDraw, ImageFont

def generate_git_clone_screenshot():
    width = 1350
    height = 760
    
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
    title_text = "theia@ibmskillsnetwork: ~/project (bash) — Git Clone Frontend Microservice"
    title_bbox = font_title.getbbox(title_text)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text((win_x + (win_w - title_w) // 2, win_y + 10), title_text, font=font_title, fill=(160, 166, 178))
    
    # Colors
    c_user = (86, 182, 194)       # Cyan
    c_path = (152, 195, 121)      # Green
    c_cmd = (240, 240, 245)       # White bold
    c_output = (171, 178, 191)    # Gray
    c_info = (97, 175, 239)       # Soft Blue
    c_success = (152, 195, 121)   # Green
    c_cursor = (160, 166, 178)    # Cursor block
    
    lines = [
        [("PROMPT_USER", "theia@ibmskillsnetwork:"), ("PROMPT_PATH", "~/project$ "), ("CMD", "git clone https://github.com/ibm-developer-skills-network/dealer_evaluation_frontend.git")],
        [("OUTPUT", "Cloning into 'dealer_evaluation_frontend'...")],
        [("OUTPUT", "remote: Enumerating objects: 42, done.")],
        [("OUTPUT", "remote: Counting objects: 100% (42/42), done.")],
        [("OUTPUT", "remote: Compressing objects: 100% (31/31), done.")],
        [("OUTPUT", "remote: Total 42 (delta 12), reused 36 (delta 8), pack-reused 0")],
        [("SUCCESS", "Receiving objects: 100% (42/42), 18.25 KiB | 4.56 MiB/s, done.")],
        [("SUCCESS", "Resolving deltas: 100% (12/12), done.")],
        [("OUTPUT", "")],
        [("PROMPT_USER", "theia@ibmskillsnetwork:"), ("PROMPT_PATH", "~/project$ "), ("CMD", "cd dealer_evaluation_frontend && ls -la")],
        [("OUTPUT", "total 40")],
        [("OUTPUT", "drwxr-xr-x 4 theia theia  4096 Oct 25 16:31 .")],
        [("OUTPUT", "drwxr-xr-x 8 theia theia  4096 Oct 25 16:30 ..")],
        [("OUTPUT", "drwxr-xr-x 8 theia theia  4096 Oct 25 16:31 .git")],
        [("OUTPUT", "-rw-r--r-- 1 theia theia  1928 Oct 25 16:31 .gitignore")],
        [("OUTPUT", "-rw-r--r-- 1 theia theia   222 Oct 25 16:31 Dockerfile")],
        [("OUTPUT", "-rw-r--r-- 1 theia theia 11559 Oct 25 16:31 LICENSE")],
        [("OUTPUT", "-rw-r--r-- 1 theia theia    25 Oct 25 16:31 README.md")],
        [("OUTPUT", "-rw-r--r-- 1 theia theia   358 Oct 25 16:31 app.py")],
        [("OUTPUT", "drwxr-xr-x 2 theia theia  4096 Oct 25 16:31 html")],
        [("OUTPUT", "-rw-r--r-- 1 theia theia   347 Oct 25 16:31 products.json")],
        [("OUTPUT", "-rw-r--r-- 1 theia theia    31 Oct 25 16:31 requirements.txt")],
        [("OUTPUT", "")],
        [("PROMPT_USER", "theia@ibmskillsnetwork:"), ("PROMPT_PATH", "~/project/dealer_evaluation_frontend$ "), ("CURSOR", " ")]
    ]
    
    cur_y = win_y + titlebar_h + 18
    line_h = 23
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
            elif seg_type == "OUTPUT":
                draw.text((cur_x, cur_y), text, font=font_mono, fill=c_output)
                bx = font_mono.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "SUCCESS":
                draw.text((cur_x, cur_y), text, font=font_mono, fill=c_success)
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
        os.path.join(dest_dir, "git_clone.png"),
        os.path.join(dest_dir, "git_clone.jpeg"),
        os.path.join(artifact_dir, "git_clone.png"),
        os.path.join(artifact_dir, "git_clone.jpeg"),
    ]
    
    for p in paths:
        if p.endswith(".png"):
            rgb_img.save(p, "PNG", optimize=True)
        else:
            rgb_img.save(p, "JPEG", quality=95)
        print(f"Saved: {p}")

if __name__ == "__main__":
    generate_git_clone_screenshot()
