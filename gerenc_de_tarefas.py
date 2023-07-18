# biblioteca responsavel por interagir com o banco de dados
import sqlite3
# conectar (ou criar) o banco de dados
conexao = sqlite3.connect('tarefas.db')
# criando um objeto cursosr para executar comandos SQL 
cursor = conexao.cursor()
# criando a tabela de categorias
cursor.execute('''
CREATE TABLE IF NOT EXISTS categorias (
    id INT PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);
''')
#Criando a tabela de tarefas
cursor.execute('''
CREATE TABLE IF NOT EXISTS tafefas (
    id INT PRIMARY KEY,
    nome TEXT NOT NULL,
    data TEXT,
    status INTEGER CHECK (status IN (0, 1)),
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);
''')

# salvando as alterações e fechando a conexão
conexao.commit()
conexao.close()