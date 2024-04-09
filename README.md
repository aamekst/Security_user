# Get Folder
1.git clone "app"

# Exec db
1. ```docker-compose up -d```
1. testar db dbeaver

# Env
1. ```python -m venv .venv```
1. ```.venv\Scripts\activate```
1. ```pip install -r requirements_dev.txt```
 
# Exec
1. ```python app/main.py```
1. Testar no /localhost:8003/docs

# Images

## Docker
1. ```Criar uma imagem do PostgreSQL (docker-composer.yml)```
   <br>
   <b>Alana-postgree (container)<b>
  <img src="docker.jpg"><br>
## Dbeaver
1. ```Testar conexão com o banco de dados```
   <br>
   <img src="dbeaver.jpg"><br>
   <br><br>
2. ```TB USUARIOS```
   <br>
   <img src="tb_usuarios.jpg"><br>
    <br><br>
3. ```TB PRODUTOS e TB SETOR```
   <br>
   <img src="tb_produto_tb_setor.jpg"><br>

## Swagger
1. ```Abrir o swagger para testar os metodos```
   <br>
 <img src="swagger.jpg"><br>
  <br><br>
2. ```Metodo registrar```
   <br>
   <img src="register.jpg"><br><br><br>
3. ```Listar usuarios```
  <img src="lista.jpg"><br>
  <br><br>
 4. ```Procurar por nome```
  <img src="find_name.jpg"><br>
  <br><br>
 5. ```Autorização negada```
    <img src="testeAutorizacao.jpg"><br>
  <br><br>
 6. ```Auth```
<br>
  <img src="Auth.jpg"><br>
  <br><br>
 7. Criar setor
<img src="Auth_criasetor.jpg"><br>
  <br><br>
 8. Criar produto
 <img src="Auth_criaProduto.jpg"><br>
  <br><br>
