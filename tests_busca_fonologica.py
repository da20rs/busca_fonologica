from busca_fonologica import Busca

fonemas_lists = [
    ['orgaozinho', "órgãozinho"],
    ['pollyana', "poliana"],
    ['wallyson', 'uallison'],
    ["amarelo", "amarelu"],
    ["passoca", "páçocã"],
    ["chuchu", "xuxu"],
    ["casa", "kasa"],
    ["ueslei", "wesley"],
    ["ualisom", "wallysson"],
    ["valter", "ualter", "walter"],
    ["wilson", "uilson"],
    ["giovanna", "geovana"]
]

not_fonemas = [
    ["chamariz", "chafariz"]
]

for term in fonemas_lists:
    assert Busca.to_fonema(term[0]) == Busca.to_fonema(term[1])

for term in not_fonemas:
    if Busca.to_fonema(term[0]) == Busca.to_fonema(term[1]):
        raise ValueError("os termos não tem o mesmo fonema")