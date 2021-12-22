CREATE DATABASE Secreto;
USE Secreto;

CREATE TABLE IF NOT EXISTS Agente(
	idAgente INT PRIMARY KEY NOT NULL,
    nome VARCHAR(45) NOT NULL,
    endereco VARCHAR(45), 
    nascimento DATE,
    habilidade VARCHAR(45),
    sexo VARCHAR(45),
    email VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS Missao(
	idMissao INT NOT NULL AUTO_INCREMENT, 
    PRIMARY KEY(idMissao),
    data DATE NOT NULL,
    nome VARCHAR(45),
    locali VARCHAR(45),
    duracao INT, 
    idVilao INT NOT NULL,
    CONSTRAINT fk_Vilao
		FOREIGN KEY(idVilao) REFERENCES Vilao(idVilao)
        ON UPDATE CASCADE
        ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS Vilao(
	idVilao INT PRIMARY KEY NOT NULL,
	nome VARCHAR(45) NOT NULL,
	num_crimes INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Agente_has_Missao(
	idAgente INT NOT NULL,
    idMissao INT NOT NULL,
    CONSTRAINT fk_Agente_has_Missao_Agente
		FOREIGN KEY(idAgente) REFERENCES Agente(idAgente)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
	CONSTRAINT fk_Agente_has_Missao_Missao
		FOREIGN KEY(idMissao) REFERENCES Missao(idMissao)
        ON UPDATE CASCADE
        ON DELETE CASCADE   
);

SELECT * FROM Agente;
SELECT * FROM Vilao;
SELECT * FROM Missao;
SELECT * FROM Agente_has_Missao;

SELECT A.nome, A.email, M.nome, M.data FROM Agente A JOIN Missao M JOIN Agente_has_Missao H ON A.idAgente = H.idAgente AND M.idMissao = H.idMissao;


SELECT A.nome, M.nome, V.nome FROM Agente A JOIN Missao M JOIN Vilao V JOIN Agente_has_Missao H ON A.idAgente = H.idAgente AND M.idMissao = H.idMissao AND M.idVilao = V.idVilao; 



















