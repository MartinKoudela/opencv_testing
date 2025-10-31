import cv2

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("Could not load stream :(")
    exit()

fps = stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(stream.get(cv2.CAP_PROP_FRAME_HEIGHT))

output = cv2.VideoWriter("assets/stream.mp4",
            cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
            fps=fps, frameSize=(width, height))

while True:
    ret, frame = stream.read()
    if not ret:
        print("Could not read frame :(")
        break

    frame = cv2.resize(frame, (width, height))
    output.write(frame)
    cv2.imshow("Webcam loaded!", frame)
    if cv2.waitKey(1) == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()  # !q
