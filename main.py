import PySimpleGUI as Sg
from Db.Db import Db


class Program:

    def __init__(self, title, layout, size):

        self.title = title
        self.layout = layout
        self.size = size

        window = Sg.Window(title, layout, size=size)

        while True:
            event, values = window.read()

            if event == Sg.WIN_CLOSED or event == 'Sair':
                break

            # Verifica se o botão de login foi clicado
            if event == 'Login':

                # Verificação se os dados estão em branco. Caso estejam exibe um erro na tela!
                if values['user'] == '' and values['password'] == '':
                    Sg.PopupError('Digite o usuário e a senha')

                elif values['user'] == '':
                    Sg.PopupError('Digite o usuário!')

                elif values['password'] == '':
                    Sg.PopupError('Digite a senha!')

                # Caso os campos não estejam vazios, ele faz a verificação se os dados constam no banco de dados!
                else:
                    user = values['user']
                    password = values['password']

                    database = Db
                    login = database.login_verify(database, user, password)

                    # Caso o login e senha estejam cadastrados no banco, ele autentica o usuário e abre a outra tela
                    if login > 0:
                        Sg.PopupOK(f'Bem vindo, {user}')
                        window.hide()
                        Program.main_window(self)
                        window.un_hide()

                    # Caso não, ele exibe o erro abaixo
                    else:
                        Sg.Popup('Usuário não cadastrado ou senha invalida!', no_titlebar=True)

            # Evento que chama a tela de cadastro de usuário
            if event == 'Cadastrar-se':
                window.hide()
                Program.register_window(self)
                window.un_hide()

            # Evento que pega os dados passados na tela de cadastro e insere no banco de dados
            if event == 'Cadastrar':
                r_firstname = values['r_firstname']
                r_lastname = values['r_lastname']
                r_email = values['r_email']
                r_user = values['r_user']
                r_password = values['r_password']

                database = Db
                insert_collection = database.create_collection(database, r_firstname, r_lastname, r_email, r_user, r_password)

                # Caso não seja possivel inserir os documentos, ele exibe um popup de erro
                if insert_collection:
                    Sg.PopupError('Não foi possivel inserir o registro!')
                # Caso contrario, ele exibi um popup de sucesso!
                else:
                    Sg.PopupOK('Registro incluido com sucesso!')
                    break

            if event == 'Voltar':
                break

        window.close()

    def login_window(self):

        Sg.theme('Default')

        title = 'Portfolio in Python - Login'

        layout = [
            [Sg.Text('Login', font=("Arial", 24), pad=[30,30])],
            [Sg.Text('User:', size=(10, 1), font=('Arial', 12)), Sg.InputText(key='user', size=[30, 30])],
            [Sg.Text('Password:', size=(10, 1), font=('Arial', 12)), Sg.InputText(key='password', size=[30, 30], password_char='*')],
            [
                Sg.Button('Login', button_color='green', size=20, pad=[0, 50]),
                Sg.Button('Cadastrar-se', button_color='blue', size=20),
                Sg.Button('Sair', button_color='red', size=20)
            ],
            [Sg.Text('Made by Solandro Sousa', pad=[30, 0])]
        ]

        column = [[Sg.VPush()],
                  [Sg.Push(), Sg.Column(layout, element_justification='c'), Sg.Push()],
                  [Sg.VPush()]]

        Program(title, column, [600,400])

    def register_window(self):

        Sg.theme('Default')

        title = 'Cadastro de usuário'

        layout = [
            [Sg.Text('First Name:', size=(10, 1)), Sg.InputText(key='r_firstname', size=[30, 30])],
            [Sg.Text('Last Name:', size=(10, 1)), Sg.InputText(key='r_lastname', size=[30, 30])],
            [Sg.Text('E-mail:', size=(10, 1)), Sg.InputText(key='r_email', size=[30, 30])],
            [Sg.Text('Username:', size=(10, 1)), Sg.InputText(key='r_user', size=[30, 30])],
            [Sg.Text('Password:', size=(10, 1)), Sg.InputText(key='r_password', size=[30, 30], password_char='*')],
            [
                Sg.Button('Cadastrar', button_color='blue', size=20),
                Sg.Button('Voltar', button_color='red', size=20)
            ],
        ]

        column = [[Sg.VPush()],
                  [Sg.Push(), Sg.Column(layout, element_justification='c'), Sg.Push()],
                  [Sg.VPush()]]

        main = Program(title, column, [600,400])

    def main_window(self):

        Sg.theme('Default')

        menu_bar = [
            ['&File', ['&Open', '&Save']],
            ['&Sair'],
        ]

        layout = [
            [Sg.Menu(menu_bar, tearoff=False, key='menu_bar')],
            [Sg.Text('Bem vindo, você está logado!')],
            [Sg.Button('Sair')]
        ]

        column = [[Sg.VPush()],
                  [Sg.Push(), Sg.Column(layout, element_justification='c'), Sg.Push()],
                  [Sg.VPush()]]

        Program('Portfolio Python - Menu', column, [600,400])

if __name__ == "__main__":
    Program.login_window(Program)
