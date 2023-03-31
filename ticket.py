from PIL import Image, ImageDraw, ImageFont
import qrcode
import csv

f=open("sample.csv" ,'r')
reader =csv.reader(f ,delimiter=',')
for i in reader:

    # Generate QR code for a string
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(i[1])
    qr.make(fit=True)

    # Save QR code image as PNG
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(i[1]+".png")
    # Open a ticket template image
    ticket_img = Image.open("temp.png")

    # Create a draw object and set font
    draw = ImageDraw.Draw(ticket_img)
    font = ImageFont.truetype("arial.ttf", size=50)

    # Add event name and details
    event_name = "Pro Show"
    event_details = "Date: April 1st, 2023 | Location: Example Venue"
    draw.text((50, 100), event_name, font=font, fill=(255, 255, 255))
    draw.text((50, 150), event_details, font=font, fill=(255, 255, 255))

    # Add QR code
    qr_img = Image.open(i[1]+".png")
    ticket_img.paste(qr_img, (2000, 300))

    # Save ticket image as PNG
    ticket_img.save(i[0]+".png")
