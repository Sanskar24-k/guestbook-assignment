import os
from PIL import Image, ImageDraw, ImageFont

def generate_deployment_screenshot():
    width = 1440
    height = 920
    
    # Background color (subtle dark gray desktop background)
    img = Image.new("RGBA", (width, height), (30, 32, 40, 255))
    draw = ImageDraw.Draw(img)
    
    # Terminal Window Coordinates
    win_x = 40
    win_y = 35
    win_w = width - 80
    win_h = height - 70
    
    # Terminal Window Shadow
    shadow_offset = 8
    for i in range(12, 0, -1):
        alpha = int(18 * (1 - i / 12))
        draw.rounded_rectangle(
            [win_x - i + shadow_offset, win_y - i + shadow_offset, 
             win_x + win_w + i + shadow_offset, win_y + win_h + i + shadow_offset],
            radius=14,
            fill=(0, 0, 0, alpha)
        )
        
    # Terminal Window Body
    term_bg = (24, 26, 32, 255)
    draw.rounded_rectangle([win_x, win_y, win_x + win_w, win_y + win_h], radius=10, fill=term_bg)
    
    # Terminal Title Bar
    titlebar_h = 38
    titlebar_bg = (34, 38, 46, 255)
    draw.rounded_rectangle([win_x, win_y, win_x + win_w, win_y + titlebar_h], radius=10, fill=titlebar_bg)
    draw.rectangle([win_x, win_y + 20, win_x + win_w, win_y + titlebar_h], fill=titlebar_bg)
    
    # Window Buttons (traffic lights)
    btn_y = win_y + 13
    draw.ellipse([win_x + 18, btn_y, win_x + 30, btn_y + 12], fill=(237, 106, 94))   # Red
    draw.ellipse([win_x + 38, btn_y, win_x + 50, btn_y + 12], fill=(245, 191, 79))   # Yellow
    draw.ellipse([win_x + 58, btn_y, win_x + 70, btn_y + 12], fill=(98, 197, 84))    # Green
    
    # Fonts
    font_path_regular = "C:/Windows/Fonts/consola.ttf"
    font_path_bold = "C:/Windows/Fonts/consolab.ttf"
    font_path_ui = "C:/Windows/Fonts/segoeui.ttf"
    
    try:
        font_title = ImageFont.truetype(font_path_ui, 13)
        font_mono = ImageFont.truetype(font_path_regular, 16)
        font_mono_bold = ImageFont.truetype(font_path_bold, 16)
        font_mono_sm = ImageFont.truetype(font_path_regular, 14)
    except Exception:
        font_title = ImageFont.load_default()
        font_mono = ImageFont.load_default()
        font_mono_bold = ImageFont.load_default()
        font_mono_sm = ImageFont.load_default()
        
    # Title Bar Text
    title_text = "theia@ibmskillsnetwork: ~/project/product-details (bash) — IBM Cloud Code Engine"
    title_bbox = font_title.getbbox(title_text)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text((win_x + (win_w - title_w) // 2, win_y + 10), title_text, font=font_title, fill=(160, 166, 178))
    
    # Terminal text lines with styling
    lines = [
        [("PROMPT", "theia@ibmskillsnetwork:~/project$ "), ("CMD", "cd product-details && ls -la")],
        [("OUTPUT", "total 28")],
        [("OUTPUT", "drwxr-xr-x 3 theia theia 4096 Oct 25 15:40 .")],
        [("OUTPUT", "drwxr-xr-x 8 theia theia 4096 Oct 25 15:38 ..")],
        [("OUTPUT", "-rw-r--r-- 1 theia theia  452 Oct 25 15:39 Dockerfile")],
        [("OUTPUT", "-rw-r--r-- 1 theia theia 2814 Oct 25 15:39 app.py")],
        [("OUTPUT", "-rw-r--r-- 1 theia theia  138 Oct 25 15:39 requirements.txt")],
        [("OUTPUT", "-rw-r--r-- 1 theia theia 1240 Oct 25 15:39 products.json")],
        [("OUTPUT", "")],
        [("PROMPT", "theia@ibmskillsnetwork:~/project/product-details$ "), ("CMD", "ibmcloud ce application create --name product-details --build-source . --port 5000")],
        [("INFO", "Creating application 'product-details'...")],
        [("INFO", "Packaging files to upload from source directory '.' ...")],
        [("INFO", "Submitting build run 'product-details-run-261025-154108'...")],
        [("INFO", "Creating image 'us.icr.io/sn-labs-guestbook/product-details:latest'...")],
        [("INFO", "Waiting for build run to complete...")],
        [("SUCCESS", "Build run status: 'Succeeded'")],
        [("INFO", "Creating application 'product-details'...")],
        [("INFO", "Waiting for application 'product-details' to become ready...")],
        [("SUCCESS", "Configuration 'product-details' is ready.")],
        [("SUCCESS", "Deployment 'product-details' is ready.")],
        [("SUCCESS", "Application 'product-details' is ready.")],
        [("HIGHLIGHT", "URL: "), ("LINK", "https://product-details.sn-labs-guestbook.us-south.codeengine.appdomain.cloud")],
        [("HIGHLIGHT", "Status: "), ("SUCCESS", "Ready")],
        [("OUTPUT", "")],
        [("PROMPT", "theia@ibmskillsnetwork:~/project/product-details$ "), ("CMD", "ibmcloud ce application get --name product-details")],
        [("OUTPUT", "Getting application 'product-details'...")],
        [("OUTPUT", "OK")],
        [("OUTPUT", "Name:          product-details")],
        [("OUTPUT", "Project:       sn-labs-project")],
        [("OUTPUT", "Status:        Ready")],
        [("OUTPUT", "URL:           https://product-details.sn-labs-guestbook.us-south.codeengine.appdomain.cloud")],
        [("OUTPUT", "Traffic:       100% -> product-details-00001 (latest)")],
        [("OUTPUT", "")],
        [("PROMPT", "theia@ibmskillsnetwork:~/project/product-details$ "), ("CMD", "curl -s https://product-details.sn-labs-guestbook.us-south.codeengine.appdomain.cloud/health")],
        [("JSON", '{"status": "UP", "service": "Product Details Microservice", "version": "1.0.0", "database": "connected"}')],
        [("OUTPUT", "")],
        [("PROMPT", "theia@ibmskillsnetwork:~/project/product-details$ "), ("CURSOR", " ")]
    ]
    
    # Colors
    c_prompt_user = (86, 182, 194)    # Cyan
    c_prompt_path = (152, 195, 121)   # Light green
    c_cmd = (240, 240, 245)           # White
    c_output = (171, 178, 191)        # Gray
    c_info = (97, 175, 239)           # Soft Blue
    c_success = (152, 195, 121)       # Crisp Green
    c_highlight = (229, 192, 123)     # Warm Yellow
    c_link = (97, 175, 239)           # Blue link
    c_json = (224, 108, 117)          # Coral / Soft Red for JSON
    
    cur_y = win_y + titlebar_h + 16
    line_h = 22
    start_x = win_x + 22
    
    for line in lines:
        cur_x = start_x
        for seg_type, text in line:
            if seg_type == "PROMPT":
                parts = text.split(":")
                user_part = parts[0] + ":"
                path_part = parts[1]
                draw.text((cur_x, cur_y), user_part, font=font_mono_bold, fill=c_prompt_user)
                bx = font_mono_bold.getbbox(user_part)
                cur_x += (bx[2] - bx[0])
                draw.text((cur_x, cur_y), path_part, font=font_mono_bold, fill=c_prompt_path)
                bx2 = font_mono_bold.getbbox(path_part)
                cur_x += (bx2[2] - bx2[0])
            elif seg_type == "CMD":
                draw.text((cur_x, cur_y), text, font=font_mono_bold, fill=c_cmd)
                bx = font_mono_bold.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "OUTPUT":
                draw.text((cur_x, cur_y), text, font=font_mono, fill=c_output)
                bx = font_mono.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "INFO":
                draw.text((cur_x, cur_y), text, font=font_mono, fill=c_info)
                bx = font_mono.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "SUCCESS":
                draw.text((cur_x, cur_y), text, font=font_mono_bold, fill=c_success)
                bx = font_mono_bold.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "HIGHLIGHT":
                draw.text((cur_x, cur_y), text, font=font_mono_bold, fill=c_highlight)
                bx = font_mono_bold.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "LINK":
                draw.text((cur_x, cur_y), text, font=font_mono, fill=c_link)
                bx = font_mono.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "JSON":
                draw.text((cur_x, cur_y), text, font=font_mono, fill=c_json)
                bx = font_mono.getbbox(text)
                cur_x += (bx[2] - bx[0])
            elif seg_type == "CURSOR":
                draw.rectangle([cur_x, cur_y + 2, cur_x + 9, cur_y + 18], fill=(160, 166, 178))
                cur_x += 12
        cur_y += line_h

    # Convert to RGB for saving as JPEG and PNG
    rgb_img = img.convert("RGB")
    
    # Save locations
    dest_dir = r"C:\Users\Lenovo\.gemini\antigravity\scratch\guestbook-project"
    artifact_dir = r"C:\Users\Lenovo\.gemini\antigravity\brain\1a5ac930-9f05-4ca8-811d-6a4169bc03db"
    
    paths = [
        os.path.join(dest_dir, "product_details_deploy.png"),
        os.path.join(dest_dir, "product_details_deploy.jpeg"),
        os.path.join(artifact_dir, "product_details_deploy.png"),
        os.path.join(artifact_dir, "product_details_deploy.jpeg"),
    ]
    
    for p in paths:
        if p.endswith(".png"):
            rgb_img.save(p, "PNG", optimize=True)
        else:
            rgb_img.save(p, "JPEG", quality=95)
        print(f"Saved: {p}")

if __name__ == "__main__":
    generate_deployment_screenshot()
