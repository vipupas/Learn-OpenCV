import cv2
import mediapipe as mp
import time
import random
import numpy as np

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)
choices = ['Stone', 'Paper', 'Scissor']

# Detect gesture
def detect_gesture(hand_landmarks):
    lm = hand_landmarks.landmark
    def is_folded(tip, pip): return lm[tip].y > lm[pip].y
    index_folded = is_folded(8, 6)
    middle_folded = is_folded(12, 10)
    ring_folded = is_folded(16, 14)
    pinky_folded = is_folded(20, 18)

    if index_folded and middle_folded and ring_folded and pinky_folded:
        return "Stone"
    elif not index_folded and not middle_folded and not ring_folded and not pinky_folded:
        return "Paper"
    elif not index_folded and not middle_folded and ring_folded and pinky_folded:
        return "Scissor"
    else:
        return "Other"

# Wait until hand appears
def wait_for_hand():
    while True:
        ret, frame = cap.read()
        if not ret:
            return None, None

        frame = cv2.flip(frame, 1)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        cv2.putText(frame, "Show your hand to start...", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.imshow("STONE-PAPER-SCISSOR", frame)
            cv2.waitKey(500)  # Wait a short moment before starting
            return results, frame

        cv2.imshow("STONE-PAPER-SCISSOR", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

# Show countdown
def show_countdown():
    for count in range(1, 4):
        start_time = time.time()
        while time.time() - start_time < 1:
            ret, frame = cap.read()
            if not ret:
                return None, None
            frame = cv2.flip(frame, 1)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            user_gesture = "No Hand"
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    user_gesture = detect_gesture(hand_landmarks)

            height, width, _ = frame.shape
            x, y = width - 100, 80
            cv2.putText(frame, str(count), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
            cv2.putText(frame, f"Gesture: {user_gesture}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            cv2.imshow("STONE-PAPER-SCISSOR", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                exit()

    # After countdown, capture one final frame
    ret, frame = cap.read()
    if not ret:
        return "No Hand", None
    frame = cv2.flip(frame, 1)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    user_gesture = "No Hand"
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            user_gesture = detect_gesture(hand_landmarks)

    return user_gesture, frame

# Show result screen
def show_result(user, computer):
    blank = 255 * np.ones(shape=[400, 600, 3], dtype=np.uint8)
    result = "Draw"
    if user == "Other" or user == "No Hand":
        result = "Invalid Gesture!"
    elif user == computer:
        result = "Draw"
    elif (user == "Stone" and computer == "Scissor") or \
         (user == "Paper" and computer == "Stone") or \
         (user == "Scissor" and computer == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"

    cv2.putText(blank, f"You: {user}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.putText(blank, f"Computer: {computer}", (50, 180), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
    cv2.putText(blank, f"Result: {result}", (50, 260), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 128, 0), 4)

    cv2.imshow("Result", blank)
    print("👉 Close the 'Result' window to play again...")

    while True:
        if cv2.getWindowProperty("Result", cv2.WND_PROP_VISIBLE) < 1:
            break
        if cv2.waitKey(100) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

# Main game loop
with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    print("Press 'q' to quit at any time.")
    while True:
        wait_for_hand()
        user_gesture, frame = show_countdown()
        computer_choice = random.choice(choices)
        show_result(user_gesture, computer_choice)

cap.release()
cv2.destroyAllWindows()
