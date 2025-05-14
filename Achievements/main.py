from visual import*
import json as j

language_id= 1
run= True
is_logged= False
#Le o dicionario de linguagem
with open("assets/languages.json", "r") as f:
    language_dict= j.loads(f.read())

with open("assets/user.json", "r") as f:
    user_data= j.loads(f.read())

mostrar_conquista(language_dict[0][f"{language_id}"],
    f"{language_dict[1][f"{language_id}"]} {user_data[0]["name"]}")

while run:
    try:
        with open("assets/achievements.json", "r") as f:
            trophy_lists= j.loads(f.read())
        indexa= -1
        for trophy in trophy_lists[1]:
            indexa= indexa+ 1
            trophy= trophy_lists[1][f'{indexa}']
            if trophy['unlocked']== 0 and trophy['has_popup']== 1:
                trophy['has_popup']= 0
                with open("assets/achievements.json","w") as f:
                    f.write(j.dumps(trophy_lists, indent=4))
            if trophy['unlocked']== 1 and trophy['has_popup']== 0:
                mostrar_conquista(trophy['title'], trophy['description'], "🏆")
                trophy['has_popup']= 1
                with open("assets/achievements.json","w") as f:
                    f.write(j.dumps(trophy_lists, indent=4))
    except Exception as e:
        mostrar_conquista(language_dict[2][f"{language_id}"], e)