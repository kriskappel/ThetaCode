from cv_bridge import CvBridge
import cv2
import rospy
from sensor_msgs.msg import Image
import numpy as np
from std_msgs.msg import Int16


movement_x = 135
movement_y = 135

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
	#video = cv2.VideoCapture("back1_25.avi")
	N = 300
	font = cv2.FONT_HERSHEY_SIMPLEX

	Comprimento_baixo_trans = N - 5
	Comprimento_alto_trans = int(250) 
	Largura_esquerda_trans = int(N*1/4)
	Largura_direita_trans = int(N*3/4)


	Linha_threshold_baixo_trans = 0
	diff_inicial_baixo_trans = 0
	pontos_maxmin_baixo_trans = 0
	Linha_threshold_alto_trans = 0
	diff_inicial_alto_trans = 0
	pontos_maxmin_alto_trans = 0
	Linha_threshold_esquerda_trans = 0
	diff_inicial_esquerda_trans = 0
	pontos_maxmin_esquerda_trans = 0
	Linha_threshold_direito_trans = 0
	diff_inicial_direito_trans = 0
	pontos_maxmin_direito_trans = 0

	centro_da_linha_baixo_trans = 0
	centro_da_linha_alto_trans = 0
	centro_da_coluna_esquerda_trans = 0
	centro_da_coluna_direita_trans = 0

	cdt = (0,0)
	cet = (0,0)
	cat = (0,0)
	cbt = (0,0)

	angulo_direita = 0
	angulo_esquerda = 0
	angulo_centro = 0

	vals = 3

	# Cross-shaped Kernel
	kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))

	# while True:
	# 	ret, orig_frame = video.read()
	# #print(ret)
	# 	if not ret:        
	# 	#video = cv2.VideoCapture("road_car_view.mp4")
	# #        video = cv2.VideoCapture(args["video"])
	# 		video = cv2.VideoCapture("back1_25.avi")        	
	# 		continue

		#frame = cv2.GaussianBlur(orig_frame, (15, 15), 0)

	pts1 = np.float32([[171,239+55],[428,234+55],[64,427+55],[527,415+55]]) # pontos da imagem original
	pts2 = np.float32([[0,0],[N,0],[0,N],[N,N]]) # pontos da imagem corrigida

	M = cv2.getPerspectiveTransform(pts1,pts2) # Cria a matriz de transformacao
	#print(M)
	transform = cv2.warpPerspective(orig_frame,M,(N,N)) # Executa a trnasformacao

	hsv_transform = cv2.cvtColor(transform, cv2.COLOR_BGR2HSV)
	low_blue = np.array([85, 50, 0])
	up_blue = np.array([125, 255, 180])
	mask_trans = cv2.inRange(hsv_transform, low_blue, up_blue)

	fechamento_trans = cv2.morphologyEx(mask_trans, cv2.MORPH_CLOSE, kernel)

	# Inicio Linhas de Derivacao Transform
	Linha_threshold_baixo_trans = fechamento_trans[Comprimento_baixo_trans].astype(np.int16) # Linha selecionada baixo
	diff_inicial_baixo_trans = np.diff(Linha_threshold_baixo_trans)                                # Derivada da linha selecionada
	pontos_maxmin_baixo_trans = np.where(np.logical_or(diff_inicial_baixo_trans > 200, diff_inicial_baixo_trans < -200)) # maximos e minimos da derivada
	cv2.line(transform,(0,Comprimento_baixo_trans),(N,Comprimento_baixo_trans),(0,255,0),1)  # Desenhar linha escaneada

	Linha_threshold_alto_trans = fechamento_trans[Comprimento_alto_trans].astype(np.int16) # Linha selecionada alto
	diff_inicial_alto_trans = np.diff(Linha_threshold_alto_trans)                          # Derivada da linha selecionada
	pontos_maxmin_alto_trans = np.where(np.logical_or(diff_inicial_alto_trans > 200, diff_inicial_alto_trans < -200)) # maximos e minimos da derivada
	cv2.line(transform,(0,Comprimento_alto_trans),(N,Comprimento_alto_trans),(0,255,0),1) # Desenhar linha escaneada

	Coluna_threshold_esquerda_trans = fechamento_trans[0:N, Largura_esquerda_trans].astype(np.int16) # Linha selecionada alto
	diff_inicial_esquerda_trans = np.diff(Coluna_threshold_esquerda_trans)                                     # Derivada da linha selecionada
	pontos_maxmin_esquerda_trans = np.where(np.logical_or(diff_inicial_esquerda_trans > 200, diff_inicial_esquerda_trans < -200)) # maximos e minimos da derivada
	cv2.line(transform,(Largura_esquerda_trans,0),(Largura_esquerda_trans,N),(0,255,0),1) # Desenhar linha escaneada

	Coluna_threshold_direita_trans = fechamento_trans[0:N, Largura_direita_trans].astype(np.int16) # Linha selecionada alto
	diff_inicial_direita_trans = np.diff(Coluna_threshold_direita_trans)                                     # Derivada da linha selecionada
	pontos_maxmin_direita_trans = np.where(np.logical_or(diff_inicial_direita_trans > 200, diff_inicial_direita_trans < -200)) # maximos e minimos da derivada
	cv2.line(transform,(Largura_direita_trans,0),(Largura_direita_trans,N),(0,255,0),1) # Desenhar linha escaneada
	# Fim Linhas de Derivacao Transform

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
	        Comprimento_baixo_trans = Comprimento_baixo_trans# % Comprimento
		#num_de_pontos_perdidos += 1
	cbt_ant = cbt
	cbt=(centro_da_linha_baixo_trans, Comprimento_baixo_trans)
	
	# print("Centroide baixo trans", cbt)

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
	        Comprimento_alto_trans = Comprimento_alto_trans# % Comprimento
	        #num_de_pontos_perdidos += 1
	cat_ant = cat
	cat=(centro_da_linha_alto_trans,Comprimento_alto_trans)
	# print("Centroide alto trans: ", cat)

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
	        Largura_esquerda_trans = Largura_esquerda_trans #% N
		#centro_da_coluna_esquerda_trans = centro_da_coluna_esquerda_trans
	        #num_de_pontos_perdidos += 1
	cet_ant = cet
	cet=(Largura_esquerda_trans, centro_da_coluna_esquerda_trans)
	# print("Centroide esquerda trans:", cet)

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
	cdt_ant = cdt
	cdt= (Largura_direita_trans, centro_da_coluna_direita_trans)
	# print("Centroide direita trans:", cdt)
	# Fim Derivadas Transform

	angulo_dir_ant = angulo_direita
	angulo_esq_ant = angulo_esquerda
	angulo_cent_ant = angulo_centro

