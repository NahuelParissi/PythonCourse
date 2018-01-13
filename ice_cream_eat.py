fancy_ice_cream_input = input("¿Te apetece un helado? (Si / No): ").upper();

if(fancy_ice_cream_input == "SI"):
    fancy_ice_cream = True;
elif(fancy_ice_cream_input == "NO"):
    fancy_ice_cream = False;
else:
    print("Te he dicho que me digas si o no, no sé que has dicho, pero cuento como que no.");
    fancy_ice_cream = False;

have_money_input = input("¿Tienes dinero para un helado? (Si / No): ").upper();
is_ice_cream_maker_man_input = input("¿Está el señor de los helados? (Si / No)").upper();
is_your_aunt_input = input("¿Estás con tu tía? (Si / No)").upper();

fancy_ice_cream = fancy_ice_cream_input == "SI";
have_money = have_money_input == "SI";
is_your_aunt = is_your_aunt_input == "SI";
can_afford_it = have_money or is_your_aunt;
is_ice_cream_maker_man = is_ice_cream_maker_man_input == "SI";

if(fancy_ice_cream and can_afford_it and is_ice_cream_maker_man):
    print("Pues cómete un helado.");
else:
    print("Pues nada.");