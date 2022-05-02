"""
2022. 05. 02. 
Byunghyun Ban

bhban@kakao.com
https://github.com/needleworm/python101


Open Source Sprites
[1] THE KNIGHT - FREE SPRITES - https://www.gameart2d.com/the-knight-free-sprites.html
[2] shiny-diamonds - https://gamesupply.itch.io/shiny-diamonds
"""

try:
    import pygame as P
except:
    import pip
    pip.main(['install', "pygame"])
    import pygame as P
    
import os
import math

# GLOBAL SETTINGS
WIDTH = 1000
HEIGHT = 750
CHAR_SIZE = 150
FPS = 40
TITLE = "BHBan_Python Stage No. "
GROUND_Y = 617


def read_images(path):
    lst = os.listdir(path)
    lst.sort()
    ret = []
    for el in lst:
        img = P.image.load(path + "/" + el)
        img.set_colorkey((0, 0, 0))
        ret.append(img)
    return ret


class Gem(P.sprite.Sprite):
    def __init__(self, x, y, spritePath):
        super(Gem, self).__init__()
        size = (CHAR_SIZE // 3, CHAR_SIZE // 3)

        images = read_images(spritePath)

        self.rect = P.Rect((x, y), size)

        self.images = [P.transform.scale(image, size) for image in images]

        # 젬의 첫번째 이미지
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        # 부양 구현을 위한 카운트
        self.count = 0
        self.y = y

    def update(self):
        self.index += 1

        a_y = math.sin(self.count*0.1) * CHAR_SIZE // 20
        self.rect.y = self.y + a_y

        self.count = (self.count + 1) % 3600

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]


class Player(P.sprite.Sprite):
    def __init__(self, x, y, spritePath):
        super(Player, self).__init__()
        size = (CHAR_SIZE, CHAR_SIZE)

        images = []
        # idle images
        images += read_images(spritePath + "/idle")
        # walk images
        images += read_images(spritePath + "/run")
        # jump images
        images += read_images(spritePath + "/jump")
        # attack images
        images += read_images(spritePath + "/attack")

        self.x = x
        self.y = y

        # rect 만들기
        self.rect = P.Rect((self.x, self.y), size)

        # Rect 크기와 Image 크기 맞추기. P.transform.scale
        self.images = [P.transform.scale(image, size) for image in images]

        # 원본 이미지 소스
        self.images_right = self.images

        # 왼쪽 보는 이미지 소스
        self.images_left = [P.transform.flip(image, True, False) for image in self.images]

        # 캐릭터 현 상태
        # 0 - idle
        # 1 - walking
        self.state = 0
        # 방향
        self.heading = "right"
        # 속도
        self.velocity_x = 0

        # 점프 구현
        self.jumping = 0
        self.jump_init_v_y = 9
        self.velocity_y = 9

        # 공격 구현
        self.attacking = 0

        # 캐릭터의 첫번째 이미지
        self.index = 0
        self.image = self.images[self.index]
        # 프레임 한장당 보여줄 이미지 시간 계산
        self.animation_time = 5
        # 현재 시간 초기화
        self.current_time = 0

    def update(self, mt):
        # IDLE
        if self.state == 0:
            count = 10
            start_Index = 0
            self.velocity_x = 0
        # RUNNING
        elif self.state == 1:
            count = 10
            start_Index = 10
            self.velocity_x = 12
        
        # 방향이 오른쪽이면, 오른쪽 이미지 선택
        if self.heading == 'right':
            self.images = self.images_right
        # 방향이 왼쪽이면 왼쪽 이미지 선택, 진행방향 x축으로 -
        elif self.heading == 'left':
            self.images = self.images_left
            self.velocity_x = abs(self.velocity_x) * -1

        # 좌우 위치값 변경, 이동
        self.rect.x += self.velocity_x

        if self.rect.left < 0:
            self.rect.x = 0
        elif self.rect.right > WIDTH:
            self.rect.x = WIDTH - self.rect.width
        
        if self.jumping > 0:
            if self.velocity_y > 0:
                a = 0.5 * (self.velocity_y ** 2)
            else:
                a = - 0.5 * (self.velocity_y ** 2)
            self.rect.y -= round(a)
            self.velocity_y -= 1
            count = 10
            start_Index = 20
            if self.rect.top > GROUND_Y - CHAR_SIZE + 10:
                self.rect.top = GROUND_Y - CHAR_SIZE + 10
                self.jumping = 0
                self.velocity_y = self.jump_init_v_y

        if self.attacking > 0:
            count = 10
            start_Index = 30
            self.attacking -= 1

        # loop 시간 더하기
        self.current_time += mt

        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index % count) + start_Index
            self.image = self.images[self.index]
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0


