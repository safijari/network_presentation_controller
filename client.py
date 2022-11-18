import pygame
import requests
import argh
import sys
import traceback
import maya


def main(ip):
    pygame.init()
    screen = pygame.display.set_mode((800, 300))

    # set the title of the screen
    pygame.display.set_caption("Client")

    # write instructions for using the app
    font = pygame.font.Font(None, 32)
    text = font.render(
        "Press the right arrow key or left arrow key to control the presentation",
        True,
        (255, 255, 255),
    )

    feedback_text = ""

    # add text to the screen
    textRect = text.get_rect()
    textRect.center = (0, 0)

    # a pygame program that intercepts the right arrow and left arrow keys and prints out which key is pressed
    while True:
        feedback_text_obj = font.render(feedback_text, True, (255, 255, 255),)

        screen.fill((0, 0, 0))
        screen.blit(text, [0, 0])
        screen.blit(feedback_text_obj, [0, 50])
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("Right arrow key pressed")
                    try:
                        requests.get(f"http://{ip}:5000/right")
                        feedback_text = f"Right arrow key pressed at {maya.now()}"
                    except Exception:
                        feedback_text = f"Error: Could not connect to server at {ip} at {maya.now()}"
                        traceback.print_exc()
                elif event.key == pygame.K_LEFT:
                    print("Left arrow key pressed")
                    try:
                        requests.get(f"http://{ip}:5000/left")
                        feedback_text = f"Left arrow key pressed at {maya.now()}"
                    except Exception:
                        feedback_text = f"Error: Could not connect to server at {ip} at {maya.now()}"
                        traceback.print_exc()


if __name__ == "__main__":
    argh.dispatch_command(main)
