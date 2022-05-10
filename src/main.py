import streamlit as st
from cv2 import (
    COLOR_BGR2RGB,
    FILLED,
    FONT_HERSHEY_PLAIN,
    VideoCapture,
    cvtColor,
    putText,
    rectangle,
)

from models.HandDetector import HandDetector
from utils.check_letter import check_letter


def main():
    st.title("LIBRAS Recognition")
    run = st.checkbox("Run")
    FRAME_WINDOW = st.image([])
    camera = VideoCapture(0)
    detector = HandDetector()

    letter = ""

    while run:
        success, frame = camera.read()

        if success:
            frame = detector.find_hands(frame)
            list_markings = detector.find_position(frame, 0)

            if len(list_markings) > 0:
                letter = check_letter(list_markings)

            rectangle(
                frame,
                (20, 20),  # Beginning of the rectangle
                (90, 100),  # End of the rectangle
                (255, 255, 255),  # Color
                FILLED,  # cv2.FILLED,
            )
            putText(frame, str(letter), (30, 85), FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

            frame = cvtColor(frame, COLOR_BGR2RGB)

            FRAME_WINDOW.image(frame)

    if not run:
        camera.release()
        st.write("Stopped")


if __name__ == "__main__":
    main()
