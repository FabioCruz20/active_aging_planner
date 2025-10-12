# Active Aging Planner

## Implantação

### Coletar arquivos estáticos

Para coletar os arquivos estáticos, como css e js, execute:
```
python manage.py collectstatic
```

### Configuração do Nginx

O diretório deploy/nginx/ contém o template do arquivo de configuração do nginx para o projeto active-aging-planner. 
Crie uma cópia do active-aging-planner.template.conf e renomeie para active-aging-planner.prod.conf.
No arquivo de configuração active-aging-planner.prod.conf, substitua as variáveis PORTA_HTTP, DOMINIO e PORTA_GUNICORN no template pelo valor correspondente.
Depois de substituir as variáveis, copie o arquivo para o diretório de configuração do nginx.
No Ubuntu, o diretório de configuração do nginx é /etc/nginx/sites-available/.
```
sudo cp deploy/nginx/active-aging-planner.prod.conf /etc/nginx/sites-available/
```

Ative o arquivo de configuração do nginx com o comando:
```
sudo ln -s /etc/nginx/sites-available/active-aging-planner.prod.conf /etc/nginx/sites-enabled/
```

Reinicie o serviço nginx:
```
sudo service nginx restart
```

### Execução do gunicorn

Para executar o gunicorn, execute:
```
gunicorn --bind 127.0.0.1:PORTA_GUNICORN active_aging_planner.wsgi:application
```
