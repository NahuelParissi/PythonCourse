chosen_pokemon = input("¿Contra qué Pokemon quieres combatir? (Squirtle / Charmander / Bulbasur): ").upper();

pikachu_hp = 100;
enemy_hp = 0;
enemy_attack = 0;

if(chosen_pokemon == "SQUIRTLE"):
    enemy_hp = 90;
    enemy_name = "Squirtle";
    enemy_attack = 8;
elif(chosen_pokemon == "CHARMANDER"):
    enemy_hp = 80;
    enemy_name = "Charmander";
    enemy_attack = 7;
elif(chosen_pokemon == "BULBASUR"):
    enemy_hp = 100;
    enemy_name = "Bulbasur";
    enemy_attack = 10;

while(pikachu_hp > 0 and enemy_hp > 0):
    chosen_attack = input("¿Qué ataque vamos a usar? (Chispazo / Bola voltio): ").upper();
    if(chosen_attack == "CHISPAZO"):
        print("Pikachu usó Chispazo, le hace 10 puntos de daño al enemigo.");
        enemy_hp -= 10;
    elif(chosen_attack == "BOLA VOLTIO"):
        print("Pikachu usó Bola voltio, le hace 12 puntos de daño al enemigo.");
        enemy_hp -= 12;

    print("La vida del {} ahora es de {}".format(enemy_name, enemy_hp));

    print("{} te hace un ataque de {} puntos de daño").format(enemy_name, enemy_attack);
    pikachu_hp -= enemy_attack;

    print("La vida del Pikachu ahora es de {}".format(pikachu_hp));

    if(enemy_hp <= 0):
        print("¡Has ganado el combate!");
    elif(pikachu_hp <= 0):
        print("¡Has perdido el combate!");

print("El combate ha terminado.");