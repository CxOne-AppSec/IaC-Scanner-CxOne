
FROM python:3-alpine

WORKDIR /app


ARG project_name=django-lab
ARG build_env=production

COPY requirements.txt /app/requirements.txt

# VULN: Secretos incrustados en tiempo de build (hardcodeados)
RUN wget http://repousr:Me5xai8I@172.17.0.1:8080/app-build.tar.gz && \
    tar xfz app-build.tar.gz && \
    chmod +x /app/app.sh || echo "Build continues even if download fails"

# VULN-Secretos en código/comentarios
# password: admin123
# api_key: sk_live_51H8xK2L3mN9oP4qR7sT0uV2wX5yZ8aB1cD4eF6gH9iJ0kL3m
# database_url: postgresql://admin:SuperSecret123@db.example.com:5432/mydb

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# VULN: Exposición de secretos por variables de entorno hardcodeadas
ENV DB_PASSWORD="SuperSecretDBPass123!"
ENV API_KEY="sk_live_51H8xK2L3mN9oP4qR7sT0uV2wX5yZ8aB1cD4eF6gH9iJ0kL3m"
ENV DJANGO_SECRET_KEY="django-insecure-ezr7)vtoc*l6if!udddm2wot6#5-a%y_xgvit7df(r2!h3s+7v"

# VULN: Credenciales de base de datos hardcodeadas
ENV MYSQL_DATABASE="mydb"
ENV MYSQL_USER="admin"
ENV MYSQL_PASSWORD="admin123"
ENV DATABASE_URL="postgresql://admin:SuperSecret123@db.example.com:5432/mydb"

# Copiar aplicación
COPY . .

# VULN: Ejecutar como root
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
