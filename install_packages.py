import os
# run file for install package


def install() -> None:
    """
    for install package
    :return:
    None
    """
    os.system("pip install customtkinter==5.1.0")
    os.system("pip install pillow")


if __name__ == "__main__":
    install()