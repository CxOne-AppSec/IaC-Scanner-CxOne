# Django Lab Docker - IaC Security Demo

Este repositorio contiene una aplicación Django contenerizada diseñada para demostrar vulnerabilidades comunes de Infraestructura como Código (IaC) y sus respectivas correcciones de seguridad. El proyecto sirve como banco de pruebas para herramientas de escaneo de seguridad como **Checkmarx One**.

## 🎯 Objetivo

El objetivo es proporcionar dos estados claros de la infraestructura:
1.  **Rama/Estado Vulnerable (`vuln`)**: Una configuración intencionalmente insegura que expone secretos, corre como root y tiene configuraciones de red permisivas.
2.  **Rama/Estado Seguro (`fix`)**: Una configuración endurecida (hardened) que mitiga los riesgos detectados, siguiendo las mejores prácticas de seguridad en Docker.

## 🚀 Estructura del Proyecto

El proyecto se basa en una aplicación Django estándar ejecutada con Docker Compose.

```
.
├── django-lab-docker/
│   ├── Dockerfile       # Definición de imagen (Varía según la rama)
│   ├── compose.yaml     # Orquestación de servicios (Varía según la rama)
│   ├── production.env   # Archivo de entorno (Evitar secretos aquí en producción)
│   ├── manage.py        # Entrypoint de Django
│   └── ...
└── README.md
```

## ⚠️ Análisis de Seguridad

A continuación se describen las diferencias clave entre las configuraciones Vulnerable y Segura:

### 🔴 Estado Vulnerable (The "Don'ts")

En la versión vulnerable (rama `vuln`), encontrarás intencionalmente:
*   **Secretos Hardcodeados**: Claves API, contraseñas de BD y credenciales de AWS escritas en texto plano dentro del `compose.yaml` y `Dockerfile`.
*   **Ejecución como Root**: Los contenedores corren con usuario `root` (`0:0`), lo cual es un riesgo crítico de seguridad.
*   **Docker Socket Expuesto**: Montaje de `/var/run/docker.sock`, permitiendo escape del contenedor y control del host.
*   **Sin Límites de Recursos**: No se definen límites de CPU/RAM, permitiendo posibles ataques de Denegación de Servicio (DoS).
*   **Puertos Expuestos Globalmente**: Servicios internos expuestos a `0.0.0.0`.

### 🟢 Estado Seguro / Fix (The "Dos")

En la versión corregida (rama `fix`), se aplican las siguientes mitigaciones:
*   **Docker Secrets**: Uso de gestión nativa de secretos (`/run/secrets/`) para evitar texto plano en variables de entorno.
*   **Usuario No-Privilegiado**: Ejecución con un usuario dedicado (ej. `1000:1000`) y directiva `privileged: false`.
*   **Sistema de Archivos Read-Only**: Montajes de solo lectura y sistema de archivos inmutable donde es posible.
*   **Capabilities Dropped**: Se eliminan permisos innecesarios del kernel (`cap_drop: ["ALL"]`).
*   **Límites de Recursos**: Restricciones claras de memoria y CPU para asegurar la disponibilidad.
*   **Healthchecks**: Verificaciones de salud robustas para la orquestación.

## 🛠️ Cómo Ejecutar

### Requisitos
*   Docker Desktop / Docker Engine
*   Docker Compose

### Levantar el entorno

```bash
cd django-lab-docker
docker-compose up --build -d
```

### Detener el entorno

```bash
docker-compose down
```

---
> **DISCLAIMER**: Este proyecto contiene configuraciones intencionalmente vulnerables con fines educativos y de prueba. **NO despliegues la versión vulnerable en un entorno de producción accesible públicamente.**
