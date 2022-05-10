import cv2
import mediapipe as mp


class HandDetector:
    def __init__(
        self,
        mode: bool = False,
        max_num_hands: int = 2,
        min_detection_confidence: float = 0.5,
        min_tracking_confidence: float = 0.5,
    ):
        self.mode = mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_num_hands,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence,
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, img, draw_hand=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        h, w, c = img.shape  # h: altura, w: largura, c: canais de cor
        if self.results.multi_hand_landmarks:
            for hand_number, hand_landmark in enumerate(
                self.results.multi_hand_landmarks
            ):
                if draw_hand:
                    self.mp_draw.draw_landmarks(
                        img, hand_landmark, self.mp_hands.HAND_CONNECTIONS
                    )

        return img

    def find_position(self, img, hand_number=0):
        h, w, c = img.shape  # h: altura, w: largura, c: canais de cor

        resultado_landmark = []
        try:
            if self.results.multi_hand_landmarks:
                chosen_hand = self.results.multi_hand_landmarks[hand_number]
                for _id, landmark in enumerate(chosen_hand.landmark):
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    resultado_landmark.append([_id, cx, cy])
            return resultado_landmark
        except:
            return []
