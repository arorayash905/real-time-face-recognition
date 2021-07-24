import test
from pyautogui import screenshot
import numpy as np
import cv2
i = 1
while True:
	img = screenshot()
	img = np.array(img)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	# size = (1280, 720)
	updatedImage = test.fun(img)
	if updatedImage is not False:
		fName = "screenshots/screenshot"+str(i)+".jpg"
		cv2.imwrite(fName, updatedImage)
		print("SS "+str(i)+" saved.")
		i = i+1
		if i > 50:
			break
	else:
		print("No face Detected.")
cv2.destroyAllWindows()
