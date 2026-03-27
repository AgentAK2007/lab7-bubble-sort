"""Pygame renderer for Bubble Sort visualization."""

from __future__ import annotations

from typing import List

import pygame

from sorting_logic import SortStep, generate_bubble_sort_steps


BACKGROUND = (18, 20, 26)
TEXT = (235, 240, 255)
BAR_DEFAULT = (76, 132, 255)
BAR_COMPARE = (255, 201, 74)
BAR_SWAP = (255, 120, 90)
BAR_NEGATIVE = (130, 220, 150)
PANEL = (36, 42, 56)


def _draw_state(
    screen: pygame.Surface,
    title_font: pygame.font.Font,
    ui_font: pygame.font.Font,
    state: SortStep,
    delay_ms: int,
    paused: bool,
) -> None:
    """Draw one visualization frame."""
    screen.fill(BACKGROUND)

    width, height = screen.get_size()
    values = state["values"]

    left = int(state["left"])
    right = int(state["right"])
    pass_num = int(state["pass_num"])
    comparison_count = int(state["comparison_count"])
    swapped = bool(state["swapped"])
    done = bool(state["done"])

    panel_rect = pygame.Rect(20, 20, width - 40, 110)
    pygame.draw.rect(screen, PANEL, panel_rect, border_radius=8)

    title_text = title_font.render("Bubble Sort 2D Visualization", True, TEXT)
    screen.blit(title_text, (32, 30))

    status = "DONE" if done else ("SWAP" if swapped else "COMPARE")
    info_line = (
        f"Pass: {pass_num}   Comparison: {comparison_count}   "
        f"Action: {status}   Delay: {delay_ms}ms"
    )
    controls_line = "Controls: Space pause/resume | Up faster | Down slower | R restart | Esc quit"

    screen.blit(ui_font.render(info_line, True, TEXT), (32, 70))
    screen.blit(ui_font.render(controls_line, True, TEXT), (32, 95))

    if not values:
        empty_text = title_font.render("No values to sort", True, TEXT)
        screen.blit(empty_text, (width // 2 - 110, height // 2))
        pygame.display.flip()
        return

    chart_x = 40
    chart_y = 150
    chart_w = width - 80
    chart_h = height - 190

    max_abs = max((abs(v) for v in values), default=1)
    bar_count = len(values)
    gap = 4
    bar_width = max(6, (chart_w - gap * (bar_count - 1)) // bar_count)
    x = chart_x

    for idx, value in enumerate(values):
        scaled = int((abs(value) / max_abs) * (chart_h - 40)) if max_abs else 0
        bar_height = max(2, scaled)
        y = chart_y + chart_h - bar_height

        color = BAR_NEGATIVE if value < 0 else BAR_DEFAULT
        if idx == left or idx == right:
            color = BAR_SWAP if swapped else BAR_COMPARE

        pygame.draw.rect(screen, color, (x, y, bar_width, bar_height), border_radius=3)

        value_text = ui_font.render(str(value), True, TEXT)
        text_x = x + (bar_width - value_text.get_width()) // 2
        text_y = max(chart_y, y - 18)
        screen.blit(value_text, (text_x, text_y))

        x += bar_width + gap

    paused_text = "PAUSED" if paused else "PLAYING"
    screen.blit(ui_font.render(paused_text, True, TEXT), (width - 110, 30))

    pygame.display.flip()


def run_pygame_visualization(values: List[int], step_delay_ms: int = 120) -> List[int]:
    """Run Bubble Sort animation in a Pygame window and return sorted values."""
    pygame.init()
    pygame.display.set_caption("Bubble Sort - Pygame Visualization")

    screen = pygame.display.set_mode((1100, 680))
    title_font = pygame.font.SysFont("consolas", 28)
    ui_font = pygame.font.SysFont("consolas", 18)

    steps = list(generate_bubble_sort_steps(values))
    delay_ms = max(10, step_delay_ms)

    step_index = 0
    paused = False
    last_step_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_UP:
                    delay_ms = max(10, delay_ms - 20)
                elif event.key == pygame.K_DOWN:
                    delay_ms = min(2000, delay_ms + 20)
                elif event.key == pygame.K_r:
                    step_index = 0
                    paused = False
                    last_step_time = pygame.time.get_ticks()

        now = pygame.time.get_ticks()
        if not paused and step_index < len(steps) - 1 and now - last_step_time >= delay_ms:
            step_index += 1
            last_step_time = now

        _draw_state(screen, title_font, ui_font, steps[step_index], delay_ms, paused)
        clock.tick(60)

    sorted_values = steps[-1]["values"] if steps else values[:]

    pygame.quit()
    return sorted_values
