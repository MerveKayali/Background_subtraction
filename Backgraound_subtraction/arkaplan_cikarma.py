import cv2
import numpy as np

cap=cv2.VideoCapture("car.mp4")
_,first_frame=cap.read()
first_frame=cv2.resize(first_frame,(640,480))
first_gray=cv2.cvtColor(first_frame,cv2.COLOR_BGRA2GRAY)
first_gray=cv2.GaussianBlur(first_gray,(5,5),0)

while 1:
    _,frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # OpenCV de arka plan temizleme işlemini absdiff metodu yapmaktadır.
    # Absdiff metodu verilen iki matris arasında çıkarma işlemi yapar
    # bu çıkarma işlemi sonucunda değişen kısımlar yani hareketli
    # kısımlar gösterilir.
    # Çıkarma işlemi sonucu mutlak değer olarak döndürülür
    diff=cv2.absdiff(first_gray,gray)#ilk frame ile diğer frameleri tek tek karşılaştıracak

    _,diff=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)

    #döngü boyunca ilk kare ile o anki kare yerine;
    # bir önceki kare ile şimdiki kareyi compare ederek güzel
    # iterative özel fonksiyona yakın sonuçlar elde edebilirdiniz.
    first_gray = gray
    
    cv2.imshow("frame",frame)
    cv2.imshow("first",first_frame)
    cv2.imshow("diff",diff)


    if cv2.waitKey(20) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()