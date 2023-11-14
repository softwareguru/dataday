def main():
    import csv, sys, os, qrcode
    from slugify import slugify

    print("Starting ...")
    if len(sys.argv) > 1:
        source_file = sys.argv[1]
    else:
        source_file = "badges.csv"


    try:
        os.mkdir("qr")
    except FileExistsError:
        pass
    except OSError:
        print ("Creation of the directory qr failed" )
    else:
        print ("Created directory ...")

    with open(source_file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            id = row['Number']
            firstname = row['First Name']
            lastname = row['Last Name']
            company = row['Company']
            title = row['Title']
            email = row['Email']
            color_r = int(row['color_r'])
            color_g = int(row['color_g'])
            color_b = int(row['color_b'])

            data = f'''BEGIN:VCARD
VERSION:3.0
N:{lastname};{firstname}
FN:{firstname} {lastname}
ORG:{company}
TITLE:{title}
EMAIL:{email}
END:VCARD'''


            qr = qrcode.QRCode(version=5)
            qr.add_data(data)
            qr.make()
            img = qr.make_image(fill_color=(color_r,color_g,color_b))
            img.save(f"qr/{id}.png")

    print("Done")

if __name__ == "__main__":
        main()

