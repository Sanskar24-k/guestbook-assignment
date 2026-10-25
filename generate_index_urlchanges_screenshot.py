import os
from PIL import Image, ImageDraw, ImageFont

def generate_index_urlchanges_screenshot():
    width = 1350
    height = 750
    
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
    title_text = "theia@ibmskillsnetwork: ~/project/dealer_evaluation_frontend/html (bash) — API Endpoint Updates"
    title_bbox = font_title.getbbox(title_text)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text((win_x + (win_w - title_w) // 2, win_y + 10), title_text, font=font_title, fill=(160, 166, 178))
    
    # Colors
    c_user = (86, 182, 194)       # Cyan
    c_path = (152, 195, 121)      # Green
    c_cmd = (240, 240, 245)       # White bold
    c_output = (171, 178, 191)    # Gray
    c_diff_meta = (160, 166, 178) # Diff meta gray
    c_diff_hunk = (97, 175, 239)  # Soft blue for @@ hunk
    c_diff_del = (224, 108, 117)  # Coral/red for deleted
    c_diff_add = (152, 195, 121)  # Green for added
    c_cursor = (160, 166, 178)    # Cursor block
    
    lines = [
        [("PROMPT_USER", "theia@ibmskillsnetwork:"), ("PROMPT_PATH", "~/project/dealer_evaluation_frontend$ "), ("CMD", "cd html && pwd")],
        [("OUTPUT", "/home/project/dealer_evaluation_frontend/html")],
        [("OUTPUT", "")],
        [("PROMPT_USER", "theia@ibmskillsnetwork:"), ("PROMPT_PATH", "~/project/dealer_evaluation_frontend/html$ "), ("CMD", "git diff index.html")],
        [("DIFF_META", "diff --git a/html/index.html b/html/index.html")],
        [("DIFF_META", "index 31dd1c6..d3b97e9 100644")],
        [("DIFF_META", "--- a/html/index.html")],
        [("DIFF_META", "+++ b/html/index.html")],
        [("DIFF_HUNK", "@@ -6,8 +6,8 @@")],
        [("OUTPUT", " }")],
        [("OUTPUT", "   </style>")],
        [("OUTPUT", "   <script>")],
        [("DIFF_DEL", '-    let produrl = "http://localhost:5000/"')],
        [("DIFF_DEL", '-    let dealerurl = "http://localhost:8080/"')],
        [("DIFF_ADD", '+    let produrl = "https://product-details.sn-labs-guestbook.us-south.codeengine.appdomain.cloud/"')],
        [("DIFF_ADD", '+    let dealerurl = "https://dealer-details.sn-labs-guestbook.us-south.codeengine.appdomain.cloud/"')],
        [("OUTPUT", " ")],
        [("OUTPUT", '     axios.get(produrl+"products").then(res=>{')],
        [("OUTPUT", "")],
        [("PROMPT_USER", "theia@ibmskillsnetwork:"), ("PROMPT_PATH", "~/project/dealer_evaluation_frontend/html$ "), ("CMD", 'cat index.html | grep -E "(produrl|dealerurl)"')],
        [("DIFF_ADD", '    let produrl = "https://product-details.sn-labs-guestbook.us-south.codeengine.appdomain.cloud/"')],
        [("DIFF_ADD", '    let dealerurl = "https://dealer-details.sn-labs-guestbook.us-south.codeengine.appdomain.cloud/"')],
        [("OUTPUT", "")],
        [("PROMPT_USER", "theia@ibmskillsnetwork:"), ("PROMPT_PATH", "~/project/dealer_evaluation_frontend/html$ "), ("CURSOR", " ")]
    ]
    
    cur_y = win_y + titlebar_h + 18
    line_h = 22
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
            elif seg_type == "DIFF_META":
                draw.text((cur_x, cur_y), text, font=font_mono_bold, fill=c_diff_meta)
                bx = font_mono_bold.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "DIFF_HUNK":
                draw.text((cur_x, cur_y), text, font=font_mono_bold, fill=c_diff_hunk)
                bx = font_mono_bold.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "DIFF_DEL":
                draw.text((cur_x, cur_y), text, font=font_mono, fill=c_diff_del)
                bx = font_mono.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "DIFF_ADD":
                draw.text((cur_x, cur_y), text, font=font_mono_bold, fill=c_diff_add)
                bx = font_mono_bold.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "OUTPUT":
                draw.text((cur_x, cur_y), text, font=font_mono, fill=c_output)
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
        os.path.join(dest_dir, "index_urlchanges.png"),
        os.path.join(dest_dir, "index_urlchanges.jpeg"),
        os.path.join(artifact_dir, "index_urlchanges.png"),
        os.path.join(artifact_dir, "index_urlchanges.jpeg"),
    ]
    
    for p in paths:
        if p.endswith(".png"):
            rgb_img.save(p, "PNG", optimize=True)
        else:
            rgb_img.save(p, "JPEG", quality=95)
        print(f"Saved: {p}")

if __name__ == "__main__":
    generate_index_urlchanges_screenshot()