# Inicio do calculo do angulo
	#vetor_direita_ant = vetor_direita
	vetor_direita = ((cdt[0]) - (cbt[0]), (cdt[1]) - (cbt[1]))
	if cdt_ant != cdt:
		norm_vet_dir = np.sqrt(np.power(vetor_direita[0],2)+np.power(vetor_direita[1],2))
		vetor_unitario_direita = (1,0)
		produto_interno_direita = vetor_direita[0]*vetor_unitario_direita[0] + vetor_direita[1]*vetor_unitario_direita[1]
		alpha = np.arccos(produto_interno_direita/(norm_vet_dir + np.sqrt(np.power(vetor_unitario_direita[0],2)+np.power(vetor_unitario_direita[1],2))))*180/np.pi
		angulo_direita = 90 - alpha
		# print('angulo direita', angulo_direita)
		girar_direita = 'Girar Direita'
	else:
		angulo_direita = 0
		# print('angulo direita', angulo_direita)
		girar_direita = ' '

	vetor_centro = ((cat[0]) - (cbt[0]), (cat[1]) - (cbt[1]))
	if cat_ant != cat:
		norm_vet_cent = np.sqrt(np.power(vetor_centro[0],2)+np.power(vetor_centro[1],2))
		vetor_unitario_centro = (1,0)
		produto_interno_centro = vetor_centro[0]*vetor_unitario_centro[0] + vetor_centro[1]*vetor_unitario_centro[1]
		alpha = np.arccos(produto_interno_centro/(norm_vet_cent + np.sqrt(np.power(vetor_unitario_centro[0],2)+np.power(vetor_unitario_centro[1],2))))*180/np.pi
		angulo_centro = 90 - alpha
		# print('angulo centro', angulo_centro)
#		girar_centro = 'Girar Centro'
	else:
		angulo_centro = 0
		# print('angulo centro', angulo_centro)
#		girar_centro = ' '

	vetor_esquerda = ((cet[0]) - (cbt[0]), (cet[1]) - (cbt[1]))
	if cet_ant != cet:
		norm_vet_esq = np.sqrt(np.power(vetor_esquerda[0],2)+np.power(vetor_esquerda[1],2))
		vetor_unitario_esquerda = (1,0)
		produto_interno_esquerda = vetor_esquerda[0]*vetor_unitario_esquerda[0] + vetor_esquerda[1]*vetor_unitario_esquerda[1]
		alpha = np.arccos(produto_interno_esquerda/(norm_vet_esq + np.sqrt(np.power(vetor_unitario_esquerda[0],2)+np.power(vetor_unitario_esquerda[1],2))))*180/np.pi
		angulo_esquerda = 90 - alpha
		# print('angulo esquerda', angulo_esquerda)
		girar_esquerda = 'Girar esquerda'
	else:
		angulo_esquerda = 0
		# print('angulo esquerda', angulo_esquerda)
		girar_esquerda = ' '

#	if np.absolute(angulo_direita - angulo_dir_ant) < vals-2:
#		angulo_direita = angulo_dir_ant
#	else:
#		angulo_direita = angulo_direita

#	if np.absolute(angulo_centro - angulo_cent_ant) < vals-2:
#		angulo_centro = angulo_cent_ant
#	else:
#		angulo_centro = angulo_centro

#	if np.absolute(angulo_esquerda - angulo_esq_ant) < vals-2:
#		angulo_esquerda = angulo_esq_ant
#	else:
#		angulo_esquerda = angulo_esquerda 	
                     	
