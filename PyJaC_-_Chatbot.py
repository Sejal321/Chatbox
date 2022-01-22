import random

# ###
# References: Just Google for the movies
# ###


# <editor-fold desc="All long lists and stuff">
comedy = "comedy"
action = "action"
romance = "romance"
rom_com = "rom-com"
thriller = "thriller"
horror = "horror"
adventure = "adventure"
drama = "drama"
documentary = "documentary"
fantasy = "fantasy"
historical_fiction = "historical fiction"
mystery = "mystery"
musical = "musical"
apocalyptic = "apocalyptic"
kids = "kids"
superhero = "superhero"
scifi = "sci-fi"

no = ["no", "No", "Nope", "nope", "n", "N"]
yes = ["yes", "Yes", "yeah", "Yeah", "yep", "Yep", "y", "Y"]

genres = [comedy, action, romance, rom_com, thriller, horror, adventure, drama,
          documentary, fantasy, historical_fiction, mystery, musical,
          apocalyptic, kids, superhero, scifi]

# <editor-fold desc="new releases">
new_releases = {comedy: ["Don't Look Up",
                         "The Lost City",
                         "Free Guy"],
                action: ["Red Notice",
                         "The Matrix: Resurrections",
                         "Infinite"],
                romance: ["Redeeming Love",
                          "After We Fell",
                          "Cyrano"],
                rom_com: ["Happily",
                          "Good on Paper",
                          "Resort to Love"],
                thriller: ["Scream",
                           "Ditched",
                           "The Legend of La Llorona"],
                horror: ["X",
                         "Fear",
                         "Orphan: First Kill"],
                adventure: ["The Lost City",
                            "Jungle Cruise",
                            "Tiger Rising"],
                drama: ["One Night in Miami",
                        "Our Friend",
                        "Music"],
                documentary: ["Seaspiracy",
                              "The Rescue",
                              "Pray Away"],
                fantasy: ["The King's Daughter",
                          "Belle",
                          "Nightbooks"],
                historical_fiction: ["Redeeming Love",
                                     "Delicious",
                                     "Warhunt"],
                mystery: ["Arctic Void",
                          "The Woman in the Window",
                          "Reminiscence"],
                musical: ["In the Heights",
                          "Annette",
                          "tick, tick... BOOM!"],
                apocalyptic: ["Moonfall",
                              "Night Raiders",
                              "Awake"],
                kids: ["Encanto",
                       "Sing 2",
                       "Hotel Transylvania: Transformania"],
                superhero: ["Spider-man: No Way Home",
                            "Thunder Force",
                            "Morbius"],
                scifi: ["Zone 414",
                        "Settlers",
                        "Voyagers"]
                }
# </editor-fold>

# <editor-fold desc="classics">
classics = {comedy: ['Bridesmaids',
                     "What's Up, Doc?",
                     'Airplane'],
            action: ["The Dark Knight",
                     "Inception",
                     "The Matrix"],
            romance: ["City Lights",
                      "Bringing Up Baby",
                      "The Philadelphia Story"],
            rom_com: ["When Harry Met Sally",
                      "You've Got Mail",
                      "Clueless"],
            thriller: ["Scream",
                       "North by Northwest",
                       "Chinatown"],
            horror: ["The Babadook",
                     "Evil Dead 2",
                     "A Nightmare on Elm Street"],
            adventure: ["Black Panther",
                        "Avengers: Endgame",
                        "Mission: Impossible - Fallout"],
            drama: ["One Night in Miami",
                    "Never Rarely Sometimes Always",
                    "Nomadland"],
            documentary: ["Won't You Be My Neighbor?",
                          "Sans Soleil",
                          "Apollo 11"],
            fantasy: ["The Purple Rose of Cairo",
                      "Pan's Labyrinth",
                      "The Thief of Baghdad"],
            historical_fiction: ["Ma Rainey's Black Bottom",
                                 "Schindler's List",
                                 "Just Mercy"],
            mystery: ["Seven",
                      "Bad Times at the El Royale",
                      "Brick"],
            musical: ["Singin' in the Rain",
                      "West Side Story",
                      "The Wizard of Oz"],
            apocalyptic: ["Elysium",
                          "Dark City",
                          "Alphaville"],
            kids: ["The Lion King",
                   "Frozen",
                   "Incredibles 2"],
            superhero: ["The Avengers",
                        "Captain America: Civil War",
                        "The Lego Batman"],
            scifi: ["The One I Love",
                    "Source Code",
                    "The Girl With All the Gifts"]}
