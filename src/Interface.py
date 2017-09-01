import readline

class Interface:
    def __init__(self, default, options):
        self.completer = AutoCompleter(options)
        self.default = default
        readline.set_completer(self.completer.complete)
        readline.parse_and_bind('tab: complete')

    def getInput(self, prompt=None):
        if (prompt == None):
            prompt = self.default 
        userInput = input(prompt)
        return userInput.lower()
        
    def getCommand(self, userInput):
        if (userInput == ""):
            return None, None
        tokens = userInput.split()
        map(lambda x: x.lower(), tokens)
        return tokens[0], " ".join(tokens[1:])

    def output(self, output=""):
        print(output)

class AutoCompleter(object):
    def __init__(self, options):
        self.options = options
        self.currentCandidates = []

    def complete(self, text, state):
        response = None
        candidates = None
        isTypingCommand = False

        if (state == 0):
            origline = readline.get_line_buffer()
            origline = origline.lower()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            being_completed = origline[begin:end]
            words = origline.split()

            if (not words):
                self.current_candidates = sorted(self.options.keys())
            else:
                try:
                    if (begin == 0):
                        candidates = self.options.keys()
                        isTypingCommand = True
                    else:
                        first = words[0]
                        candidates = self.options[first].options()

                    if being_completed:
                        self.current_candidates = [w for w in candidates
                                                   if w.startswith(being_completed)]
                    else:
                        self.current_candidates = candidates
                except (KeyError, IndexError):
                    self.current_candidates = []
            if (isTypingCommand or len(self.current_candidates) == 1):
                response = self.current_candidates[state]
            else:
                response = None
        return response
