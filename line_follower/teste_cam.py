from cv_bridge import CvBridge
import cv2
import rospy
from sensor_msgs.msg import Image
import numpy as np

def passa_video(img):
	bridge=CvBridge()

	cv_image = bridge.imgmsg_to_cv2(img, "bgr8")
    
	# (rows,cols,channels) = cv_image.shape
	# if cols > 60 and rows > 60 :
	#       cv2.circle(cv_image, (50,50), 10, 255)
	# cv2.imshow("Image window", cv_image)
	#cv2.waitKey(250)

	nome_bonito(cv_image)
	
def nome_bonito(orig_frame):
	N = 300
	dimensions = orig_frame.shape
	Largura = dimensions[1]
	Comprimento = dimensions[0]

# Inicio Dimensoes do videos
	#fps = video.get(cv2.CAP_PROP_FPS)
	# Largura,Comprimento = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
	# 	int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
	Metade_Comprimento=int(Comprimento/2)
	Metade_Largura=int(Largura/2)
	Comprimento_baixo=Comprimento-5
	Comprimento_alto = int(Comprimento - Metade_Comprimento/2)
	#Largura_esquerda = Metade_Largura - 120
	lista = list(range(1,Comprimento+1))
	Largura_esquerda = Metade_Largura - 120
	Largura_direita = Metade_Largura + 120
	#Comprimento_01=Comprimento-50
	#Comprimento_02=Comprimento-15
	#Comprimento_03=Comprimento-20
	Comprimento_baixo_trans = N - 5
	Comprimento_alto_trans = int(N/2) 
	#Largura_esquerda_trans = int(N/2) - int(N/4)
	Largura_esquerda_trans = int(N*1/4)
	Largura_direita_trans = int(N*3/4)

	centro_da_coluna_esquerda_frame = 0
	centro_da_coluna_esquerda_trans = 0
	centro_da_coluna_direita_trans = 0
	centro_da_coluna_direita_frame = 0

	centro_da_linha_baixo_frame = 0
	centro_da_linha_baixo_trans = 0
	centro_da_linha_alto_trans = 0
	centro_da_linha_alto_frame = 0

	#print ("Frames per second : ",fps)
	print ("Largura : ",Largura)
	print ("Comprimento : ",Comprimento)
	print ("Largura_esquerda : ", Largura_esquerda)

	# Inicio Kernel abertura/fechamento
	#kernel = np.ones((20,20),np.uint8)

	#Rectangular Kernel
	#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(20,20))

	# Elliptical Kernel
	#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,20))

	# Cross-shaped Kernel
	kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))
	#print(kernel)
	#while True:

	#	ret, orig_frame = video.read()
	#print(ret)
	#	if not ret:        
		#video = cv2.VideoCapture("road_car_view.mp4")
	#        video = cv2.VideoCapture(args["video"])
	#		video = cv2.VideoCapture("back1_25.avi")        	
	#		continue
	

	frame = cv2.GaussianBlur(orig_frame, (15, 15), 0)

	pts1 = np.float32([[171,239+50],[428,234+50],[64,427+50],[527,415+50]]) # pontos da imagem original
	pts2 = np.float32([[0,0],[N,0],[0,N],[N,N]]) # pontos da imagem corrigida

	M = cv2.getPerspectiveTransform(pts1,pts2) # Cria a matriz de transformacao
#print(M)
	transform = cv2.warpPerspective(frame,M,(N,N)) # Executa a trnasformacao


	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	hsv_transform = cv2.cvtColor(transform, cv2.COLOR_BGR2HSV)
	low_blue = np.array([85, 50, 0])
	up_blue = np.array([125, 255, 180])
	mask_frame = cv2.inRange(hsv_frame, low_blue, up_blue)
	mask_trans = cv2.inRange(hsv_transform, low_blue, up_blue)

 
        #  Inicio Fechamento
	fechamento_frame = cv2.morphologyEx(mask_frame, cv2.MORPH_CLOSE, kernel)
	fechamento_trans = cv2.morphologyEx(mask_trans, cv2.MORPH_CLOSE, kernel)
	#  Fim Fechamento

	# Inicio Bordas Frame
