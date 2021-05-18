import os
import shutil
import numpy as np
import face_recognition
base_dir = os.path.dirname(__file__)

for filename in os.listdir(base_dir+"\\query\\"):
    known_image = face_recognition.load_image_file(os.path.join(base_dir+"\\query\\", filename))

try:
    input_img_encoding = face_recognition.face_encodings(known_image)[0]
except IndexError as e:
    print(e)
if not os.path.exists('extracted_photos'):
	print("New directory created")
	os.makedirs('extracted_photos')

target=base_dir + '\\extracted_photos'
for filename in os.listdir(target):
        file_path = os.path.join(target, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

output_img_encoding=np.zeros((128,), dtype=float)
for file in os.listdir(base_dir + '\\faces'):
    
    unknown_image = face_recognition.load_image_file(base_dir+"\\faces\\"+file)
    try:
        output_img_encoding = face_recognition.face_encodings(unknown_image)[0]
    except IndexError as e:
        print(e)

	
    results = face_recognition.compare_faces([input_img_encoding], output_img_encoding)
    # print(results,output_img_encoding)
	
    if results[0]==True:
        temp_name=file.partition("_")[2]
        if not os.path.exists('extracted_photos'):
	        print("New directory created")
	        os.makedirs('extracted_photos')
        shutil.copy(base_dir +"\\group_of_images\\"+temp_name, base_dir+"\\extracted_photos")
        
target=base_dir + '\\faces'
for filename in os.listdir(target):
		file_path = os.path.join(target, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))
target=base_dir + '\\updated_images'

for filename in os.listdir(target):
		file_path = os.path.join(target, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))

target=base_dir + '\\group_of_images'
for filename in os.listdir(target):
		file_path = os.path.join(target, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))
target=base_dir + '\\query'
for filename in os.listdir(target):
		file_path = os.path.join(target, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))