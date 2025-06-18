import pygame
import random
import sys

# 초기화
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐎 경마 게임")

# 색상 정의
WHITE = (255, 255, 255)
TRACK_COLORS = [(255, 100, 100), (100, 255, 100), (100, 100, 255)]

# 말 정의
NUM_HORSES = 3
horses = []
for i in range(NUM_HORSES):
    horse = pygame.Rect(50, 50 + i * 100, 60, 40)
    horses.append(horse)

# 폰트
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()
finish_line = WIDTH - 100
winner = None
running = True

# 게임 루프
while running:
    screen.fill(WHITE)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 말 이동
    if winner is None:
        for i, horse in enumerate(horses):
            dx = random.randint(1, 6)
            horse.x += dx
            if horse.x >= finish_line:
                winner = i

    # 트랙과 말 그리기
    for i, horse in enumerate(horses):
        pygame.draw.rect(screen, TRACK_COLORS[i], horse)
        pygame.draw.line(screen, (0, 0, 0), (finish_line, 0), (finish_line, HEIGHT), 5)

    # 승자 표시
    if winner is not None:
        text = font.render(f"🎉 말 {winner + 1} 번 승리!", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))

    pygame.display.flip()
    clock.tick(30)
