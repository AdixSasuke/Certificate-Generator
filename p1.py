from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

data = pd.read_excel('participants.xlsx')

template_path = 'certificate_template.png'
font_path = 'MonsieurLaDoulaise-Regular.ttf'
output_folder = 'certificates'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

template = Image.open(template_path)
certificate_width, certificate_height = template.size

for index, row in data.iterrows():
    certificate = Image.open(template_path)
    draw = ImageDraw.Draw(certificate)

    font_name = ImageFont.truetype(font_path, 60)

    text = row['Name']
    text_bbox = draw.textbbox((0, 0), text, font=font_name)
    text_width = text_bbox[2] - text_bbox[0]

    x_name = (certificate_width - text_width) / 2
    y_name = 720

    draw.text((x_name, y_name), text, fill="black", font=font_name)

    output_path = os.path.join(output_folder, f"{row['Name']}_certificate.png")
    certificate.save(output_path)

print('Certificates Generated')