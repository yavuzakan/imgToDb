
# import OS module
import os
import sqlite3

from exif import Image

def kayit(r1,r2,r3,r4,r5,r6):

    try:
      
        conn = sqlite3.connect('database.db')

        c = conn.cursor()

        veriler = (r1,r2,r3,r4,r5,r6)
     

        c.execute("INSERT INTO database(r1,r2,r3,r4,r5,r6) VALUES(?,?,?,?,?,?)" , veriler)

        print("ok")
        conn.commit()
        conn.close()
    except Exception as e:
            print(e)



def ozellik( img_filename):

        #  folder_path = 'c:/deneme'
        #  img_filename = '3.jpg'
            try:
                
                #print(img_filename)
                
                
                img_path = f'{img_filename}'
                
                with open(img_path, 'rb') as img_file:
                    img = Image(img_file)
                    
               # print(img.has_exif)

                sorted(img.list_all())
                """
                # Make of device which captured image
                print(f'Make: {img.get("make")}')

                # Model of device which captured image
                print(f'Model: {img.get("model")}')

                # Software involved in uploading and digitizing image
                print(f'Software: {img.get("software")}')

                # Name of photographer who took the image
                print(f'Artist: {img.get("artist")}')

                # Original datetime that image was taken (photographed)
                print(f'DateTime (Original): {img.get("datetime_original")}')


                print(f'x: {img.get("pixel_x_dimension")}')

                print(f'y: {img.get("pixel_y_dimension")}')
               """
                make = img.get("make")
                model = img.get("model")
                datetime_original = img.get("datetime_original")
                pixel_x_dimension = img.get("pixel_x_dimension")
                pixel_y_dimension = img.get("pixel_y_dimension")

                kayit(img_filename, make ,model, datetime_original,pixel_x_dimension,pixel_y_dimension)    

            except:
             kayit(img_filename, "*" ,"*", "*","*","*") 
                  









            print("\n")

            








 
# This is my path
path = os.getcwd()

#path = f.readline()

f = open("1.txt", "r")

path = f.readline()
path = path.replace("\n", "")
print(path)

f.close()



 
 
# Scan the directory and get
# an iterator of os.DirEntry objects
# corresponding to entries in it
# using os.scandir() method
obj = os.scandir(path)
 
# List all files and directories in the specified path

for entry in obj:
    if entry.is_file():
        
        if entry.name.lower().endswith('.jpg') or entry.name.lower().endswith('.jpeg') or entry.name.lower().endswith('.png'):
            print(path+"\\"+entry.name)
            new = path+"\\"+entry.name
            ozellik(new )
    




obj = os.scandir(path)

for entry in obj:
    if entry.is_dir() :
      
        
        obj2 = os.scandir(path +"\\"+ entry.name)
        for entry2 in obj2:
            if entry.name.lower().endswith('.jpg') or entry.name.lower().endswith('.jpeg') or entry.name.lower().endswith('.png'):
              
                    newpath = path +"\\"+ entry.name
                    print(newpath +"\\"+entry2.name)
                    new = newpath+"\\"+entry2.name
                    ozellik(new)
                
      
               




