from busca_fonologica import Busca

fonemas_lists = [
    ['orgaozinho', "órgãozinho"],
    ['pollyana', "poliana"],
    ['wallyson', 'uallison'],
    ["amarelo", "amarelu"],
    ["passoca", "páçocã"],
    ["chuchu", "xuxu"],
    ["chapéuzinho", "xapeuzim"],
    ["casa", "kasa"],
    ["ueslei", "wesley"],
    ["ualisom", "wallysson"],
    ["valter", "ualter", "walter"],
    ["wilson", "uilson"],
    ["giovanna", "geovana"],
    ["coca cola zero 2L", "coca cola", "unilever", "alimento", "bebida"],
    ["detergente 500ml", "ipê", "unilever", "higiene", "limpeza"],
    ["farinha láctea 300g", "nestlè", "mondelez", "alimento", "cereais"],
    ["bebida zero"]
]

for term in fonemas_lists:
    print(term)
    # for word in term:
    #     print("FONETIPY: ", fonetipy.apply(word))
    res = []
    for word in term:
        res.append(Busca.to_fonema(word))

print("BUSCA: ", res)
# for word in term:
#     print("alt: ", alt.Busca.to_fonema(word))
