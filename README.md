# busca_fonologica

## Módulo que recebe palavras (str) em diversas grafias e retorna pseudo-fonemas (str).

Objetivo do módulo: conciliar pesquisas onde o termo digitado diverge da forma gramatical correta por se apoiar na pronúncia das palavras. O módulo retorna um termo que equivaleria ao termo falado, conciliando diversas grafias de uma mesma palavra.

É recomendado que o termo resultante não tenha vogais, mas caso haja necessidade de mantê-las na string retornada, basta enviar True (bool) para o argumento opcional "vogais" (default: False).

tags: busca fonética, buscaBR, fonetipy