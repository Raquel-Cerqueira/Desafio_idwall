import textwrap

exemplo = "In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters."
''

def justifica(texto, tamanho):
    for linha in textwrap.wrap(texto.replace('\n', ''), tamanho):
        por_palavra, sobra = divmod(tamanho - len(linha), linha.count(' '))
        por_palavra *= ' '; sobra *= [' ']
        yield ' '.join(palavra + por_palavra + (sobra.pop() if sobra else '') 
            for palavra in linha.split(' ')).rstrip()

print('\n'.join(justifica(exemplo, 40)))
