from type import *

import random


def main():
    global number_of_Mafia, number_of_Doc
    pygame.init()
    number_of_players = ""

    p = True
    display.blit(pygame.image.load("fon.jpg"), (-150, 0))
    start = Button(130, 30)
    ex = Button(130, 30)
    while p:
        p = start.draw(350, 70, 'Start Game')
        ex.draw(350, 120, "Exit", sys.exit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

    show = True
    press = False
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        number_of_players = int(number_of_players)
                    except ValueError:
                        pass
                    else:
                        show = False
                        if number_of_players > 10 or number_of_players < 5:
                            show = True
                            number_of_players = str(number_of_players)
                elif event.key == pygame.K_BACKSPACE:
                    number_of_players = number_of_players[:-1]
                else:
                    if len(number_of_players) < 5:
                        number_of_players += event.unicode
        display.blit(pygame.image.load("fon.jpg"), (-150, 0))
        print_text("Enter the number of players from 5 to 10:", 50, 130)
        print_text("_____", 485, 132)
        print_text(str(number_of_players), 485, 130)
        pygame.display.update()

    draw_main()
    for i in range(0, number_of_players):
        name = random.choice(name_list)
        player_list.append(
            Player(random.randint(18, 25), name_list.pop(name_list.index(name)), "man", random.randint(1, 50),
                   random.randint(1, 50)))
        display.blit(player_list[i].icon, ((45 + (i * 160) % 800), 140 + 200 * (i // 5)))
        print_text(player_list[i].name + ", " + str(player_list[i].age), (50 + (i * 160) % 800), 120 + 200 * (i // 5))

    p = True
    start = Button(130, 30)
    while p:
        p = start.draw(470, 30, 'Create role')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

    draw_main()
    if number_of_players == 10:
        number_of_Mafia = 3
    elif number_of_players > 7:
        number_of_Mafia = 2
    else:
        number_of_Mafia = 1
    for i in range(0, number_of_players):
        # create game role
        if number_of_Mafia > 0:
            number_of_Mafia -= 1
            item = random.choice(player_list)
            player_list.pop(player_list.index(item))
            player = Mafia(item)
            role.append(player)
            mafia_list.append(player)

        elif number_of_Doc > 0:
            number_of_Doc -= 1
            item = random.choice(player_list)
            player_list.pop(player_list.index(item))
            player = Doctor(item)
            role.append(player)
            doctor_list.append(player)
            peaceful_list.append(player)

        else:
            item = random.choice(player_list)
            player_list.pop(player_list.index(item))
            player = Peaceful_citizen(item)
            role.append(player)
            peaceful_list.append(player)

    random.shuffle(role)
    for i in range(len(role)):
        display.blit(role[i].icon, ((45 + (i * 160) % 800), 140 + 200 * (i // 5)))
        print_text(role[i].name + ", " + "0", (50 + (i * 160) % 800), 120 + 200 * (i // 5), font_color=(165, 42, 42))

    # order at night
    # mb night butterfly
    # Mafia
    # mb police
    # mb killer
    # Doctor

    # create player

    day = 1
    play = True
    d = Button(130, 30)
    n = Button(130, 30)
    start = Button(130, 30)
    while play:
        # night
        print_text("Day - " + str(day), 290, 20)
        p = True
        while p:
            p = start.draw(470, 30, 'Night')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

        draw_main()
        for i in range(len(role)):
            display.blit(role[i].icon, ((45 + (i * 160) % 800), 140 + 200 * (i // 5)))
            print_text(role[i].name + ", " + "0", (50 + (i * 160) % 800), 120 + 200 * (i // 5),
                       font_color=(165, 42, 42))
        print_text("The city is falling asleep", 90, 40)
        print_text("Night " + str(day), 200, 60)
        pygame.display.update()
        Saimon.maf_target(choose_in_night(mafia_list, peaceful_list))

        delay = 0
        while delay < 500:
            delay += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.time.delay(10)

        draw_main()
        for i in range(len(role)):
            display.blit(role[i].icon, ((45 + (i * 160) % 800), 140 + 200 * (i // 5)))
            print_text(role[i].name + ", " + "0", (50 + (i * 160) % 800), 120 + 200 * (i // 5),
                       font_color=(165, 42, 42))

        print_text("Day - " + str(day), 290, 20)
        print_text("Night " + str(day), 200, 60)

        if len(doctor_list) == 1:
            print("Saimon says: 'Doctor makes a choice' ")
            Saimon.doctor_target(choose_in_night(doctor_list, role))
            print("Saimon says: 'Doctor has made a choice' ")
        pygame.display.update()
        delay = 0
        while delay < 500:
            delay += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.time.delay(10)

        draw_main()
        for i in range(len(role)):
            display.blit(role[i].icon, ((45 + (i * 160) % 800), 140 + 200 * (i // 5)))
            print_text(role[i].name + ", " + "0", (50 + (i * 160) % 800), 120 + 200 * (i // 5),
                       font_color=(165, 42, 42))

        print_text("Day - " + str(day), 290, 20)
        print_text("Night " + str(day), 200, 60)
        print_text("Results of the nights", 170, 560)
        print_text(Saimon.results_night(), 170, 580)
        check_life()
        pygame.display.update()

        delay = 0
        while delay < 500:
            delay += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.time.delay(10)

        if len(mafia_list) < 1:
            play = False
            win = "Peaceful citizen win this game. Day - " + str(day)
            pygame.display.update()
            break
        if len(peaceful_list) < 1:
            play = False
            win = "Mafia win this game. Day - " + str(day)
            pygame.display.update()
            break
        # day

        p = True
        while p:
            p = start.draw(470, 30, 'Day')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
        draw_main()

        for i in range(len(role)):
            display.blit(role[i].icon, ((45 + (i * 160) % 800), 140 + 200 * (i // 5)))
            print_text(role[i].name + ", " + "0", (50 + (i * 160) % 800), 120 + 200 * (i // 5),
                       font_color=(165, 42, 42))
        print_text("The city is waking up", 90, 40)
        print_text("Day - " + str(day), 290, 20)
        print_text("Day " + str(day), 200, 60)
        print_text("Daily voting for the exclusion of a player", 170, 540)
        pygame.display.update()
        delay = 0
        while delay < 200:
            delay += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.time.delay(10)

        if len(role) > 1 + len(mafia_list):
            Saimon.kick(votekick(role, day))
            pygame.display.update()
            check_life()
            delay = 0
            while delay < 200:
                delay += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.time.delay(10)

        if len(mafia_list) < 1:
            play = False
            win = "Peaceful citizen win this game. Day - " + str(day)
            pygame.display.update()
            break

        if len(peaceful_list) < 1:
            play = False
            win = "Mafia win this game. Day - " + str(day)
            pygame.display.update()
            break

        p = True
        while p:
            p = start.draw(470, 30, 'Next Day')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

        day += 1
        draw_main()
        for i in range(len(role)):
            display.blit(role[i].icon, ((45 + (i * 160) % 800), 140 + 200 * (i // 5)))
            print_text(role[i].name + ", " + "0", (50 + (i * 160) % 800), 120 + 200 * (i // 5),
                       font_color=(165, 42, 42))

        print_text("Day - " + str(day), 290, 20)
        print_text("Night " + str(day), 200, 60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
    for item in role:
        player_list.append(role.pop(role.index(item)))
    draw_main()
    for i in range(len(player_list)):
        display.blit(player_list[i].icon, ((45 + (i * 160) % 800), 140 + 200 * (i // 5)))
        print_text(player_list[i].name + ", " + "age", (50 + (i * 160) % 800), 120 + 200 * (i // 5),
                   font_color=(165, 42, 42))
        if player_list[i].life:
            print_text("Life- alive", (30 + (i) * 160) % 800,
                       120 + 100 + 200 * (i // 5))
        else:
            print_text("Life- dead", (30 + (i) * 160) % 800,
                       120 + 100 + 200 * (i // 5))
        print_text("Role-" + str(player_list[i].surname), (30 + (i) * 160) % 800,
                   120 + 100 + 20 + 200 * (i // 5))
    print_text(win, 170, 560)
    pygame.display.update()
    delay = 0
    while delay < 1500:
        delay += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.delay(10)
    pygame.time.delay(5000)


if __name__ == "__main__":
    main()