#	if angulo_centro == 0:	
	# if (angulo_centro !=0 and np.absolute(angulo_centro) < vals):
	# 	girar = 'siga em frente'
	# elif (angulo_centro !=0 and angulo_centro < -vals):
	# 	girar = 'gire a esquerda'
	# elif (angulo_centro !=0 and angulo_centro > vals):
	# 	girar = 'gire a direita'
	# elif (angulo_centro == 0 and (angulo_centro < -vals or np.absolute(angulo_direita) > np.absolute(angulo_esquerda))):
	# 	girar = 'gire a direita'
	# elif (angulo_centro == 0 and (angulo_centro > vals or np.absolute(angulo_direita) < np.absolute(angulo_esquerda))):
	# 	girar = 'gire a esquerda'	
	# else:
	# 	girar = 
	girar = 0
	if(angulo_centro == 0 and np.absolute(angulo_direita) > vals and np.absolute(angulo_esquerda) > vals):
		girar = 'espere comando'
		pub_movement(135, 135)
	elif (angulo_centro != 0 and np.absolute(angulo_centro) < vals):
		girar = 'siga em frente'
		pub_movement(135, 165)
	elif (angulo_centro !=0 and angulo_centro < -vals):
		girar = 'esquerda'
		pub_movement(170,135)
	elif (angulo_centro !=0 and angulo_centro > vals):
		girar = 'direita'
		pub_movement(100,135)
	elif (angulo_centro == 0 and (angulo_centro < -vals or np.absolute(angulo_direita) > np.absolute(angulo_esquerda))):
		girar = 'direita'
		pub_movement(100,135)
	elif (angulo_centro == 0 and (angulo_centro > vals or np.absolute(angulo_direita) < np.absolute(angulo_esquerda))):
		girar = 'esquerda'
		pub_movement(170,135)
	else:
		girar = girar
		pub_movement(0, 0)
#        	if np.absolute(angulo_direita) < np.absolute(angulo_esquerda):
#			girar = 'gire a direita'
	#		else:
	#			girar = 'gira a esquerda'
		

	#	vetor_centro = ((cat[0]) - (cbt[0]), (cat[1]) - (cbt[1]))
	#	norm_vet_cent = np.sqrt(np.power(vetor_centro[0],2)+np.power(vetor_centro[1],2))
	#	vetor_unitario_centro = (1,0)
	#	produto_interno_centro = vetor_centro[0]*vetor_unitario_centro[0] + vetor_centro[1]*vetor_unitario_centro[1]
	#	alpha_centro = np.arccos(produto_interno_centro/(norm_vet_cent + np.sqrt(np.power(vetor_unitario_centro[0],2)+np.power(vetor_unitario_centro[1],2))))*180/np.pi
	#	angulo_centro = 90 - alpha_centro
	#	print('angulo_centro', angulo_centro)
		
	#	vetor_esquerda = ((cet[0]) - (cbt[0]), (cet[1]) - (cbt[1]))
	#	norm_vet_esq = np.sqrt(np.power(vetor_esquerda[0],2)+np.power(vetor_esquerda[1],2))
	#	vetor_unitario_esquerda = (1,0)
	#	produto_interno_esquerda = vetor_esquerda[0]*vetor_unitario_esquerda[0] + vetor_esquerda[1]*vetor_unitario_esquerda[1]
	#	alpha_esquerda = np.arccos(produto_interno_esquerda/(norm_vet_esq + np.sqrt(np.power(vetor_unitario_esquerda[0],2)+np.power(vetor_unitario_esquerda[1],2))))*180/np.pi
	#	angulo_esquerda = alpha_esquerda - 90
	#	print('angulo esquerda', angulo_esquerda)

	# Fim do calculo do angulo




	#	cv2.putText(transform,girar_direita,(20,280), font, 1,(255,255,255),2,cv2.LINE_AA)
	#	cv2.putText(transform,girar_esquerda,(20,200), font, 1,(255,255,255),2,cv2.LINE_AA)
	cv2.putText(transform,girar,(20,240), font, 1,(255,255,255),2,cv2.LINE_AA)
	#print('movimento:', girar)	
	cv2.imshow("Frame", transform)
	#cv2.imshow("Fechamento", fechamento_trans)


	key = cv2.waitKey(1)
# 	if key == 27:
# 			break
        
# video.release()
# cv2.destroyAllWindows() 

def pub_movement(pwm_x, pwm_y):
	global movement_x 
	global movement_y
	if( pwm_x == 0 and pwm_y == 0):
		pass
	else:
		movement_x = pwm_x
		movement_y = pwm_y

	# if( pwm_y == 0 ):
	# 	pass
	# else:
	# 	movement_y = pwm_y

	movex = rospy.Publisher('channel_x', Int16, queue_size=1)
	movex.publish(movement_x)
	movey = rospy.Publisher('channel_y', Int16, queue_size=1)
	movey.publish(movement_y)

	


if __name__ == "__main__":
	rospy.init_node("line_follower", anonymous = True) 

	rospy.Subscriber("camera/rgb/image_raw", Image, passa_video)

	rospy.spin()