# 스테이지 빌더
class Stages:
    def __init__(self, stage_number=1):
        if stage_number == 1:
            self.stage = Stage1()


# 스테이지 1
class Stage1:
    def __init__(self):
        self.background_file = "./sprites/backgrounds/background_1.png"
        self.stage_file = "./sprites/stages/stage_1.png"
        self.gem_path = "./sprites/gems/purple"
        self.char_sprite_path = "./sprites/characters/knight"
        self.stage_clear_file = "./sprites/words/stage clear.png"

        # 게임 엔진 세팅
        P.init()
        self.screen = P.display.set_mode((WIDTH, HEIGHT))
        P.display.set_caption(TITLE + "1")
        self.font = P.font.Font(None, 40)
        self.clock = P.time.Clock()

        # 스테이지 생성
        self.background = P.transform.scale(P.image.load(self.background_file), (WIDTH, HEIGHT))
        self.stage = P.transform.scale(P.image.load(self.stage_file), (WIDTH, HEIGHT))
        
        # 캐릭터 생성
        self.player = Player(50, GROUND_Y - CHAR_SIZE + 10, self.char_sprite_path)
        self.char_sprites = P.sprite.Group(self.player)

        # 젬 생성
        self.gem = Gem(800, GROUND_Y - CHAR_SIZE//1.5, self.gem_path)
        self.gem_sprites = P.sprite.Group(self.gem)

        # 클리어 문자
        self.stage_clear = P.image.load(self.stage_clear_file)

        # 게임 실행
        self.run_game()

    def run_game(self):
        running = True
        move_step = 10*60 / FPS
        clear = False
        # 게임 실행
        while running:
            # FPS 세팅
            dt = self.clock.tick(FPS)

            #이벤트 리스닝
            for event in P.event.get():
                if event.type == P.QUIT:
                    # 게임 종료
                    running = False
                    break

                # 키 입력받아 동작
                elif event.type == P.KEYDOWN:
                    if event.key == P.K_RIGHT:
                        self.player.heading = "right"
                        self.player.state = 1
                    elif event.key == P.K_LEFT:
                        self.player.heading = "left"
                        self.player.state = 1
                    if event.key == P.K_UP and not self.player.jumping:
                        self.player.jumping = 1
                    if event.key == P.K_SPACE and not self.player.jumping:
                        self.player.attacking = 10
                elif event.type == P.KEYUP:
                    if event.key == P.K_RIGHT or event.key == P.K_LEFT:
                        self.player.velocity_x = 0
                        self.player.state = 0

            # 배경 삽입
            self.screen.blit(self.background, (0, 0))

            #스테이지 삽입
            self.screen.blit(self.stage, (0, 0))

            self.char_sprites.update(move_step)
            self.char_sprites.draw(self.screen)

            self.gem_sprites.update()
            self.gem_sprites.draw(self.screen)

            P.display.update()
            # 젬과 캐릭터 충돌시
            if self.player.rect.colliderect(self.gem.rect):
                clear = True
                # 엔딩 크레딧 구현
                x, y = self.stage_clear.get_size()
                self.screen.blit(self.stage_clear, (WIDTH / 2 - x / 2, HEIGHT / 2 - y / 2))
                P.display.update()
                print("게임 클리어!")
                break

        while running and clear:
            # FPS 세팅
            dt = self.clock.tick(FPS)
            # 이벤트 리스닝
            for event in P.event.get():
                if event.type == P.QUIT or event.type == P.KEYDOWN:
                    # 게임 종료
                    running = False
                    break

        P.quit()

if __name__ == '__main__':
    Stages()
