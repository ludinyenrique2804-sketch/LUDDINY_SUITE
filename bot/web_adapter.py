import builtins
import io
import sys
from bot import start_bot

def run_command(command, extra_inputs=None):
    """
    Ejecuta UN comando del bot y devuelve la salida.
    extra_inputs: lista de respuestas para input() adicionales
    """
    if extra_inputs is None:
        extra_inputs = []

    inputs = [command] + extra_inputs + ["exit"]
    input_iter = iter(inputs)

    original_input = builtins.input
    original_stdout = sys.stdout

    sys.stdout = buffer = io.StringIO()

    def fake_input(prompt=""):
        try:
            return next(input_iter)
        except StopIteration:
            return "exit"

    builtins.input = fake_input

    try:
        start_bot()
    except SystemExit:
        pass
    finally:
        builtins.input = original_input
        sys.stdout = original_stdout

    return buffer.getvalue()

