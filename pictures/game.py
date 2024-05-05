import pygame

pygame.init()

# Screen setup
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Put these images in pairs")

# Font text thing
FONT = pygame.font.SysFont("Times new roman", 50)

# Object sizes (will use when changing the size of the objects)
OBJECT_WIDTH, OBJECT_HEIGHT = 130, 130

# Loading images
salt = pygame.image.load("salt.png")
peanutbutter = pygame.image.load("peanut_butter.png")
cat = pygame.image.load("cat.png")
jam = pygame.image.load("jam.png")
pepper = pygame.image.load("pepper.png")
dog = pygame.image.load("dog.png")

# Scale images
jamy = pygame.transform.scale(jam, (OBJECT_WIDTH, OBJECT_HEIGHT))
peppery = pygame.transform.scale(pepper, (OBJECT_WIDTH, OBJECT_HEIGHT))
dogy = pygame.transform.scale(dog, (OBJECT_WIDTH, OBJECT_HEIGHT))

salty = pygame.transform.scale(salt, (OBJECT_WIDTH, OBJECT_HEIGHT))
peanutbuttery = pygame.transform.scale(peanutbutter, (OBJECT_WIDTH, OBJECT_HEIGHT))
caty = pygame.transform.scale(cat, (OBJECT_WIDTH, OBJECT_HEIGHT))



# Initial positions of images
image_positions = {
    jamy: (450, 125),
    peppery: (450, 320),
    dogy: (450, 515),

    salty: (150, 125),
    peanutbuttery: (150, 320),
    caty: (150, 515)
}

# These are the images that won't move during the game (on the right side of the game window)
fixed_positions = {
    jamy: (450, 125),
    peppery: (450, 320),
    dogy: (450, 515)
}


# Function to draw images at their positions
def draw_images():
    for image, pos in image_positions.items():
        screen.blit(image, pos)


# Main game loop
running = True
dragging = False
drag_offset = (0, 0)
selected_image = None
score = 0 
is_salt_pepper_collided = False
is_peanutbutter_jam_collided = False
is_cat_dog_collided = False


def game_winner():
    screen.fill("pink")
    winner_text = FONT.render("You Won! Good job, yay", True, (0,0,128))
    text_rect = winner_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(winner_text, text_rect)


while running:
    screen.fill((0, 0, 100))
    pygame.draw.line(screen, (0, 0, 0), (370, 0), (370, screen_height), 10)
    draw_images()


    score_text = FONT.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (30, 30))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for image, pos in image_positions.items():
                image_rect = image.get_rect(topleft=pos)
                if image_rect.collidepoint(mouse_pos):
                    if image not in fixed_positions:  # Check if image is movable
                        dragging = True
                        selected_image = image
                        drag_offset = (mouse_pos[0] - pos[0], mouse_pos[1] - pos[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            selected_image = None
        elif event.type == pygame.MOUSEMOTION:
            if dragging and selected_image:
                mouse_pos = pygame.mouse.get_pos()
                if selected_image not in fixed_positions:  # Check if image is movable
                    image_positions[selected_image] = (mouse_pos[0] - drag_offset[0], mouse_pos[1] - drag_offset[1])
    
    salty_rect = salty.get_rect(topleft=image_positions[salty])
    peppery_rect = peppery.get_rect(topleft=image_positions[peppery])
    if salty_rect.colliderect(peppery_rect) and is_salt_pepper_collided == False:
        score += 1 
        is_salt_pepper_collided = True
        

    peanutbuttery_rect = peanutbuttery.get_rect(topleft=image_positions[peanutbuttery])
    jamy_rect = jamy.get_rect(topleft=image_positions[jamy])
    if peanutbuttery_rect.colliderect(jamy_rect) and is_peanutbutter_jam_collided == False:
        score += 1 
        is_peanutbutter_jam_collided = True




    caty_rect = peanutbuttery.get_rect(topleft=image_positions[caty])
    dogy_rect = dogy.get_rect(topleft=image_positions[dogy])
    if caty_rect.colliderect(dogy_rect) and is_cat_dog_collided == False:
        score += 1
        is_cat_dog_collided = True


    if score == 3:
        game_winner()
 
    pygame.display.update()

pygame.quit()