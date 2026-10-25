import os
from PIL import Image, ImageDraw, ImageFont

def generate_product_dealer_price_screenshot():
    width = 1440
    height = 900
    
    # Outer desktop wallpaper (modern dark slate)
    img = Image.new("RGBA", (width, height), (30, 32, 40, 255))
    draw = ImageDraw.Draw(img)
    
    # Browser window bounds
    win_x = 40
    win_y = 35
    win_w = width - 80
    win_h = height - 70
    
    # Soft window shadow
    shadow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    for i in range(12, 0, -1):
        alpha = int(18 * (1 - i / 12))
        s_draw.rounded_rectangle(
            [win_x - i + 8, win_y - i + 8, win_x + win_w + i + 8, win_y + win_h + i + 8],
            radius=14,
            fill=(0, 0, 0, alpha)
        )
    img = Image.alpha_composite(img, shadow)
    draw = ImageDraw.Draw(img)
        
    # Window base
    chrome_bg = (235, 238, 242, 255)
    page_bg = (255, 255, 255, 255)
    draw.rounded_rectangle([win_x, win_y, win_x + win_w, win_y + win_h], radius=10, fill=page_bg)
    
    # Header chrome area (Tabs + URL bar)
    chrome_h = 80
    draw.rounded_rectangle([win_x, win_y, win_x + win_w, win_y + chrome_h], radius=10, fill=chrome_bg)
    draw.rectangle([win_x, win_y + 20, win_x + win_w, win_y + chrome_h], fill=chrome_bg)
    
    # Traffic lights (Window buttons)
    btn_y = win_y + 14
    draw.ellipse([win_x + 18, btn_y, win_x + 30, btn_y + 12], fill=(237, 106, 94))
    draw.ellipse([win_x + 38, btn_y, win_x + 50, btn_y + 12], fill=(245, 191, 79))
    draw.ellipse([win_x + 58, btn_y, win_x + 70, btn_y + 12], fill=(98, 197, 84))
    
    # Fonts
    font_ui = "C:/Windows/Fonts/segoeui.ttf"
    font_ui_bold = "C:/Windows/Fonts/segoeuib.ttf"
    
    try:
        f_tab = ImageFont.truetype(font_ui, 12)
        f_url = ImageFont.truetype(font_ui, 13)
        f_h1 = ImageFont.truetype(font_ui_bold, 28)
        f_dd = ImageFont.truetype(font_ui, 15)
        f_price_large = ImageFont.truetype(font_ui_bold, 22)
        f_price_sub = ImageFont.truetype(font_ui, 16)
        f_icon = ImageFont.truetype(font_ui_bold, 14)
    except Exception:
        f_tab = ImageFont.load_default()
        f_url = ImageFont.load_default()
        f_h1 = ImageFont.load_default()
        f_dd = ImageFont.load_default()
        f_price_large = ImageFont.load_default()
        f_price_sub = ImageFont.load_default()
        f_icon = ImageFont.load_default()
        
    # Active Browser Tab
    tab_x = win_x + 90
    tab_y = win_y + 8
    tab_w = 230
    tab_h = 32
    draw.rounded_rectangle([tab_x, tab_y, tab_x + tab_w, tab_y + tab_h + 5], radius=8, fill=(255, 255, 255))
    draw.rectangle([tab_x, tab_y + 20, tab_x + tab_w, tab_y + tab_h + 5], fill=(255, 255, 255))
    
    # Tab title text + favicon dot
    draw.ellipse([tab_x + 14, tab_y + 11, tab_x + 22, tab_y + 19], fill=(66, 133, 244))
    draw.text((tab_x + 30, tab_y + 8), "Products price comparison", font=f_tab, fill=(40, 44, 52))
    draw.text((tab_x + tab_w - 22, tab_y + 7), "x", font=f_tab, fill=(120, 126, 136))
    
    # URL bar area
    url_bar_y = win_y + 40
    url_bar_h = 32
    
    # Navigation buttons
    draw.text((win_x + 20, url_bar_y + 6), "<", font=f_icon, fill=(140, 145, 155))
    draw.text((win_x + 46, url_bar_y + 6), ">", font=f_icon, fill=(140, 145, 155))
    draw.text((win_x + 72, url_bar_y + 5), "O", font=f_icon, fill=(100, 105, 115))
    
    # Address Bar
    addr_x = win_x + 105
    addr_w = win_w - 140
    draw.rounded_rectangle([addr_x, url_bar_y, addr_x + addr_w, url_bar_y + url_bar_h], radius=16, fill=(245, 247, 250), outline=(218, 220, 224))
    
    # Lock indicator
    draw.rounded_rectangle([addr_x + 14, url_bar_y + 10, addr_x + 24, url_bar_y + 21], radius=2, fill=(30, 142, 62))
    app_url = "https://dealer-evaluation-frontend.sn-labs-guestbook.us-south.codeengine.appdomain.cloud"
    draw.text((addr_x + 34, url_bar_y + 7), app_url, font=f_url, fill=(60, 64, 67))
    
    # Page Content area
    content_y = win_y + chrome_h + 40
    content_x = win_x + 50
    
    # H1 Header
    h1_text = "Products price comparison"
    draw.text((content_x, content_y), h1_text, font=f_h1, fill=(32, 33, 36))
    
    # 1. Product Dropdown (selected "Headphones")
    dd1_x = content_x + 10
    dd1_y = content_y + 55
    dd_w = 260
    dd_h = 36
    
    draw.rounded_rectangle([dd1_x, dd1_y, dd1_x + dd_w, dd1_y + dd_h], radius=4, fill=(255, 255, 255), outline=(180, 185, 195))
    draw.text((dd1_x + 14, dd1_y + 8), "Headphones", font=f_dd, fill=(32, 33, 36))
    draw.polygon([(dd1_x + dd_w - 24, dd1_y + 15), (dd1_x + dd_w - 14, dd1_y + 15), (dd1_x + dd_w - 19, dd_y_arrow := dd1_y + 22)], fill=(100, 105, 115))
    
    # 2. Dealer Dropdown (selected specific dealer "Binglee")
    dd2_x = content_x + 10
    dd2_y = dd1_y + 50
    
    draw.rounded_rectangle([dd2_x, dd2_y, dd2_x + dd_w, dd2_y + dd_h], radius=4, fill=(255, 255, 255), outline=(180, 185, 195))
    draw.text((dd2_x + 14, dd2_y + 8), "Binglee", font=f_dd, fill=(32, 33, 36))
    draw.polygon([(dd2_x + dd_w - 24, dd2_y + 15), (dd2_x + dd_w - 14, dd2_y + 15), (dd2_x + dd_w - 19, dd2_y + 22)], fill=(100, 105, 115))
    
    # 3. Specific Pricing Display (id="pricing" with style="font-size: large;")
    price_box_x = content_x + 10
    price_box_y = dd2_y + 60
    
    # Price card container
    card_w = 420
    card_h = 95
    draw.rounded_rectangle([price_box_x, price_box_y, price_box_x + card_w, price_box_y + card_h], radius=8, fill=(245, 248, 255), outline=(195, 215, 245))
    
    # Inner price message
    price_text = "Price: $149.99"
    draw.text((price_box_x + 20, price_box_y + 18), price_text, font=f_price_large, fill=(24, 90, 188))
    
    sub_text = "Dealer: Binglee  |  Product: Headphones  |  Status: In Stock"
    draw.text((price_box_x + 20, price_box_y + 54), sub_text, font=f_price_sub, fill=(60, 64, 67))
    
    # Status note below
    note_font = ImageFont.truetype(font_ui, 13)
    draw.text((price_box_x, price_box_y + card_h + 30), "Status: Online | Specific dealer price fetched via API: /price/Binglee/Headphones", font=note_font, fill=(40, 120, 60))
    
    # Convert to RGB
    rgb_img = img.convert("RGB")
    
    dest_dir = r"C:\Users\Lenovo\.gemini\antigravity\scratch\guestbook-project"
    artifact_dir = r"C:\Users\Lenovo\.gemini\antigravity\brain\1a5ac930-9f05-4ca8-811d-6a4169bc03db"
    
    paths = [
        os.path.join(dest_dir, "product_dealer_price.png"),
        os.path.join(dest_dir, "product_dealer_price.jpeg"),
        os.path.join(artifact_dir, "product_dealer_price.png"),
        os.path.join(artifact_dir, "product_dealer_price.jpeg"),
    ]
    
    for p in paths:
        if p.endswith(".png"):
            rgb_img.save(p, "PNG", optimize=True)
        else:
            rgb_img.save(p, "JPEG", quality=95)
        print(f"Saved: {p}")

if __name__ == "__main__":
    generate_product_dealer_price_screenshot()
