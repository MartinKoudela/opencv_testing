import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                     "haarcascade_frontalface_default.xml")


# smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
#                                    "haarcascade_smile.xml")

# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
#                                  "haarcascade_eye.xml")


def detect_features(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        corner_len = int(min(w, h) * 0.25)
        color = (0, 255, 0)
        thickness = 3

        cv2.line(frame, (x, y), (x + corner_len, y), color, thickness)
        cv2.line(frame, (x, y), (x, y + corner_len), color, thickness)

        cv2.line(frame, (x + w, y), (x + w - corner_len, y), color, thickness)
        cv2.line(frame, (x + w, y), (x + w, y + corner_len), color, thickness)

        cv2.line(frame, (x, h + y), (x + corner_len, y + h), color, thickness)
        cv2.line(frame, (x, h + y), (x, y + h - corner_len), color, thickness)

        cv2.line(frame, (x + w, y + h), (x + w - corner_len, y + h), color, thickness)
        cv2.line(frame, (x + w, y + h), (x + w, y + h - corner_len), color, thickness)

        face = frame[y: y + h, x: x + w]
        gray_face = gray[y: y + h, x: x + w]

    #        smiles = smile_cascade.detectMultiScale(gray_face, 2.5, minNeighbors=15)
    #       for (xp, yp, wp, hp) in smiles:
    #          face = cv2.rectangle(face, (xp, yp), (xp + wp, yp + hp),
    #                               color=(0, 0, 255), thickness=5)

    #    eyes = eye_cascade.detectMultiScale(gray_face, 2.5, minNeighbors=12)
    #   for (xp, yp, wp, hp) in eyes:
    #      face = cv2.rectangle(face, (xp, yp), (xp + wp, yp + hp),
    #                   color=(255, 0, 0), thickness=5)

    return frame


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

    frame = detect_features(frame)
    output.write(frame)
    cv2.imshow("Webcam loaded!", frame)
    if cv2.waitKey(1) == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()  # !q
