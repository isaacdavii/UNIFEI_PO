# Programação Orientada a Objetos (POO) - UNIFEI

## Sobre o Repositório

Este repositório contém todo o material de estudo da disciplina de Programação Orientada a Objetos (POO) do curso de Ciência da Computação da UNIFEI, 3º período. O conteúdo inclui exercícios, trabalhos e provas, todos implementados em Python com foco nos conceitos fundamentais da POO.

---

## 📚 Estrutura do Repositório

### 💻 Aulas Práticas

#### Aula 08 - Introdução a Classes

- **`animal.py`** - Exemplo básico de classe Animal
- **`moto.py`** - Implementação da classe Moto

#### Aula 09 - Herança e Polimorfismo

- **`academico1.py`** - Sistema acadêmico com classes Pessoa, Professor e Aluno
- **`treino.py`** - Exercícios de fixação com herança

#### Aula 10 - Polimorfismo Avançado

- **`poli_ex1.py`** - Exemplos de polimorfismo
- **`poli_ex2.py`** - Aplicações práticas de polimorfismo

#### Aula 11 - Refatoração e Boas Práticas

- **`conta_v2.py`** - Sistema de conta bancária refatorado

#### Aula 12 - Agregação e Composição

- **`spotify.py`** - Simulação do Spotify com agregação
- **`aula12_completo.py`** - Exemplo completo
- **Classes:** Album, Artista, Música, Playlist e Facilidades

#### Aula 13 - Classes Abstratas

- **`aula13.py`** - Implementação de classes abstratas com ABC

#### Aula 14 - Sobrecarga de Operadores

- **`frac1.py`** - Classe Fração básica
- **`frac2.py`** - Fração com sobrecarga de operadores

#### Aula 15 - Tratamento de Exceções

- **`exception1.py`** - Exceções básicas
- **`exception2.py`** - Try/catch avançado
- **`exception3.py`** - Múltiplas exceções
- **`exception4.py`** - Exceções customizadas
- **`exercicio_aula.py`** - Exercício prático

#### Aula 16 - Interface Gráfica com Tkinter

- **7 exemplos práticos** (`tk01.py` a `tk07.py`)
- Progressão de conceitos básicos a interfaces complexas

#### Aula 17 - Padrão MVC

- **`aula17-ex1.py`** - Implementação do padrão Model-View-Controller

#### Aulas 18-20 - Sistema Acadêmico Completo com MVC

- **Classes:** Estudante, Disciplina, Turma
- **Funcionalidades:** Cadastro, consulta e gestão acadêmica
- **Persistência:** Arquivos pickle para salvar dados

---

## 🎯 Exercícios e Trabalhos

### Exercício 3 - Empregadas Domésticas

- **Sistema de gerenciamento** com classes abstratas
- **Tipos:** Horista, Diarista, Mensalista
- **Funcionalidade:** Cálculo de salários e busca pela mais barata

### Exercício 4 - Imobiliária

- **Sistema de vendas** com vendedores e comissões
- **Classes:** Vendedor, Venda com polimorfismo

### Exercício 5-9 - Evolução de Conceitos

- Aplicação progressiva de conceitos POO
- Herança, polimorfismo e encapsulamento

### Exercício 10 - Sistema de Cupom Fiscal 🏪

- **Interface Gráfica:** Tkinter
- **Funcionalidades:**
  - Cadastro de produtos
  - Criação de cupons fiscais
  - Consultas e relatórios
- **Persistência:** Arquivos pickle
- **Padrão:** MVC implementado

### Exercício 11 - Sistema de Jogos 🎮

- **Funcionalidades:**
  - Cadastro de jogos
  - Sistema de avaliações
  - Consultas por nota
  - Persistência de dados
- **Interface:** Menu completo com Tkinter

### Exercício 12 - Sistema de Comanda 🍽️

- **Restaurante "Comida Boa"**
- **Funcionalidades:**
  - Lançamento de comandas
  - Impressão de comandas
  - Cálculo de faturamento
  - Interface gráfica profissional

---

## 🏆 Projeto Final - Sistema de Consultas Médicas

### Descrição

Sistema completo para gerenciamento de consultas médicas implementado com **padrão MVC** e interface gráfica Tkinter. Referente 'prova2_poo.py'.

### Funcionalidades Principais

#### 1. 👨‍⚕️ Cadastro de Médicos

