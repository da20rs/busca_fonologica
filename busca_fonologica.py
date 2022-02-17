"""Busca fonologica module."""
from collections import namedtuple
from unidecode import unidecode
import re


class Busca():
    "Phonetic search class."
    @staticmethod
    def to_fonema(grafema: str, vogais: bool = False) -> str:
        """Gera um pseudo-fonema para o grafema fornecido."""
        to_replace = namedtuple("termo", ["grafema", "fonema"])
        fonemas_grafemas = {
            "first_all": [to_replace(["Y"], "I"),
                          to_replace(["BR"], "B"),
                          to_replace(["PH"], "F"),
                          to_replace(["GR", "MG", "NG", "RG"], "G"),
                          to_replace(["GE", "GI", "RJ", "MJ", "NJ"], "J"),
                          to_replace(["Q", "CA", "CO", "CU"], "K"),
                          to_replace(["LH"], "L"),
                          to_replace(["N", "RM", "GM", "MD", "SM"], "M")],

            "second_all": [to_replace(["AO"], "M")],

            "third_all": [to_replace(["NH"], "N"),
                          to_replace(["PR"], "P"),
                          to_replace(["CH"], "X"),
                          to_replace(["Ç", "X", "TS", "C", "Z", "RS"], "S"),
                          to_replace(["LT", "TR", "CT", "RT", "ST"], "T"),
                          to_replace(["W"], "V")
                          ],
            "fourth_start": [to_replace(["U"], "V")],

            "fifth_end": [to_replace(["S", "Z", "R", "R", "M", "N", "AO", "L"], "")],

            "seventh_all": [to_replace(["L"], "R"),
                            to_replace(["C"], "K")],

            "eigth_all": [to_replace(["A", "E", "I", "O", "U", "H"], "")]
        }

        if vogais:
            fonemas_grafemas.pop("eigth_all")

        only_letters = "".join([i for i in grafema if not i.isdigit()])
        no_punctuation = re.sub(r'[^\w\s]', '', only_letters)
        in_caps = no_punctuation.upper()
        word = ""
        for letter in in_caps:
            word += unidecode(letter) if letter != "Ç" else "Ç"

        blocks = []
        block = ""
        for index_letter in range(len(word)):
            if word[index_letter].isspace() or (index_letter == (len(word)-1)):
                blocks.append(block)
                block = ""
            else:
                block += word[index_letter]

        for step in fonemas_grafemas.keys():
            if "start" in step:
                for relacao in fonemas_grafemas[step]:
                    for term in relacao.grafema:
                        if word[0] == term:
                            word = f"{relacao.fonema}{word[1:]}"
            if "all" in step:
                for relacao in fonemas_grafemas[step]:
                    for term in relacao.grafema:
                        word = word.replace(term, relacao.fonema)
            if "end" in step:
                for relacao in fonemas_grafemas[step]:
                    for term in relacao.grafema:
                        if word[-1] == term:
                            word = f"{word[:-1]}"
                        if word[-2:] == term:
                            word = f"{word[:-2]}"

        try:
            for index in range(len(word)-1):
                if word[index] == word[index+1]:
                    once = word[index]
                    word = word.replace(once*2, once)
        except:
            pass

        return word
