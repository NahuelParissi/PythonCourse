number_to_guess = 13;
user_number = int(input("Dime tu numero: "));

if(number_to_guess == user_number):
    print("Has ganado. Y al primer intento, eres un fiera.");
else:
    user_number = int(input("Dime tu numero: "));
    if(number_to_guess == user_number):
        print("Has ganado. En el segundo intento, muy bien.");
    else:
        user_number = int(input("Dime tu numero: "));
        if (number_to_guess == user_number):
            print("Has ganado. En el tercer intento, bien hecho.");
        else:
            user_number = int(input("Dime tu numero: "));
            if (number_to_guess == user_number):
                print("Has ganado. En el cuarto intento, necesitas mejorar.");
            else:
                user_number = int(input("Dime tu numero: "));
                if (number_to_guess == user_number):
                    print("Has ganado. En el quinto y último intento, por poco no lo cuentas.");
                else:
                    print("Has agotado todos los intentos, perdistes. Suerte la próxima vez.");