#	edges = cv2.Canny(fechamento_frame, 70, 255)
#	contours,hierarchy = cv2.findContours(fechamento_frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	#im2,contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#	cv2.drawContours(frame, contours, -1, (0,255,0), 3)
	# Fim Bordas Frame

	# Inicio Bordas Transform
#	edges = cv2.Canny(fechamento_trans, 70, 255)
#	contours,hierarchy = cv2.findContours(fechamento_trans,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	#im2,contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#	cv2.drawContours(transform, contours, -1, (0,255,0), 3)
	# Fim Bordas Transform
	
	# Inicio Linhas de Derivacao Frame
	Linha_threshold_baixo = fechamento_frame[Comprimento_baixo].astype(np.int16) # Linha selecionada baixo
	diff_inicial_baixo_frame = np.diff(Linha_threshold_baixo)                                     # Derivada da linha selecionada
	pontos_maxmin_baixo_frame = np.where(np.logical_or(diff_inicial_baixo_frame > 200, diff_inicial_baixo_frame < -200)) # maximos e minimos da derivada
	cv2.line(frame,(0,Comprimento_baixo),(Largura,Comprimento_baixo),(0,255,0),1) # Desenhar linha escaneada

	Linha_threshold_alto = fechamento_frame[Comprimento_alto].astype(np.int16) # Linha selecionada alto
	diff_inicial_alto_frame = np.diff(Linha_threshold_alto)                                     # Derivada da linha selecionada
	pontos_maxmin_alto_frame = np.where(np.logical_or(diff_inicial_alto_frame > 200, diff_inicial_alto_frame < -200)) # maximos e minimos da derivada
	cv2.line(frame,(0,Comprimento_alto),(Largura,Comprimento_alto),(0,255,0),1) # Desenhar linha escaneada

	Coluna_threshold_esquerda = fechamento_frame[0:Comprimento,Largura_esquerda].astype(np.int16) # Coluna esquerda selecionada
	diff_inicial_esquerda_frame = np.diff(Coluna_threshold_esquerda)                              # Derivada da coluna selecionada
	pontos_maxmin_esquerda_frame = np.where(np.logical_or(diff_inicial_esquerda_frame > 200, diff_inicial_esquerda_frame < -200)) # maximos e minimos da derivada
	cv2.line(frame,(Largura_esquerda,0),(Largura_esquerda,Comprimento),(0,255,0),1)              # Desenhar coluna esquerda

	Coluna_threshold_direita = fechamento_frame[0:Comprimento, Largura_direita].astype(np.int16) # Coluna direita selecionada
	diff_inicial_direita_frame = np.diff(Coluna_threshold_direita)                               # Derivada da coluna selecionada
	pontos_maxmin_direita_frame = np.where(np.logical_or(diff_inicial_direita_frame > 200, diff_inicial_direita_frame < -200))     # maximos e minimos da derivada
	cv2.line(frame,(Largura_direita,0),(Largura_direita,Comprimento),(0,255,0),1)                # Desenhar coluna direita
	# Fim Linhas de Derivacao Frame

	# Inicio Linhas de Derivacao Transform
	Linha_threshold_baixo_trans = fechamento_trans[Comprimento_baixo_trans].astype(np.int16) # Linha selecionada baixo
	diff_inicial_trans = np.diff(Linha_threshold_baixo_trans)                                # Derivada da linha selecionada
	pontos_maxmin_baixo_trans = np.where(np.logical_or(diff_inicial_trans > 200, diff_inicial_trans < -200)) # maximos e minimos da derivada
	cv2.line(transform,(0,Comprimento_baixo_trans),(N,Comprimento_baixo_trans),(0,255,0),1)  # Desenhar linha escaneada

	Linha_threshold_alto_trans = fechamento_trans[Comprimento_alto_trans].astype(np.int16) # Linha selecionada alto
	diff_inicial_alto_trans = np.diff(Linha_threshold_alto_trans)                          # Derivada da linha selecionada
	pontos_maxmin_alto_trans = np.where(np.logical_or(diff_inicial_alto_trans > 200, diff_inicial_alto_trans < -200)) # maximos e minimos da derivada
	cv2.line(transform,(0,Comprimento_alto_trans),(N,Comprimento_alto_trans),(0,255,0),1) # Desenhar linha escaneada

	Coluna_threshold_esquerda_trans = fechamento_trans[0:N, Largura_esquerda_trans].astype(np.int16) # Linha selecionada alto
	diff_inicial_trans = np.diff(Coluna_threshold_esquerda_trans)                                     # Derivada da linha selecionada
	pontos_maxmin_esquerda_trans = np.where(np.logical_or(diff_inicial_trans > 200, diff_inicial_trans < -200)) # maximos e minimos da derivada
	cv2.line(transform,(Largura_esquerda_trans,0),(Largura_esquerda_trans,N),(0,255,0),1) # Desenhar linha escaneada

	Coluna_threshold_direita_trans = fechamento_trans[0:N, Largura_direita_trans].astype(np.int16) # Linha selecionada alto
	diff_inicial_trans = np.diff(Coluna_threshold_direita_trans)                                     # Derivada da linha selecionada
	pontos_maxmin_direita_trans = np.where(np.logical_or(diff_inicial_trans > 200, diff_inicial_trans < -200)) # maximos e minimos da derivada
	cv2.line(transform,(Largura_direita_trans,0),(Largura_direita_trans,N),(0,255,0),1) # Desenhar linha escaneada
	# Fim Linhas de Derivacao Transform

	# Inicio Derivadas Frame
	if len(pontos_maxmin_baixo_frame) > 0 and len(pontos_maxmin_baixo_frame[0]) > 1: # Se encontrou algo continua
	        centro_da_linha_baixo_frame = int((pontos_maxmin_baixo_frame[0][0]+pontos_maxmin_baixo_frame[0][1])/2)
	        cv2.circle(frame,(pontos_maxmin_baixo_frame[0][0], Comprimento_baixo), 2, (255,0,0), -1)
	        cv2.circle(frame,(pontos_maxmin_baixo_frame[0][1], Comprimento_baixo), 2, (255,0,0), -1)
	        cv2.circle(frame,(centro_da_linha_baixo_frame, Comprimento_baixo), 2, (0,0,255), -1)
	        temp_pontos_baixo_frame=pontos_maxmin_baixo_frame
	        temp_centro_linha_baixo_frame=centro_da_linha_baixo_frame
	        '''
	        centro_da_linha_01 = int((pontos_maxmin_01[0][0]+pontos_maxmin_01[0][1])/2)
	        cv2.circle(frame,(pontos_maxmin_01[0][0], Comprimento_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(pontos_maxmin_01[0][1], Comprimento_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(centro_da_linha_01, Comprimento_01), 2, (0,0,255), -1)
	        '''

	else:
	        #centro_da_linha_inicial=temp_centro_linha_inicial
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][0], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][1], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(centro_da_linha_inicial, Comprimento_Inicial), 2, (0,0,255), -1)
	        #centro_da_linha_inicial = Metade_Largura
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #Comprimento_Inicial -= 5
	        Comprimento_baixo = Comprimento_baixo % Comprimento
	        #num_de_pontos_perdidos += 1
	
	cXbf= (Comprimento_baixo, centro_da_linha_baixo_frame)
	#print("Centroide baixo: ", cXbf)

	if len(pontos_maxmin_alto_frame) > 0 and len(pontos_maxmin_alto_frame[0]) > 1: # Se encontrou algo continua
	        centro_da_linha_alto_frame = int((pontos_maxmin_alto_frame[0][0]+pontos_maxmin_alto_frame[0][1])/2)
	        cv2.circle(frame,(pontos_maxmin_alto_frame[0][0], Comprimento_alto), 2, (255,0,0), -1)
	        cv2.circle(frame,(pontos_maxmin_alto_frame[0][1], Comprimento_alto), 2, (255,0,0), -1)
	        cv2.circle(frame,(centro_da_linha_alto_frame, Comprimento_alto), 2, (0,0,255), -1)
	        temp_pontos_alto_frame=pontos_maxmin_alto_frame
	        temp_centro_linha_alto_frame=centro_da_linha_alto_frame
	        '''
	        centro_da_linha_01 = int((pontos_maxmin_01[0][0]+pontos_maxmin_01[0][1])/2)
	        cv2.circle(frame,(pontos_maxmin_01[0][0], Comprimento_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(pontos_maxmin_01[0][1], Comprimento_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(centro_da_linha_01, Comprimento_01), 2, (0,0,255), -1)
	        '''

	else:
	        #centro_da_linha_inicial=temp_centro_linha_inicial
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][0], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][1], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(centro_da_linha_inicial, Comprimento_Inicial), 2, (0,0,255), -1)
	        #centro_da_linha_inicial = Metade_Largura
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #Comprimento_Inicial -= 5
	        Comprimento_alto = Comprimento_alto % Comprimento
	        #num_de_pontos_perdidos += 1
	
	cXaf= (Comprimento_alto, centro_da_linha_alto_frame)
	#print("Centroide alto: ", cXaf)	

	if len(pontos_maxmin_esquerda_frame) > 0 and len(pontos_maxmin_esquerda_frame[0]) > 1: # Se encontrou algo continua
	        centro_da_coluna_esquerda_frame = int((pontos_maxmin_esquerda_frame[0][0]+pontos_maxmin_esquerda_frame[0][1])/2)
	        cv2.circle(frame,(Largura_esquerda, pontos_maxmin_esquerda_frame[0][0]), 2, (255,0,0), -1)
	        cv2.circle(frame,(Largura_esquerda, pontos_maxmin_esquerda_frame[0][1]), 2, (255,0,0), -1)
	        cv2.circle(frame,(Largura_esquerda, centro_da_coluna_esquerda_frame), 2, (0,0,255), -1)
	        temp_pontos_esquerda_frame=pontos_maxmin_esquerda_frame
	        temp_centro_coluna_esquerda_frame=centro_da_coluna_esquerda_frame
	        '''
	        centro_da_coluna_01 = int((pontos_maxmin_01[0][0]+pontos_maxmin_01[0][1])/2)
	        cv2.circle(frame,(pontos_maxmin_01[0][0], Largura_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(pontos_maxmin_01[0][1], Largura_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(centro_da_coluna_01, Largura_01), 2, (0,0,255), -1)
	        '''

	else:
	        #centro_da_linha_inicial=temp_centro_linha_inicial
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][0], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][1], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(centro_da_linha_inicial, Comprimento_Inicial), 2, (0,0,255), -1)
	        #centro_da_linha_inicial = Metade_Largura
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #Comprimento_Inicial -= 5
	        Largura_esquerda = Largura_esquerda % Largura
	centro_da_coluna_esquerda_frame = centro_da_coluna_esquerda_frame
	        #num_de_pontos_perdidos += 1
	
	cYef= (centro_da_coluna_esquerda_frame, Largura_esquerda)
	#print("Centoride esquerda:", cYef)

	if len(pontos_maxmin_direita_frame) > 0 and len(pontos_maxmin_direita_frame[0]) > 1: # Se encontrou algo continua
	        centro_da_coluna_direita_frame = int((pontos_maxmin_direita_frame[0][0]+pontos_maxmin_direita_frame[0][1])/2)
	        cv2.circle(frame,(Largura_direita, pontos_maxmin_direita_frame[0][0]), 2, (255,0,0), -1)
	        cv2.circle(frame,(Largura_direita, pontos_maxmin_direita_frame[0][1]), 2, (255,0,0), -1)
	        cv2.circle(frame,(Largura_direita, centro_da_coluna_direita_frame), 2, (0,0,255), -1)
	        temp_pontos_direita_frame=pontos_maxmin_direita_frame
	        temp_centro_coluna_direita_frame=centro_da_coluna_direita_frame
	        '''
	        centro_da_coluna_01 = int((pontos_maxmin_01[0][0]+pontos_maxmin_01[0][1])/2)
	        cv2.circle(frame,(pontos_maxmin_01[0][0], Largura_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(pontos_maxmin_01[0][1], Largura_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(centro_da_coluna_01, Largura_01), 2, (0,0,255), -1)
	        '''

	else:
	        #centro_da_linha_inicial=temp_centro_linha_inicial
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][0], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][1], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(centro_da_linha_inicial, Comprimento_Inicial), 2, (0,0,255), -1)
	        #centro_da_linha_inicial = Metade_Largura
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #Comprimento_Inicial -= 5
	        Largura_direita = Largura_direita % Largura
	centro_da_coluna_direita_frame = centro_da_coluna_direita_frame
	        #num_de_pontos_perdidos += 1
	
	cYdf= (centro_da_coluna_direita_frame, Largura_direita)
	#print("Centroide direita: ", cYdf)

	# Fim Derivadas Frame

	# Inicio Derivadas Tranforms
	if len(pontos_maxmin_baixo_trans) > 0 and len(pontos_maxmin_baixo_trans[0]) > 1: # Se encontrou algo continua
	        centro_da_linha_baixo_trans = int((pontos_maxmin_baixo_trans[0][0]+pontos_maxmin_baixo_trans[0][1])/2)
	        cv2.circle(transform,(pontos_maxmin_baixo_trans[0][0], Comprimento_baixo_trans), 2, (255,0,0), -1)
	        cv2.circle(transform,(pontos_maxmin_baixo_trans[0][1], Comprimento_baixo_trans), 2, (255,0,0), -1)
	        cv2.circle(transform,(centro_da_linha_baixo_trans, Comprimento_baixo_trans), 2, (0,0,255), -1)
	        temp_pontos_baixo_trans=pontos_maxmin_baixo_trans
	        temp_centro_linha_baixo_trans=centro_da_linha_baixo_trans
	        '''
	        centro_da_linha_01 = int((pontos_maxmin_01[0][0]+pontos_maxmin_01[0][1])/2)
	        cv2.circle(frame,(pontos_maxmin_01[0][0], Comprimento_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(pontos_maxmin_01[0][1], Comprimento_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(centro_da_linha_01, Comprimento_01), 2, (0,0,255), -1)
	        '''

	else:
	        #centro_da_linha_inicial=temp_centro_linha_inicial
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][0], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][1], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(centro_da_linha_inicial, Comprimento_Inicial), 2, (0,0,255), -1)
	        #centro_da_linha_inicial = Metade_Largura
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #Comprimento_Inicial -= 5
	        Comprimento_baixo_trans = Comprimento_baixo_trans % Comprimento
		#num_de_pontos_perdidos += 1
	
	cbt=(centro_da_linha_baixo_trans, Comprimento_baixo_trans)
	print("Centroide baixo trans", cbt)

	if len(pontos_maxmin_alto_trans) > 0 and len(pontos_maxmin_alto_trans[0]) > 1: # Se encontrou algo continua
	        centro_da_linha_alto_trans = int((pontos_maxmin_alto_trans[0][0]+pontos_maxmin_alto_trans[0][1])/2)
	        cv2.circle(transform,(pontos_maxmin_alto_trans[0][0], Comprimento_alto_trans), 2, (255,0,0), -1)
	        cv2.circle(transform,(pontos_maxmin_alto_trans[0][1], Comprimento_alto_trans), 2, (255,0,0), -1)
	        cv2.circle(transform,(centro_da_linha_alto_trans, Comprimento_alto_trans), 2, (0,0,255), -1)
	        temp_pontos_alto_trans=pontos_maxmin_alto_trans
	        temp_centro_linha_alto_trans=centro_da_linha_alto_trans
	        '''
	        centro_da_linha_01 = int((pontos_maxmin_01[0][0]+pontos_maxmin_01[0][1])/2)
	        cv2.circle(frame,(pontos_maxmin_01[0][0], Comprimento_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(pontos_maxmin_01[0][1], Comprimento_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(centro_da_linha_01, Comprimento_01), 2, (0,0,255), -1)
        '''

	else:
	        #centro_da_linha_inicial=temp_centro_linha_inicial
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][0], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][1], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(centro_da_linha_inicial, Comprimento_Inicial), 2, (0,0,255), -1)
	        #centro_da_linha_inicial = Metade_Largura
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #Comprimento_Inicial -= 5
	        Comprimento_alto_trans = Comprimento_alto_trans % Comprimento
	        #num_de_pontos_perdidos += 1
	
	cat=(centro_da_linha_alto_trans,Comprimento_alto_trans)
	print("Centroide alto trans: ", cat)

	if len(pontos_maxmin_esquerda_trans) > 0 and len(pontos_maxmin_esquerda_trans[0]) > 1: # Se encontrou algo continua
	        centro_da_coluna_esquerda_trans = int((pontos_maxmin_esquerda_trans[0][0]+pontos_maxmin_esquerda_trans[0][1])/2)
	        cv2.circle(transform,(Largura_esquerda_trans, pontos_maxmin_esquerda_trans[0][0]), 2, (255,0,0), -1)
	        cv2.circle(transform,(Largura_esquerda_trans, pontos_maxmin_esquerda_trans[0][1]), 2, (255,0,0), -1)
	        cv2.circle(transform,(Largura_esquerda_trans, centro_da_coluna_esquerda_trans), 2, (0,0,255), -1)
	        temp_pontos_esquerda_trans=pontos_maxmin_esquerda_trans
	        temp_centro_coluna_esquerda_trans=centro_da_coluna_esquerda_trans
	        '''
	        centro_da_coluna_01 = int((pontos_maxmin_01[0][0]+pontos_maxmin_01[0][1])/2)
	        cv2.circle(frame,(pontos_maxmin_01[0][0], Largura_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(pontos_maxmin_01[0][1], Largura_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(centro_da_coluna_01, Largura_01), 2, (0,0,255), -1)
	        '''

	else:
	        #centro_da_linha_inicial=temp_centro_linha_inicial
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][0], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][1], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(centro_da_linha_inicial, Comprimento_Inicial), 2, (0,0,255), -1)
	        #centro_da_linha_inicial = Metade_Largura
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #Comprimento_Inicial -= 5
	        Largura_esquerda_trans = Largura_esquerda_trans % N
	centro_da_coluna_esquerda_trans = centro_da_coluna_esquerda_trans
	        #num_de_pontos_perdidos += 1
	
	cet=(Largura_esquerda_trans, centro_da_coluna_esquerda_trans)
	print("Centroide esquerda trans:", cet)

	if len(pontos_maxmin_direita_trans) > 0 and len(pontos_maxmin_direita_trans[0]) > 1: # Se encontrou algo continua
	        centro_da_coluna_direita_trans = int((pontos_maxmin_direita_trans[0][0]+pontos_maxmin_direita_trans[0][1])/2)
	        cv2.circle(transform,(Largura_direita_trans, pontos_maxmin_direita_trans[0][0]), 2, (255,0,0), -1)
	        cv2.circle(transform,(Largura_direita_trans, pontos_maxmin_direita_trans[0][1]), 2, (255,0,0), -1)
	        cv2.circle(transform,(Largura_direita_trans, centro_da_coluna_direita_trans), 2, (0,0,255), -1)
	        temp_pontos_direita_trans=pontos_maxmin_direita_trans
	        temp_centro_coluna_direita_trans=centro_da_coluna_direita_trans
	        '''
	        centro_da_coluna_01 = int((pontos_maxmin_01[0][0]+pontos_maxmin_01[0][1])/2)
	        cv2.circle(frame,(pontos_maxmin_01[0][0], Largura_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(pontos_maxmin_01[0][1], Largura_01), 2, (255,0,0), -1)
	        cv2.circle(frame,(centro_da_coluna_01, Largura_01), 2, (0,0,255), -1)
	        '''

	else:
	        #centro_da_linha_inicial=temp_centro_linha_inicial
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][0], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(pontos_maxmin_inicial[0][1], Comprimento_Inicial), 2, (255,0,0), -1)
	        #cv2.circle(frame,(centro_da_linha_inicial, Comprimento_Inicial), 2, (0,0,255), -1)
	        #centro_da_linha_inicial = Metade_Largura
	        #pontos_maxmin_inicial=temp_centro_linha_inicial
	        #Comprimento_Inicial -= 5
	        Largura_direita_trans = Largura_direita_trans % N
		#Largura_direita_trans = 0
		#centro_da_coluna_direita_trans = centro_da_coluna_direita_trans
	        #num_de_pontos_perdidos += 1
	
	cdt= (Largura_direita_trans, centro_da_coluna_direita_trans)
	print("Centroide direita trans:", cdt)
	# Fim Derivadas Transform

	#print('cdt', cdt)
	#print('cbt', cbt)
	vetor_direita = ((cdt[0]) - (cbt[0]), (cdt[1]) - (cbt[1]))
	#print('vetor direita', vetor_direita)
	norm_vet_dir = np.sqrt(np.power(vetor_direita[0],2)+np.power(vetor_direita[1],2))
	#print('vet direita', norm_vet_dir)
	vetor_unitario_direita = (1,0)
	produto_interno_direita = vetor_direita[0]*vetor_unitario_direita[0] + vetor_direita[1]*vetor_unitario_direita[1]
	#print('Produto interno direita', produto_interno_direita)
	alpha = np.arccos(produto_interno_direita/(norm_vet_dir + np.sqrt(np.power(vetor_unitario_direita[0],2)+np.power(vetor_unitario_direita[1],2))))*180/np.pi
	#print('alpha', alpha)
	angulo_direita = 90 - alpha
	print('angulo direita', angulo_direita)

	#print('cat', cat)
	#print('cbt', cbt)
	vetor_centro = ((cat[0]) - (cbt[0]), (cat[1]) - (cbt[1]))
	#print('vetor centro', vetor_centro)
	norm_vet_cent = np.sqrt(np.power(vetor_centro[0],2)+np.power(vetor_centro[1],2))
	#print('vet centro', norm_vet_cent)
	vetor_unitario_centro = (1,0)
	#print('vetor unitario centro', vetor_unitario_centro)
	produto_interno_centro = vetor_centro[0]*vetor_unitario_centro[0] + vetor_centro[1]*vetor_unitario_centro[1]
	#print('Produto interno centro', produto_interno_centro)
	alpha_centro = np.arccos(produto_interno_centro/(norm_vet_cent + np.sqrt(np.power(vetor_unitario_centro[0],2)+np.power(vetor_unitario_centro[1],2))))*180/np.pi
	#print('alpha centro', alpha_centro)
	angulo_centro = 90 - alpha_centro
	print('angulo_centro', angulo_centro)
	
	#print('cet', cet)
	#print('cbt', cbt)
	vetor_esquerda = ((cet[0]) - (cbt[0]), (cet[1]) - (cbt[1]))
	#print('vetor esquerda', vetor_esquerda)
	norm_vet_esq = np.sqrt(np.power(vetor_esquerda[0],2)+np.power(vetor_esquerda[1],2))
	#print('vet esquerda', norm_vet_esq)
	vetor_unitario_esquerda = (1,0)
	produto_interno_esquerda = vetor_esquerda[0]*vetor_unitario_esquerda[0] + vetor_esquerda[1]*vetor_unitario_esquerda[1]
	#print('Produto interno esquerda', produto_interno_esquerda)
	alpha_esquerda = np.arccos(produto_interno_esquerda/(norm_vet_esq + np.sqrt(np.power(vetor_unitario_esquerda[0],2)+np.power(vetor_unitario_esquerda[1],2))))*180/np.pi
	#print('alpha esquerda', alpha_esquerda)
	angulo_esquerda = alpha_esquerda - 90
	print('angulo esquerda', angulo_esquerda)


	#	cv2.imshow("Mascara", mask_trans)
	#cv2.imshow("Frame", frame)
	#cv2.imshow("Fechamento_frame", fechamento_frame)
	#cv2.imshow("video", video)
	cv2.imshow("tranformado", transform)
	#cv2.imshow("Fechamento_trans", fechamento_trans)
	key = cv2.waitKey(1)
	#if key == 27:
	#		break
        
	#video.release()
	#cv2.destroyAllWindows() 



if __name__ == "__main__":
	rospy.init_node("line_follower", anonymous = True) 

	rospy.Subscriber("camera/rgb/image_raw", Image, passa_video)

	rospy.spin()

