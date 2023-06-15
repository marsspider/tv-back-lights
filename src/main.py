import cv2
cap = cv2.VideoCapture('./data/video.mp4')


def print_output(msg):
    print(msg)


def show_video():

    if not cap.isOpened():
        print("Error opening video stream or file")

    while cap.isOpened():
        ret, base_image = cap.read()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        cv2.imshow('Frame', base_image)


if __name__ == "__main__":
    print_output("hello world")
    show_video()

    cap.release()
    cv2.destroyAllWindows()