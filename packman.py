import os, json, cmd, sys
# dependencies - path/package/package_name.json
"""
{
"package_name": "NETCARD",
"dep": ["TCPIP","SOCKET"]
}

"""

class DepMan:

    def list_deps(self, args):
        package_name = args[1]
        path = os.path.join(os.getcwd(), package_name)
        try:
            with open(path, 'r') as conf:
                deps = json.load(conf)
                print(deps["dep"])

        except:
            raise("cannot read config file")

    def add_deps(self, args):
        package = args[0]
        deps = tuple(args[1:])
        print(f"Trying to add dependencies {deps} to {package}")

    def modify_deps(self):
        pass

    def resolve_deps(self, args):
        # identify cases when package is needed and cannot be removed
        pass

class PackMan:
    def __init__(self):
        self.db = "local_db"

    def install(self, args):
        package = args[0]
        if self.already_installed(package):
            print(f"{package} is already installed.")
        else:
            print(f"Installing {package}...")

    def remove(self, args):
        package = args[0]
        print(f"Removing {package}...")

    def list(self):
        print(f"Listing all installed packages...")

    def already_installed(self, pname):
        if pname in self.db:
            return True
        else:
            return False


class CliMan(cmd.Cmd):
    intro = 'Welcome to the PackMan. Type help or ? to list available commands.\n'
    prompt = '(packman): '
    file = None

    def do_LIST(self, arg):
        p = PackMan()
        p.list()

    def do_INSTALL(self, arg):
        p = PackMan()
        p.install(parse(arg))

    def do_REMOVE(self, arg):
        p = PackMan()
        p.remove(parse(arg))

    def do_DEPEND(self, arg):
        p = DepMan()
        p.add_deps(parse(arg))


def parse(arg):
    return arg.split()

if __name__ == '__main__':
    CliMan().cmdloop()
