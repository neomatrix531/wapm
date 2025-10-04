import cv2
import numpy as np
from vpython import canvas, box, sphere, vector, rate
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# --- Load UI Image ---
icon = cv2.imread('start_icon.png')  # Replace with your image path
icon = cv2.resize(icon, (80, 80))

# --- Create OpenCV UI Canvas ---
canvas_ui = np.zeros((600, 800, 3), dtype=np.uint8)
canvas_ui[:] = (40, 40, 40)
x_offset, y_offset = 100, 100
canvas_ui[y_offset:y_offset+icon.shape[0], x_offset:x_offset+icon.shape[1]] = icon
cv2.putText(canvas_ui, "Start Game", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# --- Mouse Interaction ---
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if x_offset < x < x_offset+icon.shape[1] and y_offset < y < y_offset+icon.shape[0]:
            print("Start Game clicked!")
            launch_vpython()
            run_selenium_script()

cv2.namedWindow("Supreme Game Maker UI")
cv2.setMouseCallback("Supreme Game Maker UI", mouse_event)

# --- VPython 3D Scene ---
def launch_vpython():
    scene = canvas(title="Supreme Game World")
    box(pos=vector(0,0,0), size=vector(1,1,1), color=vector(1,0,0))
    sphere(pos=vector(2,0,0), radius=0.5, color=vector(0,1,0))
    for _ in range(100):
        rate(30)

# --- Selenium Automation ---
def run_selenium_script():
    print("Running Selenium script...")
    service = Service('path/to/chromedriver')  # Update this path
    driver = webdriver.Chrome(service=service)
    driver.get("https://example.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Supreme Game Maker")
    search_box.submit()
    driver.quit()

# --- Main Loop ---
while True:
    cv2.imshow("Supreme Game Maker UI", canvas_ui)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
