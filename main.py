import os
from bot import Bot


def main():
    try:
        f = open('token.txt', 'x')
        f.close()
        print('Created token.txt')
    except FileExistsError:
        pass

    try:
        f = open('sheets.json', 'x')
        f.close()
        print('Created sheets.json')
    except FileExistsError:
        pass

    with open('token.txt', 'r') as f:
        token = f.readline().strip()
    
    if not token:
        token = input("Paste token here: ")
        with open('token.txt', 'w') as f:
            f.write(token)
            f.close()

    bot = Bot()
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = f"cogs.{file[0:-3]}"

            try:
                bot.load_extension(extension)
                print(f"Loaded {extension}")
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(token)

if __name__ == "__main__":
    main()