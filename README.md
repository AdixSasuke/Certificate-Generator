# Certificate Generator

Generate certificates automatically using a template and an Excel list of names.

## Required Libraries

```python
from PIL import Image, ImageDraw, ImageFont  # For image processing
import pandas as pd                          # For reading Excel file
import os                                    # For file/folder operations
```

## Required Files

1. `template.png` - Certificate template image
2. `participants.xlsx` - Excel file containing:
   - Column named "Name" with participant names
3. `MonsieurLaDoulaise-Regular.ttf` - Font file for names

## Setup

1. Install required packages:
```bash
pip install Pillow pandas
```

2. Place all files in your project folder:
```
your_folder/
    ├── certificate_generator.py
    ├── template.png
    ├── participants.xlsx
    └── MonsieurLaDoulaise-Regular.ttf
```

## How to Use

1. Run the script:
```bash
python certificate_generator.py
```

2. Certificates will be generated in a new `certificates` folder
3. Each certificate will be saved as `firstname_certificate.png`

## Customization

- Change text position: modify `y_pos = 720`
- Change font size: modify `font_size = 60`
- Change output filename: modify filename in `output_path`

## Troubleshooting

- Make sure Excel file has a "Name" column
- Ensure all files are in the same folder
- Check if font file name matches exactly
