import numpy as np
from PIL import Image
import csv

def main():
    with open("in.csv", "r") as view, open("analysis.csv", "w") as analysis: # we can open two file at a time
        
        reader = csv.DictReader(view)
        #writer = csv.DictWriter(analysis, fieldnames=['id','english_title'])  # we can add header like this as well
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"]) # or else we can get the header from other file and add it
        writer.writeheader()

        for row in reader:
            print(row["id"])
            brightness = calculate_brightness(f"{row['id']}.jpg")
            print(brightness)

            writer.writerow(
                {
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": brightness
                }
            )

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    
    return brightness

main()


# for line 13 to 25 we can do this
# for row in reader:
# row["brightness"] = calculate_brightness(f"{row['id']}.jpg")
# writer.writerow(row)


# to read entire file use .read  example view.read()
# for individual line, contents = view.readlines()
# so we can extract chapter1 = contents[52:272]

# for writing we can use same view.write or view.writelines(chapter1)