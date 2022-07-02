import av
from streamlit_webrtc import VideoProcessorBase


class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.classifier_list = []
        self.active_classifiers = {}

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        # update classifiers
        if "classifiers" not in st.session_state:
            self.default_classifiers = load_classifiers()
        else:
            self.default_classifiers = st.session_state["classifiers"]

        self.active_classifiers = {
            i: self.default_classifiers[i] for i in self.classifier_list
        }

        img = frame.to_ndarray(format="bgr24")

        frame_scan(img, self.active_classifiers)

        return av.VideoFrame.from_ndarray(img, format="bgr24")
