class fake_shell():

    def __init__(self, title, working_directory, terminal_type):
        self.title = title
        self.working_directory = working_directory
        self.command = ""
        self.terminal_type = terminal_type

    def set_title(self, new):
        self.title = new
        return self

    def get_title(self) -> str:
        return self.title

    def set_working_directory(self, new):
        self.working_directory = new
        return self

    def get_working_directory(self) -> str:
        return self.working_directory

    def set_command(self, command):
        self.command = command
        return self

    def append_command(self, command):
        self.command += " ; " + command
        return self

    def make(self) -> str:
        return f"{self.terminal_type}-terminal --working-directory={self.working_directory} -e 'sh -c \"{self.command}\"' -t '{self.title}' --hide-menubar"