# </editor-fold>

film_list = [new_releases, classics]

Random = "R"
Choose = "C"
Select = "S"
A = "A"
New = "N"
Old = "O"

bad_input = ["I'm sorry, I don't understand :(",
             "I said I wouldn't understand ◕︵◕",
             "These characters ... what a mystery!"]
# </editor-fold>


def MMM() -> None:
    """ Use prompt to ask the user for what types of movies they would like to
    see. Ask a series of questions to narrow down a movie the user may enjoy.
    If the user does not like the returned movie, they may choose to restart
    the entire process or simply ask for another movie."""

    bot_name = "MMM"
    print(f"Hi! My name is Matrix the Movie Man (or {bot_name})!")

    meeting = input("\nHave we met before?")
    while meeting not in no and meeting not in yes:
        print("I'm sorry, I don't understand ;-; yes or no only please")
        meeting = input("\nHave we met before?")

    if meeting in no:
        user_name = input("\nWhat's your name?")
        print(f"\nNice to meet you, {user_name} :) I hope I can be"
              " helpful for you today!")

    print("\nIf you mess up at any point, please rerun the file.\n"
          "Please also keep in mind to only respond with the letters in the "
          "parenthesis at the end of the question\n(capitals only ಠ.ಠ)!\n"
          "Otherwise I'll be confused o~o\nLet's start!")

    selection = input("\nWould you like to choose your preferences?"
                      " Or have a random movie picked for you? (C/R)")

    while selection != Random and selection != Choose:
        received = random.choice(bad_input)
        print(f"{received} C or R only please")
        selection = input("\nWould you like to choose your preferences?"
                          " Or have a random movie picked for you? (C/R)")

    if selection == Choose:
        print("\nAwesome, let's see what typa movie you like!")

        time = input("\nDo you wanna see a new movie or an older one? "
                     " Or does you want me to pick for you >u< (N/O)?")

        while time != New and time != Old:
            received = random.choice(bad_input)
            print(f"{received} please only respond with N or O")
            time = input("\nDo you wanna see a new movie or an older one? "
                         " Or does you want me to pick for you >u< (N/O)?")
        if time == New:
            time = new_releases
        else:
            time = classics
        print("\nNoted:)")

        print("\nAs for genres, here's what you can pick from: ")
        print(*[comedy, action, romance, rom_com, thriller, horror,
              adventure, drama, documentary, fantasy, historical_fiction,
              mystery, musical, apocalyptic, kids, superhero, scifi], sep='\n')
        genre_choice = input("\nWould you like to choose your genre?"
                             " Or have a genre picked for you? (C/R)")

        while genre_choice != Choose and genre_choice != Random:
            received = random.choice(bad_input)
            print(f"{received} S or R only please")
            genre_choice = input("\nWould you like to choose your genre?"
                                 " Or have a genre picked for you? (C/R)")

        if genre_choice == Choose:
            genre = input("\nLet me know from the list above :^) "
                          "(please type in your genre exactly as the way it's "
                          "stylized above)")

            genre_not_in_genres = 0
            while genre not in genres:
                if genre_not_in_genres <= 1:
                    genre = input("\nPlease choose one of the genres I listed "
                                  "earlier, and remember to stylize it the same")
                else:
                    genre = input("\n(╯°□°）╯︵ ┻━┻ I said stylize like the "
                                  "list I gave you. plz")
                genre_not_in_genres += 1

        if genre_choice == Random:
            genre = random.choice(genres)
            print(f"\n{genre} has been picked!")

    if selection == Random:
        time = random.choice(film_list)
        if time == new_releases:
            t = "new"
        else:
            t = "classic"
        genre = random.choice(genres)
        print(f"I picked a {t} {genre} movie.")

    movie = random.choice(time[genre])
    print(f"Here's your movie! : {movie}")

    try_again = input("\nWould you like a different movie? (Y/N)")
    while try_again == "Y":
        time = random.choice(film_list)
        if time == new_releases:
            t = "new"
        else:
            t = "classic"
        genre = random.choice(genres)
        movie = random.choice(time[genre])
        print(f"How about '{movie}' ? It is a {t} {genre} movie.")
        try_again = input("\nWould you like a different movie? (Y/N)")

    print("\nThanks for asking me for a movie rec >u<! I hope you like it <3 "
          "Come back and ask again next time!")
