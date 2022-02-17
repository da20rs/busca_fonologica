# busca_fonologica

Este módulo recebe palavras (str) em diversas grafias e retorna pseudo-fonemas (str).

O objetivo é encontrar melhores correspondências em buscas mesmo em casos onde a digitação do termo desejado se apoia na pronúncia, e não na forma gramatical correta.

É recomendado que o termo resultante não tenha vogais, mas caso haja necessidade de mantê-las na string retornada, basta enviar True (bool) para o argumento opcional "vogais" (default: False).