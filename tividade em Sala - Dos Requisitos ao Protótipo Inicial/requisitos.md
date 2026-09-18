Requisitos implementados

Domínio: cadastro e login de usuários (inspirado nos padrões de segurança da aula: validação de entrada, autenticação e auditoria/log).

Requisito 1: Cadastro com validação de entrada O sistema deve cadastrar um usuário (nome + senha). O nome não pode ser vazio nem repetido, e a senha deve ter no mínimo 6 caracteres e pelo menos 1 número. A senha é guardada como hash.