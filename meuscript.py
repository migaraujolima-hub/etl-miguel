import requests

def main():
    print("Olá, mundo!")
    
    try:
        # Realiza a requisição com timeout
        response = requests.get("https://api.github.com", timeout=10)
        
        # Verifica se a requisição foi bem-sucedida
        response.raise_for_status()
        
        print("Status da requisição:", response.status_code)
        print("Requisição realizada com sucesso!")
        
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
