import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")
p1 = 530
p2 = 300
xs =[]
ys = []
# Carregue o rastreador
tracker = cv2.TrackerCSRT_create()

# Leia o primeiro quadro do vídeo
returned, img = video.read()

# Selecione a caixa delimitadora na imagem
bbox = cv2.selectROI("Tracking", img, False)

# Inicialize o rastreador em img e na caixa delimitadora
tracker.init(img, bbox)

print(bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)

    cv2.putText(img,"Rastreando",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

def goal_track(img, bbox):
    x, y,w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    # obter pontos centrais da caixa limitadora
    c1 = x + int(w/2)
    c2 = y + int(h/2)
    #desenhar circulo da bola
    cv2.circle(img, (c1,c2), 2,(20,78,42),5)
    # desenhar circulo da cesta
    cv2.circle(img, (int(p1), int(p2)), 2,(44,96,155),5)
    # calcular distancia
    dist = math.sqrt(((c1-p1)**2)+(c2-p2)**2)
    print(dist)
    # bola na cesta se a distancia for menor que 20 px
    if(dist <= 20):
        cv2.putText(img,'Cesta',(300,90),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(201,98,23),2)
    # add c1, c2 as matrises vazias xs e ys
    xs.append(c1)
    ys.append(c2)
    # loop para percorer tragetoria em xs
    for i in range(len(xs)-1):
        cv2.circle(img,(xs[i],ys[i]),1,(22,55,44),5)
                 

    ##########################
    # ADICIONE O CÓDIGO AQUI #
    ##########################

while True:
    
    check, img = video.read()   

    # Atualize o rastreador em img e na caixa delimitadora
    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img,"Errou",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    ##########################
    # ADICIONE O CÓDIGO AQUI #
    ##########################
    # chamando goal_tracker(funçao)
    goal_track(img,bbox)
    # exibindo video
    cv2.imshow("resultado", img)
    # sair da janela de exibiçao        
    key = cv2.waitKey(25)
    if key == 32:
        print("Interrompido")
        break
# liberqa a web can
video.release()
#fevha todas as janelas 
cv2.destroyALLwindows()