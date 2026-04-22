'''


'''

aluno = {
    "nome": "Ricardo Silva",
    "idade": 22,
    "notas": [8.5, 9.0, 7.5]
}

print(f"Nome do Aluno: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {', '.join(map(str, aluno['notas']))}")
print(f"Média Final: {sum(aluno['notas']) / len(aluno['notas']):.2f}")