import os
import dotenv as de
import gitlab as g
import pandas as pd
import logging

logging.basicConfig(filename='gilab_api.log', encoding='utf-8', level=logging.DEBUG)

de.load_dotenv()

def load_gitlab_object():
    """Carga de objeto de la api de Gitlab
    
    Función para autenticar al usuario en la Api de gitlab

    Returns:
        Gitlab object: Devuelve objeto de gitlab dependiendo de los los parametros recibidos
    """
    
    token = os.getenv("GITLAB_TOKEN")
    url_gitlab = os.getenv("GITLAB_URL")
    
    if token != "" and url_gitlab != "":
        return g.Gitlab(private_token=token, url=url_gitlab)
    
    elif token != "" and url_gitlab is None:
        return g.Gitlab(private_token=token)
    
    elif token is None and url_gitlab != "":
        return g.Gitlab(url_gitlab)
    
    else:
        return g.Gitlab()


def load_file(file_name):
    try:
        return pd.read_excel(file_name)
    except Exception as e:
        print(f"Error: {e}")
        return None

def register_user():
    gl = load_gitlab_object()
    user = gl.users.create({'email': f'{'Introduzca el correo del usuario'}',
                            'password': f'{'Introduzca la contraseña'}',
                            'username': f'{'Introduzca el nickname de usuario'}',
                            'name': f'{'Introduzca el nombre de usuario'}'})
    user.save()
    user.activate()
    

def register_bulk_users():
    from tkinter import Tk 
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    
    df = load_file(askopenfilename())
    
    if df is not None:
        gl = load_gitlab_object()
        count = df.shape[0]
        errors = 0
        for idx, row in df.iterrows():
            print(f'Procesing user {idx+1} of {count}, errors: {errors}', end='\r')
            try:
                user = gl.users.create({'email': f'{row.email}',
                            'password': f'{row.password}',
                            'username': f'{row.username}',
                            'name': f'{row.name}'})
                user.save()
                user.activate()
            except Exception as e:
                logging.error(f'{e} username: {row.username}')
                errors+=1
        else:
            
            print("Finalizado, todos los usuarios procesados")
            
def check_users_by_name():
    pass 