from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

data = pd.read_excel('participants.xlsx')

template_path = 'template.png'  # Change templateName here
font_path = 'MonsieurLaDoulaise-Regular.ttf'  # Change font here
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

    x_pos = (certificate_width - text_width) / 2
    y_pos = 720  # you can adjust height here

    draw.text((x_pos, y_pos), text, fill="black", font=font_name)

    first_name = row['Name'].split()[0]
    output_path = os.path.join(output_folder, f"{first_name}_certificate.png")  # Change exported fileName here
    certificate.save(output_path)

print('Certificates Generated')
