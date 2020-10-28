import re

from src.ProgramInternalForm import ProgramInternalForm
from src.SymbolTable import SymbolTable


class Scanner:
    def __init__(self, reserved_words, operators, separators):
        self.__symbol_table = SymbolTable(10)
        self.__pif = ProgramInternalForm()
        self.__reserved_words = reserved_words
        self.__operators = operators
        self.__separators = separators

    def check_identifier(self, identifier) -> bool:
        return re.match('[a-zA-Z][a-zA-Z0-9]{0,}', identifier) is not None

    def check_constant(self, constant) -> bool:
        if constant == 'true':
            return True
        if constant == 'false':
            return False
        if re.match('[0-9a-zA-Z]', constant) is not None:
            return True
        if re.match('[a-zA-Z]{0,}', constant) is not None:
            return True
        if re.match('[+-]?[1-9][0-9]{0,}', constant) is not None:
            return True
        return False

    def check_operator(self, operator) -> bool:
        return operator in self.__operators

    def get_tokens(self, l, line_idx):
        line = l.strip()  # dont need u whitespace
        token = ''
        tokens = []
        error = ""
        index = 0
        while index < len(line):
            if self.check_operator(line[index]):
                if token:
                    tokens.append(token)
                token = ''
                while index < len(line) and self.check_operator(line[index]):
                    token += line[index]
                    index += 1
                tokens.append(token)
                token = ''
            elif line[index] == '\"':
                if token:
                    tokens.append(token)
                token = ''
                quotes = 0
                index += 1
                while index < len(line) and quotes < 2:
                    if line[index] == '\"':
                        quotes += 1
                        break
                    token += line[index]
                    index += 1
                tokens.append(token)
                token = ''
                if quotes < 2:
                    error += "Lexical error at token " + token + " on line: " + str(line_idx) + "\n"
            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token = ''
                quotes = 0
                index += 1
                while index < len(line) and quotes < 2:
                    if line[index] == '\'':
                        quotes += 1
                        break
                    token += line[index]
                    index += 1
                if len(token) >= 2:
                    error += "Lexical error at token " + token + " on line: " + str(line_idx) + "\n"
                if quotes < 2:
                    error += "Lexical error at token " + token + " on line: " + str(line_idx) + "\n"
                tokens.append(token)
                token = ''
            elif line[index] in self.__separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''
            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens, error

    def read_file(self, file_name):
        error = ""
        with open(file_name, 'r') as lines:
            line_counter = 0
            for line in lines:
                line_counter += 1
                tokens, err = self.get_tokens(line, line_counter)
                error += err
                for token in tokens:
                    if token in self.__reserved_words or token in self.__separators or token in self.__operators:
                        if token == ' ':
                            continue
                        self.__pif.add(token, (-1, -1))
                    elif self.check_identifier(token):
                        self.__symbol_table.add(token)
                        position = self.__symbol_table.getPosition(token)
                        self.__pif.add('id', position)
                    elif self.check_constant(token):
                        self.__symbol_table.add(token)
                        position = self.__symbol_table.getPosition(token)
                        self.__pif.add('constant', position)
                    else:
                        error += "Lexical error at token " + token + " on pisition: " + line_counter + "\n"
        if error == "":
            print("Lexically correct!!!")
        else:
            print(error)

    def write_files(self, st_file, pif_file):
        with open(st_file, 'w') as writer:
            writer.write(str(self.__symbol_table))
        with open(pif_file, 'w') as writer:
            writer.write(str(self.__pif))
