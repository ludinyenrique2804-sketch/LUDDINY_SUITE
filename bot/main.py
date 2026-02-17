import sys
from bot.bot import start_bot


if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_bot(sys.argv[1])  # recibe argumento desde consola
    else:
        start_bot()


