
                for enemy in enemies:
                    if enemy.is_hit(mouse_pos):
                        enemies.remove(enemy)
                        score += 1
                        break