- **Campos:** Nome, CRM, Especialidade
- **Validações:** Especialidades pré-definidas
- **Exceções:** `EspecialidadeInvalidaException`

#### 2. 📅 Marcação de Consultas

- **Campos:** Paciente, Data/Hora, Especialidade, Médico
- **Validações:**
  - Dias: 1-30 (`DiaInvalidoException`)
  - Horários: 9h-17h (`HoraInvalidaException`)
  - Conflitos: (`ConsultaExistenteException`)

#### 3. 📋 Relatórios

- **Lista de consultas por médico**
- **Ordenação:** Por data e horário
- **Interface:** Tabelas organizadas

### Arquitetura Técnica

- **Padrão:** MVC (Model-View-Controller)
- **Interface:** Tkinter com menus e formulários
- **Persistência:** Arquivos pickle
- **Tratamento:** Exceções customizadas

---

## 🛠️ Tecnologias e Conceitos

### Linguagem

- **Python 3.x** - Linguagem principal

### Conceitos POO Aplicados

- ✅ **Encapsulamento** - Proteção de dados
- ✅ **Herança** - Reutilização de código
- ✅ **Polimorfismo** - Múltiplas formas
- ✅ **Abstração** - Classes abstratas (ABC)
- ✅ **Agregação/Composição** - Relacionamentos entre classes

### Bibliotecas Utilizadas

- **`tkinter`** - Interface gráfica
- **`abc`** - Classes abstratas
- **`pickle`** - Persistência de dados
- **`os`** - Operações do sistema

### Padrões de Design

- **MVC (Model-View-Controller)** - Separação de responsabilidades
- **Exception Handling** - Tratamento robusto de erros

---

## 📊 Estrutura de Arquivos por Tipo

```text
📁 Implementações Práticas/
├── 🔧 Aula 08/ → Classes Básicas
├── 🔄 Aula 09/ → Herança
├── 🎭 Aula 10/ → Polimorfismo
├── 📦 Aula 12/ → Agregação (Spotify)
├── 🎨 Aula 16/ → Interface Gráfica
└── 🏗️ Aulas 18-20/ → Sistema MVC

📁 Exercícios/
├── 📋 Exercício 3/ → Empregadas Domésticas
├── 🏢 Exercício 4/ → Imobiliária
├── ...
├── 🛒 Exercício 10/ → Sistema Cupom Fiscal
├── 🎮 Exercício 11/ → Sistema de Jogos
└── 🍽️ Exercício 12/ → Sistema de Comanda

📁 Projeto Final/
└── 🏥 Prova/ → Sistema Consultas Médicas
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x instalado
- Tkinter (geralmente incluído no Python)

### Executando os Projetos

#### Sistemas com Interface Gráfica

```bash
# Sistema de Cupom Fiscal
cd "Exercícios/Exercício 10"
python main.py

# Sistema de Jogos
cd "Exercícios/Exercício 11"
python main.py

# Sistema de Comanda
cd "Exercícios/Exercício 12"
python main.py

# Sistema de Consultas Médicas
cd "Prova"
python prova1_poo.py  # ou prova2_poo.py
```

#### Exemplos de Aula

```bash
# Spotify (Aula 12)
cd "Aula 12"
python spotify.py

# Sistema Acadêmico (Aulas 18-20)
cd "Aula 18/Aula18-parte2"
python main.py
```

---

## 🎓 Aprendizados e Evolução

### Progressão do Conhecimento

1. **Básico:** Classes simples e métodos
2. **Intermediário:** Herança e polimorfismo
3. **Avançado:** Padrões de design, interfaces gráficas
4. **Especializado:** Sistemas completos com persistência

### Principais Conquistas

- ✅ Domínio completo dos conceitos POO
- ✅ Implementação de interfaces gráficas funcionais
- ✅ Aplicação do padrão MVC
- ✅ Desenvolvimento de sistemas completos
- ✅ Tratamento profissional de exceções
- ✅ Persistência de dados com pickle

---

## 📝 Observações

- **Persistência:** Vários projetos utilizam arquivos `.pickle` para salvar dados
- **Interface:** Evolução gradual de console para GUI com Tkinter
- **Organização:** Código bem estruturado seguindo boas práticas
- **Documentação:** Comentários e estrutura clara em todos os projetos

---

**⭐ Este repositório representa uma jornada completa de aprendizado em POO, desde conceitos básicos até sistemas profissionais mais complexos!**
