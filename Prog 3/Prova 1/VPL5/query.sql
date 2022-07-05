select aluno.aluno_key, aluno.nome , aluno.ingresso, cidade.nome, sexo.nome, disciplina.sigla from aluno, cidade, sexo, matricula, disciplina
where aluno.sexo_key = sexo.sexo_key and aluno.cidade_key = cidade.cidade_key and aluno.aluno_key = matricula.aluno_key and disciplina.disciplina_key = matricula.disciplina_key
and aluno.sexo_key = 1 and disciplina.disciplina_key = 4