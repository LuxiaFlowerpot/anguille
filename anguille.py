import os
import random
import re

import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='/')

# connection


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="câliner des anguilles"))

# commandes basiques


@bot.command(description="Dis coucou au gentil robot!",
                brief="Politesse avant tout!",
                pass_context=True)
async def hello(context):
    possible_responses = [
        "おはよう",
        "Hello",
        "Non. ",
    ]
    await bot.say(random.choice(possible_responses) + context.message.author.mention)


@bot.command(description="Je te le dis, tu vas le regretter, ne fais pas ça.",
                brief="Ne fais pas ça.")
async def non():
    videos_infernales = [
        "https://www.youtube.com/watch?v=juqyzgnbspY",
        "https://www.youtube.com/watch?v=InQC3MvDZM4",
    ]
    await bot.say("Tu l'auras voulu :) " + random.choice(videos_infernales))


# Descriptions des admins

@bot.command(name="Silonix",
                description="Permet d'obtenir des informations sur notre très cher Silonix.",
                brief="Détails sur Silonix")
async def silonix():
    await bot.say("Fondateur de Elydra et ancien administrateur de Malm, Silonix est un loriste investi, "
                     "un MJ démoniaque, mais aussi une personne fort sympathique, malgré les airs un peu hautains "
                     "qu'il se donne par moments. Il est responsable des Wizel, et adore les anguilles. :)")


@bot.command(name="Styx",
                description="Permet d'obtendir des informations sur notre très cher Styx.",
                brief="Détails sur Styx")
async def styx():
    await bot.say("Fondateur de Elydra et ancien fondateur de Malm, Styx est un loriste sérieux, un MJ assidu, "
                     "mais aussi une personne fort sympathique, malgré les airs un peu froids et distants qu'il se "
                     "donne par moments. Il est responsable des Widriens, et adore les cailloux. :)")


@bot.command(name="Luxia",
                description="Permet d'obtenir des informations sur notre très chère Luxia.",
                brief="Détails sur Luxia")
async def luxia():
    await bot.say("Fondatrice de Elydra et ancienne fondatrice de Malm, Luxia est une loriste désastreuse, une MJ "
                     "catastrophique, mais aussi une personne fort sympathique [parfois], malgré les airs un peu "
                     "excentriques [de psychopathe] qu'elle se donne par moments. Elle n'est responsable de rien"
                     " [trop dangereux], mais surveille le règlement, ce bot et les parties de Cards Against "
                     "Humanity. Elle sert aussi de psychologue à ses heures perdues, et adore les pots de fleurs "
                     "et les tomates. Personne n'est certain qu'elle soit réellement de sexe féminin.")


# commandes citation règlement


@bot.command(name="règle1",
                description="Cite la règle 1",
                brief="Cite la règle 1")
async def rule1():
    await bot.say("**Tous propos insultants, rabaissants, diffamatoires, racistes, homophobes, discriminants à "
                     "l’encontre de qui que ce soit sont formellement interdits.** Même à titre humoristiques.")


@bot.command(name="règle2",
                description="Cite la règle 2",
                brief="Cite la règle 2")
async def rule2():
    await bot.say("**Le spam, le contenu à caractère pornographique ou NSFW, ainsi que les publicités pour d’autres"
                     " serveurs sont prohibés.** Vous n’aurez qu’à faire tout ce qui concerne ce qui vient d’être "
                     "énoncé en privé.")


@bot.command(name="règle3",
                description="Cite la règle 3",
                brief="Cite la règle 3")
async def rule3():
    await bot.say("**Les personnages de RP doivent être équilibrés, mortels, pas intouchables, respecter les meurs "
                     "et les règles des clans auxquels ils appartiennent.** Pour que le jeu soit agréable pour chacun, "
                     "chaque personnage doit rester dans un champ “possible” et raisonnable par rapport au lore.")


@bot.command(name="règle4",
                description="Cite la règle 4",
                brief="Cite la règle 4")
async def rule4():
    await bot.say("**En rp, les actions d’un personnage doivent être logiques, plausibles et cohérentes avec l’"
                     "univers.** De sorte à garder une ambiance agréable pour ceux qui jouent avec vous. **En cas de "
                     "besoin, n’hésitez pas à utiliser les dés pour déterminer l’issue d’une action résultant de la "
                     "chance.**")


@bot.command(name="règle5",
                description="Cite la règle 5",
                brief="Cite la règle 5")
async def rule5():
    await bot.say("**En rp, il est interdit de jouer le personnage d’un autre à sa place** (à moins que celui-ci en "
                     "ait donné l’autorisation). Vous ne faites agir que votre propre personnage.")


@bot.command(name="règle6",
                description="Cite la règle 6",
                brief="Cite la règle 6")
async def rule6():
    await bot.say("**Votre pseudo devra être le prénom accompagné, si vous le désirez, du nom de votre personnage.**"
                     " Pour rappel, vous pouvez changer votre surnom sur ce serveur en appuyant sur le bouton “Eydra” "
                     "puis “Changer de pseudo”. De plus, **il est obligatoire de remplir sa fiche entièrement selon le "
                     "modèle épinglé dans #présentations pour pouvoir être validé.**")


@bot.command(name="règle7",
                description="Cite la règle 7",
                brief="Cite la règle 7")
async def rule7():
    await bot.say("**Il est interdit de tuer le personnage de quelqu’un d’autre.** Cependant, il est quand même "
                     "possible de mourir, durant des évent ou encore si vous repoussez trop les limites de votre "
                     "personnage, suite à une décision du staff, accompagnée de l’action de MJs.")


