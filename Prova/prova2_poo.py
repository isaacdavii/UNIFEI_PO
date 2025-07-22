import tkinter as tk
from tkinter import messagebox, ttk
import pickle
import os

class EspecialidadeInvalidaException(Exception):
    def __init__(self, message = "Especialidade inválida!"):
        self.message = message
        super().__init__(self.message)

class DiaInvalidoException(Exception):
    def __init__(self, message = "Dia deve estar entre 1 e 30!"):
        self.message = message
        super().__init__(self.message)

class HoraInvalidaException(Exception):
    def __init__(self, message = "Hora deve estar entre 9 e 17!"):
        self.message = message
        super().__init__(self.message)

class ConsultaExistenteException(Exception):
    def __init__(self, message = "Já existe consulta agendada nesta data, escolha outra"):
        self.message = message
        super().__init__(self.message)

class Medico:
    def __init__(self, nome, crm, especialidade):
        self.__nome = nome
        self.__crm = crm
        self.__especialidade = especialidade

    @property
    def nome(self):
        return self.__nome

    @property
    def crm(self):
        return self.__crm

    @property
    def especialidade(self):
        return self.__especialidade

    def __str__(self):
        return f"{self.nome} - CRM: {self.crm} - {self.especialidade}"


class Consulta:
    def __init__(self, paciente, dia, hora, medico):
        self.__paciente = paciente
        self.__dia = dia
        self.__hora = hora
        self.__medico = medico

    @property
    def paciente(self):
        return self.__paciente

    @property
    def dia(self):
        return self.__dia

    @property
    def hora(self):
        return self.__hora

    @property
    def medico(self):
        return self.__medico

    def __str__(self):
        return f"Dia {self.dia} - {self.hora}h - {self.paciente}"

class LimitePrincipal:
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Sistema de Consultas Médicas")

        self.menubar = tk.Menu(self.root)

        self.medicoMenu = tk.Menu(self.menubar)
        self.medicoMenu.add_command(label = "Cadastrar", command=self.controle.cadastrarMedico)
        self.menubar.add_cascade(label = "Médico", menu=self.medicoMenu)

        self.consultaMenu = tk.Menu(self.menubar)
        self.consultaMenu.add_command(label = "Cadastrar", command = self.controle.cadastrarConsulta)
        self.consultaMenu.add_command(label = "Listar Consultas", command = self.controle.listarConsultas)
        self.menubar.add_cascade(label = "Consulta", menu = self.consultaMenu)

        self.root.config(menu = self.menubar)

        self.labelTitulo = tk.Label(
            self.root, text = "Sistema de Consultas Médicas", 
            font=("Arial", 16, "bold")
        )
        self.labelTitulo.pack(pady = 20)

        self.labelInfo = tk.Label(
            self.root,
            text="Use o menu acima para navegar pelo sistema",
            font=("Arial", 12),
        )
        self.labelInfo.pack(pady =10)

