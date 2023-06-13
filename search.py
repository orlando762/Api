import requests

def listar_commits(usuario, repositorio):
    url = f"https://api.github.com/repos/{usuario}/{repositorio}/commits"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    response = requests.get(url, headers=headers)
    commits = response.json()
    
    if response.status_code == 200:
        for commit in commits:
            autor = commit["commit"]["author"]["name"]
            mensagem = commit["commit"]["message"]
            print(f"Autor: {autor}")
            print(f"Mensagem: {mensagem}")
            print("---")
    else:
        print(f"Erro ao buscar commits: {response.status_code}")


# Exemplo de uso
usuario = "orlando762"
repositorio = "Api"

listar_commits(usuario, repositorio)