@bot.command(name="règle8",
                description="Cite la règle 8",
                brief="Cite la règle 8")
async def rule8():
    await bot.say("**Les messages HRP entre parenthèses sont autorisés dans le RP** mais doivent rester "
                     "exceptionnels et être supprimés après coup. De plus, **il est interdit d’utiliser un langage "
                     "abrégé ou des smileys dans le rp.** Essayez de conserver une orthographe correcte, et démarquez "
                     "les paroles des actions de votre personnage en mettant par exemple les paroles entre guillemets, "
                     "et le reste en Italique. (Rappel, vous pouvez mettre un texte en Italique en mettant des étoiles "
                     "ou des underscores au début et à la fin de votre texte, ``*comme ceci*`` ou ``_comme cela_``.)")


@bot.command(name="règle9",
                description="Cite la règle 9",
                brief="Cite la règle 9")
async def rule9():
    await bot.say("Enfin, **vous êtes autorisés à avoir autant de comptes que vous le souhaitez**, pour autant que "
                     "vous fassiez de votre mieux pour les garder actifs un minimum. Refondre ses personnages est aussi"
                     " possible sans conditions.")

# lancers de dés


@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await bot.send_message(ctx.message.channel, "Utilisation: `.r #d#` e.g. `.r 1d20`\nUtilise .help pour plus "
                                                    "d'informations.")


@bot.command(description="Lance un dé utilisant le format #d#.\nExemple = /r 3d6",
             brief="Permet de lancer un ou des dés",
             pass_context=True)
async def r(ctx, roll: str):

    resultTotal = 0
    resultString = ''
    try:
        try:
            numDice = roll.split('d')[0]
            diceVal = roll.split('d')[1]
        except Exception as e:
            print(e)
            await bot.say("La commande doit être au format #d# %s." % ctx.message.author.name)
            return

        if int(numDice) > 500:
            await bot.say("Je ne peux pas lancer autant de dés %s." % ctx.message.author.name)
            return

        bot.type()
        await bot.say("En train de rouler %s d%s pour %s" % (numDice, diceVal, ctx.message.author.mention))
        rolls, limit = map(int, roll.split('d'))

        for r in range(rolls):
            number = random.randint(1, limit)
            resultTotal = resultTotal + number

            if resultString == '':
                resultString += str(number)
            else:
                resultString += ', ' + str(number)

        if numDice == '1':
            await bot.say("Dé de " + ctx.message.author.mention + "  :game_die: . . . \n**Résultat:** " + resultString)
        else:
            await bot.say(
                "Dé de " + ctx.message.author.mention + "  :game_die: . . . \n**Résultat:** " + resultString +
                "\n**Total:** " + str(resultTotal))

    except Exception as e:
        print(e)
        return


@bot.command(description="Lance un dé utilisant le format #d#s# , où s est un comparateur de réussite ( < , > ou = ).\n"
                         "Exemple = /rt 3d10<15 (Le jet sera réussi si le résultat est inférieur à 15.",
             brief="Permet de jeter un ou des dés avec un comparateur",
             pass_context=True)
async def rt(ctx, roll: str):

    numberSuccesses = 0
    resultString = ''

    try:
        valueList = re.split("(\d+)", roll)
        valueList = list(filter(None, valueList))

        diceCount = int(valueList[0])
        diceValue = int(valueList[2])
        thresholdSign = valueList[3]
        successThreshold = int(valueList[4])

    except Exception as e:
        print(e)
        await bot.say("La commande doit être au format #d#t# %s." % ctx.message.author.mention)
        return

    if int(diceCount) > 500:
        await bot.say("Je ne peux pas lancer autant de dés %s." % ctx.message.author.mention)
        return

    bot.type()
    await bot.say("En train de rouler %s d%s pour %s avec une réussite %s %s" % (
        diceCount, diceValue, ctx.message.author.name, thresholdSign, successThreshold))

    try:
        for r in range(0, diceCount):

            number = random.randint(1, diceValue)
            isRollSuccess = False

            if thresholdSign == '<':
                if number < successThreshold:
                    numberSuccesses += 1
                    isRollSuccess = True

            elif thresholdSign == '=':
                if number == successThreshold:
                    numberSuccesses += 1
                    isRollSuccess = True

            else:  # >
                if number > successThreshold:
                    numberSuccesses += 1
                    isRollSuccess = True

            if resultString == '':
                if isRollSuccess:
                    resultString += '**' + str(number) + '**'
                else:
                    resultString += str(number)
            else:
                if isRollSuccess:
                    resultString += ', ' + '**' + str(number) + '**'
                else:
                    resultString += ', ' + str(number)

            isRollSuccess = False

        if diceCount == 1:
            if numberSuccesses == 0:
                await bot.say(
                    "Dé de " + ctx.message.author.mention + "  :game_die: . . .\n**Résultat:** " + resultString +
                    "\n**Réussite:** :x:")
            else:
                await bot.say(
                    "Dé de " + ctx.message.author.mention + "  :game_die: . . .\n**Résultat:** " + resultString +
                    "\n**Réussite:** :white_check_mark:")
        else:
            await bot.say(
                "Dé de " + ctx.message.author.mention + "  :game_die: . . . \n**Résultat:** " + resultString +
                "\n**Réussite:** " + str(numberSuccesses))
    except Exception as e:
        print(e)
        return
    
# message d'arrivée
    
@bot.event
async def on_member_join(channel, member):
    await bot.send_message(channel, "Bonjour et bienvenue " + member.name)

    role = discord.utils.get(member.server.roles, name="Non validé")
    await bot.add_roles(member, role)

bot.run(os.getenv('TOKEN'))