class LimiteCadastroMedico(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("Cadastro de Médico")
        self.controle = controle

        self.frameMain = tk.Frame(self)
        self.frameMain.pack(padx = 20, pady = 20, fill = "both", expand = True)

        self.frameNome = tk.Frame(self.frameMain)
        self.frameNome.pack(fill = "x", pady = 5)
        self.labelNome = tk.Label(self.frameNome, text = "Nome:", width = 15, anchor = "w")
        self.labelNome.pack(side = "left")
        self.entryNome = tk.Entry(self.frameNome, width = 30)
        self.entryNome.pack(side = "left", fill = "x", expand = True)
        
        self.frameCRM = tk.Frame(self.frameMain)
        self.frameCRM.pack(fill = "x", pady = 5)
        self.labelCRM = tk.Label(self.frameCRM, text = "CRM:", width = 15, anchor = "w")
        self.labelCRM.pack(side = "left")
        self.entryCRM = tk.Entry(self.frameCRM, width = 30)
        self.entryCRM.pack(side = "left", fill = "x", expand = True)

        self.frameEsp = tk.Frame(self.frameMain)
        self.frameEsp.pack(fill = "x", pady = 5)
        self.labelEsp = tk.Label(
            self.frameEsp, text = "Especialidade:", width = 15, anchor = "w"
        )
        self.labelEsp.pack(side = "left")
        self.entryEsp = tk.Entry(self.frameEsp, width = 30)
        self.entryEsp.pack(side = "left", fill = "x", expand = True)

        self.labelInfo = tk.Label(
            self.frameMain,
            text = "Especialidades válidas:\nPediatria, Cardiologia, Neurologia, Oftalmologia,\nOrtopedia, Gastroenterologia, Psiquiatria, Pneumologia",
            font = ("Arial", 9),
            fg = "blue",
        )
        self.labelInfo.pack(pady = 10)

        self.frameButtons = tk.Frame(self.frameMain)
        self.frameButtons.pack(pady = 20)

        self.buttonCadastrar = tk.Button(
            self.frameButtons,
            text = "Cadastrar",
            command = self.controle.cadastrarMedicoHandler,
        )
        self.buttonCadastrar.pack(side = "left", padx = 5)

        self.buttonLimpar = tk.Button(
            self.frameButtons, text = "Limpar", command = self.limparCampos
        )
        self.buttonLimpar.pack(side = "left", padx = 5)

        self.buttonFechar = tk.Button(
            self.frameButtons, text = "Fechar", command = self.destroy
        )
        self.buttonFechar.pack(side = "left", padx = 5)

    def limparCampos(self):
        self.entryNome.delete(0, tk.END)
        self.entryCRM.delete(0, tk.END)
        self.entryEsp.delete(0, tk.END)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteCadastroConsulta(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("500x400")
        self.title("Marcação de Consulta")
        self.controle = controle

        self.frameMain = tk.Frame(self)
        self.frameMain.pack(padx = 20, pady = 20, fill = "both", expand = True)

        self.framePaciente = tk.Frame(self.frameMain)
        self.framePaciente.pack(fill = "x", pady = 5)
        self.labelPaciente = tk.Label(
            self.framePaciente, text = "Nome do Paciente:", width = 15, anchor = "w"
        )
        self.labelPaciente.pack(side = "left")
        self.entryPaciente = tk.Entry(self.framePaciente, width = 30)
        self.entryPaciente.pack(side = "left", fill = "x", expand = True)

        self.frameDia = tk.Frame(self.frameMain)
        self.frameDia.pack(fill = "x", pady = 5)
        self.labelDia = tk.Label(
            self.frameDia, text = "Dia (1-30):", width = 15, anchor = "w"
        )
        self.labelDia.pack(side = "left")
        self.entryDia = tk.Entry(self.frameDia, width = 30)
        self.entryDia.pack(side = "left", fill = "x", expand = True)

        self.frameHora = tk.Frame(self.frameMain)
        self.frameHora.pack(fill = "x", pady = 5)
        self.labelHora = tk.Label(
            self.frameHora, text = "Hora (9-17):", width = 15, anchor = "w"
        )
        self.labelHora.pack(side = "left")
        self.entryHora = tk.Entry(self.frameHora, width = 30)
        self.entryHora.pack(side = "left", fill = "x", expand = True)

        self.frameEspecialidade = tk.Frame(self.frameMain)
        self.frameEspecialidade.pack(fill = "x", pady = 10)
        self.labelEspecialidade = tk.Label(
            self.frameEspecialidade, text = "Especialidade:", width = 15, anchor = "w"
        )
        self.labelEspecialidade.pack(side = "left")
        self.comboEspecialidade = ttk.Combobox(
            self.frameEspecialidade, state = "readonly"
        )
        self.comboEspecialidade.pack(side = "left", fill = "x", expand = True)
        self.comboEspecialidade.bind(
            "<<ComboboxSelected>>", self.controle.especialidadeSelecionada
        )

        self.frameMedico = tk.Frame(self.frameMain)
        self.frameMedico.pack(fill = "both", expand = True, pady = 10)
        self.labelMedico = tk.Label(self.frameMedico, text = "Médico:")
        self.labelMedico.pack(anchor = "w")

        self.listboxMedico = tk.Listbox(self.frameMedico, height = 6)
        self.listboxMedico.pack(fill = "both", expand = True)

        self.frameButtons = tk.Frame(self.frameMain)
        self.frameButtons.pack(pady = 20)

        self.buttonCadastrar = tk.Button(
            self.frameButtons,
            text = "Cadastrar Consulta",
            command = self.controle.cadastrarConsultaHandler,
        )
        self.buttonCadastrar.pack(side = "left", padx = 5)

        self.buttonLimpar = tk.Button(
            self.frameButtons, text = "Limpar", command = self.limparCampos
        )
        self.buttonLimpar.pack(side = "left", padx = 5)

        self.buttonFechar = tk.Button(
            self.frameButtons, text = "Fechar", command = self.destroy
        )
        self.buttonFechar.pack(side = "left", padx = 5)

    def limparCampos(self):
        self.entryPaciente.delete(0, tk.END)
        self.entryDia.delete(0, tk.END)
        self.entryHora.delete(0, tk.END)
        self.comboEspecialidade.set("")
        self.listboxMedico.delete(0, tk.END)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteListarConsultas(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("600x400")
        self.title("Lista de Consultas por Médico")
        self.controle = controle

        self.frameMain = tk.Frame(self)
        self.frameMain.pack(padx = 20, pady = 20, fill = "both", expand = True)

        self.frameMedico = tk.Frame(self.frameMain)
        self.frameMedico.pack(fill = "x", pady = 10)
        self.labelMedico = tk.Label(self.frameMedico, text = "Selecione o Médico:")
        self.labelMedico.pack(anchor = "w")

        self.comboMedico = ttk.Combobox(self.frameMedico, state = "readonly")
        self.comboMedico.pack(fill = "x", pady = 5)
        self.comboMedico.bind("<<ComboboxSelected>>", self.controle.medicoSelecionado)

        self.frameConsultas = tk.Frame(self.frameMain)
        self.frameConsultas.pack(fill = "both", expand = True, pady = 10)
        self.labelConsultas = tk.Label(self.frameConsultas, text = "Consultas:")
        self.labelConsultas.pack(anchor = "w")

        self.treeConsultas = ttk.Treeview(
            self.frameConsultas, columns = ("dia", "hora", "paciente"), show = "headings"
        )
        self.treeConsultas.heading("dia", text = "Dia")
        self.treeConsultas.heading("hora", text = "Hora")
        self.treeConsultas.heading("paciente", text = "Paciente")
        self.treeConsultas.column("dia", width = 80)
        self.treeConsultas.column("hora", width = 80)
        self.treeConsultas.column("paciente", width = 200)
        self.treeConsultas.pack(fill = "both", expand = True)

        self.buttonFechar = tk.Button(
            self.frameMain, text = "Fechar", command = self.destroy
        )
        self.buttonFechar.pack(pady = 10)

class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlMedico = ControleMedico(self)
        self.ctrlConsulta = ControleConsulta(self)

        self.carregarDados()

        self.limite = LimitePrincipal(self.root, self)

        self.cadastrarMedicosIniciais()

        self.root.mainloop()

    def cadastrarMedico(self):
        self.ctrlMedico.cadastrarMedico()

    def cadastrarConsulta(self):
        self.ctrlConsulta.cadastrarConsulta()

    def listarConsultas(self):
        self.ctrlConsulta.listarConsultas()

    def carregarDados(self):
        self.ctrlMedico.carregarMedicos()
        self.ctrlConsulta.carregarConsultas()

    def salvarDados(self):
        self.ctrlMedico.salvarMedicos()
        self.ctrlConsulta.salvarConsultas()

    def cadastrarMedicosIniciais(self):
        if len(self.ctrlMedico.listaMedicos) == 0:
            medicos_iniciais = [
                ("Dr. João Silva", "12345-SP", "Pediatria"),
                ("Dra. Maria Santos", "23456-SP", "Pediatria"),
                ("Dr. Carlos Lima", "34567-SP", "Cardiologia"),
                ("Dra. Ana Costa", "45678-SP", "Cardiologia"),
                ("Dr. Pedro Oliveira", "56789-SP", "Neurologia"),
                ("Dra. Clara Souza", "67890-SP", "Neurologia"),
            ]

            for nome, crm, especialidade in medicos_iniciais:
                try:
                    medico = Medico(nome, crm, especialidade)
                    self.ctrlMedico.listaMedicos.append(medico)
                except:
                    pass

            self.ctrlMedico.salvarMedicos()

class ControleMedico:
    def __init__(self, controlePrincipal):
        self.controlePrincipal = controlePrincipal
        self.listaMedicos = []
        self.especialidades_validas = [
            "Pediatria",
            "Cardiologia",
            "Neurologia",
            "Oftalmologia",
            "Ortopedia",
            "Gastroenterologia",
            "Psiquiatria",
            "Pneumologia",
        ]

    def cadastrarMedico(self):
        self.limiteCadastro = LimiteCadastroMedico(self)

    def cadastrarMedicoHandler(self):
        try:
            nome = self.limiteCadastro.entryNome.get().strip()
            crm = self.limiteCadastro.entryCRM.get().strip()
            especialidade = self.limiteCadastro.entryEsp.get().strip()

            if not nome or not crm or not especialidade:
                raise ValueError("Todos os campos devem ser preenchidos!")

            if especialidade not in self.especialidades_validas:
                raise EspecialidadeInvalidaException(
                    f"Especialidade '{especialidade}' é inválida!\n"
                    f"Especialidades válidas: {', '.join(self.especialidades_validas)}"
                )

            medico = Medico(nome, crm, especialidade)
            self.listaMedicos.append(medico)
            self.salvarMedicos()

            self.limiteCadastro.mostraJanela(
                "Sucesso", "Médico cadastrado com sucesso!"
            )
            self.limiteCadastro.limparCampos()

        except EspecialidadeInvalidaException as e:
            self.limiteCadastro.mostraJanela("Erro", str(e))
        except Exception as e:
            self.limiteCadastro.mostraJanela("Erro", str(e))

    def carregarMedicos(self):
        try:
            if os.path.exists("medicos.pickle"):
                with open("medicos.pickle", "rb") as f:
                    self.listaMedicos = pickle.load(f)
        except:
            self.listaMedicos = []

    def salvarMedicos(self):
        try:
            with open("medicos.pickle", "wb") as f:
                pickle.dump(self.listaMedicos, f)
        except:
            pass

    def getMedicosPorEspecialidade(self, especialidade):
        return [
            medico
            for medico in self.listaMedicos
            if medico.especialidade == especialidade
        ]

class ControleConsulta:
    def __init__(self, controlePrincipal):
        self.controlePrincipal = controlePrincipal
        self.listaConsultas = []

    def cadastrarConsulta(self):
        if len(self.controlePrincipal.ctrlMedico.listaMedicos) == 0:
            messagebox.showwarning(
                "Aviso", "É necessário cadastrar médicos antes de marcar consultas!"
            )
            return

        self.limiteCadastro = LimiteCadastroConsulta(self)
        self.atualizarEspecialidades()

    def atualizarEspecialidades(self):
        especialidades = list(
            set(
                [
                    medico.especialidade
                    for medico in self.controlePrincipal.ctrlMedico.listaMedicos
                ]
            )
        )
        especialidades.sort()
        self.limiteCadastro.comboEspecialidade["values"] = especialidades

    def especialidadeSelecionada(self, event):
        especialidade = self.limiteCadastro.comboEspecialidade.get()
        medicos = self.controlePrincipal.ctrlMedico.getMedicosPorEspecialidade(
            especialidade
        )

        self.limiteCadastro.listboxMedico.delete(0, tk.END)
        for medico in medicos:
            self.limiteCadastro.listboxMedico.insert(tk.END, medico.nome)

    def cadastrarConsultaHandler(self):
        try:
            paciente = self.limiteCadastro.entryPaciente.get().strip()
            dia_str = self.limiteCadastro.entryDia.get().strip()
            hora_str = self.limiteCadastro.entryHora.get().strip()

            if not paciente:
                raise ValueError("Nome do paciente é obrigatório!")

            try:
                dia = int(dia_str)
                if dia < 1 or dia > 30:
                    raise DiaInvalidoException()
            except ValueError:
                raise DiaInvalidoException("Dia deve ser um número entre 1 e 30!")

            try:
                hora = int(hora_str)
                if hora < 9 or hora > 17:
                    raise HoraInvalidaException()
            except ValueError:
                raise HoraInvalidaException("Hora deve ser um número entre 9 e 17!")

            selecao = self.limiteCadastro.listboxMedico.curselection()
            if not selecao:
                raise ValueError("Selecione um médico!")

            nome_medico = self.limiteCadastro.listboxMedico.get(selecao[0])
            medico = None
            for m in self.controlePrincipal.ctrlMedico.listaMedicos:
                if m.nome == nome_medico:
                    medico = m
                    break

            if not medico:
                raise ValueError("Médico não encontrado!")

            for consulta in self.listaConsultas:
                if (
                    consulta.medico.nome == medico.nome
                    and consulta.dia == dia
                    and consulta.hora == hora
                ):
                    raise ConsultaExistenteException()

            consulta = Consulta(paciente, dia, hora, medico)
            self.listaConsultas.append(consulta)
            self.salvarConsultas()

            self.limiteCadastro.mostraJanela("Sucesso", "Consulta marcada com sucesso!")
            self.limiteCadastro.limparCampos()

        except (
            DiaInvalidoException,
            HoraInvalidaException,
            ConsultaExistenteException,
        ) as e:
            self.limiteCadastro.mostraJanela("Erro", str(e))
        except Exception as e:
            self.limiteCadastro.mostraJanela("Erro", str(e))

    def listarConsultas(self):
        if len(self.controlePrincipal.ctrlMedico.listaMedicos) == 0:
            messagebox.showwarning("Aviso", "Não há médicos cadastrados!")
            return

        self.limiteLista = LimiteListarConsultas(self)
        self.atualizarComboMedicos()

    def atualizarComboMedicos(self):
        medicos = [
            medico.nome for medico in self.controlePrincipal.ctrlMedico.listaMedicos
        ]
        self.limiteLista.comboMedico["values"] = medicos

    def medicoSelecionado(self, event):
        nome_medico = self.limiteLista.comboMedico.get()
        
        for item in self.limiteLista.treeConsultas.get_children():
            self.limiteLista.treeConsultas.delete(item)

        consultas_medico = [
            consulta
            for consulta in self.listaConsultas
            if consulta.medico.nome == nome_medico
        ]
        
        consultas_medico.sort(key=lambda c: (c.dia, c.hora))

        for consulta in consultas_medico:
            self.limiteLista.treeConsultas.insert(
                "", "end", values=(consulta.dia, f"{consulta.hora}h", consulta.paciente)
            )

    def carregarConsultas(self):
        try:
            if os.path.exists("consultas.pickle"):
                with open("consultas.pickle", "rb") as f:
                    self.listaConsultas = pickle.load(f)
        except:
            self.listaConsultas = []

    def salvarConsultas(self):
        try:
            with open("consultas.pickle", "wb") as f:
                pickle.dump(self.listaConsultas, f)
        except:
            pass

if __name__ == "__main__":
    ControlePrincipal()
