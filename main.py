import cv2
from face_recognition import load_image_file, face_locations, face_encodings, face_distance, compare_faces


print("Imported")
print("Data Processing Initiated...")
imgYash = load_image_file("D:\FreeLancer\yash.png")
imgYash = cv2.cvtColor(imgYash, cv2.COLOR_BGR2RGB)
# faceLocY = face_locations(imgYash)[0]
encodeYash = face_encodings(imgYash)[0]

imgAbhishek = load_image_file("D:\FreeLancer\Abhishek.jpg")
imgAbhishek = cv2.cvtColor(imgAbhishek, cv2.COLOR_BGR2RGB)
# faceLocA = face_locations(imgAbhishek)[0]
encodeAbhishek = face_encodings(imgAbhishek)[0]

imgSiddhant = load_image_file("D:\FreeLancer\siddhant.jpg")
imgSiddhant = cv2.cvtColor(imgSiddhant, cv2.COLOR_BGR2RGB)
# faceLocS = face_locations(imgSiddhant)[0]
encodeSiddhant = face_encodings(imgSiddhant)[0]

imgSahil = load_image_file("D:\FreeLancer\sahil.jpg")
imgSahil = cv2.cvtColor(imgSahil, cv2.COLOR_BGR2RGB)
# faceLocSa = face_locations(imgSahil)[0]
encodeSahil = face_encodings(imgSahil)[0]

print("Data is Processed.")


def fun(image):
    faceLoc = face_locations(image)
    encodeTest = face_encodings(image)
    if len(encodeTest) > 0:
        for i in range(len(encodeTest)):
            if face_distance([encodeYash], encodeTest[i]) <= 0.55:
                cv2.rectangle(image, (faceLoc[i][3], faceLoc[i][0]), (faceLoc[i][1], faceLoc[i][2]), (255, 0, 255), 2)
                cv2.putText(image, "Yash Arora", (faceLoc[i][3], faceLoc[i][0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            elif face_distance([encodeAbhishek], encodeTest[i]) <= 0.55:
                cv2.rectangle(image, (faceLoc[i][3], faceLoc[i][0]), (faceLoc[i][1], faceLoc[i][2]), (255, 0, 255), 2)
                cv2.putText(image, "Abhishek", (faceLoc[i][3], faceLoc[i][0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            elif face_distance([encodeSiddhant], encodeTest[i]) <= 0.55:
                cv2.rectangle(image, (faceLoc[i][3], faceLoc[i][0]), (faceLoc[i][1], faceLoc[i][2]), (255, 0, 255), 2)
                cv2.putText(image, "Siddhant", (faceLoc[i][3], faceLoc[i][0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            elif face_distance([encodeSahil], encodeTest[i]) <= 0.55:
                cv2.rectangle(image, (faceLoc[i][3], faceLoc[i][0]), (faceLoc[i][1], faceLoc[i][2]), (255, 0, 255), 2)
                cv2.putText(image, "Sahil", (faceLoc[i][3], faceLoc[i][0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        # print("Initiated.")
        return image

    else:
        return False
