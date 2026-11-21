def main():
    #приветствие
		print('Hello, user. Here''s the rules: you have 3 attempts afore defeat. Choose wisely and destroy the enemy. Your units: grunt Rock, sergeunt Scissors and captain Papper')
    #юзеры
		first_combatmant = input('Choose the first challenger. Thine name is: ')
		second_combatmant = input('Choose the second challenger. Thine name is: ')
    print('To choose grunt Rock agaisnt the enemy, type 1. For Scissors and Papper type 2 and 3 respectively.')
    #каунтеры очков для победы
		score_first = 0
    score_second = 0
		#цикл проходится по трем попыткам для выяснения победителя
    for i in range(3):
        first_gesture = input()
        second_gesture = input()
        if first_gesture == 1:
            if second_gesture == 2:
                score_first += 1
            elif second_combatmant == 3:
                score_second += 1
        #Задавание условий победы через if

if __name__ == "__main__":
    main()