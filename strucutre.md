inventario_punto_venta/
├── main.py                          # Archivo principal que inicializa la aplicación
├── README.md                        # Descripción del proyecto
├── requirements.txt                 # Dependencias de Python
├── config/
│   └── config.py                    # Configuración general (credenciales, configuración de DB, etc.)
├── dao/                             # Data Access Objects (DAO)
│   ├── base_dao.py                  # Clase base para DAOs (conexión, operaciones genéricas)
│   ├── producto_dao.py              # DAO para la entidad Producto
│   ├── usuario_dao.py               # DAO para la entidad Usuario
│   └── venta_dao.py                 # DAO para la entidad Venta
├── db/
│   ├── database.db                  # Archivo de la base de datos SQLite (opcional, depende del motor usado)
│   └── schema.sql                   # Archivo SQL para la creación de tablas
├── models/                          # Modelos o entidades de datos
│   ├── producto.py                  # Clase Producto
│   ├── usuario.py                   # Clase Usuario
│   └── venta.py                     # Clase Venta
├── services/                        # Lógica de negocio
│   ├── inventario_service.py        # Servicios para la gestión de inventario
│   ├── venta_service.py             # Servicios para la gestión de ventas
│   └── usuario_service.py           # Servicios para la gestión de usuarios
├── controllers/                     # Controladores de la aplicación
│   ├── inventario_controller.py     # Controlador para inventario
│   ├── venta_controller.py          # Controlador para ventas
│   └── usuario_controller.py        # Controlador para usuarios
├── ui/                              # Interfaces de usuario usando customtkinter
│   ├── main_window.py               # Ventana principal
│   ├── inventario_view.py           # Vista para gestión de inventario
│   ├── venta_view.py                # Vista para punto de venta
│   └── usuario_view.py              # Vista para administración de usuarios
└── utils/
    ├── helpers.py                   # Funciones utilitarias
    └── validators.py                # Validaciones (ej: formato de datos)
