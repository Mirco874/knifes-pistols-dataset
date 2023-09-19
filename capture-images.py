import cv2 
cap = cv2.VideoCapture(0)

total_images = 40;
num = 1
interval = 2000

folder = "./train"
object ="cuchillo"

while (cap.isOpened()):
    ret_flag, Vshow = cap.read();
    cv2.imshow("Capture_test", Vshow)

    k= cv2.waitKey(2000) & 0xFF
    cv2.imwrite( folder + "/" + object + str(num) + ".jpg", Vshow);
    print("image: "+ str(num) )
    num+=1;


    if(k==ord("q") or num == total_images):
        break;

cap.release();
cv2.destroyAllWindows();


