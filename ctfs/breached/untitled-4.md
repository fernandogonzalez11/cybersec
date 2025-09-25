### **Tabla de Recursos para el Funcionamiento del Sistema**  

| **Recurso**                     | **Tipo**   | **Espacio (Memoria/Disco)**                                                                 | **Tiempo (Procesamiento)**                                                                 |
|---------------------------------|------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **Servidor de Producción**      | Hardware   | - **RAM:** 16 GB (mínimo para ~1000 usuarios concurrentes).<br>- **Disco:** 200 GB (base de datos + archivos multimedia). | - **CPU:** 4 núcleos a 2.5 GHz.<br>- **Red:** Ancho de banda mínimo de 100 Mbps.           |
| **Base de Datos (MySQL Cloud)** | Software   | - **Inicial:** 20 GB (para usuarios, experiencias, reservas).<br>- **Crecimiento:** 5 GB/mes. | - **Consultas simples:** ≤ 50 ms.<br>- **Consultas complejas (JOINs):** ≤ 500 ms.          |
| **Backend (Node.js + Express)** | Software   | - **RAM:** 1-2 GB (dependiendo de la carga).<br>- **Disco:** 500 MB (para dependencias).    | - **Peticiones API promedio:** ≤ 200 ms.<br>- **Picos de carga:** ≤ 1 segundo.             |
| **Firebase Storage**            | Software   | - **Almacenamiento inicial:** 50 GB (imágenes de experiencias y perfiles).                 | - **Subida/descarga de imágenes:** ≤ 2 segundos (por archivo).                            |
| **Redis (Caché)**              | Software   | - **RAM:** 512 MB - 1 GB (para caché de sesiones y consultas frecuentes).                  | - **Lectura/escritura:** ≤ 1 ms.                                                          |
| **Servicio de Correo (SMTP)**  | Software   | - No aplica (servicio externo).                                                            | - **Envío de correos:** ≤ 10 segundos (confirmaciones, notificaciones).                   |
| **Generación de PDFs**         | Software   | - **Librería:** 50 MB (PDFKit u equivalente).                                              | - **Generación de comprobantes:** ≤ 3 segundos.                                           |
| **Procesamiento de Imágenes**  | Software   | - **Sharp/ImageMagick:** 100 MB (para redimensionamiento).                                 | - **Compresión de imágenes:** ≤ 500 ms (por imagen).                                      |
| **Chatbot (Dialogflow/API)**   | Software   | - No aplica (servicio externo).                                                            | - **Respuestas:** ≤ 1 segundo (latencia de API).                                          |
| **Google Maps API**           | Software   | - No aplica (servicio externo).                                                            | - **Carga de mapas interactivos:** ≤ 2 segundos.                                         |
| **Frontend (React Native)**   | Software   | - **Bundle de la app:** ≤ 50 MB (APK).<br>- **Almacenamiento local:** 100 MB (caché).      | - **Tiempo de carga inicial:** ≤ 4 segundos (en 4G).                                     |
| **Servidor de Notificaciones** | Software   | - **Firebase Cloud Messaging (FCM):** No aplica.                                           | - **Entrega de notificaciones push:** ≤ 5 segundos.                                      |
| **Balanceador de Carga**      | Hardware   | - **AWS ALB o Nginx:** Configuración para alta disponibilidad.                             | - **Redirección de tráfico:** ≤ 10 ms.                                                   |
| **Backups Automatizados**     | Software   | - **Espacio adicional:** 50 GB (copias diarias en la nube).                                | - **Tiempo de restauración:** ≤ 30 minutos (en caso de fallo).                           |

---

### **Notas Clave**  
1. **Escalabilidad**:  
   - La base de datos y el servidor están dimensionados para soportar un crecimiento del 20% mensual en usuarios y reservas.  
2. **Tolerancia a Fallos**:  
   - Se incluyen backups diarios y redundancia en la nube para evitar pérdida de datos.  
3. **Rendimiento**:  
   - Los tiempos de respuesta están optimizados para una experiencia fluida (ej.: < 3 segundos en acciones críticas).  

---

### **Diferencias vs. Proyecto Anterior**  
- **Mayor almacenamiento**: Se incrementó el espacio en disco para manejar imágenes de experiencias y menús.  
- **Nuevos servicios**: Firebase Storage (para multimedia) y Google Maps API (para ubicaciones).  
- **Optimización**: Tiempos de respuesta más estrictos en comparación con la versión anterior.  

¿Necesitas ajustar algún recurso o métrica? 😊