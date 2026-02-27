# Inventario Sastrería

Proyecto Django para gestionar inventario, clientes y alquileres de una sastrería.

Requisitos:

- Python 3.8+
- Django
- djangorestframework

Instalación rápida:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Endpoints principales:

- Admin: `/admin/`
- API: `/api/items/`, `/api/clients/`, `/api/rentals/`
