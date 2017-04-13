# Primeira Avaliação

Imprima na saída padrão (STDOUT) os números de 1 a 100. Em todos os múltiplos de 5, troque o número por Nama. Nos múltiplos de 7 troque o número por Team e nos múltiplos de 35 por Nama Team. 

O formato de impressão dos números precisa ser **EXATAMENTE** igual a esse:

1, 2, 3, 4, Nama, 6, Team, ........ 33, 34, Nama Team, 36 ....., 97, Team, 99, Nama

# Execução do Script

## Testes

```
$ python3 -m unittest discover
```

## Formatação de Código

É necessário instalar a lib flake8

```
$ pip install flake8
```

### Verificação da formatação e complexidade dos métodos.

```
$ flake8 max-complexity=10 .
```

## Saida Padrão

```
$ python3 nama.py
```
