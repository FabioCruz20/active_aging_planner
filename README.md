# Active Aging Planner

## Implantação

### Configuração do Nginx

O diretório deploy/nginx/ contém o template do arquivo de configuração do nginx para o projeto active-aging-planner. 
Substitua as variáveis PORTA_HTTP, DOMINIO e PORTA_WAITRESS no template pelo valor correspondente.
Depois de substituir as variáveis, copie o arquivo para o diretório de configuração do nginx.
No Ubuntu, o diretório de configuração do nginx é /etc/nginx/sites-available/.
Ative o arquivo de configuração do nginx com o comando:
```
sudo ln -s /etc/nginx/sites-available/active-aging-planner.template.conf /etc/nginx/sites-enabled/
```
Restart the nginx service:
```
sudo service nginx restart
```