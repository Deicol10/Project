from Class import *



clock = pygame.time.Clock()
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Mafia Model")
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)

Saimon = Leader()
display.blit(pygame.image.load("fon.jpg"), (-150, 0))


def print_text(message, x, y, font_color=(224, 255, 255), font_type='NeutralFace.otf', font_size=17):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


def draw_main():
    display.blit(pygame.image.load("fon.jpg"), (-150, 0))
    display.blit(Saimon.icon, (display_width / 2 - 40, Saimon.y))


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (105, 105, 105)
        self.active_color = (23, 204, 58)

    def draw(self, x, y, message, action=None, size=17):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_color, (x, y, self.width, self.height))
            print_text(message, x + 5, y + 5, font_size=size)
            if click[0] == True:
                pygame.time.delay(300)
                if action is not None:
                    action()
                return False

        else:
            pygame.draw.rect(display, self.inactive_color, (x, y, self.width, self.height))
            print_text(message, x + 5, y + 5, font_size=size)

        return True


def choose_in_night(killer, victim):
    target_list = []
    max_roll = -1
    roll = []
    flag = False

    # create targe_list
    for i in range(len(killer)):
        target_list.append(random.choice(victim))
        print_text("Target-" + str(target_list[i].name), (30 + (role.index(killer[i]) * 160) % 800),
                   120 + 100 + 200 * (role.index(killer[i]) // 5))
    pygame.display.update()
    delay = 0
    while delay < 100:
        delay += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.delay(10)
    # checking for identical targets

    for item in target_list:
        if target_list.count(item) >= 2:
            target = item
            flag = True

    # if not identical targets than check high ROLL
    if not flag:
        if len(killer) > 1:
            for i in range(len(killer)):
                r = killer[i].roll()
                print_text("Roll D12- " + str(r), (30 + (role.index(killer[i]) * 160) % 800),
                           120 + 100 + 20 + 200 * (role.index(killer[i]) // 5))
                # print(i, r)
                if max_roll <= r:
                    max_roll = r
                    save = i
                elif max_roll == r:
                    a = max_roll
                    b = r
                    while a == b:
                        a = killer[save].roll()
                        b = killer[i].roll()

                    if a > b:
                        save = save
                        print_text("MAX Roll D12- " + str(r), (30 + (role.index(killer[i]) * 160) % 800),
                                   120 + 100 + 40 + 200 * (role.index(killer[i]) // 5))
                        print_text("MAX Roll D12- " + str(r), (30 + (role.index(killer[i]) * 160) % 800),
                                   120 + 100 + 40 + 200 * (role.index(killer[i]) // 5))
                    elif a < b:
                        save = i
                        print_text("MAX Roll D12- " + str(r), (30 + (role.index(killer[i]) * 160) % 800),
                                   120 + 100 + 40 + 200 * (role.index(killer[i]) // 5))
                        print_text("MAX Roll D12- " + str(r), (30 + (role.index(killer[i]) * 160) % 800),
                                   120 + 100 + 40 + 200 * (role.index(killer[i]) // 5))
            target = target_list[save]
        else:
            target = target_list[0]
    pygame.display.update()

    delay = 0
    while delay < 150:
        delay += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.delay(10)

    print_text("Target of the night for " + killer[0].surname + " - " + str(target.name), 170, 560)
    pygame.display.update()

    return target


def check_life():
    for item in role:
        item.choice = 0
        if item.life == False:
            player_list.append(role.pop(role.index(item)))
    for item in mafia_list:
        if item.life == False:
            mafia_list.pop(mafia_list.index(item))
    for item in doctor_list:
        if item.life == False:
            doctor_list.pop(doctor_list.index(item))
    for item in peaceful_list:
        if item.life == False:
            peaceful_list.pop(peaceful_list.index(item))


def votekick(role, day):
    choice_list = {}
    vote_list = []
    for item in role:
        choice_list[item] = 0
    i = -1
    for item in role:
        i += 1
        choice_value = item.choose(len(role))
        # choose person to kick, mafia don't vote vs himself
        if item.surname == "Mafia":
            while role[choice_value].surname == "Mafia" or item == role[choice_value]:
                choice_value = item.choose(len(role))
        if item.surname == "Doctor":
            while item == role[choice_value]:
                choice_value = item.choose(len(role))
        if item.surname == "Citizen":
            while item == role[choice_value]:
                choice_value = item.choose(len(role))
        choice_list[role[choice_value]] += 1
        print_text("Vote - " + str(role[choice_value].name), (30 + i * 160) % 800,
                   120 + 100 + 200 * (i // 5))
        pygame.display.update()

    delay = 0
    while delay < 200:
        delay += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.delay(10)
    draw_main()
    for j in range(len(role)):
        display.blit(role[j].icon, ((45 + (j * 160) % 800), 140 + 200 * (j // 5)))

    print_text("The city is waking up", 90, 40)
    print_text("Day - " + str(day), 290, 20)
    print_text("Day " + str(day), 200, 60)
    print_text("Daily voting for the exclusion of a player", 170, 540)
    pygame.display.update()

    i = -1
    for key in choice_list:
        i += 1
        print_text(key.name + ", " + str(choice_list[key]), (50 + (i * 160) % 800), 120 + 200 * (i // 5),
                   font_color=(165, 42, 42))
    pygame.display.update()
    delay = 0
    while delay < 50:
        delay += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.delay(10)

    max_vote = 0
    counter = 0
    for key in choice_list:
        if choice_list[key] > max_vote:
            max_vote = choice_list[key]
            counter = 0
            counter += 1
        elif choice_list[key] == max_vote:
            counter += 1

    # if vote >=3 victim than skip
    if counter >= 3:
        print_text("The vote decided nothing", 170, 580)
        pygame.display.update()

        return 0
    # if vote = 2, choose 1 victim
    elif counter == 2:
        delay = 0
        while delay < 200:
            delay += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.time.delay(10)
        draw_main()
        for j in range(len(role)):
            display.blit(role[j].icon, ((45 + (j * 160) % 800), 140 + 200 * (j // 5)))
            print_text(role[i].name + ", " + "0", (50 + (i * 160) % 800), 120 + 200 * (i // 5),
                       font_color=(165, 42, 42))
        print_text("The city is waking up", 90, 40)
        print_text("Day - " + str(day), 290, 20)
        print_text("Day " + str(day), 200, 60)
        print_text("A vote of two", 170, 540)

        for key in choice_list:
            if max_vote == choice_list[key]:
                vote_list.append(key)

        a = vote_list[0].roll()
        b = vote_list[1].roll()

        while a == b:
            a = vote_list[0].roll()
            b = vote_list[1].roll()

        delay = 0
        while delay < 200:
            delay += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.time.delay(10)
        draw_main()
        for j in range(len(role)):
            display.blit(role[j].icon, ((45 + (j * 160) % 800), 140 + 200 * (j // 5)))
        print_text("The city is waking up", 90, 40)
        print_text("Day - " + str(day), 290, 20)
        print_text("Day " + str(day), 200, 60)
        print_text("A vote of two", 170, 540)

        choice_list_res = {}
        choice_list_res[vote_list[0]] = 1
        choice_list_res[vote_list[1]] = 1
        for item in role:
            if item == vote_list[0]:
                continue
            elif item == vote_list[1]:
                continue
            else:
                x = item.D20()
                # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
                if a > b:
                    print_text("I don't Mafia ", (30 + (role.index(vote_list[0]) * 160) % 800),
                               120 + 100 + 200 * (role.index(vote_list[0]) // 5))
                    # highest chance kick #2
                    if x > 8:
                        choice_list_res[vote_list[1]] += 1
                    elif x <= 8:
                        choice_list_res[vote_list[0]] += 1
                elif a < b:
                    # highest chance kick #1
                    print_text("I don't Mafia ", (30 + (role.index(vote_list[1]) * 160) % 800),
                               120 + 100 + 200 * (role.index(vote_list[1]) // 5))
                    if x > 8:
                        choice_list_res[vote_list[0]] += 1
                    elif x <= 8:
                        choice_list_res[vote_list[1]] += 1
        for i in range(len(role)):
            if vote_list[1] != role[i] and vote_list[0] != role[i]:
                print_text(str(role[i].name) + ", " + "0", (50 + (i * 160) % 800), 120 + 200 * (i // 5),
                           font_color=(165, 42, 42))
            else:
                print_text(str(role[i].name) + ", " + str(choice_list_res[role[i]]), (50 + (i * 160) % 800),
                           120 + 200 * (i // 5),
                           font_color=(165, 42, 42))
        pygame.display.update()


        max_vote = 0
        counter = 0
        for key in choice_list_res:

            if max_vote < choice_list_res[key]:
                max_vote = choice_list_res[key]
                counter = 0
                counter += 1
                kicked = key

            elif max_vote == choice_list_res[key]:

                counter += 1


        if counter == 1:
            print_text(str(key.name) + " was kicked", 170, 560)
            print_text(str(key.name) + " - " + str(key.surname), 170, 580)
            return key
        elif counter == 2:
            print_text("The vote decided nothing", 170, 580)

            return 0
        # if vote for 1 kick him
    elif counter == 1:
        for key in choice_list:
            if max_vote == choice_list[key]:
                # print("was kicked")
                print_text(str(key.name) + " was kicked", 170, 560)
                print_text(str(key.name) + " - " + str(key.surname), 170, 580)
                pygame.display.update()

                return key
