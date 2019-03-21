import sys
try:
    from pick import pick
except ImportError:
    raise Exception("pick could not be installed. Please run `pip3 install pick` to install")


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def printC(text, colour=HEADER):
    text = str(text)
    print(colour + text + ENDC)


def question(prompt):
    printC(prompt, OKGREEN)
    return input("")


def build_cli(title, options, function_list, **kwargs):
    """
    Builds a cli for input
    :param title: The title of the CLI
    :param options: A list of string options to select from
    :param function_list: A list of functions of equal size to options list
    :return: TBD
    """
    options.append("{:30}| Quit the program".format("Quit"))
    while True:
        option, index = pick(options, title)

        if index == len(options) - 1:
            sys.exit(0)
        function_list[index](**kwargs)
        input("hit Enter key to continue")
