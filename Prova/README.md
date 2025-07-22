# Sistema de Consultas Médicas - Padrão MVC

## Descrição

Sistema completo para gerenciamento de consultas médicas implementado em Python usando o padrão MVC (Model-View-Controller) com interface gráfica Tkinter. Referente a 'prova2_poo.py'.

## Funcionalidades Implementadas

### 1. Cadastro de Médicos

- **Menu**: Médico → Cadastrar
- **Campos**: Nome, CRM, Especialidade
- **Validação**: Especialidade deve ser uma das opções válidas:
  - Pediatria
  - Cardiologia  
  - Neurologia
  - Oftalmologia
  - Ortopedia
  - Gastroenterologia
  - Psiquiatria
  - Pneumologia
- **Exception**: `EspecialidadeInvalidaException` para especialidades inválidas

### 2. Marcação de Consultas

- **Menu**: Consulta → Cadastrar
- **Campos**:
  - Nome do paciente
  - Dia (1-30)
  - Hora (9-17)
  - Especialidade (ComboBox)
  - Médico (ListBox - preenchido automaticamente após seleção da especialidade)

- **Validações**:
  - Dia deve estar entre 1 e 30 (`DiaInvalidoException`)
  - Hora deve estar entre 9 e 17 (`HoraInvalidaException`)
  - Verificação de conflito de horário (`ConsultaExistenteException`)

### 3. Lista de Consultas por Médico

- **Menu**: Consulta → Listar Consultas
- **Funcionalidade**:
  - ComboBox com todos os médicos cadastrados
  - Ao selecionar um médico, exibe suas consultas em formato de tabela
  - Mostra: Dia, Hora, Nome do Paciente
  - Consultas ordenadas por dia e hora

## Arquitetura MVC

### Models

- **Medico**: Classe com nome, CRM e especialidade
- **Consulta**: Classe com paciente, dia, hora e médico

### Views (Limites)

- **LimitePrincipal**: Janela principal com menu
- **LimiteCadastroMedico**: Formulário para cadastro de médicos
- **LimiteCadastroConsulta**: Formulário para marcação de consultas
- **LimiteListarConsultas**: Interface para listar consultas por médico

### Controllers

- **ControlePrincipal**: Controlador principal do sistema
- **ControleMedico**: Gerencia operações relacionadas aos médicos
- **ControleConsulta**: Gerencia operações relacionadas às consultas

## Exceptions Customizadas

- **EspecialidadeInvalidaException**: Especialidade não está na lista válida
- **DiaInvalidoException**: Dia não está entre 1 e 30
- **HoraInvalidaException**: Hora não está entre 9 e 17
- **ConsultaExistenteException**: Já existe consulta no mesmo dia/hora para o médico

## Persistência

- Dados salvos em arquivos pickle:
  - `medicos.pickle`: Lista de médicos cadastrados
  - `consultas.pickle`: Lista de consultas marcadas

## Dados Iniciais

O sistema vem pré-configurado com 6 médicos de 3 especialidades diferentes - para efeito de teste:

- **Pediatria**: Dr. João Silva, Dra. Maria Santos
- **Cardiologia**: Dr. Carlos Lima, Dra. Ana Costa  
- **Neurologia**: Dr. Pedro Oliveira, Dra. Clara Souza

## Como Executar

```bash
python prova2_poo.py
```

## Exemplo de Uso

1. Execute o programa
2. Use "Médico → Cadastrar" para adicionar novos médicos
3. Use "Consulta → Cadastrar" para marcar consultas:
   - Digite nome do paciente
   - Digite dia (ex: 15) e hora (ex: 14)
   - Selecione especialidade no ComboBox
   - Selecione médico no ListBox
   - Clique "Cadastrar Consulta"
4. Use "Consulta → Listar Consultas" para ver consultas por médico

## Observações Técnicas

- Interface responsiva e intuitiva
- Validação em tempo real
- Mensagens de erro claras
- Persistência automática dos dados
- Código bem estruturado seguindo princípios de POO
