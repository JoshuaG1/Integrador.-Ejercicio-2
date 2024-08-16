import cv2

# Inicia la captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Lee el primer frame
ret, prev_frame = cap.read()

while True:
    # Lee el siguiente frame
    ret, current_frame = cap.read()
    
    if not ret:
        break
    
    # Convierte ambos frames a escala de grises para simplificar el cálculo de diferencias
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    
    # Calcula la diferencia absoluta entre el frame actual y el frame anterior
    frame_diff = cv2.absdiff(current_gray, prev_gray)
    
    # Muestra el frame actual
    cv2.imshow('Frame Actual', current_frame)
    
    # Muestra la diferencia entre frames
    cv2.imshow('Diferencia entre Frames', frame_diff)
    
    # Asigna el frame actual al frame anterior para la siguiente iteración
    prev_frame = current_frame
    
    # Espera 1ms para presionar 'q' y salir del loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra todas las ventanas
cap.release()
cv2.destroyAllWindows()
