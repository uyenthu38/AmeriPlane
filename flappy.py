import pygame, sys, random
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen= pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',35)
score = 0
high_score = 0
max_health=100
health=100
def health_bar(health_current):
    ratio=health/max_health
    pygame.draw.rect(screen, "red", (66, 5, 300, 40))
    pygame.draw.rect(screen, "green", (66, 5, 300 * ratio, 40))
def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))
def choose_random_grade():
    return random.choice(grade_images)
def create_grade():
    random_grade_pos = random.choice(grade_height)
    grade_rect = grade_current.get_rect(midtop =(500,random_grade_pos))
    return grade_rect
def move_grade(grades):
    for grade in grades :
        grade.centerx -= 5
    return grades
def draw_grade(grades, grade_appear):
    for grade, grade_current1 in zip(grades, grade_appear):
        screen.blit(grade_current1, grade)
def check_collision(grades, grade_current_list):
    for grade, grade_current2 in zip(grades,grade_current_list):
        if bird_rect.colliderect(grade) and grade_current2==gradeF_surface:
            hit_sound.play()
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
            return False
    if health <=0:
            return False
    return True
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_movement*3,1)
    return new_bird
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird, new_bird_rect
def score_display(game_state):
    if game_state == 'main game':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface,score_rect)


        high_score_surface = game_font.render(f'High Score: {int(high_score)}',True,(255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (216,630))
        screen.blit(high_score_surface,high_score_rect)
def update_score(score,high_score):
    if score > high_score:
        high_score = score
    return high_score
#Tạo các biến cho trò chơi
gravity = 0.8
bird_movement = 0
game_active = True
#chèn background
bg = pygame.image.load('assets/bg1234.jpg').convert()
#chèn sàn
floor = pygame.image.load('assets/dat2.gif').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#tạo chim
bird_down = pygame.image.load('assets/red0.png').convert_alpha()
bird_mid = pygame.image.load('assets/red1.png').convert_alpha()
bird_up = pygame.image.load('assets/red2.png').convert_alpha()
bird_list= [bird_down,bird_mid,bird_up] #0 1 2
bird_index = 0
bird = bird_list[bird_index]
bird= pygame.image.load('assets/red1.png').convert_alpha()
bird_rect = bird.get_rect(center = (100,384))


#tạo timer cho bird
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap,200)
#tạo ống
gradeF_surface = pygame.image.load('assets/wf.png').convert_alpha()
gradeD_surface = pygame.image.load('assets/wd.png').convert_alpha()
gradeC_surface = pygame.image.load('assets/wc.png').convert_alpha()
gradeB_surface = pygame.image.load('assets/wb.png').convert_alpha()
gradeA_surface = pygame.image.load('assets/wa.png').convert_alpha()
grade_appear_list=[]
grade_images = [gradeF_surface,gradeD_surface, gradeC_surface, gradeB_surface, gradeA_surface]
grade_list =[]
#tạo timer
spawnpipe= pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1000)
grade_height = [100,200,300,400,500]
#Tạo màn hình kết thúc
game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/GO.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(216,384))
#Chèn âm thanh
flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 100
#while loop của trò chơi
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement =-12
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active==False:
                game_active = True
                grade_list.clear()
                bird_rect.center = (100,384)
                bird_movement = 0
                score = 0
                health=100
        if event.type == spawnpipe:
            grade_current=random.choice(grade_images)
            grade_appear_list.append(grade_current)
            grade_list.append(create_grade())
        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index =0
            bird, bird_rect = bird_animation()    
    for grade, grade_current2 in zip(grade_list,grade_appear_list):   
        if bird_rect.colliderect(grade) and grade_current2==gradeD_surface:
            hit_sound.play()
            grade.centerx = -1000
            grade.centery = -1000
            health -=20
        if bird_rect.colliderect(grade) and grade_current2==gradeC_surface:
            hit_sound.play()
            grade.centerx = -1000
            grade.centery = -1000
            health -=10
        if bird_rect.colliderect(grade) and grade_current2==gradeB_surface:
            score_sound.play()
            grade.centerx = -1000
            grade.centery = -1000
            health +=20
        if bird_rect.colliderect(grade) and grade_current2==gradeA_surface:
            score_sound.play()
            grade.centerx = -1000
            grade.centery = -1000
            health +=30  
    if health >=100: health=100
    if health <=0: health=0
    screen.blit(bg,(0,0))
    if game_active:
        #chim
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)      
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird,bird_rect)
        game_active= check_collision(grade_list,grade_appear_list)
        health -=0.1
        health_bar(health)      
        #ống
        grade_list = move_grade(grade_list)
        draw_grade(grade_list, grade_appear_list)
        score += 0.01
        score_display('main game')
    
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score = update_score(score,high_score)
        score_display('game_over')
    #sàn
    floor_x_pos -= 3
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos =0
   
    pygame.display.update()
    clock.tick(50)
    
